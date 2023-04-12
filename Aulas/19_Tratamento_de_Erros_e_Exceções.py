'''
-> SINTAXE
    - erros de "escrita"
    - ex: primt()

-> SEMÂNTICO
    - erros de "significado"
    - ex: 
        > digitar "print(x)" sem especificar o "x" (o "x" não existe)
    
-> VALUEERROR (exceção)
    - erro de valor
    - ex: str / int (operações entre str e int)

-> INDEXERROR (exceção)
    - ex: buscar um índice que não existe na lista/tupla/dicionário

-> Exceções
    - erros de casos específicos

-> Try...: Except: Else: Finally:
    - semelhante ao if/else
    - Try (tente) algo:
        > pode ter vários except
        > cada ação do bloco try, pode ter um bloco try 
    Except:
        > resposta caso o Try não funcione
        > except Exception as erro:
            - informa qual foi o erro 
            - pode ter vários diferentes
            - se for colocar mais de um erro no mesmo except, coloca entre ( ), separando por vírgula
    Else:
        > diz o que vai acontecer se o try funcionou 
        > cláusula opcional
    Finally:
        > acontece independente se deu certo ou se deu erro
        > cláusula opcional
'''

try:
    a = int(input('Numerador:  '))
    b = int(input('Denominador:  '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito Obrigado!')
