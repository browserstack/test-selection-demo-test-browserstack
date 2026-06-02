from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_increment_and_decrement_buttons_update_quantity(demo):
    demo.add_product_to_cart(5)
    demo.open_cart_page()
    quantity_locator = (
        By.XPATH, "//div[@id='cart-item']//span[contains(@id,'item-quantity')]")
    plus_button = demo.driver.find_element(
        By.XPATH, "//div[@id='cart-item']//button[text()='+']")
    minus_button = demo.driver.find_element(
        By.XPATH, "//div[@id='cart-item']//button[text()='-']")
    plus_button.click()
    demo.wait_for(5).until(EC.text_to_be_present_in_element(quantity_locator, "2"))
    minus_button.click()
    demo.wait_for(5).until(EC.text_to_be_present_in_element(quantity_locator, "1"))
