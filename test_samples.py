import properties
from baseClass import baseMethods
from selenium import webdriver as driver
import output
from executor import Executor


class Tests():
    def test_sample_One(self):
        executor = Executor(driver)
        executor.execute("launch the default browser")
        executor.execute("open the URL")
        executor.execute("quit the browser")
    
    # def test_sample_Two(self):
    #     baseClass = baseMethods(driver)
    #     baseClass.invokeBrowser()
    #     baseClass.openURL("https://www.facebook.com")
    #     baseClass.quitBrowser()

    
