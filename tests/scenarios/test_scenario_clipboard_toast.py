import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_clipboard_button_shows_link_copied_toast(demo):
    demo.open_scenarios_page()
    copy_button = demo.wait_for(5).until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Copy share link')]")))
    copy_button.click()
    time.sleep(0.5)
    copied_value = demo.driver.find_element(By.ID, "share-copy-result").text.strip()
    assert "https://demo-app.local/scenario" in copied_value
