print("--------------------------------")
print("---------Jogo da Forca----------")
print("--------------------------------")

palavra_secreta = 'banana'
acertou = False
enforcou = False
erros = 0

letras_corretas = ['_', '_', '_', '_', '_', '_']

print(letras_corretas)

while (not acertou and not enforcou):
    chute = input('Qual a letra? ')

    if (chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_corretas[posicao] = letra
            posicao += 1
    else:
        erros += 1

    acertou = '_' not in letras_corretas
    enforcou = erros == 6
    print(letras_corretas)

if (acertou):
    print("Você ganhou!!")
else:
    print("Você perdeu!!")

print('Fim do Jogo')