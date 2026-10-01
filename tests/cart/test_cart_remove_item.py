from selenium.webdriver.common.by import By


def test_remove_item_link_removes_single_item(demo):
    demo.add_products_to_cart(7, 8)
    demo.open_cart_page()
    before_items = demo.driver.find_elements(By.ID, "cart-item")
    demo.driver.find_element(
        By.XPATH, "(//div[@id='cart-item']//button[contains(text(),'Remove')])[1]").click()
    demo.wait_for(5).until(
        lambda d: len(d.find_elements(By.ID, "cart-item")) == len(before_items) - 1
    )
