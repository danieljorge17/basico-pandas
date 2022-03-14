##### Programa para testar as funções básicas do pandas #####
import pandas as pd

df_pokemon_data = pd.read_csv('/Volumes/SSD - Dados/Programação/basico-pandas/pokemon_data.csv')

### Filtra valores de uma coluna
# print(df_pokemon_data.loc[df_pokemon_data['HP'] >= 100])

### Filtra valores de várias colunas
# print(df_pokemon_data.loc[(df_pokemon_data['HP'] >= 100) & (df_pokemon_data['Defense'] >= 100)])

### Reseta os índices de um dataframe
# df_pokemon_data_filtrado = df_pokemon_data.loc[df_pokemon_data['HP'] >= 100]
# df_pokemon_data_filtrado.reset_index(inplace=True, drop=True)
# print(df_pokemon_data_filtrado)

### Filtra por valor específico na string
# print(df_pokemon_data.loc[df_pokemon_data['Name'].str.contains('Mega')])

### Filtra pela ausência de valor específico na string
# print(df_pokemon_data.loc[~df_pokemon_data['Name'].str.contains('Mega')])

### Altera os valores de uma filtragem específica
# print(df_pokemon_data['Defense'].loc[df_pokemon_data['HP'] >= 200])
# df_pokemon_data.loc[df_pokemon_data['HP'] >= 200, ['Defense']] = '100'
# print(df_pokemon_data['Defense'].loc[df_pokemon_data['HP'] >= 200])

### Agrupa os dados
print(df_pokemon_data.groupby(['Type 1']).mean().sort_values(['Attack'], ascending=False))
