from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configuração do WebDriver
options = webdriver.ChromeOptions()


driver = webdriver.Chrome(options=options)

def test_login():
    try:
        # Acessa a página de login
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)  # Aguarda o carregamento da página

        # Localiza os campos de usuário e senha
        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        # Insere credenciais inválidas
        username_input.send_keys("usuario_teste")
        password_input.send_keys("senha_errada")
        login_button.click()
        time.sleep(2)

        # Verifica se a mensagem de erro aparece
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
        assert "Epic sadface" in error_message.text

        print("Teste de login inválido: SUCESSO")
    except Exception as e:
        print(f"Teste de login inválido: FALHA - {e}")
    finally:
        driver.quit()

# Executa o teste
test_login()