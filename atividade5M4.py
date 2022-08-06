
def maiuscula(string):
    novaString = string.upper()
    return novaString

def minuscula(string):
    novaString = string.lower()
    return novaString

def tamanho(string):
    tamanho = len(string)
    return tamanho

def removerEspacos(string):
    novaString = string.replace(' ', '')
    return novaString

string = input('Digite uma string: ')
print(f'String em letras maiusculas: {maiuscula(string)}\nString em letras minusculas: {minuscula(string)}\nTamanho da string: {tamanho(string)}\nString sem espaços: {removerEspacos(string)}')