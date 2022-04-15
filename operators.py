def add():
  # TODO: retorne a soma dos parâmetros first_number e second_number
  first_number = int(input('Digite o primeiro número: '))
  second_number = int(input('Digite o segundo número: '))
  soma = first_number + second_number
  print('A soma de {} mais {} é igual a {}'.format(first_number, second_number, soma))
add()

def sub(first_number, second_number):
  # TODO: retorne a subtração dos parâmetros first_number e second_number
  sub = first_number-second_number
  return(sub)

def mult(first_number, second_number):
  # TODO: retorne a multiplicação dos parâmetros first_number e second_number
  mult = first_number*second_number
  return(mult)

def div(first_number, second_number):
  # TODO: retorne a divisão dos parâmetros first_number e second_number
  div = first_number/second_number
  return(div)

def expo(first_number, second_number):
  # TODO: retorne a exponenciação dos parâmetros first_number e second_number
  expo = first_number**second_number
  return(expo)

def remai(first_number, second_number):
  # TODO: retorne o resto da divisão dos parâmetros first_number e second_number
  remai = first_number%second_number
  return(remai)

def quoti_remai(first_number, second_number):
  # TODO: retorne o quociente e o resto da divisão, nesta exata ordem, dos parâmetros first_number e second_number
  quoti_remai = divmod(first_number, second_number)
  return(quoti_remai)