from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import random

def feed_liker(browser,posts,wait):

    url = "https://www.linkedin.com/feed/"

    # Open url with driver
    browser.get(url)
    count=0
    refresh_flag = False
    while count<=posts:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(random.uniform(wait,wait*2))

        feedcotainers = browser.find_elements_by_xpath('//div[contains(@class,"relative ember-view") ]')

        for container in feedcotainers:
            if count > posts:
                break
            likelist = container.find_elements_by_xpath(
                './/button[contains(@class,"react-button__trigger artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view")]')

            if len(likelist)>0:
                like=likelist[0]
                if like.get_attribute('aria-pressed') == 'false':

                    print('Post ' + str(count)+ ' on feed.')
                    count += 1

                    action = ActionChains(browser)
                    sleep(random.random())
                    action.move_to_element(like).click().perform()
                    sleep(random.uniform(wait,wait*2))
                    if count % 15 == 0 and count>0:
                        refresh_flag = True
        if refresh_flag==True:
            refresh_flag=False
            browser.refresh()
            print('Updated the page because we reached ' + str(count) + 'posts!')
            sleep(random.uniform(wait,wait*2.5))



def hashtagliker_profileview(browser,posts,wait,hashtaglist):
    for hashtag in hashtaglist:
        print('In hashtag: #'+ hashtag)
        url = "https://www.linkedin.com/feed/hashtag/" + hashtag

        # Open url with driver
        browser.get(url)
        linkslist=[]
        count = 0
        refresh_flag = False
        while count <= posts:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            sleep(random.uniform(wait,wait*2))
            feedcotainers=browser.find_elements_by_xpath('//div[contains(@class,"relative ember-view") ]')

            for container in feedcotainers[count:]:
                if count>posts:
                    break
                likelist = container.find_elements_by_xpath(
                    './/button[contains(@class,"react-button__trigger artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view")]')
                if len(likelist) > 0:
                    like = likelist[0]
                    if like.get_attribute('aria-pressed')=='false':

                        print('Post ' + str(count) + ' in hashtag ' + '#'+ hashtag)
                        count += 1

                        action = ActionChains(browser)
                        sleep(wait + random.random())
                        action.move_to_element(like).click().perform()
                        sleep(random.uniform(wait,wait*2))

                        profilelink_list= container.find_elements_by_xpath('.//a[contains(@class,"feed-shared-actor__container-link relative display-flex flex-grow-1 app-aware-link ember-view") ]')
                        if len(profilelink_list)>0:
                            linkslist.append(profilelink_list[0].get_attribute('href'))
                        if count % 15 == 0 and count > 0:
                            refresh_flag = True

            if refresh_flag == True:
                refresh_flag = False
                browser.get(url)
                print('Updated the page because we reached ' + str(count) + 'posts!')
                sleep(random.uniform(wait,wait*2.5))


        prof_count=0
        for profile in linkslist:
            print('Viewing Profile '+str(prof_count)+' of hashtag #'+hashtag)
            browser.get(profile)
            sleep(random.uniform(wait,wait*3))
            prof_count += 1
