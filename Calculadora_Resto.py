def rest():
  print('Calculadora Resto da Divisão de Números Inteiros')
  first_number = int(input('Digite o dividendo: '))
  second_number = int(input('Digite o divisor: '))
  resto = float(first_number % second_number)
  print('Ao dividir {} por {} sobra o resto {}'.format(first_number, second_number, resto))
rest()