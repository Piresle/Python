
# Mudança de cores no terminal 

'''
ex:  \033[ _ ; _ ; _ m
# O primeiro número corresponde ao tipo de letra (personalização, estilo);
     -> 0: sem personalização
     -> 1: negrito
     -> 4: underline
     -> 7: negative (inverte as cores)
# O segundo corresponde à cor do texto (de 30 a 37);
    -> branco, vermelho, verde, amarelo, azul, roxo, ciano, cinza 
# E o terceiro corresponde à cor do terminal/fundo (40 ao 47)
    -> branco, vermelho, verde, amarelo, azul, roxo, ciano, cinza

-> sempre começa com \033[ e termina com a letra m
-> usa   \033[m  para usar as configurações normais
-> coloca \033[m ao final para 'cancelar' a personalização digitada antes 
'''

print('\033[36mHello World!')
print('\033[1;35;46mHello World!')
print('\033[7mHello World!') 
a = 'Leticia'
b = 'Pires' 
print(f'\033[36{a}\033[m Silva \033[34m{b}\033[m.')

