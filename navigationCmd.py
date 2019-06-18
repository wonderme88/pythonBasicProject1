from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="")
driver.get("https://www.youtube.com")
time.sleep(5)

print(driver.title)

driver.back()
time.sleep(5)

print(driver.title)

driver.forword()
time.sleep(5)

print(driver.title)




