import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.double_click()
#action.context_click()
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//a[.='Reload']")).click().perform()
time.sleep(2)


driver.close()