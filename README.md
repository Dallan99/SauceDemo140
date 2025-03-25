# SauceDemo Test Automation

Este projeto tem como objetivo automatizar os testes de login no site **Sauce Demo** utilizando o **Selenium WebDriver** e a biblioteca **Behave** para testes BDD (Behavior-Driven Development).

O script automatiza os seguintes cenários de teste de login:
- Login com usuário e senha válidos
- Login com senha inválida
- Login com usuário inválido
- Login com campos de usuário e senha em branco

## Tecnologias Usadas

- **Python**: Linguagem de programação usada para a automação de testes.
- **Selenium WebDriver**: Biblioteca para automação de navegação em navegadores.
- **Behave**: Biblioteca para testes BDD (Behavior-Driven Development) em Python.
- **ChromeDriver**: Driver do Chrome necessário para o Selenium WebDriver.
- **VS Code**: Ambiente de desenvolvimento integrado (IDE) utilizado para editar o código.

## Pré-Requisitos

Antes de rodar os testes, você precisa garantir que as seguintes ferramentas estão instaladas no seu ambiente:

- **Python**: Você pode verificar se o Python está instalado usando o comando:
    ```bash
    python --version
    ```
    Se não estiver instalado, [faça o download aqui](https://www.python.org/downloads/).

- **Selenium**: Para instalar o Selenium, execute:
    ```bash
    pip install selenium
    ```

- **Behave**: Para instalar o Behave, execute:
    ```bash
    pip install behave
    ```

- **ChromeDriver**: Certifique-se de que o ChromeDriver esteja instalado e configurado no seu sistema. Você pode fazer o download [aqui](https://sites.google.com/chromium.org/driver/).

## Estrutura do Projeto


### **Explicação dos Arquivos**

- **selecionar_produtos.feature**: 
  Este arquivo contém a especificação dos cenários de teste no formato Gherkin, que é utilizado pelo Behave. Aqui estão definidos os cenários de login, como por exemplo, login com usuário e senha válidos, login com usuário ou senha inválidos, e login com campos em branco.

- **login_steps.py**: 
  Este arquivo contém a implementação dos passos definidos no arquivo `.feature`. Cada passo é associado a um código Python que realiza ações no navegador usando o Selenium WebDriver, como preencher os campos de login e verificar as mensagens de erro.

## Como Rodar os Testes

1. **Clone este repositório**:
    ```bash
    git clone https://github.com/Dallan99/SauceDemo140.git
    cd SauceDemo140
    ```

2. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Execute os testes**:
    Para rodar os testes, você pode usar o seguinte comando:
    ```bash
    behave
    ```

    O Behave irá executar os cenários definidos no arquivo `selecionar_produtos.feature` e os passos definidos no arquivo `login_steps.py`.

4. **Verifique os resultados**:
    Após a execução, o Behave fornecerá um relatório com os resultados dos testes. Caso algum teste falhe, você poderá ver a mensagem de erro correspondente.

## Como Contribuir

1. Faça um **fork** deste repositório.
2. Crie uma nova **branch**:
    ```bash
    git checkout -b nome-da-sua-branch
    ```
3. Faça as alterações desejadas e adicione um commit:
    ```bash
    git commit -am 'Descrição do que foi alterado'
    ```
4. Envie para o repositório remoto:
    ```bash
    git push origin nome-da-sua-branch
    ```
5. Abra um **Pull Request** com as alterações.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

