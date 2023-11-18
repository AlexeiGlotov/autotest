
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class CFilter_page(Base):

    def __init__(self,driver,action):
        super().__init__(driver,action)
        self.driver = driver
        self.action = action

    #locators 
    
    l_find_input = "//input[@id='searchQuery']"

    l_find_button = "//button[@type='submit' and @name='s']"

    l_check_find_shirts = '//*[@id="right"]/h3'

    l_filter_price_max = "//input[@name='arrFilter_P1_MAX']" 
    
    l_filter_material_click = "//*[@id='smartFilterForm']/div[2]/div[1]"

    l_filter_cotton_checkbox = "//label[@for='arrFilter_11_3717599290']"

    l_filter_brand_checkbox = "//label[@for='arrFilter_408_2917010317']"

    l_filter_scroll_fix = '//*[@id="smartFilterForm"]/div[5]/div[1]/span'

    l_filter_sort = "//select[@name='sortFields']"

    l_filter_sort_price = "//*[@id='selectSortParams']/option[3]"

    l_filter_check_price = "//*[@id='bx_1741660521_138111']/div/div[2]/div[2]/a[2]"
    
    #Getters 

    def get_find_input(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_find_input)))
    
    def get_find_button(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_find_button)))
    
    def get_check_find_shirts(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_check_find_shirts)))
    
    def get_filter_max_price(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_filter_price_max)))
    
    def get_filter_material_click(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_filter_material_click)))
    
    def get_filter_cotton_checkbox(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_filter_cotton_checkbox)))
    
    def get_filter_brand_checkbox(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_filter_brand_checkbox)))
    
    def get_filter_sort(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_filter_sort)))
    
    def get_filter_sort_price(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_filter_sort_price)))
    
    def get_filter_scroll_fix(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH,self.l_filter_scroll_fix)))
    
    def get_filter_check_price(self):
        return WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.XPATH,self.l_filter_check_price)))
    

   
    
    #Actions 

    def input_find(self,find):
        self.get_find_input().click()
        self.get_find_input().send_keys(find)
        print('input_find')


    def send_button_find(self):
        self.get_find_button().click()
        print('send_button_find')


    def check_shirts(self):
        self.assert_word(self.get_check_find_shirts().text,'Товары по запросу: «Майки»')
        

    def send_filter_max_price(self,summ):
        self.move_to_element(self.get_filter_material_click())#
        self.get_filter_max_price().click()
        self.get_filter_max_price().clear()
        self.get_filter_max_price().send_keys(summ)
        print('send_filter_max_price')


    def send_filter_material(self):
        self.get_filter_material_click().click()
        self.get_filter_cotton_checkbox().click()
        print('send_filter_material')


    def send_filter_brand(self):
        self.get_filter_brand_checkbox().click()
        print('send_filter_brand')


    def window_default(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        print('window_default')


    def set_sort(self):
        self.get_filter_sort().click()
        self.get_filter_sort_price().click()
        print('set_sort')


    def check_price(self):
        assert int(self.isDigit(self.get_filter_check_price().text)) < 3000
        print('check_price')

    #Methods

    def install_filter(self):
        #Ввод в поиск и нажатие поиска
        self.input_find('Майки')
        self.send_button_find()

        #Проверяем что поиск сработал и мы нашли "Майки"
        self.check_shirts()
        
        #Сортируем по убыванию цеы
        self.set_sort()
        
        #Фильтра на MAX цену в 3000
        self.send_filter_max_price(3000)

        #Пролистывание страницы
        self.move_to_element(self.get_filter_scroll_fix())
       
        #Устанавливаем материал майки = хлопок 
        self.send_filter_material()

        #Еще раз пролистываем страницу , так как в материалах раскрывали список.
        self.move_to_element(self.get_filter_scroll_fix())
        
        #Устанавливаем бренд маек.
        self.send_filter_brand()

        #Возвращаемся в начало страниц
        self.window_default()

        print('Фильтра установлены.')

        # Проверяем что цена товара меньше 3000.
        self.check_price()
        self.screenshot('filter')