from flask import Flask, request, render_template  
from sqlalchemy import create_engine, text  

app = Flask(__name__)  # Cria uma instância da classe Flask, representando a aplicação web

# Configuração do banco de dados
engine = create_engine('sqlite:///cias_abertas.db')  # Cria uma conexão com o banco de dados SQLite

@app.route('/')  # Define a rota para a URL raiz
def index():  # Define uma função para a rota '/'
    return render_template('index.html')  # Renderiza o template 'index.html' e o retorna para o navegador

@app.route('/search', methods=['GET'])  # Define a rota para '/search' e especifica que aceita apenas solicitações GET
def search():  # Define uma função para a rota '/search'
    date = request.args.get('date')  # Obtém o valor do parâmetro 'date' da solicitação GET
    name = request.args.get('name')  # Obtém o valor do parâmetro 'name' da solicitação GET

    query = "SELECT * FROM cias_abertas WHERE 1=1"  # Cria uma consulta SQL inicial
    params = {}  # Cria um dicionário para armazenar os parâmetros da consulta
    
    if date:  # Verifica se o parâmetro 'date' foi fornecido na solicitação
        query += " AND DT_REG = :date"  # Adiciona uma cláusula WHERE à consulta SQL
        params['date'] = date  # Adiciona o parâmetro 'date' ao dicionário de parâmetros
    
    if name:  # Verifica se o parâmetro 'name' foi fornecido na solicitação
        query += " AND DENOM_SOCIAL LIKE :name"  # Adiciona uma cláusula WHERE à consulta SQL
        params['name'] = f"%{name}%"  # Adiciona o parâmetro 'name' ao dicionário de parâmetros
    
    if not date and not name:  # Verifica se nenhum parâmetro de pesquisa foi fornecido
        query = "SELECT * FROM cias_abertas LIMIT 10"  # Define uma consulta SQL padrão

    with engine.connect() as connection:  # Estabelece uma conexão com o banco de dados
        result = connection.execute(text(query), params)  # Executa a consulta SQL com os parâmetros
        rows = [dict(zip(result.keys(), row)) for row in result]  # Formata os resultados em um dicionário de linhas
    
    return render_template('index.html', rows=rows)  # Renderiza o template 'index.html' com os resultados da consulta

if __name__ == '__main__':  # Verifica se o script está sendo executado diretamente
    app.run(debug=True)  # Inicia o servidor de desenvolvimento do Flask com a opção de depuração ativada
