#selecionar o número 2 nos objetos abaixo
# Exemplo: para selecionar o número do 2 em lista1 = [[1,3,4],5,[1,3,[2]]]

# item (a)
lista = [1,3,[1,3,{1:3,3:2}]]
print(lista[2][2][3])

# item (b)
dict1 = {'a':1, 'b':[1,3,{'a':1, 'b':2}]}
print(dict1['b'][2]['b'])

# item (c)
mat = [[1,3,4],[5,6,8],[[1,2,3]]]
print(mat[2][0][1])