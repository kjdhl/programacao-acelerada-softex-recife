import enum
import os

class candidatos(enum.Enum):
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    branco = 0


votos = {'candidato_X': 0, 'candidato_Y': 0, 'candidato_Z': 0, 'brancosEnulos': 0}

while 1:
    try:
        print('lista de candidatos:\n\
        candidato_X = 889\n\
        candidato_Y = 847\n\
        candidato_Z = 515\n\
        branco = 0\n')

        voto = int(input('Insira seu voto: '))
        if(voto == candidatos.candidato_X.value):
            votos['candidato_X'] +=1
        elif(voto == candidatos.candidato_Y.value):
            votos['candidato_Y'] +=1
        elif(voto == candidatos.candidato_Z.value):
            votos['candidato_Z'] +=1
        elif(voto == candidatos.branco.value):
            votos['brancosEnulos'] +=1
        else:
            votos['brancosEnulos'] +=1
        
        print('Finalizar votação?\n"S"- sim  Qualquer outra tecla - não')
        inp = input()
        if(inp == 'S'):
            break
        os.system('cls')
    except:
        os.system('cls')
        print('Voto invalido!')


brancosEnulos = votos.pop('brancosEnulos')
print('\nResultado da eleição: ')
for i in sorted(votos, key = votos.get, reverse = True):
    print(i,': ' ,votos[i], ' votos')
print('Votos Brancos e Nulos: ',brancosEnulos, ' votos')


