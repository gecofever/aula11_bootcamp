class Carro:

    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.vel_min = 0
        self.vel_max = 300

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print("Carro foi ligado")
        else:
            print("O carro já está ligado!")

    def desliga(self):
        if not self.ligado:
            print("Carro já está desligado!")
        else:
            self.ligado = False
            print("Carro encontra-se ligado?", self.ligado)

    def acelera(self):
        if self.velocidade < self.vel_max:
            self.velocidade += 10
            print(f'Velocidade {self.velocidade} km/h' )
        else:
            print("Você está na velocidade maxima")

    def desacelera(self):
        if self.velocidade > self.vel_min:
            self.velocidade -= 10
            print(f'Velocidade {self.velocidade} km/h' )
        else:
            print("O carro está parado")

carro = Carro('Preto', 'Civic')

carro.liga()
carro.acelera()
carro.acelera()
    