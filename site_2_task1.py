from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_value_1():
    url = 'http://demo.guru99.com/test/newtours/register.php'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)
    chrome.fullscreen_window()

    fn = chrome.find_element(By.NAME, 'firstName')
    fn.send_keys("Egor")
    sn = chrome.find_element(By.NAME, 'lastName')
    sn.send_keys("Ablovacky")
    ph = chrome.find_element(By.NAME, 'phone')
    ph.send_keys("123456789")
    email = chrome.find_element(By.NAME, 'userName')
    email.send_keys("egor@mail.ru")

    address = chrome.find_element(By.NAME, 'address1')
    address.send_keys("Lobonka, 1")
    city = chrome.find_element(By.NAME, 'city')
    city.send_keys("Minsk")
    state = chrome.find_element(By.NAME, 'state')
    state.send_keys("Minskaya")
    postal = chrome.find_element(By.NAME, 'postalCode')
    postal.send_keys("220000")
    country = chrome.find_element(By.NAME, 'country')
    country.click()
    country_1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'BELARUS')]")
    country_1.click()

    user = chrome.find_element(By.NAME, 'email')
    user.send_keys("egor@mail.ru")
    password = chrome.find_element(By.NAME, 'password')
    password.send_keys("12345")
    c_password = chrome.find_element(By.NAME, 'confirmPassword')
    c_password.send_keys("12345")

    button = chrome.find_element(By.NAME, 'submit')
    button.click()
    time.sleep(3)


    name_second = 'Egor Ablovacky'
    second_page = chrome.find_element(By.XPATH, "//*[contains(text(), 'Egor Ablovacky')]").text
    assert name_second == second_page

    name_user = 'egor@mail.ru'
    check_user = chrome.find_element(By.XPATH, "//*[contains(text(), 'egor@mail.ru')]").text
    assert name_user == check_user




