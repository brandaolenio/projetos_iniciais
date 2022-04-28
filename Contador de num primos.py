def is_prime_number(number):
  if isinstance(number, int) == True and number > 1: 
    contador = 0
    for num in range(2, number):
      if number % num == 0:
        contador +=1
    
    if contador > 0:
      return False 
    else:
      return True
  else:
    return False

print(is_prime_number(11))