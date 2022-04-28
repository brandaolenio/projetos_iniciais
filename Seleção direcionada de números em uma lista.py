def selecting_positive(list1, number):
    # A função retornará uma nova lista apenas com os valores maiores que number, estando number ou não
    # na lista. Exemplo: list1 = [10,20,30,40,50] e number = 20, a função deve retornar [30,40,50]
    new_list = []
    for x in list1:
        if x > number:
            new_list.append(x)
    return(new_list)