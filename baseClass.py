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
import json
import pytest
import random
from selenium.webdriver.common.by import By
import platform

all_testcase_result = {}
result_json = {}
test_steps = []

class baseMethods():
    Browser_Name = properties.Browser_Name.lower()
    
    def __init__(self, driver, Test_name = None):
        self.driver = driver
        self.Test_name = Test_name

    @allure.step('Browser launched')
    def invokeBrowser(self, arg_browser = None):
        if arg_browser is not None:
            Final_Browser = arg_browser.lower()
        else:
            Final_Browser = self.Browser_Name
        try:
            result_json.update({"Testcase Name":self.Test_name})
            current_time = datetime.now()
            result_json["Time started"] = current_time.strftime("%m/%d/%Y, %H:%M:%S")
            if Final_Browser == "chrome":
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
                result_json["Browser Launched"] = Final_Browser
            elif Final_Browser == "firefox":
                self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                result_json["Browser Launched"] = Final_Browser
            elif Final_Browser == "edge":
                self.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
                result_json["Browser Launched"] = Final_Browser
            elif Final_Browser == "opera":
                self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
                result_json["Browser Launched"] = Final_Browser
            elif Final_Browser == "safari":
                self.driver = webdriver.Safari()
                result_json["Browser Launched"] = Final_Browser
            else:
                print("Browser Name is Invalid or not available")
                result_json["Error"] = "Browser Name is Invalid or not available"
        except Exception as e:
            print(e)
            result_json["Exception"] = str(e)
        finally:
            result_json["OS"] = platform.system()
            result_json["OS-release"] = platform.release()
            result_json["OS-version"] = platform.version()

        return self.driver

    def openURL(self, url=None):
        try:
            if url is None:
                self.driver.get(properties.Launch_URL)
                result_json["URL"] = properties.Launch_URL
            else:
                self.driver.get(url)
                result_json["URL"] = url
        except Exception as e:
            print(e)
            result_json["Exception"] = str(e)
    
    @allure.step('Browser is closed')     
    def quitBrowser(self):
        try:
            self.driver.quit()
            result_json["Browser quitted"] = "yes"
            result_json["Test steps"] = test_steps
            jsonString = json.dumps(result_json, indent=4)
            obj = json.loads(jsonString)
            all_testcase_result["TC-ID"+str(random.randint(10000,99999))] = obj
            with open("results.json", "w") as write_file:
                json.dump(all_testcase_result, write_file, indent=4)
            test_steps.clear()
            result_json.clear()
        except Exception as e:
            print(e)
        
        
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
            self.driver.set_page_load_timeout(int(properties.Page_load))
            result_json["Page Load Time"] = int(properties.Page_load)
        else:
            self.driver.set_page_load_timeout(int(seconds))
            result_json["Page Load Time (seconds)"] = int(seconds)
    
    def implicitlyWait(self, seconds = None):
        if seconds is None:
            self.driver.implicitly_wait(int(properties.Implicit_Wait))
            result_json["Implicit wait time (seconds)"] = int(properties.Implicit_Wait)
        else:
            self.driver.set_page_load_timeout(int(seconds))
            result_json["Implicit wait time (seconds)"] = int(seconds)
    
    def click_Element_by_link_text(self, link_text):
        try:
            # elements = self.driver.find_element_by_link_text(link_text)
            elements = self.driver.find_element(By.LINK_TEXT,link_text)
            elements.click()
            test_steps.append("Element is clicked using Link text")
        except Exception as e:
            print(e)
            result_json["Error"] = str(e)


