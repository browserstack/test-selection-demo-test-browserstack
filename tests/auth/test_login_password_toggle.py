from selenium.webdriver.common.by import By


def test_show_password_toggle_changes_input_type(demo):
    demo.open_login_page()
    password_field = demo.driver.find_element(By.ID, "password-input")
    assert password_field.get_attribute("type") == "password"
    demo.driver.find_element(By.ID, "show-password").click()
    assert password_field.get_attribute("type") == "text"
