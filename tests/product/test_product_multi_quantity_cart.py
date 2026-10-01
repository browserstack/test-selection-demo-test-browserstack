from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_adding_multiple_quantity_persists_in_cart(demo):
    demo.add_product_to_cart(3, quantity=3)
    demo.open_cart_page()
    cart_item = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "cart-item")))
    assert "x 3" in cart_item.text
