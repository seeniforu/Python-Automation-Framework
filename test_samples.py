from selenium import webdriver
from executor import Executor
from baseClass import baseMethods
from Locators import locatorObjects as loc
import allure
import pytest


#https://python.plainenglish.io/create-your-customized-html-report-in-pytest-9c6b521b7e99 - for customize reporting
#https://qxf2.com/blog/reportportal-integration-with-pytest/ - another type of report
#https://qxf2.com/blog/allure-integration-with-pytest/ - report with docker and email (see comments)
# using different classes hybrid code in single test.
# headless and incognito
# create another sample test file and test it. create a test folder.
# get element,text etc., needs to be worked.
# middle file to write detail coding methods - test it 


class Tests():

    def test_sample_1(self):
        executor = Executor(webdriver,"AI based BDD Execution")
        executor.dynamic_title("AI based BDD Test")
        executor.dynamic_description("This test case in test suite is executed with BDD like Executed with help of normal English commands.")
        executor.execute("execute in chrome browser")
        executor.execute("set page load time as default seconds")
        executor.execute("set implicit wait which is default")
        executor.execute("open the URL")
        executor.execute("click the element using link text", loc.LocatorObject["forgot_password_link_text"])
        executor.execute("with id *search_button* as locator click it")
        #executor.click_Element_by_id("search_button")
        executor.execute("sleep for *3* seconds")
        executor.execute("quit the browser")
        executor.execute("clear all process and tear it down")

    @allure.title("Programmatic Execution")
    @allure.description_html("""
        <h4>This test case in test suite is executed with usual coding stuff.</h4>""")
    def test_sample_2(self):
        baseClass = baseMethods(webdriver,"Programmatic Execution")
        baseClass.invokeBrowser()
        baseClass.pageLoad(5)
        baseClass.implicitlyWait(11)
        baseClass.openURL("https://www.facebook.com")
        baseClass.click_Element_by_link_text(loc.LocatorObject["forgot_password_link_text"])
        baseClass.click_Element_by_id("search_button")
        baseClass.threadSleep(3)
        baseClass.quitBrowser()
        baseClass.tearDown()
    
