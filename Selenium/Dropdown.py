import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:\driver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

'''
driver.get("https://rahulshettyacademy.com/angularpractice/")
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1) #start with 0 (to select "Male" use index "0) you can select by value as well
'''
#auto sugest dropdown list
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
#total countries display when send key "ind".
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break #after get India value the loop is exit.

print(driver.find_element(By.ID, "autosuggest").text) #when the page is ope the value is not ther so it will not ptint.
print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) #to display text
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India" #another way to know india selected or not

time.sleep(2)
driver.close()