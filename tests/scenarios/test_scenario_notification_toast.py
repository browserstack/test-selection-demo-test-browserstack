from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def _wait_for_toast_with_title(demo, title_text):
    return demo.wait_for(5).until(EC.visibility_of_element_located((
        By.XPATH,
        f"//div[contains(@class,'font-semibold') and contains(normalize-space(), '{title_text}')]"
    )))


def test_notification_button_shows_toast(demo):
    demo.open_scenarios_page()
    submit_button = demo.wait_for(5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[title='Submit']")))
    submit_button.click()
    toast = _wait_for_toast_with_title(demo, "Demo notification")
    assert toast.is_displayed(), "Toast title should be visible"
