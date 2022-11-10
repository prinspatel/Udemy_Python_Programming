from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()  # maximize window
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/lifetime-access")  # second website
driver.minimize_window()  # minimize window

driver.back()  # back to first website
driver.refresh()  # refresh window
driver.maximize_window()
driver.forward()  # go back to second website

driver.close()