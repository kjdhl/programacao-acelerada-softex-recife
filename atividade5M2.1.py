def calculadora(num1, num2, op):
    if(op == '1'):
        return num1 +num2
    elif(op == '2'):
        return num1 - num2
    elif(op == '3'):
        return num1 * num2
    elif(op == '4'):
        return num1 / num2
    else:
        return 0

def verificandoOp(op):
    if op !='1' and op !='2' and op !='3' and op !='4' and op !='0':
        return 0
    elif(op == '0'):
        return 1
    else: 
        return ''


def entrada():
    num1 = float(input('numero 1: '))
    num2 = float(input('numero 2: '))
    return num1, num2




while 1:
    op = input('Digite o numero correspondente a opção desejada:\n \
    1 : Adição\n \
    2 : Subtração \n \
    3 : Multiplicação \n \
    4 : Divisão\n \
    0 : Sair\n')
    
    if(verificandoOp(op) == 0):
        print('Essa opção não existe!\n')
        continue
    elif(verificandoOp(op) == 1):
        print('Saindo ...')
        break

    num1, num2 = entrada()
    resultado = calculadora(num1, num2, op)
    print (f'Resultado = {resultado:.2f}\n')
    