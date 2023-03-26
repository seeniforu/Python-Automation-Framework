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
from selenium.webdriver.common.by import By
import platform
import executor
import os
import time

locatorDic = {}
allKeys = []
pageKeys = {}
allLocatorFiles = []

class baseMethods():
    Browser_Name = properties.Browser_Name.lower()
    
    def __init__(self, driver, Test_name = None, Test_id = None):
        self.driver = driver
        self.Test_name = Test_name
        self.Test_id = Test_id
        self.preSetup()
    
    def preSetup(self):
        forLinux = "/"
        forWindows = "\\"
        runningOS = None
        if platform.system() == "Windows":
            runningOS = forWindows
        else:
            runningOS = forLinux
        try:
            with os.scandir(os.getcwd()+runningOS+"Locators"+runningOS) as entries:
                for entry in entries:
                    allLocatorFiles.append(entry.name)
            # print(allLocatorFiles)
            for i in allLocatorFiles:
                if "json" in i:
                    with open(os.getcwd()+runningOS+"Locators"+runningOS+i) as json_file:
                        data = json.load(json_file)
                        locatorDic = data
                        pageKeysOfJsonFile = data.keys()
                        #print(pageKeysOfJsonFile)
                        for i in pageKeysOfJsonFile:
                            tempDic = locatorDic[i]
                            pageKeys.update(tempDic)
                        # print(pageKeys)
                PageLocatorKeys = pageKeys.keys()
                for i in PageLocatorKeys:
                    allKeys.append(i)
                # print(allKeys)
                # print(pageKeys["search_button"])
        except Exception as e:
            print(e)
            print("Either Locator folder or locator json files missing.")

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
        try:
            self.driver.quit()
        except Exception as e:
            print(e)
    
    def tearDown(self):
        forLinux = "/"
        forWindows = "\\"
        runningOS = None
        if platform.system() == "Windows":
            runningOS = forWindows
        else:
            runningOS = forLinux
        cache_path = os.getcwd()+runningOS+"tempData"
        try:
            if len(executor.temp_dic) >=1:
                if os.path.exists(cache_path):
                    with open(cache_path+runningOS+"temp.txt", "a") as write_file:
                        write_file.write("\n")
                        write_file.writelines(str(executor.temp_dic))
                else:
                    os.mkdir(cache_path)
                    with open(cache_path+runningOS+"temp.txt", "a") as write_file:
                        write_file.write("\n")
                        write_file.writelines(str(executor.temp_dic))
                executor.temp_dic.clear()
        except Exception as e:
            print(str(e))
        
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
        else:
            self.driver.set_page_load_timeout(int(seconds))
    
    def implicitlyWait(self, seconds = None):
        if seconds is None:
            self.driver.implicitly_wait(int(properties.Implicit_Wait))
        else:
            self.driver.set_page_load_timeout(int(seconds))
    
    def threadSleep(self, seconds):
        time.sleep(int(seconds))
    
    def click_Element(self, Locator):
        try:
            if type(Locator) is tuple: 
                try:
                    elements = self.driver.find_element(*Locator)
                    elements.click()
                except Exception as e1:
                    print(e1)
        except Exception as e:
            print(e)
    
    def click_Element_by_id(self, id):
        try:
            if type(id) is tuple:
                try:
                    elements = self.driver.find_element(*id)
                    elements.click()
                except Exception as e1:
                    print(e1)
            elif id in allKeys: 
                try:
                    elements = self.driver.find_element(By.ID, pageKeys[id])
                    elements.click()
                except Exception as e1:
                    print(e1)
            else:
                try:
                    elements = self.driver.find_element(By.ID, id)
                    elements.click()
                except Exception as e2:
                    print(e2)
        except Exception as e:
            print(e)
    
    def click_Element_by_name(self, name):
        try:
            if type(name) is tuple:
                try:
                    elements = self.driver.find_element(*name)
                    elements.click()
                except Exception as e1:
                    print(e1)
            elif name in allKeys: 
                try:
                    elements = self.driver.find_element(By.NAME, pageKeys[name])
                    elements.click()
                except Exception as e1:
                    print(e1)
            else:
                try:
                    elements = self.driver.find_element(By.NAME, name)
                    elements.click()
                except Exception as e2:
                    print(e2)
        except Exception as e:
            print(e)
    
    def click_Element_by_class_name(self, class_name):
        try:
            if type(class_name) is tuple:
                try:
                    elements = self.driver.find_element(*class_name)
                    elements.click()
                except Exception as e1:
                    print(e1)
            elif class_name in allKeys: 
                try:
                    elements = self.driver.find_element(By.CLASS_NAME, pageKeys[class_name])
                    elements.click()
                except Exception as e1:
                    print(e1)
            else:
                try:
                    elements = self.driver.find_element(By.CLASS_NAME, class_name)
                    elements.click()
                except Exception as e2:
                    print(e2)
        except Exception as e:
            print(e)
    
    def click_Element_by_css_selector(self, css_selector):
        try:
            if type(css_selector) is tuple:
                try:
                    elements = self.driver.find_element(*css_selector)
                    elements.click()
                except Exception as e1:
                    print(e1)
            elif css_selector in allKeys: 
                try:
                    elements = self.driver.find_element(By.CSS_SELECTOR, pageKeys[css_selector])
                    elements.click()
                except Exception as e1:
                    print(e1)
            else:
                try:
                    elements = self.driver.find_element(By.CSS_SELECTOR, css_selector)
                    elements.click()
                except Exception as e2:
                    print(e2)
        except Exception as e:
            print(e)

    def click_Element_by_xpath(self, xpath):
        try:
            if type(xpath) is tuple:
                try:
                    elements = self.driver.find_element(*xpath)
                    elements.click()
                except Exception as e1:
                    print(e1)
            elif xpath in allKeys: 
                try:
                    elements = self.driver.find_element(By.XPATH, pageKeys[xpath])
                    elements.click()
                except Exception as e1:
                    print(e1)
            else:
                try:
                    elements = self.driver.find_element(By.XPATH, xpath)
                    elements.click()
                except Exception as e2:
                    print(e2)
                    
        except Exception as e:
            print(e)
           
    def click_Element_by_link_text(self, link_text):
        try:
            if type(link_text) is tuple:
                try:
                    elements = self.driver.find_element(*link_text)
                    elements.click()
                except Exception as e1:
                    print(e1)
            elif link_text in allKeys: 
                try:
                    elements = self.driver.find_element(By.LINK_TEXT, pageKeys[link_text])
                    elements.click()
                except Exception as e1:
                    print(e1)
            else:
                try:
                    elements = self.driver.find_element(By.LINK_TEXT, link_text)
                    elements.click()
                except Exception as e2:
                    print(e2)
        except Exception as e:
            print(e)

    def click_Element_by_partial_link_text(self, partial_link_text):
        try:
            if type(partial_link_text) is tuple:
                try:
                    elements = self.driver.find_element(*partial_link_text)
                    elements.click()
                except Exception as e1:
                    print(e1)
            elif partial_link_text in allKeys: 
                try:
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, pageKeys[partial_link_text])
                    elements.click()
                except Exception as e1:
                    print(e1)
            else:
                try:
                    elements = self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link_text)
                    elements.click()
                except Exception as e2:
                    print(e2)
        except Exception as e:
            print(e)

