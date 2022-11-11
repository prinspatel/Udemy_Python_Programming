import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\driver\chromdriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
    value = checkbox.get_attribute("value")
    if value == "option2":
        checkbox.click()
        break

radiobuttons = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
radiobuttons[2].click() #it will click second radiobutton

#for loop click one by one all the radio button
for radio in radiobuttons:
    radio.click()
    print(radio.is_selected())

time.sleep(2)