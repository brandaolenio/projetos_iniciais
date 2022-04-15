def sub():
  print('Calculadora Subtração de Números Inteiros')
  first_number = int(input('Digite o minuendo: '))
  second_number = int(input('Digite o subtraendo: '))
  subtracao = first_number - second_number
  print('A subtração de {} - {} é igual a {}'.format(first_number, second_number, subtracao))
sub()