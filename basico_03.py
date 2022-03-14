##### Programa para testar as funções básicas do pandas #####
import pandas as pd

df_pokemon_data = pd.read_csv('/Volumes/SSD - Dados/Programação/basico-pandas/pokemon_data.csv')

### Soma todos os valores de uma coluna verticalmente
# print(df_pokemon_data['HP'].sum(axis=0))

### Soma todos os valores das colunas horizontalmente
### Forma 1
# df_pokemon_data['Power'] = df_pokemon_data.iloc[:,4:7].sum(axis=1)
# print(df_pokemon_data['Power'])

### Forma 2
# df_pokemon_data['Power'] = df_pokemon_data[['HP', 'Attack', 'Defense']].sum(axis=1)
# print(df_pokemon_data['Power'])

### Salva o arquivo como csv, com os índices
#df_pokemon_data.to_csv('arquivo_teste.csv')

### Salva o arquivo como csv, sem os índices
#df_pokemon_data.to_csv('arquivo_teste.csv', index=False)

### Salva o arquivo como csv, sem os índices
#df_pokemon_data.to_excel('arquivo_teste.xlsx', index=False)

### Salva o arquivo como txt, com separador específico
df_pokemon_data.to_csv('arquivo_teste.txt', index=False, sep='\t')
