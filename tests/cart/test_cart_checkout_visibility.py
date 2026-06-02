from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_checkout_button_hidden_when_logged_out(demo):
    demo.add_product_to_cart(6)
    demo.open_cart_page()
    notice = demo.wait_for(5).until(EC.visibility_of_element_located(
        (By.XPATH, "//div[contains(@class,'text-yellow-800')]")))
    assert "Please" in notice.text
