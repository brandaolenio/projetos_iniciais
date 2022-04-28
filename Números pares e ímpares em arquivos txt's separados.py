def escrever_pares_impares():
    pares = open('pares.txt', 'a')
    impares = open('impares.txt', 'a')

    for numero in range(101):
        if numero % 2 == 0:
            pares.write("{} ".format(numero))
        else:
            impares.write("{} ".format(numero))
    
    pares.close()
    impares.close()

escrever_pares_impares()