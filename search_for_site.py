from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_search_by_css_xpath_class():
    url = 'https://ultimateqa.com/complicated-page/'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)


    time.sleep(2)

    xpath = chrome.find_element(By.XPATH, '//a[@class="et_pb_button et_pb_button_4 et_pb_bg_layout_light"]')
    xpath.click()

    time.sleep(2)

    css = chrome.find_element(By.CSS_SELECTOR, ".et_pb_button.et_pb_button_4.et_pb_bg_layout_light")
    css.click()

    time.sleep(2)

    class_name = chrome.find_element(By.CLASS_NAME, "et_pb_button, et_pb_button_4, et_pb_bg_layout_light")
    class_name.click()



