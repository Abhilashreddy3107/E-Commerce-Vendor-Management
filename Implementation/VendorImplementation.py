from Abstractions.Vendor import Vendor
from Models.VendorModel import VendorModel
from Models.VendorSessionModel import VendorSessionModel

class VendorImplementation(Vendor):

    def __init__(self):
        self.vendor_model = VendorModel()
        self.vendor_session = VendorSessionModel()

    def login(self, username, password):
        if self.vendor_model.is_correct_vendor(username, password):
            self.vendor_session.login(username)
            return f"User {username} logged in successfully!"
        else:
            return "Invalid username or password."

    def logout(self, username):
        if self.vendor_session.check_login(username):
            self.vendor_session.logout(username)
            return f"User {username} logged out successfully!"
        else:
            return "Invalid vendor."