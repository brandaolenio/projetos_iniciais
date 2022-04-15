def exp():
  print('Calculadora Potência de Números Inteiros')
  first_number = int(input('Digite a base: '))
  second_number = int(input('Digite o expoente: '))
  potencia = first_number ** second_number
  print('{} elevado a {} é igual a {}'.format(first_number, second_number, potencia))
exp()