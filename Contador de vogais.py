def contar_vogais():   
    string = str(input('Digite uma palavra ou frase: '))
    string_em_minusc = string.lower()
    soma_vogais = 0
    vogais = 'aeiou'
    for i in vogais:
     if i in string_em_minusc:
        soma_vogais += string_em_minusc.count(i)
    print(soma_vogais)


contar_vogais()