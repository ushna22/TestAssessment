from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(r"C:\\selenium browser drivers\\chromedriver.exe")

driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/r")

my_Username = "ushna"
my_Password = "12345"

Username_input_box = driver.find_element(By.NAME, "username")
Password_input_box = driver.find_element(By.NAME, "current-account")
Create_button = driver.find_element(By.NAME, "Create Account")
Username_input_box.clear()
Password_input_box.clear()
Username_input_box.send_keys(my_Username)
time.sleep(2)
Password_input_box.send_keys(my_Password)
time.sleep(2)
Create_button.click()
time.sleep(30)

driver.close()
