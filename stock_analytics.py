import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import yfinance as yfin
yfin.pdr_override()
import matplotlib.pyplot as plt
from scipy.stats import norm

saudacao = "Bem-vindo! Carregando..."
print(saudacao)
print()

# definir nossa acao (PETR4.SA) e o período de análise:
print("Vamos definir os padrões de nossa pesquisa...\n")
print()
acao = str(input("Digite a sigla do ativo:")) + ".SA"
inicio_periodo = str(input("Digite a data de início do período a analisar (YYYY-MM-DD):"))
DATA_acao = wb.get_data_yahoo(acao, start=inicio_periodo)

# cálculo de retornos simples:
print("Apresentando gráfico de retornos simples...\n")
DATA_acao['simple_return'] = (DATA_acao['Adj Close'] / DATA_acao['Adj Close'].shift(1)) - 1
DATA_acao['simple_return'].plot(figsize=(8, 5))
plt.show()
print()
print()

# cálculo de retornos médios:
avg_returns_a = DATA_acao['simple_return'].mean() * 251
print('O retorno médio é ' + str(round(avg_returns_a, 5) * 100) + ' %')
print()
print()

# cálculo do retorno logarítmico:
print("Apresentando gráfico de retornos logarítmicos...\n")
DATA_acao['log_return'] = np.log(DATA_acao['Adj Close'] / DATA_acao['Adj Close'].shift(1))
DATA_acao['log_return'].plot(figsize=(8, 5))
plt.show()
print()
print()

# cálculo do retorno logarítmico médio:
avg_log_returns_a = DATA_acao['log_return'].mean() * 251
print('O retorno logarítmico médio é ' + str(round(avg_log_returns_a, 5) * 100) + ' %')
print()
print()

# comparação entre ação e índice da bolsa:
ativos = [acao, '^BVSP']
dados = pd.DataFrame()
for ativo in ativos:
    dados[ativo] = wb.get_data_yahoo(ativo, start=inicio_periodo)['Adj Close']

# apresentação gráfica:
(dados / dados.iloc[0] * 100).plot(figsize=(15, 6))  # aplicação da fórmula
plt.title("Preços: Ativo vs IBOV")
plt.show()
print()
print()

# retorno anual (ação vs. índice):
retorno_indice = (dados / dados.shift(1)) - 1
retorno_anual_indice = retorno_indice.mean() * 251
print('O retorno anual do índice é :')
print(retorno_anual_indice)
print()
print()

# plotagem de "bar graph":
plt.style.use('ggplot')
x = [acao, '^BVSP']
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, retorno_anual_indice * 100, color='green')
plt.xlabel("Ativo(s)")
plt.ylabel("Percentual de Retorno Anual (Médio)")
plt.title("Retorno do ativo ante o Índice da Bovespa")
plt.xticks(x_pos, x)
plt.show()
print()
print()