from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class CCart_page(Base):

    def __init__(self,driver,action):
        super().__init__(driver,action)
        self.driver = driver
        self.action = action

    #locators 
    
    l_go_to_order = "//a[@class='btn-simple btn-medium goToOrder']"

    l_pickup = '//*[@id="bx_soa_item_delivery_id_3"]/div/div[1]/div[1]/span'
    l_pickup_ok = '//*[@id="bx-soa-pickup"]/div[1]/h2/div'
    l_pickup_scroll = '//*[@id="bx_soa_item_delivery_id_183"]/div/div[1]/div[1]/span'

    l_scroll_finaly = '//*[@id="bx-soa-orderSave"]/a'

    l_input_fio = '//*[@id="soa-property-96"]'
    l_input_email = '//*[@id="soa-property-2"]'
    l_input_phone = '//*[@id="soa-property-3"]'
    l_input_address = '//*[@id="soa-property-7"]'
    l_input_comment = '//*[@id="orderDescription"]'

    l_button_go_order = '//*[@id="bx-soa-total"]/div[2]/div[1]/div[6]/a[1]'


    l_button_payment = "//div[@class='pay_name']"
    
    #Getters 
    
    def get_go_to_order(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_go_to_order)))
   
    def get_pickup(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_pickup)))
    
    def check_pickup_ok(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_pickup_ok)))
    
    def get_pickup_scroll(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_pickup_scroll)))
    
    def get_scroll_finaly(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_scroll_finaly)))
    
    def get_input_fio(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_input_fio)))
    
    def get_input_email(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_input_email)))
    
    def get_input_phone(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_input_phone)))
    
    def get_input_address(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_input_address)))
    
    def get_input_comment(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_input_comment)))
    
    def get_button_go_order(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_button_go_order)))
    
    def get_payment(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_button_payment)))
    
    #Actions 

    def click_go_to_order(self):
        self.get_go_to_order().click()
        print('click_go_to_order')


    def click_pickup(self):
        self.get_pickup().click()
        print('click_pickup')

    def input_fio(self,fio):
        self.get_input_fio().click()
        self.get_input_fio().clear()
        self.get_input_fio().send_keys(fio)
        print('input_fio')

    def input_email(self,email):
        self.get_input_email().click()
        self.get_input_email().clear()
        self.get_input_email().send_keys(email)
        print('input_email')

    def input_phone(self,phone):
        self.get_input_phone().click()
        self.get_input_phone().clear()
        self.get_input_phone().send_keys(phone)
        print('input_phone')

    def input_address(self,address):
        self.get_input_address().click()
        self.get_input_address().clear()
        self.get_input_address().send_keys(address)
        print('input_address')

    def input_comment(self,comment):
        self.get_input_comment().click()
        self.get_input_comment().clear()
        self.get_input_comment().send_keys(comment)
        print('input_comment')

    def send_button_go_order(self):
        self.get_button_go_order().click()
        print('send_button_go_order')

    def check_payments(self):
        self.get_payment()
        

    #Methods

    def go_to_order(self):
        
        #Необходимо продвинуть страницу , из-за нижнего бара на сайте. 
        #Привязаться ниже к какому то элементу нет возможности 
        #использовать move_element_to_with_offset не получилось
        self.driver.execute_script("window.scrollTo(0,100)")

        # прожатие кнопки "Оформить заказ"
        self.click_go_to_order()

        #Прокрутка до выбора типа доставки.
        self.move_to_element(self.get_pickup_scroll())

        #Выбор типа доставки ПВЗ
        self.click_pickup()

        #Проверяем что ПВЗ выбран и доступен.
        self.check_pickup_ok()
        
        #Крутим до ввода данных
        self.move_to_element(self.get_scroll_finaly())

        #Ввод данных
        self.input_fio('Фамилия Имя Отчество')
        self.input_email('bb@yandex.ru')
        self.input_phone('9999991122')
        self.input_address('Москва, 2-я Хуторская улица, 38Ас15, 115 офис')
        self.input_comment('Тестовый заказ, можно удалить.')

        #Оформляем закакз
        self.send_button_go_order()

        self.screenshot('cart-one')

        #Проверка что оформили заказ.
        self.check_payments()

        print('Заказ успешно оформлен.')

        self.screenshot('cart-finaly')


        
    
       
      
            

        