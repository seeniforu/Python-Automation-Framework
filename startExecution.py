import os
import properties

test_case_to_execute = properties.Execute_all_cases

test_module = properties.Module_Name
test_class = properties.Class_Name
test_name = properties.Test_Name

def startExecutionWithResults():
    name = properties.report_Name
    try:
        if test_case_to_execute.lower() == "yes":
            if name is None or name is "" or name is " ":
                os.system("pytest --alluredir=report/ -v -s && allure serve report/")
            else:
                os.system("pytest --alluredir="+name+"/ -v -s && allure serve "+name+"/")
        else:
            if name is None or name is "" or name is " ":
                os.system("pytest "+test_module+"::"+test_class+"::"+test_name+" --alluredir=report/ -v -s && allure serve report/")
            else:
                os.system("pytest "+test_module+"::"+test_class+"::"+test_name+" --alluredir="+name+"/ -v -s && allure serve "+name+"/")
    except Exception as e:
        print(e)

def startExecutionWithoutResults():
    try:
        if test_case_to_execute.lower() == "yes":
            os.system("py.test -v -s")
        else:
            os.system("pytest "+test_module+"::"+test_class+"::"+test_name+" -v -s")
    except Exception as e:
        print(e)

if properties.With_Results.lower() == "yes":
    startExecutionWithResults()
else:
    startExecutionWithoutResults()

