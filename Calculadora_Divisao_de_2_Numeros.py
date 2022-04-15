def div():
  print('Calculadora Divisão de Números Inteiros')
  first_number = int(input('Digite o dividendo: '))
  second_number = int(input('Digite o divisor: '))
  if second_number == 0:
      print('Não se pode dividir nenhum número por 0')
  else:
      divisao = first_number / second_number
      print('A divisão de {} / {} é igual a {}'.format(first_number, second_number, divisao))
div()