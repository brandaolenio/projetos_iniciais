def is_even():
  #Retorna se número é par ou se é impar
    number = int(input('Digite o número a ser verificado: '))
    if (number%2) == 0:
        print('Número é par')
    else:
        print("Número é ímpar")

is_even()