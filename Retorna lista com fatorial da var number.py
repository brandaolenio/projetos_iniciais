def factorial(number):
    multiplicacao = 1
    i = 1
    while i <= number:
        multiplicacao = i*multiplicacao
        i +=1
    return(multiplicacao)

print(factorial(9))