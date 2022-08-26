import selenium
import properties
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.chrome.options import Options
import pytest

class baseMethods():
    Browser_Name = properties.Browser_Name.lower()
    def __init__(self, driver):
        self.driver = driver
    def invokeBrowser(self, arg_browser = None):
        if arg_browser is not None:
            Final_Browser = arg_browser
        else:
            Final_Browser = self.Browser_Name
        try:
            if Final_Browser == "chrome":
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
            elif Final_Browser == "firefox":
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            elif Final_Browser == "edge":
                self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            elif Final_Browser == "opera":
                self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
            elif Final_Browser == "safari":
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