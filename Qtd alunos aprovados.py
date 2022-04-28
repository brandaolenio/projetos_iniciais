def approved_alunes():
    # Usar dicionário para criar uma função que retorne a quantidade de alunos aprovados
    # Considerando média 70
    alunos = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}
    aprovados = 0
    for notas in alunos.values():
            if notas >= 70:
                aprovados +=1
    return aprovados

print(approved_alunes())