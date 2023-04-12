# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa 
# encerra quando ele disser que quer mostrar 0 termos. 

a1 = int(input('primeiro termo: '))
r = int(input('razão: '))
termo = a1
cont = 1 
total = 0
mais = 10
while mais != 0:
    total += mais 
    while cont <= total:
        print(termo, end=' -> ')
        termo += r
        cont += 1 
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')

 