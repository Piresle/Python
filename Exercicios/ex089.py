# Crie um porgrama que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada 
# aluno individualmente. 

ficha = []
while True:
    nome = str(input('Nome:  ')).capitalize().strip()
    nota1 = float(input('Nota 1:  '))
    nota2 = float(input('Nota 2:  '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    esc = str(input('Quer continuar? [S/N]  ')).upper()
    if esc == 'N': # ou -> if esc in 'Nn':
        break
print('-'*60)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-'*60)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*60)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)  '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('-'*60)
