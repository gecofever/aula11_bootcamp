import pandas as pd

df = pd.read_csv("./carros.csv", sep=";")
print(df.head().to_string(index=False))

df_filtrado_marca = df[df['marca'] == 'Honda']
print()
print(df_filtrado_marca)

df_filtrado_valor = df[df['valor'] > 98000]
print()
print(df_filtrado_valor)