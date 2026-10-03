
import random

def soma(lista):
    total = 0
    for x in lista:
        total = total + x
    return total


def media(lista):
    return soma(lista) / len(lista)


def maior(lista):
    m = lista[0]
    for x in lista:
        if x > m:
            m = x
    return m


def menor(lista):
    m = lista[0]
    for x in lista:
        if x < m:
            m = x
    return m


def estaOrdenadaCrescente(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i + 1]:
            return False
        i = i + 1
    return True


def estaOrdenadaDecrescente(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] < lista[i + 1]:
            return False
        i = i + 1
    return True


def procura(lista, elem):
    i = 0
    while i < len(lista):
        if lista[i] == elem:
            return i
        i = i + 1
    return -1


# Programa principal

lista = []

opcao = -1

while opcao != 0:

    print("\n----- MENU -----")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n = int(input("Quantos elementos quer na lista? "))
        lista = []

        for i in range(n):
            lista.append(random.randint(1, 100))

        print("Lista criada:", lista)

    elif opcao == 2:
        n = int(input("Quantos elementos quer introduzir? "))
        lista = []

        for i in range(n):
            x = int(input("Introduza um número: "))
            lista.append(x)

        print("Lista criada:", lista)

    elif opcao == 3:
        if len(lista) > 0:
            print("Soma:", soma(lista))
        else:
            print("A lista está vazia!")

    elif opcao == 4:
        if len(lista) > 0:
            print("Média:", media(lista))
        else:
            print("A lista está vazia!")

    elif opcao == 5:
        if len(lista) > 0:
            print("Maior elemento:", maior(lista))
        else:
            print("A lista está vazia!")

    elif opcao == 6:
        if len(lista) > 0:
            print("Menor elemento:", menor(lista))
        else:
            print("A lista está vazia!")

    elif opcao == 7:
        if len(lista) > 0:
            if estaOrdenadaCrescente(lista):
                print("Sim")
            else:
                print("Não")
        else:
            print("A lista está vazia!")

    elif opcao == 8:
        if len(lista) > 0:
            if estaOrdenadaDecrescente(lista):
                print("Sim")
            else:
                print("Não")
        else:
            print("A lista está vazia!")

    elif opcao == 9:
        elem = int(input("Que elemento pretende procurar? "))
        print("Posição:", procura(lista, elem))

    elif opcao == 0:
        print("Lista final:", lista)
        print("Programa terminado!")

    else:
        print("Opção inválida!")