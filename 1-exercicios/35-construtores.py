
# CONSTRUTORES:
    # https://docs.python.org/pt-br/3.13/tutorial/classes.html

# ----------------------------------------------------------- #
from datetime import datetime
class Usuarios:
    def __init__(self, nome, sobrenome, ano):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano = ano
        
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    def idade_usuario(self):
        ano_atual = datetime.now().year
        self.ano = int(ano_atual - self.ano)
        return self.ano
        
        
        
usuario1 = Usuarios('Eduardo','Lentz',1996)
usuario2 = Usuarios('Henrique', 'Corso', 1997)
usuario3 = Usuarios('Gabriela','Lentz',2006)

print(usuario1.nome)
print(usuario2.sobrenome)
print(usuario3.ano)
print(usuario1.nome_completo())
print(usuario1.idade_usuario())