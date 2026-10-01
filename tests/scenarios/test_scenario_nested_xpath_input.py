from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_nested_xpath_input_is_interactable(demo):
    demo.open_scenarios_page()
    nested_input = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "xpath-input")))
    nested_input.send_keys("Nested input text")
    assert nested_input.get_attribute("value") == "Nested input text"
