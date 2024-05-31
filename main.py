import requests
import pandas as pd
from sqlalchemy import create_engine
import io

# URL para obter os dados
url = "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv"

# Baixar os dados
response = requests.get(url)
csv_content = response.content.decode('latin-1')

# Ler os dados em um DataFrame
df = pd.read_csv(io.StringIO(csv_content), sep=';', encoding='latin-1')

# Configuração do banco de dados
engine = create_engine('sqlite:///cias_abertas.db')

# Salvar os dados no banco de dados
df.to_sql('cias_abertas', engine, if_exists='replace', index=False)

