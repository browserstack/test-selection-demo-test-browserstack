import os
import random
import time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DEFAULT_APP_URL = "https://demo-app-sts.surge.sh"


class DemoApp:
    """Shared helpers for interacting with the BrowserStack demo storefront.

    Python/pytest port of the Java BaseUiTest helper class.
    """

    def __init__(self, driver):
        self.driver = driver

    def base_url(self):
        configured = os.environ.get("APP_URL")
        if configured and configured.strip():
            return configured.rstrip("/")
        return DEFAULT_APP_URL

    def open_path(self, path):
        normalized = path if path.startswith("/") else "/" + path
        self.driver.get(self.base_url() + normalized)
        time.sleep(5)

    def wait_for(self, seconds):
        return WebDriverWait(self.driver, seconds)

    def go_home(self):
        self.open_path("/")
        self.wait_for(30).until(EC.visibility_of_element_located((By.ID, "hero-title")))

    def open_scenarios_page(self):
        self.open_path("/scenarios")
        self.wait_for(30).until(EC.visibility_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Scenarios')]")))

    def open_login_page(self):
        self.open_path("/login")
        self.wait_for(30).until(
            lambda d: "/login" in d.current_url or "/profile" in d.current_url
        )

    def login_as(self, email, password):
        self.open_login_page()
        wait = self.wait_for(10)
        email_input = wait.until(EC.element_to_be_clickable((By.ID, "email-input")))
        email_input.clear()
        email_input.send_keys(email)
        password_input = self.driver.find_element(By.ID, "password-input")
        password_input.clear()
        password_input.send_keys(password)
        self.driver.find_element(By.ID, "login-submit").click()
        wait.until(EC.url_contains("/products"))
        wait.until(EC.visibility_of_element_located((By.ID, "shopping-cart-btn")))

    def login_with_random_demo_user(self):
        self.open_login_page()
        select = self._user_select()
        choices = self._selectable_user_options(select)
        if not choices:
            raise RuntimeError("No demo users found in the login dropdown")
        email = random.choice(choices).get_attribute("value")
        self._complete_quick_select_login(select, email)

    def login_using_quick_select(self, email):
        self.open_login_page()
        select = self._user_select()
        self._complete_quick_select_login(select, email)

    def first_demo_user_email(self):
        self.open_login_page()
        options = self._selectable_user_options(self._user_select())
        if not options:
            raise RuntimeError("No demo users found in the login dropdown")
        return options[0].get_attribute("value")

    def open_products_page(self):
        self.open_path("/products")
        self.wait_for(30).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "[id^='product-card-']")))

    def open_profile_page(self):
        self.open_path("/profile")
        self.wait_for(30).until(
            lambda d: "/profile" in d.current_url or "/login" in d.current_url
        )

    def open_orders_page(self):
        self.open_path("/orders")
        self.wait_for(30).until(
            lambda d: "/orders" in d.current_url or "/login" in d.current_url
        )

    def add_product_to_cart(self, product_id, quantity=1):
        self.open_products_page()
        wait = self.wait_for(10)
        card = wait.until(EC.visibility_of_element_located(
            (By.ID, f"product-card-{product_id}")))
        quantity_field = card.find_element(By.CSS_SELECTOR, "input[type='number']")
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))
        before = self.cart_badge_count()
        add_button = card.find_element(By.ID, f"add-to-cart-{product_id}")
        wait.until(EC.element_to_be_clickable(add_button)).click()
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#shopping-cart-btn span"), str(before + quantity)))

    def add_products_to_cart(self, *product_ids):
        for pid in product_ids:
            self.add_product_to_cart(pid)

    def cart_badge_count(self):
        text = self.driver.find_element(
            By.CSS_SELECTOR, "#shopping-cart-btn span").text.strip()
        try:
            return int(text)
        except ValueError:
            return 0

    def open_cart_page(self):
        self.driver.find_element(By.ID, "shopping-cart-btn").click()
        self.wait_for(10).until(EC.visibility_of_element_located(
            (By.XPATH, "//h1[contains(text(),'Shopping Cart')]")))

    def _user_select(self):
        wait = self.wait_for(10)
        element = wait.until(EC.visibility_of_element_located((By.ID, "user-select")))
        return Select(element)

    def _selectable_user_options(self, select):
        return [opt for opt in select.options
                if opt.get_attribute("value") and opt.get_attribute("value").strip()]

    def _complete_quick_select_login(self, select, email):
        wait = self.wait_for(10)
        select.select_by_value(email)
        wait.until(EC.text_to_be_present_in_element_value((By.ID, "email-input"), email))
        self.driver.find_element(By.ID, "login-submit").click()
        wait.until(EC.url_contains("/products"))

    def scroll_into_view(self, element):
        if element is None:
            return
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        time.sleep(0.2)

    def click_with_retry(self, element):
        if element is None:
            return
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)
