#Greb text from product and create list
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
products = driver.find_elements(By.XPATH, "//div[@class='products-wrapper']/div/div/h4")
list = [""]
for product in products:
    list.append(product.text)
print(list)

driver.close()