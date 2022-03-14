##### Programa para testar as funções básicas do pandas #####
import pandas as pd

df_pokemon_data = pd.read_csv('/Volumes/SSD - Dados/Programação/basico-pandas/pokemon_data.csv')

### Retorna as primeiras linhas de um dataframe
# print(df_pokemon_data.head(10))

### Retorna as ultimas linhas de um dataframe
# print(df_pokemon_data.tail(10))

### Retorna todas as linhas que possuem o parametro passado
# print(df_pokemon_data.loc[df_pokemon_data['Type 2'] == 'Poison'])

### Retorna uma linha com index em específico em diante
# print(df_pokemon_data.loc[10:])

### Retorna uma linha com index em específico até outro. Valor inicial e final incluso
# print(df_pokemon_data.loc[10:20])

### NOTA: '.loc' funciona apenas para linhas e colunas de mesma notação
###       '.iloc' funciona para navegar como uma matriz passando posições inteiras
###       como referência. Ex: df_pokemon_data.iloc[10:20]

### Exemplo acima. Valor inicial incluso, final excluso.
# print(df_pokemon_data.iloc[10:20]) 

### Sendo assim, é possível interar entre rótulos não inteiros como rótulos de colunas
### Colunas 10 à 12. Valor inicial incluso, final excluso.
# print(df_pokemon_data.iloc[:,10:12])

### Informa dados úteis sobre as colunas
# print(df_pokemon_data.describe())

### Ordena os dados pelo índice de forma ascendente
# print(df_pokemon_data.sort_index())

### Ordena os dados pelo índice de forma descendente
# print(df_pokemon_data.sort_index(ascending=False))

### Ordena os dados da coluna de forma ascendente
# print(df_pokemon_data.sort_values('Name'))

### Ordena os dados tendo como base as colunas passadas por parâmetro
# print(df_pokemon_data.sort_values(['Name', 'HP'], ascending=[True, False]))

### Soma valores de colunas
# df_pokemon_data_total = df_pokemon_data['HP'] + df_pokemon_data['Attack'] + df_pokemon_data['Defense']
# print(df_pokemon_data_total)

### Cria uma nova coluna com base em outras colunas
### Forma 1
# df_pokemon_data['Power'] = df_pokemon_data['HP'] + df_pokemon_data['Attack'] + df_pokemon_data['Defense']
# print(df_pokemon_data.head())

### Forma 2
# df_pokemon_data['Power'] = df_pokemon_data.iloc[:,4:10].sum(axis=1)
# print(df_pokemon_data.head())

##### Deleta uma coluna de um dataframe
### Forma 1
# df_pokemon_data_modificada = df_pokemon_data.drop(columns=['Generation'])
# print(df_pokemon_data_modificada.head())

### Forma 2
# df_pokemon_data_modificada = df_pokemon_data.drop('Generation', axis=1)
# print(df_pokemon_data_modificada.head())

##### Deleta uma linha de um dataframe
### Forma 1
# df_pokemon_data_modificada = df_pokemon_data.drop(index=[1])
# print(df_pokemon_data_modificada.head())

### Forma 2
# df_pokemon_data_modificada = df_pokemon_data.drop(1, axis=0)
# print(df_pokemon_data_modificada.head())

### Remoção de múltiplas linhas consecutivas
# df_pokemon_data_modificada = df_pokemon_data.drop(df_pokemon_data.index[3:5])
# print(df_pokemon_data_modificada.head())

### Caso não queira criar uma cópia do dataframe e que a alteração seja aplicada
df_pokemon_data.drop(df_pokemon_data.index[3:5], inplace=True)
print(df_pokemon_data.head())
