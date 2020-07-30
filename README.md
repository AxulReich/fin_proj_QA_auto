# fin_proj_QA_auto
Параметризованный тест:
@pytest.mark.parametrize('product_url_name, product_title', PRODUCTS)
def test_guest_can_add_product_to_basket(self, browser, product_url_name, product_title)
не проходит в некоторых случаях, так как не было проверить все продукты, 
