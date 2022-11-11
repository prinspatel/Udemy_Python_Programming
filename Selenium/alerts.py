import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()  # maximize window
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Prince")
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()
time.sleep(3)

alerbox = driver.switch_to.alert
message = alerbox.text
alerbox.accept()
# to press cancel use decline
# alerbox.dismiss()


print(message)

driver.close()