import selenium
import properties
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(properties.Launch_URL)
driver.close()
