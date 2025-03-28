print("--------------------------------")
print("--------Vamos Adivinhar---------")
print("--------------------------------")

numero_secreto = 50

seu_numero = int(input("Digite seu numero: "))

acertou = seu_numero == numero_secreto
maior = seu_numero > numero_secreto
menor = seu_numero < numero_secreto

if (acertou):
    print("Você acertou")
elif (maior):
    print("Você errou, seu numero é maior do que o Numero Secreto")
elif (menor):
    print("Você errou, seu numero é menor do que o Numero Secreto")