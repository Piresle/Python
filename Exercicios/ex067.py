# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo 
# usuário. O programa será interrompido quando o número solicitado for negativo.

print('-----'*3,'TABUADA','-----'*3)
while True:
    tab = int(input('Digite um número: '))
    print('-' * 30)
    if tab < 0:
        break
    for n in range(1, 11):
        print(f'{tab} x {n} = {tab*n}')
    print('-' * 30)
print('Tabuada encerrada!')

