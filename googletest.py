import time
import urllib
import urlparse
import sys

from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (GASelenium; X11; Gaselenium; rv:9.0.1) Gecko/20100101 GASelenium")

GOOGLE_URL = "http://www.google.com/?%s"
BASE_QUERY = {'q':None,'hl':'fr'}

domain = sys.argv[1]
keywords = open(sys.argv[2]).read().split('\n')

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

browser = webdriver.Firefox(profile) # Get local session of firefox

for keyword in keywords:
    query = BASE_QUERY
    query['q'] = keyword
    url = GOOGLE_URL%urllib.urlencode(query)
    browser.get(url)
    browser.find_element_by_name('btnK').click()
    time.sleep(1)
    results = browser.find_elements_by_class_name('l')

    for result in results:
        if check_domain(result.get_attribute('href')):
            result.click()
            time.sleep(2)
            break
    time.sleep(2)
    browser.delete_all_cookies()

browser.close()
