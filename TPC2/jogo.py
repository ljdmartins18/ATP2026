print ("Modalidade do jogo: 1 - Utilizador adivinha o número, 2 - Computador adivinha o número")  
modalidade = input ("Escolha a modalidade do seu jogo:")
if modalidade == "1":
    
    from random import randint
    computador = randint(0, 100)
    jogador = int(input("Em que número estou a pensar?(0-100): ")) 
    tentativas = 0

    while jogador != computador:
        if jogador < computador:
            print("O número que estou a pensar é maior.")
            jogador = int(input("Em que número estou a pensar?(0-100): ")) 
            tentativas = tentativas + 1
        elif jogador > computador:
            print("O número que estou a pensar é menor.")
            jogador = int(input("Em que número estou a pensar?(0-100): "))
            tentativas = tentativas + 1 
        
    tentativas = tentativas + 1 
    print(f"Acertou o número em {tentativas} tentativas")


elif modalidade == "2":

    print("Pensa num número de 0 a 100, se o número que escolheste for maior, digita 'maior', se o número for menor, digita 'menor'.")
    min = 0
    max = 100
    tentativas = 0
    palpite = int((min + max)/2)
    print(palpite)
    resposta = input("Como foi o meu palpite? (maior, menor, acertou): ")

    while resposta != "acertou":
        if resposta == "maior":
            min = palpite + 1
            palpite = int((min + max)/2)
            print(palpite)
            resposta = input("Como foi o meu palpite? (maior, menor, acertou): ")
            tentativas = tentativas + 1
        elif resposta == "menor":
            max = palpite - 1
            palpite = int((min + max)/2)
            print(palpite)
            resposta = input("Como foi o meu palpite? (maior, menor, acertou): ")
            tentativas = tentativas + 1
        
    tentativas = tentativas + 1
    print (f"Acertei o número em {tentativas} tentativas")
    
else:
    print ("Modalidade inválida.")
