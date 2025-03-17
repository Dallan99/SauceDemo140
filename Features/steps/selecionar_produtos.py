# 1 - Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By 

# 2 - Steps
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
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

@then(u'sou direcionado para a página Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products" #confirma se está escrito Products no elemento
    #time.sleep(2) # Parando o processamento para 2 segundos

    # teardown / encerramento
    context.driver.quit() # encerra / destrói o objeto do Selenium Webdriver da memória 

@then(u'exibi uma mensagem de erro no login')
def step_impl(context):
    #validar a mensagem de erro:
    assert context.driver.find_element(By.CSS_SELECTOR,"h3").text == "Epic sadface: Username and password do not match any user in this service"
    context.driver.quit()# encerra / destrói o objeto do Selenium Webdriver da memória 