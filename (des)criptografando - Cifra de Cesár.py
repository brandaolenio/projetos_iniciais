def criptografar(chave, texto):
    criptografada = ""
    for i in texto:
        if i == " ":
            criptografada += i
        elif i.islower():
            criptografada += chr((ord(i) + chave - 97) % 26+97)
        else:
            criptografada += chr((ord(i) + chave - 65) % 26+65)
    print(criptografada)


def descriptografar(chave, texto):
    descriptografada = ""
    for i in texto:
        if i == " ":
            descriptografada += i
        elif i.islower():
            descriptografada += chr((ord(i) - chave - 97) % 26+97)
        else:
            descriptografada += chr((ord(i) - chave - 65) % 26+65)
    print(descriptografada)
