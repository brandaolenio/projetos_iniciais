def prime_numbers(number):
  num_primos = []
  if isinstance(number, int) == True and number > 1:
    for num in range(2, number):
      if num == 2 or num == 3:
        num_primos.append(num)
      elif num % 2 == 0 or num % 3 == 0:
        continue
      elif num % 2 > 0:
        num_primos.append(num)
    return num_primos
  else:
    return num_primos

print(prime_numbers(2))