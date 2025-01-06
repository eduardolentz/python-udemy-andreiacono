# Functions (Funções)
    #PARAMETROS --> ARGUMENTOS
    # Varios argumentos --> XARGS identificando o perametro

def agencia(**carro): 
    return carro

print(agencia(modelo='Gol', cor='Branco', motor=1.0, placa=1234))
print(agencia(modelo='Gol', cor='Azul', motor=1.0))
print(agencia(modelo='Gol', cor='Preto', motor=1.0, placa=1444))

