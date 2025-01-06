# Functions (Funções)
    #PARAMETROS --> ARGUMENTOS
    # Varios argumentos --> XARGS


def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado    
    

def media(*numeros):
    media = (numeros[0] + numeros[1] + numeros[2] + numeros[3])/4
    return media
    
# Pedindo valores    
num_um = int(input('Digite o primeiro numero:'))
num_dois = int(input('Digite o segundo numero:'))
num_tres = int(input('Digite o terceiro numero:'))
num_quatro = int(input('Digite o quarto numero:'))

resultado_soma = soma(num_um, num_dois, num_tres, num_quatro)
resultado_media = media(num_um, num_dois, num_tres, num_quatro)

print(f'A média dos dois valores informados é {resultado_media} e a soma dos mesmos é {resultado_soma}')


    