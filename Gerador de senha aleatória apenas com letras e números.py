import string
import random

def advanced_password_generator(password_size):
  letras = random.choices(string.ascii_letters + string.digits, k=password_size)
  password = "".join(letras)
  return password

print(advanced_password_generator(5))