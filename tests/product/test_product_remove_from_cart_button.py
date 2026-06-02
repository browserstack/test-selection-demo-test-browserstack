from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_remove_from_cart_button_appears_for_items(demo):
    demo.add_product_to_cart(2)
    remove_button = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "remove-from-cart-2")))
    before = demo.cart_badge_count()
    remove_button.click()
    demo.wait_for(5).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#shopping-cart-btn span"), str(before - 1)))
    assert demo.driver.find_elements(By.ID, "remove-from-cart-2") == []
