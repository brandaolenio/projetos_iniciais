def multiplication_table(number):
    tabuada = []
    for i in range(1,11):
        tabuada.append(number*i)
    return tabuada

print(multiplication_table(9))