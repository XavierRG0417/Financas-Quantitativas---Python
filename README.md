# Python Para Finanças
O código é uma função chamada "risk_analysis" que realiza a análise de risco de ações de várias empresas com base em dados históricos de preços de ações, plotando vários gráficos para cada uma das ações.

Para executar a análise, a função solicita ao usuário que insira o símbolo da ação (ticker) separado por vírgula, bem como a data de início e término do período de análise. A partir desses inputs, a função faz a requisição dos dados históricos de preços de ações usando a biblioteca yfinance.

A análise é composta por cinco gráficos para cada ação:

O primeiro gráfico é um gráfico de linhas que representa o preço ajustado de fechamento da ação ao longo do tempo, utilizando a biblioteca plotly.express. Esse gráfico é importante para visualizar a tendência de preços ao longo do tempo.

O segundo gráfico é um gráfico de linhas que representa os retornos diários da ação ao longo do tempo, utilizando a biblioteca plotly.express. Esse gráfico é importante para visualizar a volatilidade da ação.

A função também imprime a média de retorno diário e anual da ação, que são importantes para calcular o retorno esperado.

O quarto gráfico é um histograma que representa a distribuição dos retornos da ação, utilizando a biblioteca plotly.express. Além disso, é plotada uma linha que representa a distribuição normal dos retornos. Esse gráfico é importante para verificar se a distribuição dos retornos segue uma distribuição normal, o que é um pressuposto importante para alguns modelos de análise de risco.

O último gráfico é um gráfico Q-Q plot (quantile-quantile plot) que representa a relação entre os quantis da distribuição dos retornos da ação e os quantis da distribuição normal, utilizando a biblioteca statsmodels.api e matplotlib. Esse gráfico é importante para verificar a normalidade da distribuição de retornos e para verificar se há algum desvio significativo da distribuição normal.

No geral, a função é útil para realizar uma análise de risco preliminar de várias ações, permitindo ao usuário visualizar a tendência de preços, a volatilidade, a distribuição dos retornos e a normalidade da distribuição dos retornos. Essas informações são importantes para o processo de tomada de decisão de investimento.
