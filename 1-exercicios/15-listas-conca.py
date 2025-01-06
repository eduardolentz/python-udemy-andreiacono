# CONCATENANDO LISTAS

numeros = [2,3,4,5]
dobro = numeros * 4

print(dobro)

letras = ['b','c','d','e','f']
soma = numeros + letras
print(soma)

numeros.extend(letras)
print(numeros)

# Listas dentro de listas

itens = [['um','dois'],['tres','quatro']]

print(itens[1][1])

# Extranindo variaveis de lista

item = itens[1][0]
print(item)

# Unpacking lists

produtos =['arroz', 'feijao','laranja','banana',5,6,7,'Manga']

produto1, produto2, produto3, produto4, *outros, produto8 = produtos

print(produto1)
print(produto4)
print(outros)
print(produto8)