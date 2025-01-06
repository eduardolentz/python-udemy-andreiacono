
#For loops - Numeros
'''
for numero in range(0,101,10):
    print(numero)
'''    
    
#For loops - Strings
'''
palavra = input('Digite uma palavra:')

for letra in palavra:
    print(letra)
'''

#For loops - utilizando if e else
'''
compra_confirmada = False
dados_compra = 'Compra no valor de R$12,50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Dados enviados para o seu email')
        break
    else:
        print('Falha na compra')
        break
'''

#For loop - nested loop (outer loop and inner loop)
'''
for numero1 in range(10,51,10):
    print('Produto ' + str(numero1))
    for numero2 in range(1,4):
         print(numero1, numero2)
'''

#For loop - Separando Strings
'''
palavra = input('Digite um palavra:')

for space in palavra:
    print(space.upper(), end=' ')
'''

#For loop - Criando um retangulo

linhas = 6
colunas = 6
simbolo = '#'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end=' ')
    print() 