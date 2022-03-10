from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(r"C:\\selenium browser drivers\\chromedriver.exe")

driver.get("https://testing-assessment-foh15kew9-edvora.vercel.app/s")

my_Fullname = "ushnazahid"
my_MobileNumber = "123456"
my_DOB = "02-sep-1997"
my_gender = "female"
my_address = "pakistan"
my_Password = "54321"

Edit_button = driver.find_element(By.NAME, "Edit")

Fullname_input_box = driver.find_element(By.NAME, "fullname")
MobileNumber_input_box = driver.find_element(By.NAME, "mobileNumber")
DOB_input_box = driver.find_element(By.NAME, "dateOfBirth")
gender_input_box = driver.find_element(By.NAME, "....")
address_input_box = driver.find_element(By.NAME, "address")
Password_input_box = driver.find_element(By.NAME, "Password")
Save_button = driver.find_element(By.NAME, "Save")
Fullname_input_box.clear()
MobileNumber_input_box.clear()
DOB_input_box.clear()
gender_input_box.clear()
address_input_box.clear()
Password_input_box.clear()
Edit_button.click()
Fullname_input_box.send_keys(my_Fullname)
time.sleep(2)
MobileNumber_input_box.send_keys(my_MobileNumber)
time.sleep(2)
DOB_input_box.send_keys(my_DOB)
time.sleep(2)
gender_input_box.send_keys(my_gender)
time.sleep(2)
address_input_box.send_keys(my_address)
time.sleep(2)
Password_input_box.send_keys(my_Password)
time.sleep(2)
Save_button.click()
time.sleep(30)

driver.close()
