## Requisitos

- Python 3.7 ou superior
- pip (Python package installer)

## Instalação

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu_usuario/sparta-python.git
    cd sparta-python
    ```

2. **Crie um ambiente virtual**:
    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual**:
    - No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - No Linux/MacOS:
        ```bash
        source venv/bin/activate
        ```

4. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Baixar e salvar os dados

1. **Execute o script `main.py`**:
    ```bash
    python main.py
    ```
    Este script baixa os dados das companhias abertas e os salva em um banco de dados SQLite (`cias_abertas.db`).

### Iniciar o servidor Flask

1. **Execute o script `app.py`**:
    ```bash
    python app.py
    ```

2. **Abra um navegador e vá para `http://localhost:5000`**:
    A interface de busca será carregada. Você pode buscar por data e/ou nome da empresa.

### Estrutura dos Scripts

#### `main.py`

Este script é responsável por baixar os dados das companhias abertas a partir de um link público, processar esses dados usando Pandas e armazená-los em um banco de dados SQLite usando SQLAlchemy.

#### `app.py`

Este script cria um servidor web usando Flask. Ele define duas rotas:
- `/`: Exibe um formulário de busca.
- `/search`: Realiza a busca no banco de dados com base na data e/ou nome da empresa fornecidos pelo usuário.

### Estrutura do HTML

O arquivo `index.html` na pasta `templates` define a estrutura da página web, incluindo o formulário de busca e a tabela para exibir os resultados.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue ou entrar em contato:

- Igor Barcelo
- igor_codmw@hotmail.com