import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, NAME, CPATH, CSSselector, Class name, linktext

driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("aBc@123")
driver.find_element(By.ID, "exampleCheck1").click() #checkbox

# XPATH     //tagname[@attribute='value]
# css selector tagname[attribut='value']

driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("prins")
Message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(Message)
assert "Success" in Message   # check test pass or fail

driver.close()