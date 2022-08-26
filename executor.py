import properties
from baseClass import baseMethods
from selenium import webdriver as driver
import output


class Executor(baseMethods):
    def  __init__(self,driver):
        self.driver = driver
        super().__init__(self.driver)
    def execute(self,commandOne):
        command1 = commandOne.lower()
        Processed_Final_Text = output.resultGeneration(command1)
        if Processed_Final_Text == "launch browser method":
            if "chrome" in command1:
                super().invokeBrowser("chrome")
            elif "firefox" in command1:
                super().invokeBrowser("firefox")
            elif "edge" in command1:
                super().invokeBrowser("edge")
            elif "opera" in command1:
                super().invokeBrowser("opera")
            elif "safari" in command1:
                super().invokeBrowser("safari")
            else:
                super().invokeBrowser()
        if Processed_Final_Text == "launch url method":
            if "*" in commandOne:
                first = commandOne.find("*")
                last = commandOne.rfind("*")
                print(commandOne[first+1:last])
                super().openURL(commandOne[first+1:last])
            else:
                super().openURL()

        if Processed_Final_Text == "quit browser method":
            super().quitBrowser()

    
