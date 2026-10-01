from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_logout_from_profile_clears_session(demo):
    demo.login_with_random_demo_user()
    demo.open_profile_page()
    demo.wait_for(5).until(EC.visibility_of_element_located(
        (By.XPATH, "//button[contains(text(),'Logout')]"))).click()
    login_header = demo.wait_for(5).until(EC.visibility_of_element_located(
        (By.XPATH, "//h1[contains(text(),'Login') or contains(text(),'Welcome Back')]")))
    assert "Login" in login_header.text or "Welcome" in login_header.text
