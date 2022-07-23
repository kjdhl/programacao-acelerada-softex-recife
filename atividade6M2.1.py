nome = input('Nome do usuário: ')
while 1:
    try:
        anoNasc = int(input('Ano de nascimento: '))

        if(anoNasc<1922 or anoNasc>2021):
            raise Exception('Valor de ano invalido!')
        else:
            break
    except Exception as err:
        print(err)
idade = 2022 - anoNasc
print(f'{nome} possui {idade} anos')