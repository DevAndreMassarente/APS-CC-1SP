# APS-CC-1S

## Descrição
Projeto de urna eletrônica com hash, criptografia e desencriptação sem bibliotecas externas. Cada usuário tem direito a um voto apenas.

## Estrutura do Projeto
- `app.py`: Arquivo principal da aplicação Flask.
- `autocompletar.py`: Script para autocompletar os nomes dos times.
- `cores_times.py`: Script contendo as cores dos times.
- `static/`: Pasta contendo arquivos estáticos (imagens, CSS, JS).
- `templates/`: Pasta contendo os templates HTML.
- `criptografia_votos.py`: Script para criptografar os votos.
- `desencriptografia_votos.py`: Script para desencriptografar os votos.
- `urna.py`: Script principal para registrar os votos.

## Requisitos
- Python 3.x
- Flask

## Instalação
1. Clone o repositório:
    ```bash
    git clone https://github.com/DevAndreMassarente/APS-CC-1S.git
    cd APS-CC-1S
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install Flask
    ```

## Execução
1. Execute a aplicação:
    ```bash
    python app.py
    ```

2. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:5000
    ```

## Deploy no Netlify
Para fazer o deploy no Netlify, você pode seguir os passos descritos abaixo.

## Contribuição
Sinta-se à vontade para contribuir com o projeto. Faça um fork do repositório, crie uma branch para suas alterações e envie um pull request.

## Licença
Este projeto está licenciado sob a MIT License.