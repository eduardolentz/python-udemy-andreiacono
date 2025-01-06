# DICIONARIOS

aluno = {'nome':'Eduardo','idade':28, 'aprovado':True}

for x in aluno:
    print(x)
    
print(aluno.keys())

for x in aluno.values():
    print(x)
    
for x in aluno.items():
    print(x)
    
for keys, values in aluno.items():
    print(keys, values)
    
for x, y in aluno.items():
    print(f'-{x} é {y}')

