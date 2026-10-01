from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_can_place_order_and_reach_order_history(demo):
    demo.login_with_random_demo_user()
    demo.add_product_to_cart(1)
    demo.open_cart_page()
    demo.driver.find_element(By.ID, "checkout-btn").click()
    demo.wait_for(5).until(
        EC.visibility_of_element_located((By.ID, "place-order-btn"))).click()
    demo.wait_for(10).until(EC.url_contains("/orders"))
    assert demo.driver.find_elements(By.CSS_SELECTOR, "li.order-list-item") != []
