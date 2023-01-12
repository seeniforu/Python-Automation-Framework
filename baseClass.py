import selenium
import properties
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import allure
from allure_commons.types import AttachmentType
from datetime import datetime  

class baseMethods():
    Browser_Name = properties.Browser_Name.lower()
   
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Browser launched')
    def invokeBrowser(self, arg_browser = None):
        if arg_browser is not None:
            Final_Browser = arg_browser.lower()
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

    @allure.step('URL Launched : {1}')
    def openURL(self, url=None):
        try:
            if url is None:
                self.driver.get(properties.Launch_URL)
            else:
                self.driver.get(url)
        except Exception as e:
            print(e)
    
    @allure.step('Browser is closed')     
    def quitBrowser(self):
        self.driver.quit()

    def currentTimestamp(self):
        current_time = datetime.now() 
        timestamp = current_time.timestamp()
        date_time = datetime.fromtimestamp(timestamp)
        str_date_time = date_time.strftime("%H-%M-%S")
        return str_date_time

    def captureScreenshot(self, arg_Name = None):
        if arg_Name is not None:
            allure.attach(self.driver.get_screenshot_as_png(), name=arg_Name, attachment_type=AttachmentType.PNG)
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot-"+self.currentTimestamp(), attachment_type=AttachmentType.PNG)

    def pageLoad(self, seconds = None):
        if seconds is None:
            self.driver.set_page_load_timeout(properties.Page_load)
            print(properties.Page_load)
        else:
            self.driver.set_page_load_timeout(seconds)
            print(seconds)
    
    def implicitlyWait(self, seconds = None):
        if seconds is None:
            self.driver.implicitly_wait(properties.Implicit_Wait)
            print(properties.Implicit_Wait)
        else:
            self.driver.set_page_load_timeout(seconds)
            print(seconds)
    
    def click_Element_by_link_text(self, link_text):
       elements = self.driver.find_element_by_link_text(link_text)
       elements.click()


