from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_checkbox():
    url = 'http://the-internet.herokuapp.com/dynamic_controls'
    chrome = webdriver.Chrome('./chromedriver')
    chrome.get(url)

    check = chrome.find_element(By.XPATH, '//input[@type="checkbox"]').click()
    chrome.find_element(By.XPATH, '//button[contains(text(),"Remove")]').click()
    try:
        WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="message"]')))
    finally:
        print('Тест прошел')

    assert check is None

    chrome.find_element(By.XPATH, '//button[contains(text(),"Enable")]').click()
    text = chrome.find_element(By.XPATH, '//p[@id="message"]')
    t = "It's time"
    assert t in text













