Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo 
        When preencho os campos de login com usuário standard_user e senha secret_sauce
        Then sou direcionado para a página Home

    Scenario: login com a senha inválida
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuário standard_user e senha laranja
        Then exibi uma mensagem de erro no login

    Scenario Outline: login negativo
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuário <usuario> e senha <senha>
        Then exibi uma mensagem de erro no login

        Examples: 
        |ID| usuário        |  senha       | mensagem                                                                  |
        |01| standard_user  | laranja      | Epic sadface: Username and password do not match any user in this service |
        |02| standard_user  |              | Epic sadface: Password is required                                        |
        |03|                | secret_sauce | Epic sadface: Username is required                                        |
        |04|juca            | secret_sauce | Epic sadface: Username and password do not match any user in this service |
        |05|juca            | laranja      | Epic sadface: Username and password do not match any user in this service |
        |06|juca            |              | Epic sadface: Password is required                                        |
        |07|                |              | Epic sadface: Username is required                                        |
        |08|                |laranja       | Epic sadface: Username is required                                        |