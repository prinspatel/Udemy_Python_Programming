from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:\Driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH, "//a[@class='blinkingText']").click()

tab = driver.window_handles

driver.switch_to.window(tab[1])
email = driver.find_element(By.XPATH, "//a[.='mentor@rahulshettyacademy.com']").text

driver.switch_to.window(tab[0])
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("abc@123")
driver.find_element(By.XPATH, "//div[@class='form-check-inline']//label[1]//span[2]").click()

dropdown_list = driver.find_elements(By.XPATH, "//div[@class='form-group'][4]")

for dropdown in dropdown_list:
    print(dropdown.text)
    if dropdown.text == "Student":
        dropdown.click()
driver.find_element(By.CSS_SELECTOR, "#terms").click()
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()


time.sleep(2)
message = driver.find_element(By.XPATH, "//*[@id='login-form']/div[1]//strong").text

print(message)

driver.quit()