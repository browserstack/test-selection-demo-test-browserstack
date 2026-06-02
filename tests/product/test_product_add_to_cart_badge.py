def test_add_to_cart_updates_badge_count(demo):
    demo.open_products_page()
    before = demo.cart_badge_count()
    demo.add_product_to_cart(1)
    assert demo.cart_badge_count() == before + 1
