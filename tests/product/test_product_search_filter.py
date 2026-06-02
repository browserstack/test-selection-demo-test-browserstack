import time

from selenium.webdriver.common.by import By


def test_search_filters_results(demo):
    demo.open_products_page()
    search_input = demo.driver.find_element(
        By.CSS_SELECTOR, "input[placeholder='Search products...']")
    search_input.clear()
    search_input.send_keys("pixel")
    time.sleep(0.5)
    visible_cards = len(demo.driver.find_elements(
        By.CSS_SELECTOR, "[id^='product-card-']"))
    assert visible_cards == 1, "Filtered catalog should show exactly 1 result"
