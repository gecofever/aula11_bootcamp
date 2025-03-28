import pandas as pd

class CsvProcessor:

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path, sep=";")
        return self.df

    def filtrar_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]

    def filtro_valor(self, coluna, atributo):
        return self.df[self.df[coluna] > atributo]
    

arquivo_csv = './carros.csv'
filtro = 'marca'
limite = 'Honda'

arquivo_CSV = CsvProcessor(arquivo_csv)
df = arquivo_CSV.carregar_csv()

print(df.head().to_string(index=False))
print()

print(arquivo_CSV.filtrar_por(filtro, limite))
print()

filtro = 'valor'
limite = 105000

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtro_valor(filtro, limite))