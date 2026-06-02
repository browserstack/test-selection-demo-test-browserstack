from selenium.webdriver.support import expected_conditions as EC


def test_visiting_login_while_authenticated_redirects_to_profile(demo):
    demo.login_with_random_demo_user()
    demo.open_login_page()
    demo.wait_for(5).until(EC.url_contains("/profile"))
    assert demo.driver.current_url.endswith("/profile")
