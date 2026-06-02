from selenium.webdriver.common.by import By


def test_cart_badge_starts_at_zero(demo):
    demo.go_home()
    badge_value = demo.driver.find_element(
        By.CSS_SELECTOR, "#shopping-cart-btn span").text.strip()
    assert badge_value == "0"
