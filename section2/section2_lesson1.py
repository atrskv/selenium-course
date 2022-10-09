from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

# GIVEN
try:
    browser.get('https://suninjuly.github.io/math.html')
    x_value = browser.find_element(By.ID, 'input_value').text

    result = calc(x_value)

    text_field = browser.find_element(By.ID, 'answer')
    text_field.send_keys(result)

    people_check = browser.find_element(By.ID, 'robotCheckbox')
    people_check.click()

    people_radiobutton = browser.find_element(By.ID, 'peopleRule')
    people_checked = people_radiobutton.get_attribute('checked')

    robots_radiobutton = browser.find_element(By.ID, 'robotsRule')

    robots_checked = robots_radiobutton.get_attribute('checked')

    assert people_checked is not None, 'FALSE'  # если ничего нет, get_attribute возвращает none, если есть - true (с маленькой буквы)

    robots_radiobutton.click()

    submit = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()
