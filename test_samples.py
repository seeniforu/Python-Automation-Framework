from selenium import webdriver as driver
from executor import Executor
from baseClass import baseMethods
import allure
import pytest

#https://python.plainenglish.io/create-your-customized-html-report-in-pytest-9c6b521b7e99 - for customize reporting
#https://qxf2.com/blog/reportportal-integration-with-pytest/ - another type of report
#https://qxf2.com/blog/allure-integration-with-pytest/ - report with docker and email (see comments)
#data set update --> "open chrome" got launch url method

class Tests():
    
    forgot_password = "Forgotten password?"

    @allure.title("Basic browser launch")
    def test_sample_One(self):
        executor = Executor(driver)
        executor.execute("execute in firefox browser")
        executor.setProperties("set page load time as *9* seconds")
        executor.setProperties("set implicit wait which is default")
        executor.execute("open the URL")
        executor.click_Element_by_link_text(self.forgot_password)
        executor.execute("quit the browser")
        
    def test_sample_Two(self):
        baseClass = baseMethods(driver)
        baseClass.invokeBrowser()
        baseClass.pageLoad(5)
        baseClass.implicitlyWait(11)
        baseClass.openURL("https://www.facebook.com")
        baseClass.captureScreenshot()
        baseClass.quitBrowser()

    
