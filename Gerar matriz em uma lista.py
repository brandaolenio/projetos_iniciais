#Usar laço de repetição para criar uma matriz 3x3 em que cada posição (i,j) recebe o valor i*j
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        matriz[i][j] = i*j
print(matriz)