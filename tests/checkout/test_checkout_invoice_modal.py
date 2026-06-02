from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_invoice_modal_displays_line_items(demo):
    demo.login_with_random_demo_user()
    demo.add_product_to_cart(2)
    demo.open_cart_page()
    demo.driver.find_element(By.ID, "checkout-btn").click()
    demo.wait_for(5).until(
        EC.element_to_be_clickable((By.ID, "place-order-btn"))).click()
    demo.wait_for(10).until(EC.url_contains("/orders"))
    first_order = demo.wait_for(5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "li.order-list-item")))
    order_id = first_order.get_attribute("data-order-id")
    demo.driver.find_element(By.ID, f"view-invoice-btn-{order_id}").click()
    modal_header = demo.wait_for(5).until(EC.visibility_of_element_located(
        (By.XPATH, "//h2[contains(text(),'Invoice for Order')]")))
    assert order_id in modal_header.text
    assert demo.driver.find_elements(
        By.XPATH, "//div[contains(@class,'shadow-lg')]//li") != []
