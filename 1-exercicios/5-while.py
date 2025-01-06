# While loop
'''
valor = 100
dia = 0

while valor>20:
    dia += 1
    print(f'No dia {dia} o produto vai ser vendido por R${valor}')
    #print(valor)
    valor -= 10    
'''   
# Ternary operator

idade = 15
'''
if idade>= 16:
    resultado = print('Voto permitido')
else:
    resultado = print('Voto não permitido')
'''
''' 
resultado = "Voto permitido" if idade>=16 else "Voto não permitido"
print(resultado)
'''

# while loops
valor = float(input('Digite o valor do seu produto:'))

while valor > 20:
    valor = (valor*0.10) + valor
    print(f'O valor final do do seu produto será de R${valor:.2f}')
    break