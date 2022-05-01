#Indicar quantos alunos são. Indicar seus nomes e notas. Printe o(s) nome(s) do(s) 
# alunos(s) que recebeu/receberam a segunda menor nota. Se há múltiplos alunos que
#  receberam essa segunda menor nota, printe-os em ordem alfabética. Deverá haver
# pelo menos 2 alunos na lista aninhada.

import operator
def nested_list():
    lista1 = []
    for i in range(int(input('Escolha quantos alunos serão(pelo menos 2 alunos): '))):
        nome = input('Informe o aluno: ')
        nota = float(input("Informe a nota desse aluno: "))
        lista1.append([nome, nota])
        lista1.sort(key=operator.itemgetter(1))
    lista2 = []
    for i in lista1:
        if i[1] > lista1[0][1]:
           lista2.append(i)
           lista2.sort(key=operator.itemgetter(1))
    alunos = []
    for j in lista2:
        if j[1] == lista2[0][1]:
            alunos.append(j)
            alunos.sort()
    for x in alunos:
        print(x[0])

nested_list()