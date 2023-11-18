
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains

from base.base_class import Base
import time

class CProduct_page(Base):

    def __init__(self,driver,action):
        super().__init__(driver,action)
        self.driver = driver
        self.action = action


    #locators 
    
    l_find_product = "//*[@id='bx_1741660521_138111']"
    l_button_cart = "//a[contains(@class,'addCart changeID changeQty changeCart')]"
    l_button_cart_sussec = "//td[@class='goToBasket']"

    l_check_brand = "//*[@id='browse']/div[2]/div[3]/div/div[2]/div[1]/div[2]"
    l_check_material = "//*[@id='browse']/div[2]/div[3]/div/div[2]/div[2]/div[2]"
    
    #Getters 

    def get_product(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_find_product)))
        
    
    def get_button_cart(self):
        ok = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,self.l_button_cart)))
        return self.driver.find_elements(By.XPATH,self.l_button_cart) 
    
    def get_button_cart_succes(self):
        return WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,self.l_button_cart_sussec)))
    
    def get_check_brand(self):
        return WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,self.l_check_brand)))
    
    def get_check_material(self):
        return WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,self.l_check_material)))
      
    
    #Actions 

    def click_product(self):
        self.get_product().click()
        print('click_product')

    def click_button_cart(self):
        self.get_button_cart()[1].click()
        print('click_button_cart')

    def click_button_cart_sussec(self):
        self.get_button_cart_succes().click()
        print('click_button_cart_sussec')

    def check_brand(self):
        self.assert_word(self.get_check_brand().text,'Serge')
        print('check_brand')

    def check_material(self):
        self.assert_word(self.get_check_material().text,'Хлопок / Эластан')
        print('check_material')

    #Methods

    def add_to_cart(self):
        #Клик на продукт
        self.click_product()

        #Проверка что у товара правильный бренд и материал , выбранный с фильтров. 
        self.check_material()
        self.check_brand()

        #Добавление товара в корзину.
        self.click_button_cart()
       
        # Подверждение заказа товара и переход в корзину
        self.click_button_cart_sussec()

        # Проверяем что мы в корзине.
        self.assert_url('https://www.vsempodarok.com/personal/cart/')

        print('Product_page OK!')
        self.screenshot('product')
      
            

        