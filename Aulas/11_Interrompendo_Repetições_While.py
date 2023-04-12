
'''
 -> break 
    - quando usado, o comando break interrompe imediatamente o laço 

 -> while true: (loop infinito)

'''

cont = 1 
while cont <= 10:
   print(cont, '...', end='')
   cont += 1
print('Acabou')

print('-----'*10)

n = contad = 0
while n != 999: #quando digitar 999, o porgrama acaba, caso contrário, continua infinitamente
   n = int(input('Digite um número: [999 para parar] '))
   contad += 1

print('-----'*10)
'''
while True: #infinito
   print(cont, ' -> ', end='')
   cont += 1
print('FIM')
'''

print('-----'*10)

x = y = 0
while True:
   x = int(input('Digite um valor: [999 para parar] '))
   if x == 999: 
      break # o programa encerra se o número digitado for 999
   y += x
print(f'A soma vale {y}')

print('-----'*10)

