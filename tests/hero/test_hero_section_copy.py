from selenium.webdriver.common.by import By


def test_hero_section_displays_expected_copy(demo):
    demo.go_home()
    hero_title = demo.driver.find_element(By.ID, "hero-title")
    hero_subtitle = demo.driver.find_element(By.ID, "hero-subtitle")
    assert "Demo Playground" in hero_title.text
    assert "BrowserStack-ready" in hero_subtitle.text
