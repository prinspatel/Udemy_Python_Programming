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
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

btn = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
for button in btn:
    button.click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//*[@id='root']/div/header/div/div[3]/div[2]/div[2]/button").click()
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
message = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(message)

time.sleep(5)
driver.close()