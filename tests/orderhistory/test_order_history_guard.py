from selenium.webdriver.common.by import By


def test_order_history_route_is_guarded(demo):
    demo.open_orders_page()
    assert demo.driver.find_element(By.ID, "login-submit").is_displayed()
