from selenium import webdriver
from selenium.webdriver.common.by import By


def test_frames():
    url = 'http://the-internet.herokuapp.com/frames'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)

    chrome.find_element(By.XPATH, "//a[@href='/iframe']").click()
    chrome.switch_to.frame(chrome.find_element(By.XPATH, "//iframe[@id='mce_0_ifr']"))

    text = chrome.find_element(By.XPATH, "//textarea[@id='mce_0'])")
    assert text == 'Your content goes here.'