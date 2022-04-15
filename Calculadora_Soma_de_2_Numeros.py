def add():
  # TODO: retorne a soma dos parâmetros first_number e second_number
  first_number = int(input('Digite o primeiro número: '))
  second_number = int(input('Digite o segundo número: '))
  soma = first_number + second_number
  print('A soma de {} mais {} é igual a {}'.format(first_number, second_number, soma))
add()