class Pizza:
    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor

    def pegar_pedaco(self):
        """Método da Instância"""
        self.pedacos -= 1

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos

mus = Pizza('Mussarela')
print(mus.pedacos)
mus.pegar_pedaco()
mus.pegar_pedaco()

print(Pizza.pedacos)

Pizza.mudar_tamanho(12)
print(Pizza.pedacos)

print(mus.pedacos)