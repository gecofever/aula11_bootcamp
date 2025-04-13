from car_poo import *
from random import randint


carros= []

for i in range(10):
    placa = randint(1000, 5000)
    carros.append(Carro(placa))

motos = []

for i in range(20):
    placa = randint(5100, 9999)
    motos.append(Moto(placa))

estacionamento = Estacionamento(5, 5)
#print(estacionamento)

for i in range(3):
    estacionamento.estacionar_carro(carros[i])

estacionamento.estacionar_carro(carros[3])
print(estacionamento)

estacionamento.estacionar_moto(motos[6])
print(estacionamento)