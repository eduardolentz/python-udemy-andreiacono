
# CONSTRUTORES:
    # https://docs.python.org/pt-br/3.13/tutorial/classes.html

# ----------------------------------------------------------- #

class Usuarios:
    def __init__(self, nome, sobrenome, data):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data = data
        
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
        
        
usuario1 = Usuarios('Eduardo','Lentz','13/08/1996')
usuario2 = Usuarios('Henrique', 'Corso', '11/05/1997')
usuario3 = Usuarios('Gabriela','Lentz','29/04/2006')

print(usuario1.nome)
print(usuario2.sobrenome)
print(usuario3.data)
print(usuario1.nome_completo())