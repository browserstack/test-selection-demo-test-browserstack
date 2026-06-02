from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_progress_buttons_update_status(demo):
    demo.open_scenarios_page()
    demo.driver.find_element(By.ID, "progress-btn-100").click()
    status = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "progress-status-id")))
    assert "Complete" in status.text

    demo.driver.find_element(By.ID, "progress-btn-50").click()
    status_in_progress = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "progress-status-id")))
    assert "In Progress" in status_in_progress.text
