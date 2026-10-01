import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login_fails_with_invalid_credentials(demo):
    demo.open_login_page()
    demo.driver.find_element(By.ID, "email-input").send_keys("fake@example.com")
    demo.driver.find_element(By.ID, "password-input").send_keys("wrong-password")
    time.sleep(1)
    demo.driver.find_element(By.ID, "login-submit").click()
    error_banner = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "login-error")))
    assert "Login failed" in error_banner.text, \
        "Inline login error banner should mention login failure"
    assert "/login" in demo.driver.current_url
