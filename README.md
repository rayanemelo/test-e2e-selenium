# Testes E2E com Selenium - Unsplash

Este projeto realiza testes automatizados end-to-end utilizando **Selenium com Python** no site [Unsplash](https://unsplash.com/pt-br). Os testes simulam ações comuns de um usuário na plataforma.

## Como executar os testes

1. **Clone o repositório**

    ```git clone https://github.com/rayanemelo/test-e2e-selenium```

2. **Acesse a pasta do projeto**

    ```cd test-e2e-selenium```

3. Execute os testes com Docker

    ```docker compose up --build --abort-on-container-exit```


## Testes automatizados
* Realiza uma busca e acessa o perfil de um fotógrafo a partir dos resultados.

* Navega até a seção onde usuários podem se tornar colaboradores da plataforma.

* Realiza o download de uma imagem disponível no site.

* Testa a funcionalidade da barra de pesquisa.

* Simula a navegação do usuário por categorias de imagens no menu principal.