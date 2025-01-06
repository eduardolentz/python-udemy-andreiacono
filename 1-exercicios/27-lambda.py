# LAMBDA FUNCTION
    # é uma função (pequena) sem nome
    # pode ter varios argumentos mas somente uma expressão
    # muito utilizadas dentro de outras funções
    # código mais limpo
    
def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 4

print(somar(2))