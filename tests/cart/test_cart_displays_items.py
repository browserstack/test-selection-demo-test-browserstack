from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_cart_displays_items_added_from_catalog(demo):
    demo.add_product_to_cart(4)
    demo.open_cart_page()
    name = demo.wait_for(5).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='cart-item']//div[contains(@class,'font-semibold')]")))
    assert "Galaxy Note" in name.text
