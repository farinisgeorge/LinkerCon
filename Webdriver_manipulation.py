from selenium import webdriver
import concurrent.futures
from itertools import repeat

#Function that initialize the webdriver options
def set_options():

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("disable-infobars")
    options.add_experimental_option("excludeSwitches", ['enable-automation']);
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("start-maximised")
    options.add_argument("user-agent=whatever you want")
    return options

#Function that creates a webdriver instance
def webdriver_spawn(num,options):

    browser=webdriver.Chrome('chromedriver', options=options)
    browser.implicitly_wait(12)
    return browser


#Function that closes a webdriver instance
def webdriver_kill(browser,num):

    browser.quit()
    return

def multikill(parallel_pages,drivers):
 #Multithreading the call of webdriver_kill function, which closes every browser instance
    for k in range(parallel_pages):
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            p_drivers=executor.map(webdriver_kill, drivers[k][:], list(range(20)),timeout=None)


def multispawn(parallel_pages):
    browsers = []
    # Create a number of webdriver instances that are needed to scrape in parallel
    for i in range(parallel_pages):
        p_drivers2 = []
        with concurrent.futures.ThreadPoolExecutor(
                max_workers=None) as executor:  # Multithreading the webdriver instances creation with 20 threads
            p_drivers = executor.map(webdriver_spawn, list(range(20)), repeat(set_options()),
                                     timeout=None)  # Call webdriver_spawn function with each thread
            for p_driver in p_drivers:
                p_drivers2.append(p_driver)
            browsers.append(p_drivers2)
    return browsers