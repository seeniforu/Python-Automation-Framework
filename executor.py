import properties
from baseClass import baseMethods
import requests
from datetime import datetime
import json

temp_dic = {}

class Executor(baseMethods):
    def  __init__(self,driver = None, Test_name = None, Test_id = None):
        self.driver = driver
        self.Test_name = Test_name
        self.Test_id = Test_id
        super().__init__(self.driver, self.Test_name, self.Test_id)
    
    def getResponse(self, command_from_user):
        try:
            command_to_API = requests.get('http://54.152.205.59/getResponse?name='+command_from_user)
            #command_to_API = requests.get('http://localhost:8080/getResponse?name='+command_from_user)
            API_response_process = json.loads(command_to_API.text)
            self.getcache(command_from_user, API_response_process["response"])
        except Exception as e:
            print(e)
        return API_response_process["response"]

    def getcache(self, user_commanad, response):
        current_time = datetime.now()
        temp_dic["Time"] = current_time.strftime("%m/%d/%Y, %H:%M:%S")
        temp_dic[user_commanad] = response
    
    def getParameters(self, commandOne):
        if "*" in commandOne:
            first = commandOne.find("*")
            last = commandOne.rfind("*")
        return commandOne[first+1:last]

    def execute(self,commandOne, locator=None):
        if commandOne == None or len(commandOne) == 0 or commandOne == " ":
            print("Command/Argument passed is empty or Null")
        else:
            command_from_user = commandOne.lower()
            Processed_Final_Text = self.getResponse(command_from_user)
            if Processed_Final_Text == "launch browser method":
                if "chrome" in command_from_user:
                    super().invokeBrowser("chrome")
                elif "firefox" in command_from_user:
                    super().invokeBrowser("firefox")
                elif "edge" in command_from_user:
                    super().invokeBrowser("edge")
                elif "opera" in command_from_user:
                    super().invokeBrowser("opera")
                elif "safari" in command_from_user:
                    super().invokeBrowser("safari")
                else:
                    super().invokeBrowser(properties.Browser_Name)

            elif Processed_Final_Text == "launch url method":
                if "*" in commandOne:
                    super().openURL(self.getParameters(commandOne))
                else:
                    super().openURL(properties.Launch_URL)

            elif Processed_Final_Text == "page load time" or Processed_Final_Text == "implicit wait time":
                self.setProperties(commandOne)

            elif Processed_Final_Text == "click element method":
                if "*" in commandOne:
                    super().click_Element(self.getParameters(commandOne))
                else:
                    super().click_Element(locator)
            
            elif Processed_Final_Text == "click element using id":
                if "*" in commandOne:
                    super().click_Element_by_id(self.getParameters(commandOne))
                else:
                    super().click_Element_by_id(locator)

            elif Processed_Final_Text == "click element using xpath":
                if "*" in commandOne:
                    super().click_Element_by_xpath(self.getParameters(commandOne))
                else:
                    super().click_Element_by_xpath(locator)
            
            elif Processed_Final_Text == "click element using name":
                if "*" in commandOne:
                    super().click_Element_by_name(self.getParameters(commandOne))
                else:
                    super().click_Element_by_name(locator)

            elif Processed_Final_Text == "click element using class name":
                if "*" in commandOne:
                    super().click_Element_by_class_name(self.getParameters(commandOne))
                else:
                    super().click_Element_by_class_name(locator)
            
            elif Processed_Final_Text == "click element using css selector":
                if "*" in commandOne:
                    super().click_Element_by_css_selector(self.getParameters(commandOne))
                else:
                    super().click_Element_by_css_selector(locator)

            elif Processed_Final_Text == "click element using link text":
                if "*" in commandOne:
                    super().click_Element_by_link_text(self.getParameters(commandOne))
                else:
                    super().click_Element_by_link_text(locator)

            elif Processed_Final_Text == "click element using partial link text":
                if "*" in commandOne:
                    super().click_Element_by_partial_link_text(self.getParameters(commandOne))
                else:
                    super().click_Element_by_partial_link_text(locator)

            elif Processed_Final_Text == "thread sleep":
                if "*" in commandOne:
                    super().threadSleep(self.getParameters(commandOne))

            elif Processed_Final_Text == "quit browser method":
                super().quitBrowser()

            elif Processed_Final_Text == "teardown method":
                super().tearDown()
    
    def setProperties(self, property):
        properties = property.lower()
        Processed_Final_Text = self.getResponse(properties)
        if Processed_Final_Text == "page load time":
            if "*" in property:
                super().pageLoad(self.getParameters(properties))
            else:
                super().pageLoad()
        if Processed_Final_Text == "implicit wait time":
            if "*" in property:
                super().implicitlyWait(self.getParameters(properties))
            else:
                super().implicitlyWait()
        
        


    
