from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Chrome driver Path
PATH = '/Users/christophernichols/Downloads/chromedriver'

driver = webdriver.Chrome(PATH)
driver.get('https://origenrealty.com')

time.sleep(3)

# Click the "Contact" menu item
driver.find_element(By.XPATH, '//*[@id="menu-item-273"]/a').click()

time.sleep(3)

# Find the form elements
name_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/span[1]/input')
email_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/div/span[1]/input')
phone_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/div/span[2]/input')
message_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/span[2]/input')

# Enter the form values
name_field.send_keys("test")
email_field.send_keys("Testuser@mail.com")
phone_field.send_keys("7777777777")
message_field.send_keys("test message")

# Find the submit button element
submit_button = driver.find_element(By.XPATH, "//*[@id='wpcf7-f271-p272-o1']/form/div[2]/input")

# Click the submit button
submit_button.click()

# To keep chrom open
time.sleep(30)

# To close chrome
driver.quit()
