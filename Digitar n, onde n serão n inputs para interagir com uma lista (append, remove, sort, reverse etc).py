#Digitar o input N, onde N serão n inputs para interagir com lista, com os códigos insert, print, remove,
#append, sort, pop, reverse
#Exemplo:
#N = 4
#append 1
#append 2
#insert 3 1
#print 
N = int(input())
lista= []
for i in range(N):
    n = str(input())    
    if n.startswith('i'):
        insert = n.split()
        i = insert[1]
        j = insert[2]
        lista.insert(int(i),int(j))
    elif n.startswith('pr'):
        print(lista)
    elif n.startswith('rem'):
        for i in n:
            if i.isnumeric() == True:
                lista.remove(int(i))
    elif n.startswith('a'):
        apend = n.split()
        i = apend[1]
        lista.append(int(i))
    elif n.startswith('s'):
        lista.sort()
    elif n.startswith('po'):
        for i in n:
            if i.isnumeric() == True:
                lista.pop(int(i))
        lista.pop()
    elif n.startswith('rev'):
        lista.reverse()