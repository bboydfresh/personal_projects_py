from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'/Users/donalddang/Downloads/chromedriver')
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

def Get_To_Job_Screen(driver):
    Job_Query = driver.find_element_by_class_name('jobs-search-box__text-input')
    Job_Query.send_keys('Data Scientist')
    time.sleep(2)
    Location_Query = driver.find_element_by_id('jobs-search-box-location-id-ember486')
    Location_Query.send_keys('Los Angeles, California, United States')
    time.sleep(2)
    Yeet_Messaging_popup = driver.find_element_by_xpath('//*[@id="msg-overlay"]/div[1]/header')
    Yeet_Messaging_popup.click()
    time.sleep(2)
    Search_Button = driver.find_element_by_xpath('//*[@id="ember486"]/button')
    Search_Button.click()
    print('Looking for data scientist in Los Angeles')

def Login_To_LinkedIn(driver):
    Email_Query = driver.find_element_by_id('username')
    Email_Query.send_keys('username@linkedin.com')

    Password_Query = driver.find_element_by_id('password')
    Password_Query.send_keys('password')

    try:
        Click_Button = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
        Click_Button.click()
    except Exception:
        Click_Button2 = driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[4]/button')
        Click_Button2.click()
    Click_Job_thing = driver.find_element_by_xpath('//*[@id="ember26"]')
    Click_Job_thing.click()
    time.sleep(5)

def Apply_to_Job(driver):
    Click_Job = driver.find_elements_by_class_name('//*[@id="ember2488"]')
    Click_Job.click()

    Enter_Phone_Number = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:1949206260,9014333,phoneNumber~nationalNumber)"]')
    Enter_Phone_Number.send_keys('6475741501')



    Click_Continue = driver.find_element_by_xpath('//*[@id="ember2939"]')
    Click_Continue.click()
Login_To_LinkedIn(driver)
Get_To_Job_Screen(driver)
Apply_To_Job(driver)