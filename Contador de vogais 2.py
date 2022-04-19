def contar_vogais():
    string = str(input('Digite uma frase ou palavra: '))
    string_em_minusc = string.lower()
    dicio_vogais = {}
    for vogais in "aeiou":
        contar = string_em_minusc.count(vogais)
        dicio_vogais[vogais] = contar
    valores = dicio_vogais.values()
    tds_vogais = sum(valores)
    print(tds_vogais)

contar_vogais()