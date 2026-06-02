from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_clear_cart_button_removes_all_items(demo):
    demo.add_products_to_cart(1, 2)
    demo.open_cart_page()
    clear_button = demo.wait_for(5).until(
        EC.element_to_be_clickable((By.ID, "clear-cart-btn")))
    clear_button.click()
    empty_message = demo.wait_for(5).until(EC.visibility_of_element_located(
        (By.XPATH, "//p[text()='Your cart is empty.']")))
    assert empty_message.is_displayed()
