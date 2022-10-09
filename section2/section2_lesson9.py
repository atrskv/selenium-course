'''

стандартный модуль Python для работы с операционной системой — os.

import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element.send_keys(file_path)

'''
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



browser = webdriver.Chrome()


# GIVEN
try:
    browser.get('http://suninjuly.github.io/file_input.html')

    firstname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    firstname.send_keys('Aleksei')

    lastname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lastname.send_keys('Torsukov')

    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('torsukov@gmail.com')

    image = browser.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'avatar.jpg')           # добавляем к этому пути имя файла

    image.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()



