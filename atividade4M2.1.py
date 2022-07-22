
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

num1 = float(input('numero 1: '))
num2 = float(input('numero 2: '))
op = input('Escolha a operação operação, digite entre 1 e 4 para:\n \
1 : Adição\n \
2 : Subtração \n \
3 : Multiplicação \n \
4 : Divisão\n')

resultado = calculadora(num1, num2, op)
print (f'Resultado = {resultado:.2f}')
    