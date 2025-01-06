
# LIST COMPREHEMSION COM STRINGS
    # Mais simples de escrever
    # Utilizaado quando voce precisa criar uma nova lista a partir de uma existente
    # https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
    # [expressao for inten in intems]
    
    
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']


'''frutas2 = []

for item in frutas1:
    if 'n' in item:
        frutas2.append(item)'''

#frutas2 = [item for item in frutas1 if 'n' in item]

#print(frutas2)

# -------------------------------------------------------------- #
# LIST COMPREHEMSION COM NUMEROS

valores = [x for x in range(0, 101, 10)]
print(valores)






