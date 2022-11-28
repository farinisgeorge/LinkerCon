from time import sleep

def endorse(browser,people):
    url = "https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22F%22%5D&origin=MEMBER_PROFILE_CANNED_SEARCH"

    # Open url with driver
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(4)
    pages = browser.find_elements_by_class_name(
        'artdeco-pagination__indicator.artdeco-pagination__indicator--number.ember-view')

    for i in range(1, int(pages[-1].text) + 1):
        browser.get(url + "&page=" + str(i))
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        page_connections = browser.find_elements_by_class_name('search-result.search-result__occluded-item.ember-view')
        for connection in page_connections:
            conn_name = connection.find_element_by_xpath('.//span[contains(@class,"name actor-name")]').text
            print(conn_name)