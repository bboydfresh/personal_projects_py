from selenium import webdriver
import time
def Login_to_Indeed(driver):
    SignInButton = driver.find_element_by_xpath('//*[@id="gnav-main-container"]/div/div/div[3]/div[3]/a/span')
    SignInButton.click()
    EmailPrompt = driver.find_element_by_xpath('//*[@id="login-email-input"]')
    EmailPrompt.send_keys('username@username.com')
    PasswordPrompt = driver.find_element_by_xpath('//*[@id="login-password-input"]')
    PasswordPrompt.send_keys('password')
    ClickLoginButton = driver.find_element_by_xpath('//*[@id="login-submit-button"]')
    ClickLoginButton.click()
def closepopup(driver):
    yeetpopup = driver.find_element_by_xpath('//*[@id="popover-x"]/a')
    yeetpopup.click()
def Apply_to_Job(driver):
    while True:
        try:
            time.sleep(3)
            Indeed_Apply_Button = driver.find_element_by_class_name('indeed-apply-button') 
            Indeed_Apply_Button.click()
            time.sleep(2)
            Press_Continue = driver.find_element_by_class_name('icl-button ')
            Press_Continue.click()
            print('Great Success!')
        except Exception:
            Press_X = driver.find_element_by_class_name('popover-x-span')
            Press_X.click()
            return True
        except Exception:
            See_JavaScript_Void = driver.find_element_by_partial_link_text('void(0)')
            Press_X_Applied_Job_Already = driver.find_elements_by_class_name('icl-CloseButton ')
            Press_X_Applied_Job_Already.click()
            print('Already Applied to job!')
        except Exception:
            Close_PopUp_X = driver.find_element_by_class_name('close-popup dismiss-apply')
            Close_PopUp_X.click()
            


def Close_Popup2(driver):
    ClickX = driver.find_element_by_id('popover-x')
    ClickX.click()


driver = webdriver.Chrome(executable_path=r'/Users/user/Downloads/chromedriver')
driver.get('https://ca.indeed.com/jobs?q=data+scientist&l=Canada')
time.sleep(5)
Login_to_Indeed(driver)
time.sleep(4)
while True:
    try:
        jobname = driver.find_element_by_class_name('jobtitle ')
        jobname.click()
        Apply_to_Job(driver)
    except Exception:
        closepopup(driver)
    except Exception:
        Close_Popup2(driver)
    except Exception:
        driver.switch_to_window(driver.window_handles[0])
        print('this is an external job posting')
    except Exception: 
        dislike = driver.find_element_by_xpath('//*[@id="tt_set_0"]/div/button[2]')
        dislike.click()
        
