# Listas com looping
'''
valores = [50,80,110,150,170]

index = 0
soma = 0

for num in valores:
    index += 1
    soma += num
    print(f'O valor {index} é {num}')
    
print(f'A soma dos valores é {soma}')
'''
# ---------------------------------------------- #

cores = ['amarelo','verde', 'azul', 'vermelho']

cor_desejada = input('Digite uma cor:')

if cor_desejada.lower() in cores:
    print('Sim')
else:
    print('Não')