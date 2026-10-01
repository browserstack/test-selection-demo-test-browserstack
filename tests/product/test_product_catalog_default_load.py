from selenium.webdriver.common.by import By


def test_catalog_default_shows_all_products(demo):
    demo.open_products_page()
    demo.wait_for(5).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "[id^='product-card-']")) == 10
    )
    total_cards = len(demo.driver.find_elements(By.CSS_SELECTOR, "[id^='product-card-']"))
    assert total_cards == 10, "Default catalog load should render 10 products"
