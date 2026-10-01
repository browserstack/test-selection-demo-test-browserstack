from selenium.webdriver.common.by import By


def test_primary_cta_navigates_to_scenarios(demo):
    demo.go_home()
    demo.driver.find_element(By.ID, "primary-cta").click()
    demo.wait_for(10).until(lambda d: "/scenarios" in d.current_url)
    assert demo.driver.find_element(By.ID, "static-id-field").is_displayed()
