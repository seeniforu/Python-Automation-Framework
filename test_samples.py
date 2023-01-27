from selenium import webdriver as driver
from executor import Executor
from baseClass import baseMethods
from Locators import locatorObjects as loc
import allure
import pytest

#https://python.plainenglish.io/create-your-customized-html-report-in-pytest-9c6b521b7e99 - for customize reporting
#https://qxf2.com/blog/reportportal-integration-with-pytest/ - another type of report
#https://qxf2.com/blog/allure-integration-with-pytest/ - report with docker and email (see comments)

class Tests():

    @allure.title("Basic browser launch")
    def test_sample_1(self):
        executor = Executor(driver,"AI based BDD Execution")
        executor.execute("execute in chrome browser")
        executor.execute("set page load time as default seconds")
        executor.execute("set implicit wait which is default")
        executor.execute("open the URL")
        executor.execute("click the element using link text", loc.LocatorObject["forgot_password_link_text"])
        executor.execute("with id *search_button* as locator click it")
        executor.execute("sleep for *3* seconds")
        executor.execute("quit the browser")
        executor.execute("clear all process and tear it down")

        
    def test_sample_2(self):
        baseClass = baseMethods(driver,"Programmatic Execution")
        baseClass.invokeBrowser()
        baseClass.pageLoad(5)
        baseClass.implicitlyWait(11)
        baseClass.openURL("https://www.facebook.com")
        baseClass.click_Element_by_link_text(loc.LocatorObject["forgot_password_link_text"])
        baseClass.click_Element_by_id("search_button")
        baseClass.threadSleep(3)
        baseClass.quitBrowser()
        baseClass.tearDown()
    
