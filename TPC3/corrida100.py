
import random

def computador_joga(total):
    numero = 11 - (total % 11)

    if numero > 10:
        numero = random.randint(1, 10)

    return numero


def corrida_100():
    print("CORRIDA PARA OS 100")
    print("1 - Computador joga primeiro")
    print("2 - Jogador joga primeiro")

    opcao = int(input("Escolha uma opção: "))

    total = 0

    if opcao == 1:
        vez_computador = True
    else:
        vez_computador = False

    while total < 100:

        print("\nTotal atual:", total)

        if vez_computador:
            numero = computador_joga(total)
            print("O computador adicionou:", numero)

        else:
            numero = int(input("Escolha um número de 1 a 10: "))

            while numero < 1 or numero > 10:
                numero = int(input("Valor inválido. Escolha de 1 a 10: "))

        total = total + numero

        print("Novo total:", total)

        if total == 100:
            if vez_computador:
                print("O computador venceu!")
            else:
                print("Parabéns! Venceste!")
        else:
            vez_computador = not vez_computador


corrida_100()