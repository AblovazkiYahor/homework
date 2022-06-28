from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_value():
    url = 'https://demoqa.com/select-menu'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)
    chrome.fullscreen_window()
    dropdown_value = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select Option')]")
    dropdown_value.click()
    time.sleep(2)

    dropdown_inf = chrome.find_element(By.XPATH, "//*[contains(text(), 'Group 1, option 1')]")
    dropdown_inf.click()
    time.sleep(4)

    dropdown_one = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select Title')]")
    dropdown_one.click()
    time.sleep(3)

    dropdown_inf_1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Dr.')]")
    dropdown_inf_1.click()
    time.sleep(3)

    dropdown_old = chrome.find_element(By.ID, 'oldSelectMenu')
    dropdown_old.click()
    time.sleep(3)

    dropdown_old_1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Green')]")
    dropdown_old_1.click()
    time.sleep(3)

    drop_multi = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select...')]")
    drop_multi.click()
    time.sleep(3)
    value_multi = chrome.find_element(By.XPATH, "//*[contains(text(), 'Black')]")
    value_multi.click()
    time.sleep(3)

    dropdown_test = chrome.find_element(By.XPATH, "//*[contains(text(), 'Group 1, option 1')]").text
    drop_test_1 = 'Group 1, option 1'
    assert dropdown_test == drop_test_1

    dropdown_inf_1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Dr.')]").text
    drop_test_2 = 'Dr.1'
    assert dropdown_inf_1 == drop_test_2

    dropdown_old_1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Green')]").text
    drop_test_3 = 'Green'
    assert dropdown_old_1 == drop_test_3

    value_multi = chrome.find_element(By.XPATH, "//*[contains(text(), 'Black')]").text
    drop_test_4 = 'Black'
    assert drop_test_4 == value_multi















