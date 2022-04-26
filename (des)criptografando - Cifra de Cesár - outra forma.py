def criptografar(chave, texto):
  letras = []
  alfabeto_minusc = 'abcdefghijklmnopqrstuvwxyz'
  alfabeto_maiusc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for letra in texto:
      if letra == " ":
          letras.append(letra)
      elif letra in alfabeto_minusc:
          letras.append(alfabeto_minusc[(alfabeto_minusc.index(letra)+chave) % len(alfabeto_minusc)])
      elif letra in alfabeto_maiusc:
          letras.append(alfabeto_maiusc[(alfabeto_maiusc.index(letra)+chave) % len(alfabeto_maiusc)])
      password = "".join(letras)
  print(password)


def descriptografar(chave, texto):
  letras = []
  alfabeto_minusc = 'abcdefghijklmnopqrstuvwxyz'
  alfabeto_maiusc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for letra in texto:
      if letra == " ":
          letras.append(letra)
      elif letra in alfabeto_minusc:
          letras.append(alfabeto_minusc[(alfabeto_minusc.index(letra)-chave) % len(alfabeto_minusc)])
      elif letra in alfabeto_maiusc:
          letras.append(alfabeto_maiusc[(alfabeto_maiusc.index(letra)-chave) % len(alfabeto_maiusc)])
      password = "".join(letras)
  print(password)