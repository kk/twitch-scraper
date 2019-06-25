from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

available = []

textfile = open("textfiles/4-letter-words.txt", "r")
handles = textfile.read().splitlines()
#handles = [x for x in handles if len(x) > 3]

browser = webdriver.Chrome("./chromedriver")
browser.get("https://www.twitch.tv/signup")

#browser.implicitly_wait(5)
#elem = browser.find_element_by_link_text('Download')
print(len(browser.find_elements_by_css_selector(".tw-c-text-error")))
#elem1 = browser.find_element_by_css_selector(".tw-c-text-error")
elem = browser.find_element_by_css_selector("input[type='text']")
for handle in handles:
    elem.send_keys(handle)
    time.sleep(1.3)
    err_message_count = len(browser.find_elements_by_css_selector(".tw-c-text-error")) # 1 if name available and 2/3 if taken

    if err_message_count == 1:
        print(handle + " is available")
        available.append(handle)
        print(available)
    else:
        print(handle + " is not available")
        
    elem.send_keys(Keys.CONTROL + "a")
    elem.send_keys(Keys.DELETE)

#elem.send_keys('woo')
#time.sleep(1)
#print(len(browser.find_elements_by_css_selector(".tw-c-text-error")))
#elem.send_keys(Keys.CONTROL + "a")
#elem.send_keys(Keys.DELETE)

#elem.send_keys('wehdiwuedhie')
#time.sleep(1)
#print(len(browser.find_elements_by_css_selector(".tw-c-text-error")))
#elem.send_keys(Keys.CONTROL + "a")
#elem.send_keys(Keys.DELETE)

#elem.send_keys('drtgerggergergeg')
#print(len(browser.find_elements_by_css_selector(".tw-c-text-error")))
#elem.send_keys(Keys.DELETE)
#tw-c-text-error tw-font-size-7
#elem.click()
#searchBar = browser.find_element_by_id('q')
#elem = browser.find_element_by_class_name('tw-font-size-6 tw-full-width tw-input tw-pd-l-1 tw-pd-r-1 tw-pd-y-05')
#print(elem.text)
#elem.send_keys('testo')
#if len(browser.find_element_by_css_selector("input[type='text']")) > 0:
#    print("found it")
#else:
#    print("found nuttin")
#print(x.text)
#username_input = browser.find_element_by_class_name('tw-block tw-border-bottom-left-radius-medium tw-border-bottom-right-radius-medium tw-border-top-left-radius-medium tw-border-top-right-radius-medium tw-font-size-6 tw-full-width tw-input tw-pd-l-1 tw-pd-r-1 tw-pd-y-05')

#print(username_input)
#username_input.send_keys('testo')

#searchBar.send_keys('download')
#searchBar.sendkeys(Keys.ENTER)
