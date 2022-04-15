def mult():
  print('Calculadora Multiplicação de Números Inteiros')
  first_number = int(input('Digite o primeiro fator: '))
  second_number = int(input('Digite o segundo fator: '))
  multiplicacao = first_number * second_number
  print('A multiplicação de {} x {} é igual a {}'.format(first_number, second_number, multiplicacao))
mult()