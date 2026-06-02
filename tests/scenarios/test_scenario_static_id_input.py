from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_static_id_field_accepts_input(demo):
    demo.open_scenarios_page()
    static_field = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "static-id-field")))
    static_field.clear()
    static_field.send_keys("ORD-2025-001")
    assert static_field.get_attribute("value") == "ORD-2025-001"
