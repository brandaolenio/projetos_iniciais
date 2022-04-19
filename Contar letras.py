string = 'texto'
string_em_minusc = string.lower()
dicio_letras = {}
for letras in "abcdefghijklmnopqrstuvxwyz":
        dicio_letras[letras] = string_em_minusc.count(letras)           
print(dicio_letras)