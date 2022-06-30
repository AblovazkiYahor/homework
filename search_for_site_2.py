import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Test_search_site():
    # Проверка наличия сообщения "Form filled out successfully"
    @pytest.mark.xfail
    def test_valid_1(self):
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome = webdriver.Chrome('./chromedriver')
        chrome.get(url)

        name = chrome.find_element(By.ID, 'et_pb_contact_name_0')
        name.send_keys('Egor')
        time.sleep(2)

        mess = chrome.find_element(By.ID, 'et_pb_contact_message_0')
        mess.send_keys('Привет')
        time.sleep(2)

        button1 = chrome.find_element(By.CLASS_NAME, 'et_pb_contact_submit, et_pb_button')
        button1.click()

        exp_text = 'Form filled out successfully'
        fact_text = chrome.find_element(By.CLASS_NAME, 'et-pb-contact-message').text
        assert exp_text == fact_text
        chrome.close()

    def test_valid_2(self):

        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome = webdriver.Chrome('./chromedriver')
        chrome.get(url)

        name_1 = chrome.find_element(By.ID, 'et_pb_contact_name_0')
        name_1.send_keys('Egor')
        time.sleep(2)

        button2 = chrome.find_element(By.CLASS_NAME, 'et_pb_contact_submit, et_pb_button')
        button2.click()

        exp_text = chrome.find_element(By.CLASS_NAME, 'et-pb-contact-message').text
        assert exp_text == 'Please, fill in the following fields:\nMessage'
        chrome.close()

    def test_valid_3(self):
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome = webdriver.Chrome('./chromedriver')
        chrome.get(url)

        name_2 = chrome.find_element(By.ID, 'et_pb_contact_message_0')
        name_2.send_keys('Egor')
        time.sleep(2)

        button3 = chrome.find_element(By.CLASS_NAME, 'et_pb_contact_submit, et_pb_button')
        button3.click()

        exp_text1 = chrome.find_element(By.CLASS_NAME, 'et-pb-contact-message').text
        assert exp_text1 == 'Please, fill in the following fields:\nName'
        chrome.close()








