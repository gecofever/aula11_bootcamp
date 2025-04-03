print("--------------------------------")
print("--------Vamos Adivinhar---------")
print("--------------------------------")

print("\nEscolha o nível de dificuldade")
print("1 - Facil | 2 - Médio | 3 - Dificil")
nivel = int(input("Qual nível pretende jogar: "))

if nivel == 1:
    max_tentativas = 12
elif nivel == 2:
    max_tentativas = 8
elif nivel == 3:
    max_tentativas = 4

numero_secreto = 50
rodada = 1
pontos = 1000
print("\nVocê tem 1000 pontos\n")

for rodada in range(1, max_tentativas+1):
    print(f"Tentativa de numero: {rodada}")
    seu_numero = int(input("Digite seu numero: "))

    acertou = seu_numero == numero_secreto
    maior = seu_numero > numero_secreto
    menor = seu_numero < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    elif (maior):
        print("Você errou, seu numero é maior do que o Numero Secreto\n")
        pontos = pontos - 25
    elif (menor):
        print("Você errou, seu numero é menor do que o Numero Secreto\n")
        pontos = pontos - 25
    
    max_tentativas -= 1

print(f"Você terminou com {pontos} pontos")