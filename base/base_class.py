import time

class Base():
    def __init__(self,driver,action):
        self.driver = driver
        self.action = action

    """Получение URL в моменте"""

    def get_current_url(self):
        return self.driver.current_url
    
    """Проверка двух строк"""

    def assert_word(self,word,result):
        assert word == result
        print(f'[GOOD] assert_word {word} == {result}')

    """Проверка URL в бразуере с URL из строки"""
    def assert_url(self,url):
        assert self.driver.current_url == url
        print(f'[GOOD] assert_url {self.driver.current_url} == {url}')
  
    """Аналогично выше функции , но проверят как подстроку."""

    def assert_url_part(self,url):
        result = self.driver.current_url.find(url)
        assert result != -1
        print(f'[GOOD] assert_url {self.driver.current_url} == {url}')

    """Проверка что выбран checkbox или radio button"""

    def checked_radio_checkbox(self,element,expectation):
        assert expectation == element.is_selected()
        print(f'[GOOD] checked_radio_checkbox') 

    """Установить фокус на конкретный элемент"""

    def move_to_element(self,elem):
        self.action.move_to_element(elem).perform()
        print(f'[GOOD] move_to_element')

    """Выдрать из строки только цифры"""

    def isDigit(self,text):
        stri = ''
        for x in text:
            if x.isdigit():
                stri = stri + x

        return stri
    
    """Сделать скриншот"""

    def screenshot(self,moduls):
        self.driver.save_screenshot(f'C:\\Users\\Alexei\\vsempodarok\\screen\\{moduls}-{time.time()}.png')
           