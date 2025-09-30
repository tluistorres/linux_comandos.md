import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import requests

APIs = {
    'Awesome API': 'https://economia.awesomeapi.com.br/last/{MOEDA}-BRL',
}

MOEDAS = ['USD', 'EUR', 'JPY', 'ARS', 'MXN', 'BTC', 'ETH', 'LTC']

class MeuAplicativo(App):
    def build(self):
        layout = GridLayout(cols=1)
        for moeda in MOEDAS:
            link = APIs['Awesome API'].replace('{MOEDA}', moeda)
            try:
                requisicao = requests.get(link)
                requisicao.raise_for_status()  
                dic_requisicao = requisicao.json()
                cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
                label = Label(text=f"{moeda} R${cotacao}")
                layout.add_widget(label)
            except requests.exceptions.RequestException as e:
                label = Label(text=f"Erro ao obter cotação do {moeda}: {e}")
                layout.add_widget(label)
        return layout

MeuAplicativo().run()

# label = Label(text=f"{moeda} R${format(float(cotacao), '.2f')}"), para formatar moedas com duas casas decimais.


######################################################################################

# Importa as bibliotecas necessárias: Código comentado.

# Importa as bibliotecas necessárias
# import kivy
# from kivy.app import App
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# import requests

# # Define as APIs para cotações de moedas
# APIs = {
#     'Awesome API': 'https://economia.awesomeapi.com.br/last/{MOEDA}-BRL',
#     'ExchangeRate-API': 'https://api.exchangerate-api.com/v4/latest/{MOEDA}',
#     'CoinGecko API': 'https://api.coingecko.com/api/v3/simple/price?ids={MOEDA}&vs_currencies=BRL',
#     'Alpha Vantage API': 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={MOEDA}&to_currency=BRL&apikey=SEU_API_KEY'
# }

# Define as moedas disponíveis
# MOEDAS = ['USD', 'EUR', 'BTC', 'ETH', 'LTC']

# Cria uma classe para o aplicativo
# class MeuAplicativo(App):
# Define o método build, que é chamado quando o aplicativo é iniciado
#     def build(self):
# Cria um layout em grade com 1 coluna
#         layout = GridLayout(cols=1)
        
# Loop pelas moedas disponíveis
#         for moeda in MOEDAS:
# Substitui o placeholder {MOEDA} pela moeda atual
#             link = APIs['Awesome API'].replace('{MOEDA}', moeda)
            
# Faz uma requisição GET para a API
#             requisicao = requests.get(link)
            
# Converte a resposta em um dicionário
#             dic_requisicao = requisicao.json()
            
# Extrai a cotação da moeda
#             cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
            
# Cria um label com a cotação da moeda
#             label = Label(text=f"{moeda} R${format(float(cotacao), '.2f')}")
            
# Adiciona o label ao layout
#             layout.add_widget(label)
        
# Retorna o layout
#         return layout

# # Inicia o aplicativo
# MeuAplicativo().run()