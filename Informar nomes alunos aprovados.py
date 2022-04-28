def approved_alunes_names():
    # Usar dicionário abaixo para criar função que retorna o nome dos alunos aprovados
    # Considerando média 70
    alunos = {'Tulio':80,
              'Laercio':20,
              'Ana':50,
              'Rafaela':90,
              'Fernando':91,
              'Jones':10}

    aprovados = []
    for alunos, notas in alunos.items():
        if notas >= 70:
            aprovados.append(alunos)
    return(aprovados)