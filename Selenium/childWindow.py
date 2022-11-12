import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()

tab = driver.window_handles #it will create list of all the windows open in list

driver.switch_to.window(tab[1])
print(driver.find_element(By.TAG_NAME,"h3").text)

driver.switch_to.window(tab[0])
print(driver.find_element(By.TAG_NAME, "h3").text)

driver.quit()