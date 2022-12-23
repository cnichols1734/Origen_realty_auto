from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome driver Path
PATH = '/Users/christophernichols/Downloads/chromedriver'

driver = webdriver.Chrome(PATH)
driver.get('https://origenrealty.com')

# Sleep to allow site to load
time.sleep(.5)

# Click the "Contact" menu item
driver.find_element(By.XPATH, '//*[@id="menu-item-273"]/a').click()

# Sleep to allow site to load
time.sleep(1)

# Scroll down 1/5 of the page
scroll_amount = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, "
"document.documentElement.clientHeight, document.documentElement.scrollHeight, "
"document.documentElement.offsetHeight );") / 5
driver.execute_script(f"window.scrollTo(0, {scroll_amount});")

# Find the form elements
name_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/span[1]/input')
email_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/div/span[1]/input')
phone_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/div/span[2]/input')
message_field = driver.find_element(By.XPATH, '//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/span[2]/input')
other_comments = driver.find_element(By.XPATH,'//*[@id="wpcf7-f271-p272-o1"]/form/div[2]/span[3]/textarea')

# Enter the form values
name_field.send_keys("Test Software")
email_field.send_keys("Testuser@mail.com")
phone_field.send_keys("7777777777")
message_field.send_keys("Test message")
other_comments.send_keys("This is written by automated software :)")

# Find the submit button element
submit_button = driver.find_element(By.XPATH, "//*[@id='wpcf7-f271-p272-o1']/form/div[2]/input")

# Click the submit button
#submit_button.click()

# To keep chrom open
time.sleep(30)

# To close chrome
driver.quit()
