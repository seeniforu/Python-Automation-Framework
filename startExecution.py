import os
import properties

# To start execution with results give 1, without results give 2
decider = 2

# If want to execute all cases give "all" || if not specify as "not all" 
# If "not all" is given MUST enter class and method to execute
test_case_to_execute = "not All"

test_module = "test_samples.py"
test_class = "Tests"
test_name = "test_sample_One"

def startExecutionWithResults():
    name = properties.report_Name
    try:
        if test_case_to_execute.lower() == "all":
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
        if test_case_to_execute.lower() == "all":
            os.system("py.test -v -s")
        else:
            os.system("pytest "+test_module+"::"+test_class+"::"+test_name+" -v -s")
    except Exception as e:
        print(e)

if decider == 1:
    startExecutionWithResults()
else:
    startExecutionWithoutResults()

