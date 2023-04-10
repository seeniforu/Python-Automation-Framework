import os
import json
import properties
import platform
import sys

allJsonTestFiles = []
withResults = "YES"

arg = sys.argv[1]
rmJson = arg[:-5].rstrip()
data = {}
forLinux = "/"
forWindows = "\\"
runningOS = None
if platform.system() == "Windows":
    runningOS = forWindows
else:
    runningOS = forLinux
try:
    with os.scandir(os.getcwd()+runningOS+"testcases"+runningOS) as entries:
        for entry in entries:
            allJsonTestFiles.append(entry.name)
    #print(allJsonTestFiles)
    for i in allJsonTestFiles:
        if "json" in i and i == arg:
            with open(os.getcwd()+runningOS+"testcases"+runningOS+i) as json_file:
                data = json.load(json_file)
                #print(data)
except Exception as e:
    print(e)

# with open(arg) as json_file:
#     data = json.load(json_file)

id = data.keys()
# print(id)
test_steps = []
j=0

for i in id:
    testcase = data[i]
    # print(testcase)
    if testcase["Test Turned ON or OFF"] == "ON" and testcase["test suite"] == "smoke":
        test_steps = testcase['testcase steps']
        # print(test_steps)
        test_name = str(testcase['test name'])
        fun = """
from executor import Executor
from selenium import webdriver as driver

def test_json_"""+str(i)+"""():
    executor = Executor(driver,\""""+test_name+"""\")
    executor.preSetup()
    for i in """+str(test_steps)+""":
        executor.execute(i)
    executor.tearDown()\n"""
        with open('test_'+rmJson+'.py','a+') as file:
            file.write(fun)
    else:
        j=j+1

if j>=1:
    print("Please ensure test suite and if Testcases are turned ON or OFF.")

findTempTest = []
try:
    with os.scandir(os.getcwd()+runningOS) as entries:
        for entry in entries:
            findTempTest.append(entry.name)
    if 'test_'+rmJson+'.py' in findTempTest and withResults == "NO":
        os.system('pytest test_'+rmJson+'.py -v -s')
    elif 'test_'+rmJson+'.py' in findTempTest and withResults == "YES":
        os.system('pytest test_'+rmJson+'.py --alluredir='+properties.report_Name+' -v -s && allure serve '+properties.report_Name)
    else:
        print("No tests Found for execution.")
except Exception as e:
    print(e)
finally:
    path = os.getcwd()+'//test_'+rmJson+'.py'
    if os.path.exists(path):
        os.remove(path)


        






