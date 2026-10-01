from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def _place_order_for_product(demo, product_id):
    demo.add_product_to_cart(product_id)
    demo.open_cart_page()
    demo.driver.find_element(By.ID, "checkout-btn").click()
    demo.wait_for(5).until(
        EC.element_to_be_clickable((By.ID, "place-order-btn"))).click()
    demo.wait_for(10).until(EC.url_contains("/orders"))


def test_latest_order_appears_first(demo):
    demo.login_with_random_demo_user()
    _place_order_for_product(demo, 3)
    first_order_id = demo.wait_for(5).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "li.order-list-item"))).get_attribute("data-order-id")
    _place_order_for_product(demo, 4)
    latest_order_id = demo.wait_for(5).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "li.order-list-item"))).get_attribute("data-order-id")
    assert latest_order_id != first_order_id
