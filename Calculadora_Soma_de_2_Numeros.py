def add():
  print('Calculadora Soma de Números Interios')
  first_number = int(input('Digite a primeira parcela: '))
  second_number = int(input('Digite a segunda parcela: '))
  soma = first_number + second_number
  print('A soma de {} + {} é igual a {}'.format(first_number, second_number, soma))
add()