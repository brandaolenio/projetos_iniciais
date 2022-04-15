def quot_rest():
  print('Calculadora Quociente e Resto de Números Inteiros')
  first_number = int(input('Digite o dividendo: '))
  second_number = int(input('Digite o divisor: '))
  if second_number == 0:
      print('Não se pode dividir nenhum número por 0')
  else:
      divisao = divmod(first_number, second_number)
      print('A divisão de {} / {} retorna, respectivamente, o quociente e o resto {}'.format(first_number, second_number, divisao))
quot_rest()