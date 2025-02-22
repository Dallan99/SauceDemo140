# 1 - Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # setup / inicialização
    context.driver = webdriver.Chrome() #instanciar o objeto do Selenium Webdriver como Chrome    
    context.driver.maximize_window() #maximizar a janela do navegador
    context.driver.implicitly_wait(10) #define o tempo de espera padrão em 10 segundos
    # passo em sí
    context.driver.get("https://www.saucedemo.com/") #acessar o site

@when(u'preencho os campos de login com usuário {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element_by_id("user-name").send_keys(usuario)
    context.driver.find_element_by_name("password").send_keys(senha)
    context.driver.find_element_by_id("login-button").click()
    time.speep(2) # Parando o processamento para 2 segundos

@then(u'sou direcionado para a página Home')
def step_impl(context):
    assert context.driver.find_element_by_id("title").text == "Products" #confirma se está escrito Products no elemento
    time.sleep(2) # Parando o processamento para 2 segundos

    # teardown / encerramento
    context.driver.quit() # encerra / destrói o objeto do Selenium Webdriver da memória 
 
