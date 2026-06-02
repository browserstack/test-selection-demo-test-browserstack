from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_category_filter_limits_results_for_ios(demo):
    demo.open_products_page()
    category_select = Select(demo.driver.find_element(By.CSS_SELECTOR, "select"))
    category_select.select_by_value("ios")
    demo.wait_for(5).until(
        lambda d: len(d.find_elements(By.ID, "product-card-1")) == 0
    )
    visible_cards = len(demo.driver.find_elements(
        By.CSS_SELECTOR, "[id^='product-card-']"))
    assert visible_cards == 2, "Filtered catalog should show exactly two results"
