import properties
from baseClass import baseMethods
import requests
from datetime import datetime

temp_dic = {}

class Executor(baseMethods):
    def  __init__(self,driver, Test_name = None, Test_id = None):
        self.driver = driver
        self.Test_name = Test_name
        self.Test_id = Test_id
        super().__init__(self.driver, self.Test_name, self.Test_id)
    
    def getResponse(self, command_from_user):
        command_to_API = requests.get('http://54.152.205.59/index?name='+command_from_user)
        API_response_process = command_to_API.text
        self.getcache(command_from_user, API_response_process.strip('\"'))
        return API_response_process.strip('\"')

    def getcache(self, user_commanad, response):
        current_time = datetime.now()
        temp_dic["Time"] = current_time.strftime("%m/%d/%Y, %H:%M:%S")
        temp_dic[user_commanad] = response

    def execute(self,commandOne):
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

            if Processed_Final_Text == "launch url method":
                if "*" in commandOne:
                    first = commandOne.find("*")
                    last = commandOne.rfind("*")
                    super().openURL(commandOne[first+1:last])
                else:
                    super().openURL(properties.Launch_URL)

            if Processed_Final_Text == "page load time" or Processed_Final_Text == "implicit wait time":
                self.setProperties(commandOne)
            
            if Processed_Final_Text == "click element using link text":
                if "*" in commandOne:
                    first = commandOne.find("*")
                    last = commandOne.rfind("*")
                    super().click_Element_by_link_text(commandOne[first+1:last])

            if Processed_Final_Text == "quit browser method":
                super().quitBrowser()
    
    def setProperties(self, property):
        properties = property.lower()
        Processed_Final_Text = self.getResponse(properties)
        if Processed_Final_Text == "page load time":
            if "*" in property:
                first = property.find("*")
                last = property.rfind("*")
                super().pageLoad(property[first+1:last])
            else:
                super().pageLoad()
        if Processed_Final_Text == "implicit wait time":
            if "*" in property:
                first = property.find("*")
                last = property.rfind("*")
                super().implicitlyWait(property[first+1:last])
            else:
                super().implicitlyWait()
        
        


    
