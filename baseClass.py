import selenium
import properties
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import pytest

class baseMethods():
    Browser_Name = properties.Browser_Name.lower()
    def __init__(self, driver):
        self.driver = driver
    def invokeBrowser(self):
        try:
            if self.Browser_Name == "chrome":
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
            elif self.Browser_Name == "firefox":
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            elif self.Browser_Name == "edge":
                self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            elif self.Browser_Name == "opera":
                self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
            elif self.Browser_Name == "safari":
                self.driver = webdriver.Safari()
            else:
                print("Browser Name is Invalid or not available")
        except Exception as e:
            print(e)
        return self.driver

    def openURL(self, url=None):
        try:
            if url is None:
                self.driver.get(properties.Launch_URL)
            else:
                self.driver.get(url)
        except Exception as e:
            print(e)
         
    def quitBrowser(self):
        self.driver.quit()