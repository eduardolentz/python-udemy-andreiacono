
# TRY  E EXCEPT
    # excelente para testes
    # não realiza o 'stop' do programa
    # mensagens customizadas quando encontro o erro
    # https://docs.python.org/3/tutorial/errors.html


'''try:
    letras =  ['a','b','c']
    print(letras[3])
except IndexError:
    print('Index não existe')
    
print('Olá')'''

# ----------------------------------------------------------------- #
# Usando input

'''try:
    valor = int(input('Digite o valor do seu produto:'))
    print(valor)
except ValueError:
    print('Não é um valor válido')
    
    
print('Mais código abaixo')'''

# ----------------------------------------------------------------- #
# Adicionando else e finally

try:
    valor = int(input('Digite o valor do seu produto:'))
    print(valor)
except ValueError:
    print('Digitar um valor em número')
else:                      # --> É executado só se não dar erro
    print('Usuario digitou um valor correto')
    resultado = valor * 2
    print(resultado)
finally:                   # --> É executado independente de dar erro ou não
    print('Código ok') 
    
    
print('Mais código abaixo')