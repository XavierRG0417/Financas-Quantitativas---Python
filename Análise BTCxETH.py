# Importar as bibliotecas necessárias
import yfinance as yf  # Biblioteca para obter dados financeiros do Yahoo Finance
import quantstats as qs  # Biblioteca para análise estatística e visualização de ativos financeiros
import pandas as pd  # Biblioteca para manipulação e análise de dados
import matplotlib.pyplot as plt  # Biblioteca para criação de gráficos

# Obter dados do Bitcoin (BTC-USD) e Ethereum (ETH-USD)
# A função yf.download busca os dados históricos de fechamento de preços dos ativos.
btc_data = yf.download("BTC-USD", start="2016-01-01", end="2023-04-10")['Close']
eth_data = yf.download("ETH-USD", start="2016-01-01", end="2023-04-10")['Close']

# Calcular os retornos diários percentuais
# A função pct_change() calcula a variação percentual entre os valores consecutivos de uma série.
# A função dropna() remove os valores NaN (Not a Number) gerados no primeiro valor dos retornos.
btc_returns = btc_data.pct_change().dropna()
eth_returns = eth_data.pct_change().dropna()

# Estender o índice de data para incluir ambos os ativos
# A função union() combina os índices de data dos dois ativos, garantindo que todos os dados sejam incluídos.
extended_index = btc_returns.index.union(eth_returns.index)
# A função reindex() ajusta os índices dos DataFrames de retorno para o índice estendido, preenchendo os valores ausentes usando o método 'ffill' (preenchimento para frente).
btc_returns = btc_returns.reindex(extended_index, method='ffill')
eth_returns = eth_returns.reindex(extended_index, method='ffill')

# Comparar o desempenho usando QuantStats
# A função qs.reports.html() gera um relatório HTML detalhado comparando os retornos dos ativos.
qs.reports.html(btc_returns, eth_returns, output='report.html', title='Relatório de Desempenho: BTC vs ETH')

# Mostrar os retornos acumulados
# A função qs.plots.returns() plota um gráfico de linha mostrando os retornos acumulados dos ativos.
qs.plots.returns(btc_returns, eth_returns, cumulative=True, figsize=(15, 7))

# Exibir o gráfico
plt.show()
