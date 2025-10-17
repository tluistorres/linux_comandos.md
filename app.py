import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import requests

# Define as APIs para cotações de moedas
APIs = {
    'Awesome API': 'https://economia.awesomeapi.com.br/last/{MOEDA}-BRL',
    # Outras APIs comentadas, adicioná-las se for usar
    # 'ExchangeRate-API': 'https://api.exchangerate-api.com/v4/latest/{MOEDA}',
    # 'CoinGecko API': 'https://api.coingecko.com/api/v3/simple/price?ids={MOEDAS}&vs_currencies=brl',
    # 'Alpha Vantage API': 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={MOEDA}&to_currency=BRL&apikey=YOUR_API_KEY',
}

# Define as moedas disponíveis
MOEDAS = ['USD', 'EUR', 'JPY', 'ARS', 'MXN', 'BTC', 'ETH', 'LTC']

# Cria uma classe para o aplicativo
class MeuAplicativo(App):
    # Define o método build, que é chamado quando o aplicativo é iniciado
    def build(self):
        # Cria um layout em grade com 1 coluna
        layout = GridLayout(cols=1)
        layout.add_widget(Label(text="Cotações de Moedas")) # Título

        # Loop pelas moedas disponíveis
        for moeda in MOEDAS:
            link = APIs['Awesome API'].replace('{MOEDA}', moeda)
            try:
                # Faz uma requisição GET para a API
                requisicao = requests.get(link, timeout=5) # Adicione um timeout para evitar que a requisição trave
                requisicao.raise_for_status()  # Levanta um erro para status HTTP 4xx/5xx

                # Converte a resposta em um dicionário
                dic_requisicao = requisicao.json()

                # Extrai a cotação da moeda
                # A chave pode variar dependendo da moeda. 'BTCBRL', 'USDBRL' etc.
                # O AwesomeAPI retorna um dicionário com uma única chave que é o par da moeda
                if f"{moeda}BRL" in dic_requisicao:
                    cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
                    label_text = f"{moeda}: R$ {float(cotacao):.2f}"
                else:
                    label_text = f"Cotação {moeda}: Dados não encontrados."

            except requests.exceptions.RequestException as e:
                label_text = f"Erro ao obter {moeda}: {e}"
            except KeyError:
                label_text = f"Erro ao processar dados de {moeda}."
            except Exception as e:
                label_text = f"Ocorreu um erro inesperado para {moeda}: {e}"

            # Cria um label com a cotação da moeda
            label = Label(text=label_text)
            # Adiciona o label ao layout
            layout.add_widget(label)

        # Retorna o layout completo
        return layout

# Inicia o aplicativo
if __name__ == '__main__':
    MeuAplicativo().run()
