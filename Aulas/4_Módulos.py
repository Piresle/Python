
# Utilizando módulos 

# bibliotecas 
#   - import 
#      - importar bibliotecas externas 
#      - from ____ import ____  -> 1.biblioteca / 2.parte específica da biblioteca 
#   - ex: math (biblioteca de matemática); ceil/floor/trunc/pow/sqrt/factorial (partes específicas da bib. math)
#   - para importar mais de uma parte específica, usa-se vírgula (ex: from math import ceil, trunc)
 

# EX 
import math  # OU ->  from math import sqrt 
num = int(input('Digite um número: '))
raiz = math.sqrt(num) # depois do ponto em math, aparecem todas as funcionalidades da biblioteca # raiz = sqrt()
print(f'A raiz de {num} é igual a {raiz}')

# para ver todas as bibliotecas do Python
#   - site Python 

import random 
n = random.random() # random gera um número real entre 0 e 1 
print(n) 

# import + (ctrl + space)   -> mostra as bibliotecas 

