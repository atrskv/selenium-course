'''

>>> assert abs(-42) == -42, "Should be absolute value of a number"

'''

'''

Составные ассерты

catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"  

'''

'''

assert expected_result == actual_result, f'expected 8, got 11

'''


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

if __name__ == "__main__": # если был запущен самостоятельно, то:
    test_abs1()
    print("All tests passed!")
# Нужно использовать, если используем с двух сторон

'''
__name__ хранит имя модуля
__main__ говорит о том, что скрипт был запущен самостоятельно
'''
'''
служит для подтверждения того, что данный скрипт был запущен напрямую, 
а не вызван внутри другого файла в качестве модуля
'''



Для unittest существуют собственные дополнительные правила:

Тесты обязательно должны находиться в специальном тестовом классе.
Вместо assert должны использоваться специальные assertion методы.

import unittest


class TestAbs(unittest.TestCase): # создаем класс, который наследуется от TestCase
    def test_abs1(self): # делаем из функций методы, ссылаясь на self
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number") # исправляем ассерт

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")


if __name__ == "__main__":
    unittest.main() # заменяем запуск