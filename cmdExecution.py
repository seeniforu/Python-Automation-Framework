import sys
import json

from selenium import webdriver as driver
from executor import Executor
from baseClass import baseMethods

arg = sys.argv[1]

with open(arg) as json_file:
    data = json.load(json_file)

def test_sample(commands):
    executor.execute(commands)

id = data.keys()
# print(id)
test_steps = []
for i in id:
    testcase = data[i]
    # print(testcase)
    if testcase["Test Turned ON or OFF"] == "ON":
        test_steps = testcase['testcase steps']
        # print(test_steps)
        test_name = testcase['test name']
        executor = Executor(driver,test_name, i)
        executor.preSetup()
        for i in test_steps:
            test_sample(i)
        executor.tearDown()





