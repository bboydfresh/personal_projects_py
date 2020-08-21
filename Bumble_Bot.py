from selenium import webdriver
import time
from random import random

driver = webdriver.Chrome(executable_path=r'/Users/donalddang/Downloads/chromedriver')
driver.get('https://bumble.com/get-started')

time.sleep(10)
ClickFacebook = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
ClickFacebook.click()
#this part logs into Facebook
time.sleep(10)
driver.switch_to_window(driver.window_handles[1])
Username = driver.find_element_by_xpath('//*[@id="email"]')
Username.send_keys('lonelyguy082@gmail.com')
time.sleep(2)
Password = driver.find_element_by_xpath('//*[@id="pass"]')
Password.send_keys('Breakdance4l1f3')
time.sleep(2)
ClickLoginFB = driver.find_element_by_xpath('//*[@id="loginbutton"]')
ClickLoginFB.click()
time.sleep(8)
#AcceptPermissions = driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button')
#AcceptPermissions.click()
#Now that I've logged into Facebook, we shall now like away!
driver.switch_to_window(driver.window_handles[0])
time.sleep(6)
while True:
    time.sleep(14)
    #try:
    rand = random()
    if rand < .73:
        Hot = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span')
        Hot.click()
    else:
        NotHot = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span')
        NotHot.click()
    