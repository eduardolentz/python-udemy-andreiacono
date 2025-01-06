# Functions (Funções)
    #PARAMETROS --> ARGUMENTOS
    #Realizam uma tarefa
    #Calcula e retorna um valor
'''
def cliente1(nome):
    print(f'Olá {nome}')
    
    
# função com retorno
def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('Maria')
y = cliente2('Jose')

print(x)
print(y)
'''
#função sem retorno
def soma(num1, num2):
    soma = num1 + num2
    print(f'A soma dos dois numeros é {soma}')

#funçaõ com retorno
def media2(num1, num2):
    media = (num1 + num2) /2
    return media
    
# Pedindo valores    
num_um = int(input('Digite um numero:'))
num_dois = int(input('Digite outro numero:'))

# Chamando função com retorno
resultado = media2(num_um, num_dois)
print(f'A média dos dois valores informados é {resultado}')

#Chamando função sem retorno
soma(num_um, num_dois)
    