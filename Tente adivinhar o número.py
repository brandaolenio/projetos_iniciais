#Brincar de adivinhar!
# Tente advinhar o número pseudoaleatório escolhido.
# caso contrário avise se ele deve chutar um número maior ou menor do que o número chutado.
# O programa deve continuar pedindo por um chute até que o jogador acerte!
import random
def advinha():
    print('Tente advinhar o número por mim escolhido')
    x = random.choice(range(20))
    y = int(input('>'))
    while y != x:
        if y - 2 < x < y + 2:
            if y < x:
                print('Você está quente. Escolha um número maior')
                y = int(input('>'))
            else:
                print('Você está quente. Escolha um número menor')
                y = int(input('>'))
        elif y - 5 < x < y + 5:
            if y < x:
                print('Você está frio. Escolha um número maior')
                y = int(input('>'))
            else:
                print('Você está frio. Escolha um número menor')
        elif y < x:
            print('Você está congelando. Escolha um número maior')
            y = int(input('>'))
        elif  y > x:
            print('Você está congelando. Escolha um número menor')
            y = int(input('>'))
    print('Você acertou! Parabéns')

advinha()