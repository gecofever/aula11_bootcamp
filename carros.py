import pandas as pd

df = pd.read_csv("./carros.csv", sep=";")
print(df.head().to_string(index=False))

df_filtrado_marca = df[df['marca'] == 'Honda']
print()
print(df_filtrado_marca)

df_filtrado_valor = df[df['valor'] > 98000]
print()
print(df_filtrado_valor)

df_1 = df[['modelo', 'ano_fabricacao', 'valor']]
ano_maximo = df_1['ano_fabricacao'].max()
df_1_mais_novo = df_1[df_1['ano_fabricacao'] == ano_maximo]
print()
print(df_1_mais_novo)

valor_maximo = df_1_mais_novo['valor'].max()
df_1_maior_valor = df_1_mais_novo[df_1_mais_novo['valor'] == valor_maximo]
print(df_1_maior_valor)