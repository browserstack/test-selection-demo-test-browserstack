from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_feature_toggle_changes_visual_state(demo):
    demo.open_scenarios_page()
    toggle_button = demo.wait_for(5).until(
        EC.element_to_be_clickable((By.ID, "feature-toggle-btn")))
    initial_class = toggle_button.get_attribute("class")
    toggle_button.click()
    demo.wait_for(5).until(
        lambda d: toggle_button.get_attribute("class") != initial_class
    )
    assert "bg-blue-" in toggle_button.get_attribute("class")
