from selenium import webdriver
import time
from random import random

driver = webdriver.Chrome(executable_path=r'/Users/donalddang/Downloads/chromedriver 2')
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
                    try:
                        try:
                            rand = random()
                            if rand > 0.25:
                                time.sleep(5)
                                SwipeRight(driver)
                            else:
                                time.sleep(4)
                                SwipeLeft(driver)
                        except Exception:
                            time.sleep(20)
                            Its_A_Match = driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[4]/button')
                            Its_A_Match.click()
                    except Exception:
                        time.sleep(16)
                        Dont_Add_Tinder_To_Home_Screen = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
                        Dont_Add_Tinder_To_Home_Screen.click()
                except Exception:
                    time.sleep(5)
                    Maybe_Later = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
                    Maybe_Later.click()
            except Exception:
                Tinder_Plus = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button')
                Tinder_Plus.click()
                Press_Back = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/div/div[1]/button')
                Press_Back.click()
        except Exception:
            Dontsuperlike = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')
            Dontsuperlike.click()
def AcceptTerms(driver):
    time.sleep(10)
    AcceptTerms = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    AcceptTerms.click()
    time.sleep(5)

def PhoneLogin(driver):
    ClickLogin = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button')
    ClickLogin.click()
    time.sleep(4)
    LoginWithPhone = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[3]/button')
    LoginWithPhone.click()
    time.sleep(8)
    EnterPhone = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
    EnterPhone.send_keys('1111111111')
    ClickContinue = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
    ClickContinue.click()
    time.sleep(30) #this is a long sleep because I need to confirm my phone number, lol. It's not fully automated due to 2FA
    ClickNextContinue = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
    ClickNextContinue.click()
    time.sleep(60) #this is a long sleep because I need to confirm my email, lol. It's not fully automated due to 2FA
    ConfirmEmail = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
    ConfirmEmail.click()
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
        PhoneLogin(driver)
        while True:
            try:
                AllowLocation(driver)
                try:
                    EnableNotifs(driver)
                except Exception:
                    Auto_Swipe(driver)
            except Exception:
                Auto_Swipe(driver)
