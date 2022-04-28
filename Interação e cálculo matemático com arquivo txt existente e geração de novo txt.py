def leitura_escrita_arquivo():
    pares = open('pares.txt', 'r')
    #O arquivo 'pares.txt' já deve existir em algum diretório, preferencialmente no mesmo
    # diretório do arquivo.py dessa função
    num_pares = pares.read().split()

    multiplos = open('multiplos.txt', 'a')
    for num in num_pares:
        num = int(num)
        if num % 3 == 0:
            multiplos.write('{}, '.format(num))
        else:
            continue
    multiplos.close()

leitura_escrita_arquivo()