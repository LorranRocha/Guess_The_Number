#   Importando módulos
import random
import os
import time

os.system('cls')

def gameplay():
    #   Gerar número aleatório de 0 a 10
    numero = random.randint(0, 10)
    vidas = 3
    valor = None

#   Jogo com escolhas do usuário

    while valor != numero:
        if numero <= 5:
            print("O número gerado é menor ou igual a 5\n\n")
        else:
            print("O número gerado é maior ou igual a 5\n\n")
        valor = int(input("Digite um valor: "))

        if valor == numero:
            print("Você acertou!!!")
            time.sleep(2)
            os.system('cls')
            
            opcao = int(input("Deseja Jogar Novamente?\n1: Sim\n2: Não\nResposta: "))
            if opcao == 1:
                os.system('cls')
                gameplay()
            else:
                break
        else:
            vidas -= 1
            print("Você errou!")
            print("Vidas restantes => {}".format(vidas))
            if vidas < 1:
                os.system('cls')
                print("Game Over\n")
                print("O número gerado foi: {}".format(numero))
                time.sleep(3)

                os.system('cls')
                opcao = int(input("Deseja Jogar Novamente?\n1: Sim\n2: Não\nResposta: "))
                if opcao == 1:
                    os.system('cls')
                    return gameplay()
                else:
                    break
            time.sleep(2)
            os.system('cls')

gameplay()