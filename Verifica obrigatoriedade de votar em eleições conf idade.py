def can_vote(age):
  #Retornar se dada pessoa poderá votar nas eleições considerando sua idade
  if age >= 0 and age < 16:
    return('Não pode votar')
  if age >= 16 and age <= 17:
      return('Pode votar mas não é obrigado')
  if age >= 18 and age <= 70:
      return('Deve votar orbigatoriamente')
  if age > 70:
      return('Pode votar mas não é obrigado')
  else:
    return('Idade inexistente')

print(can_vote(16))
