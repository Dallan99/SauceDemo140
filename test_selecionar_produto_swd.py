#  1 - Bibliotecas
import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Teste_Produtos():

    # 2.1 Atributos
    url = "https://www.saucedemo.com"        # endereço do site alvo

    # 2.2 Funções e Métodos
    def setup_method(self, method):               # ou def iniciar(method): TAMBÉM FUNCIONA  // Método de inicualização dos testes
        self.driver = webdriver.Chrome()    # instacia o objeto do Selenium WbeDriver como Chrome
        self.driver.implicitly_wait(10)    # Define o tempo de espera padrão em 10 segundos

    def teardown_method(self, method):   # ou def finalizar(method): TAMBÉM FUNCIONA // metodo de finalização dos testes // teardown(self, method):      # def finalizar(method): também funciona // metodo de finalização dos testes
        self.driver.quit()   # encerra / destrói o objeto do Selenium Webdriver da memória

    def test_selecionar_produto(self):    # Método de teste
        self.driver.get(self.url)                # Abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")  # user name é o nome do local e o standard user é o login
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")   #escreve a senha
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()# Clica no botão de login
        #transição de página

        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"  # confirma se está escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack" # confirma se é a mochila
        # confirma o preço da mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99" 