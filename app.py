import requests
from tinydb import TinyDB, Query
from datetime import datetime

# Configurar o banco de dados TinyDB
db = TinyDB('cotacoes.json')
tabela_cotacoes = db.table('cotacoes')

# Função para obter a cotação BTC/USD da Coinbase
def obter_btc_usd():
    url = "https://api.coinbase.com/v2/prices/spot?currency=USD"
    response = requests.get(url)
    data = response.json()
    return float(data['data']['amount'])

# Função para obter a cotação USD/BRL da AwesomeAPI
def obter_usd_brl():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    response = requests.get(url)
    data = response.json()
    return float(data['USDBRL']['bid'])

# Obter o timestamp atual
timestamp = datetime.now()

# Obter as cotações
btc_usd = obter_btc_usd()
usd_brl = obter_usd_brl()

# Calcular BTC/BRL
btc_brl = btc_usd * usd_brl

# Preparar os dados para salvar
dados = {
    'timestamp': timestamp.isoformat(),
    'btc_usd': btc_usd,
    'usd_brl': usd_brl,
    'btc_brl': btc_brl
}

# Salvar no banco de dados
tabela_cotacoes.insert(dados)

print(f"Cotações salvas em {timestamp}:")
print(f"BTC/USD = {btc_usd:.2f}")
print(f"USD/BRL = {usd_brl:.2f}")
print(f"BTC/BRL = {btc_brl:.2f}")