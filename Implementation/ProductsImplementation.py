from Abstractions.Products import Products
from Models.ProductModel import ProductModel
from Models.VendorSessionModel import VendorSessionModel

class ProductsImplementation(Products):

    def __init__(self, username):
        self.product_model = ProductModel()
        self.vendor_session = VendorSessionModel()
        self._username = username

    def add_product(self, product_name, product_type, available_quantity, unit_price):
        if self.vendor_session.check_login(self._username):
            self.product_model.add_product(product_name, product_type, available_quantity, unit_price)
            return True
        else:
            return False

    def search_product_by_name(self, product_name):
        if self.vendor_session.check_login(self._username):
            product = self.product_model.search_product(product_name)
            if product:
                return product
            else:
                return False
        else:
            return False

    def get_all_products(self):
        if self.vendor_session.check_login(self._username):
            products = self.product_model.all_products()
            if products:
                return products
            else:
                return False
        else:
            return False