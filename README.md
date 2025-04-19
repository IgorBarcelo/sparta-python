# 📊 Sparta Python

Projeto em Python que realiza o download de dados de Portal Dados Abertos CVM, armazena-os em um banco de dados SQLite e fornece uma interface web para consulta utilizando Flask.

## 📸 Demonstrativo

![demo](https://github.com/IgorBarcelo/sparta-python/blob/main/public/demo.png?raw=true)

## 🧰 Tecnologias Utilizadas

- Python 3.7 ou superior  
- Flask  
- SQLite  
- Requests  
- BeautifulSoup
- Pandas
- SQLAlchemy  


## 🚀 Instalação

1. Clone o repositório:

```bash 
    git clone https://github.com/IgorBarcelo/sparta-python.git
    cd sparta-python 
```

2. Crie e ative um ambiente virtual:

- No Windows:

```bash
    python -m venv venv
    .\venv\Scripts\activate
```

- No Linux/MacOS:

```bash
    python3 -m venv venv
    source venv/bin/activate
```

3. Instale as dependências:

```bash
    pip install -r requirements.txt
```

🛠️ Uso
1. Baixar e armazenar os dados
Execute o script main.py para baixar os dados das companhias abertas e armazená-los no banco de dados SQLite:

```bash
    python main.py
```

2. Iniciar o servidor Flask
Após o banco de dados ser criado, inicie o servidor Flask para acessar a interface web:

```bash
    python app.py
```

Acesse http://localhost:5000 no seu navegador para utilizar a interface de busca por data e/ou nome da empresa.


## Créditos
Desenvolvido por [Igor Barcelo](https://www.linkedin.com/in/igor-barcelo-631010216/)
