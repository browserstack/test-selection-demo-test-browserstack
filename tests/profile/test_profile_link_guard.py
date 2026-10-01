from selenium.webdriver.common.by import By


def test_profile_link_redirects_to_login_when_logged_out(demo):
    demo.go_home()
    demo.driver.find_element(By.ID, "profile-btn").click()
    demo.wait_for(10).until(lambda d: "/login" in d.current_url)
    assert demo.driver.find_element(By.ID, "login-title").text == "Welcome Back"
