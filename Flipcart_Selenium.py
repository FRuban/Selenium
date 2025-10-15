from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time

driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
driver.maximize_window()

a = driver.find_element(By.XPATH, '//*[@id="searchbox_input"]')
time.sleep(2)
a.send_keys("Flipkart")
a.send_keys(Keys.RETURN)
time.sleep(2)

b = driver.find_element(By.XPATH,'//*[@id="r1-0"]/div[3]/h2/a/span')
b.click()
time.sleep(2)

c = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[1]/div[2]/form/div/div/input')
c.send_keys("5g Mobiles")
c.send_keys(Keys.RETURN)
time.sleep(2)

d = driver.find_elements(By.CLASS_NAME, 'CGtC98')

if d:
    e = random.choice(d)
    driver.execute_script("arguments[0].scrollIntoView();", e)
    e.click()
    time.sleep(5)

# it will move to the new tab that opened after it randomaly click it's product[-1]-Represents a new tab or recent tab that open and we tell that selenium to move on to next tab
driver.switch_to.window(driver.window_handles[-1])
time.sleep(2)

f = driver.find_element(By.CLASS_NAME, 'QqFHMw').click()
time.sleep(2)

g = driver.find_element(By.CLASS_NAME,'zA2EfJ').click()
time.sleep(2)

h = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]/div/form/div[1]/input')
h.send_keys("8667570687")
h.send_keys(Keys.RETURN)
time.sleep(2)

i = driver.find_element(By.CLASS_NAME,'_7Pd1Fp').click()
time.sleep(5000)

