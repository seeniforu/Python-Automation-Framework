from baseClass import baseMethods
from Locators import locatorObjects as loc


class ForgotPage(baseMethods):
    def __init__(self, driver):
        self.driver = driver

    def clickCancel(self):
        self.click_Element(loc.LocatorObject["search_button"])
        print("cancel is executed")