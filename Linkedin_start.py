from time import sleep,time
from selenium.webdriver import ActionChains
from Webdriver_manipulation import webdriver_spawn,webdriver_kill,set_options
from liker import feed_liker,hashtagliker_profileview
from logging import log


userid="farinisgiorgos@gmail.com"
password=".,.,.,Gefo"

start_time = time()
options = set_options()
browser = webdriver_spawn(1, options)
action=ActionChains(browser)


try:

    browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    sleep(5)
    browser.find_element_by_xpath("""//*[@id="username"]""").send_keys(userid)
    browser.find_element_by_xpath("""//*[@id="password"]""").send_keys(password)
    login_button=browser.find_element_by_class_name('btn__primary--large.from__button--floating')
    action.move_to_element(login_button).click().perform()
    print("Got into profile!")

    feed_liker(browser, 150, 4)
    hashtaglist = ['machinelearning','webdevelopment', 'ai','python','javascript','engineering','devops']
    # hashtaglist = ['machinelearning','google','microsoft','googledevelopers','accenture','artificialintelligence']
    hashtagliker_profileview(browser, 20, 4, hashtaglist)



except Exception as err:
            print('\nUpdate failed!\n')
            browser.save_screenshot('error.png')
            log(error=err)
finally:
    end_time=time()
    print(f'Total executing time: {str((end_time-start_time)/60)} minutes')
    webdriver_kill(browser,1)
