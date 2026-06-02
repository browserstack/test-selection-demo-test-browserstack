from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_cart_shows_empty_state_for_empty_cart(demo):
    demo.login_with_random_demo_user()
    demo.open_cart_page()
    empty = demo.wait_for(5).until(EC.visibility_of_element_located(
        (By.XPATH, "//p[contains(text(),'Your cart is empty.')]")))
    assert empty.is_displayed()
