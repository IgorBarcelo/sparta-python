from flask import Flask, request, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Configuração do banco de dados
engine = create_engine('sqlite:///cias_abertas.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    date = request.args.get('date')
    name = request.args.get('name')

    query = "SELECT * FROM cias_abertas WHERE 1=1"
    params = {}
    
    if date:
        query += " AND DT_REG = :date"
        params['date'] = date
    
    if name:
        query += " AND DENOM_SOCIAL LIKE :name"
        params['name'] = f"%{name}%"
    
    if not date and not name:
        query = "SELECT * FROM cias_abertas LIMIT 10"

    with engine.connect() as connection:
        result = connection.execute(text(query), params)
        rows = [dict(zip(result.keys(), row)) for row in result]
    
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
