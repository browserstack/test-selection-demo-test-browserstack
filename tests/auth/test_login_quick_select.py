from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_quick_select_user_can_login(demo):
    email = demo.first_demo_user_email()
    demo.login_using_quick_select(email)
    demo.open_profile_page()
    demo.wait_for(10).until(EC.visibility_of_element_located(
        (By.XPATH, "//h2[contains(@class,'text-xl')]")))
    profile_email = demo.driver.find_element(
        By.XPATH, "//div[contains(@class,'text-gray-600')][1]")
    assert email in profile_email.text
