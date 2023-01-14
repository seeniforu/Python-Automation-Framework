import properties
from baseClass import baseMethods
import requests

class Executor(baseMethods):
    def  __init__(self,driver, Test_name = None):
        self.driver = driver
        self.Test_name = Test_name
        super().__init__(self.driver, self.Test_name)

    def execute(self,commandOne):
        if commandOne == None or len(commandOne) == 0 or commandOne == " ":
            print("Command/Argument passed is empty or Null")
        else:
            command1 = commandOne.lower()
            command_to_API = requests.get('http://54.152.205.59/index?name='+command1)
            API_response_process = command_to_API.text
            Processed_Final_Text = API_response_process.strip('\"')
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
                    super().invokeBrowser(properties.Browser_Name)

            if Processed_Final_Text == "launch url method":
                if "*" in commandOne:
                    first = commandOne.find("*")
                    last = commandOne.rfind("*")
                    super().openURL(commandOne[first+1:last])
                else:
                    super().openURL(properties.Launch_URL)

            if Processed_Final_Text == "quit browser method":
                super().quitBrowser()
    
    def setProperties(self, property):
        properties = property.lower()
        command_to_API = requests.get('http://54.152.205.59/index?name='+properties)
        API_response_process = command_to_API.text
        Processed_Final_Text = API_response_process.strip('\"')
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
        


    
