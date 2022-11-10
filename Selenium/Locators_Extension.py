import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

services_obj = Service("C:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=services_obj)

driver.get("https://rahulshettyacademy.com/client/auth/login")

driver.find_element(By.XPATH, "/html/body/app-root/app-login/div[1]/section[2]/div/div[2]/a").click()
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("demo@gmail.com")
driver.find_element(By.XPATH, "//input[@id='userPassword']").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "button[type='submit']").click()
