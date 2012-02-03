import time
import urllib
import urlparse
import sys

from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "GASelenium")

GOOGLE_URL = "http://www.google.com/?%s"
BASE_QUERY = {'q':None,'hl':'fr'}

domain = sys.argv[1]
keywords = open(sys.argv[2]).read().split('\n')
max_pages = 20
if len(sys.argv) >= 4:
    max_pages = int(sys.argv[3])

def check_domain(url):
    if not url.startswith('http://www.google'):
        return url.startswith(domain)
    o = urlparse.urlparse(url)
    params = o.query.split('&')
    for param in params:
        if param.startswith('url='):
            rdomain = urllib.unquote(param[4:])
            return domain == rdomain
    return False

def watch_results(browser):
    results = browser.find_elements_by_class_name('r')
    for result in results:
        if check_domain(result.find_elements_by_tag_name('a')[0].get_attribute('href')):
            result.find_elements_by_tag_name('a')[0].click()
            time.sleep(2)
            return True
    return False

browser = webdriver.Firefox(profile) # Get local session of firefox
for keyword in keywords:
    query = BASE_QUERY
    query['q'] = keyword
    url = GOOGLE_URL%urllib.urlencode(query)
    browser.get(url)
    browser.find_element_by_name('btnG').click()
    time.sleep(1)

    for i in range(1, max_pages):
        if watch_results(browser) == False:
            browser.find_element_by_css_selector('#nav .b:last-child a').click()
            time.sleep(1)
        else:
            break;
    browser.delete_all_cookies()

browser.close()
