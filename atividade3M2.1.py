import time

num = int(input('Segundos até a detonação da bomba: '))
print('Iniciando contagem regressiva')
for i in range(num+1):
    if(i<num): 
        if(i<10):
            print('0'+str(i))
            time.sleep(1) 
        else:
            print(i)
            time.sleep(1)

    else:
        if(i<10):
            print('0'+str(i))
            print('BUM!')
        else:
            print(i)
            print('BUM!') 
        

    
    