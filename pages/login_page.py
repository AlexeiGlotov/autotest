
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Login_page(Base):

    def __init__(self,driver,action):
        super().__init__(driver,action)
        self.driver = driver

    #locators 
    
    l_entry = "//li[@class='top-auth-login']"

    l_login = "//input[@name='USER_LOGIN']"
    l_password = "//input[@name='USER_PASSWORD']"

    l_come_in = "//input[@name='Login']"

    l_check_auth = "//li[@class='top-auth-personal']"

    #Getters 

    def get_button_entry(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_entry)))
    
    def get_input_login(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_login)))
    
    def get_input_password(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_password)))
    
    def get_button_login(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_come_in)))
    
    def get_auth_check(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_check_auth)))
 
    
    #Actions 

    def click_button_entry(self):
        self.get_button_entry().click()
        print('click_button_entry')

    def input_login(self,username):
        self.get_input_login().click()
        self.get_input_login().send_keys(username)
        print('input_login')

    def input_password(self,password):
        self.get_input_password().click()
        self.get_input_password().send_keys(password)
        print('input_password')

    def click_button_login(self):
        self.get_button_login().click()
        print('click_button_login')

    def get_auth_text(self):
        self.assert_word(self.get_auth_check().text,"Личный кабинет")
        print('get_auth_text')
      


    #Methods

    def Authorization(self,username,password):
        # Клик по надписи "Войти"
        self.click_button_entry()

        # Ввод в инпут логина и пароля
        self.input_login(username)
        self.input_password(password)

        # Нажатие кнопки войти
        self.click_button_login()

        # Проверка что успешно авторизовались, 
        # появляется надпись на гл.странице "Личный кабинет"
        self.get_auth_text()

        print('Auth OK!')
        self.screenshot('auth')
        