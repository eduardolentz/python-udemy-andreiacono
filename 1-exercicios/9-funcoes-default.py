# Functions (Funções)
    #PARAMETROS --> ARGUMENTOS
    #Default e non-default

def boas_vindas(nome, quant=7):
    print(f'Olá {nome}.')
    print(f'Temos {str(quant)} de laptops.')
    
dig_nome = input('digite nome:')

    
boas_vindas(dig_nome)
boas_vindas(dig_nome, 9)
