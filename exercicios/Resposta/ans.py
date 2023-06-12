import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ler os dados
dados = pd.read_csv('./exercicios/transferencias05_2023.csv')

# remova a cola ano/mes
dados = dados.drop(columns=['ANO / MÊS'])

# converte a coluna valor transferido em float
dados['VALOR TRANSFERIDO'] = dados['VALOR TRANSFERIDO'].str.replace(',', '.').astype(float)

"""
#valor máximo, medio, minimo
print(np.max(dados['VALOR TRANSFERIDO']))
print(np.min(dados['VALOR TRANSFERIDO']))
print(np.median(dados['VALOR TRANSFERIDO']))
"""

tipo = dados['TIPO FAVORECIDO'].unique()
valor = dados.groupby('TIPO FAVORECIDO')['VALOR TRANSFERIDO'].sum()

plt.bar(tipo, valor)

plt.xlabel('Tipo favorecido')
plt.ylabel('valor transferido')
plt.title('Transferências')
plt.xticks(rotation = 45)
plt.show()   
