import properties
from baseClass import baseMethods
from selenium import webdriver as driver

class Tests():
    def test_sample_One(self):
        baseClass = baseMethods(driver)
        baseClass.invokeBrowser()
        baseClass.openURL()
        baseClass.quitBrowser()

    
