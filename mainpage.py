from baseClass import baseMethods
from Locators import locatorObjects as loc
from forgotpage import ForgotPage

class MainPage(baseMethods):
    def __init__(self, driver, Test_id = None):
        self.driver = driver
        self.Test_id = Test_id

    def clickForgotPassword(self):
        self.click_Element(loc.LocatorObject["forgot_password_link_text"])
        
        
