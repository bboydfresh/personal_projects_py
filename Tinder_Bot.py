from selenium import webdriver
import time
from random import random

driver = webdriver.Chrome(executable_path=r'/Users/user/Downloads/chromedriver')
driver.get('https://tinder.com')

def SwipeRight(driver):
    Swipe_Right = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
    Swipe_Right.click()

def SwipeLeft(driver):
    Swipe_Left = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
    Swipe_Left.click()

def Auto_Swipe(driver):
    while True:
        try:
            try:
                try:
                    rand = random()
                    if rand > 0.25:
                        time.sleep(10)
                        SwipeRight(driver)
                    else:
                        time.sleep(7)
                        SwipeLeft(driver)
                except Exception:
                    time.sleep(20)
                    Its_A_Match = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
                    Its_A_Match.click()
            except Exception:
                time.sleep(16)
                Dont_Add_Tinder_To_Home_Screen = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                Dont_Add_Tinder_To_Home_Screen.click()
        except Exception:
            time.sleep(5)
            Maybe_Later = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            Maybe_Later.click()
def AcceptTerms(driver):
    time.sleep(10)
    AcceptTerms = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    AcceptTerms.click()
    time.sleep(5)

def FacebookLogin(driver):
    LoginWithFacebook = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    LoginWithFacebook.click()
    time.sleep(8)
    driver.switch_to_window(driver.window_handles[1])
    Facebook_Login = driver.find_element_by_xpath('//*[@id="email"]')
    Facebook_Login.send_keys('mzuckerberg@facebook.com')
    time.sleep(2)
    Facebook_Password = driver.find_element_by_xpath('//*[@id="pass"]')
    Facebook_Password.send_keys('myfacebookpassword')
    time.sleep(4)
    Click_login = driver.find_element_by_xpath('//*[@id="loginbutton"]')
    Click_login.click()
    time.sleep(25) #I have 2FA so I have to enter this manually, by applying a sleep function.
    driver.switch_to_window(driver.window_handles[0])

def AllowLocation(driver):
    time.sleep(10)
    Allow_Location_services = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    Allow_Location_services.click()
def EnableNotifs(driver):
    time.sleep(8)
    Enable_Notifications = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
    Enable_Notifications.click()
while True:
    try:
        AcceptTerms(driver)
    except Exception:
        FacebookLogin(driver)
        while True:
            try:
                AllowLocation(driver)
                try:
                    EnableNotifs(driver)
                except Exception:
                    Auto_Swipe(driver)
            except Exception:
                Auto_Swipe(driver)