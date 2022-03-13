##### Programa para testar as funções básicas do pandas #####
from this import d
import pandas as pd

pokemon_data_xlsx = pd.ExcelFile('/Volumes/SSD - Dados/Programação/basico-pandas/pokemon_data.xlsx')
# df_pokemon_data = pd.read_excel(pokemon_data_xlsx, 'pokemon_data')
df_pokemon_data = pd.read_csv('/Volumes/SSD - Dados/Programação/basico-pandas/pokemon_data.csv')

##### Formas de capturar o valor de linhas de um dataframe #####
# Desempenho ótimo
print(len(df_pokemon_data.index))

# Desempenho ótimo
print(df_pokemon_data.shape[0])

# Desempenho mediano
print(len(df_pokemon_data))

# Desempenho baixo
print(df_pokemon_data.count().iloc[0])

### Informações adicionais ###
# Retorna uma tupla com número de linhas e colunas respectivamente
print(df_pokemon_data.shape)

# Retorna valores de linhas de cada coluna
print(df_pokemon_data.count())

##### Formas de capturar o valor de colunas de um dataframe #####
# Desempenho ótimo
print(len(df_pokemon_data.columns))

# Desempenho ótimo
print(df_pokemon_data.shape[1])

##### Formas de imprimir valores das linhas de um dataframe ######
# Imprimindo o conteúdo de uma linha específica
print(df_pokemon_data.loc[0])

##### Formas de imprimir valores das colunas de um dataframe ######
print(df_pokemon_data.columns)

print(df_pokemon_data['Name'])

# Quantidade de valores únicos daquela coluna
print(df_pokemon_data['Legendary'].nunique())

# Imprime o começo, fim e alcance dos índices
print(df_pokemon_data.index)

# Imprime todo o dataframe
print(df_pokemon_data)
