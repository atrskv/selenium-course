from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # GIVEN
    link = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # WHEN
    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    first_name.send_keys('Aleksei')

    second_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    second_name.send_keys('Torsukov')

    email = browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    email.send_keys('email@email.com')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(1)


    # THEN
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()


    '''
    Проблема со своевременным поиском элемента — одна из самых больших проблем, 
    которую приходится решать при разработке автотестов для UI. 
    В условиях постоянно изменяющейся скорости сетевого соединения и неравномерности нагрузки 
    на серверы скорость загрузки страницы может сильно варьироваться. 
    Еще одним фактором, влияющим на стабильность работы тестов, является принцип асинхронности 
    выполнения кода JavaScript. На простых страницах вы можете этого и не заметить, 
    но на функционально богатых страницах время появления элементов страницы может быть непредсказуемо. 
    '''


    '''
    Также вы можете увидеть тег label рядом с input. Этот тег используется, чтобы сделать кликабельным текст, 
    который отображается рядом с флажком. Этот текст заключен внутри тега label. 
    Элемент label связывается с элементом input с помощью атрибута for,
     в котором указывается значение атрибута id для элемента input
    '''