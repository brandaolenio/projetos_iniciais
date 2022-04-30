lista_de_compras = {'itens':['banana','maçã','uva','laranja'],
          'quantidade':[5,10,1,7],
          'preço_unitario':[1.20, 1.10, 3.15, 4.25]}

#item (a)
#Para cada item do dicionário imprimir na tela uma frase
# que identifique a fruta, seu valor unitário, sua quantidade e 
# o valor que custará para a aquisição da fruta na quantidade indicada
for fruta in range(4):
    if lista_de_compras['quantidade'][fruta] > 1:
        print('O valor unitário da {} é {}, as {} {}s custarão {}'.format(lista_de_compras['itens'][fruta], 
        lista_de_compras['preço_unitario'][fruta], lista_de_compras['quantidade'][fruta], lista_de_compras['itens'][fruta], 
        lista_de_compras['preço_unitario'][fruta]*lista_de_compras['quantidade'][fruta]))
    else:
        print('O valor unitário da {} é {}, então {} {} custará {}'.format(lista_de_compras['itens'][fruta], 
        lista_de_compras['preço_unitario'][fruta], lista_de_compras['quantidade'][fruta], 
        lista_de_compras['itens'][fruta], lista_de_compras['preço_unitario'][fruta]*lista_de_compras['quantidade'][fruta]))

# item (b)
# Calcule o total da compra
for fruta in range(4):
    total = 0
    total += lista_de_compras['preço_unitario'][fruta]*lista_de_compras['quantidade'][fruta]
print(f'O valor total da compra é de {total}')