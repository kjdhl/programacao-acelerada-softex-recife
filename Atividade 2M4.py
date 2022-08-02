
class carro:
    totalCarros = 0
    def __init__(self, modelo,):
        self.modelo = modelo
    def registrarCarro(self):
        carro.totalCarros += 1

    
    
carro1 = carro('Ford GT40')
carro1.registrarCarro()
carro2 = carro('McLaren Senna')
carro2.registrarCarro()
carro3 = carro('Ferrari F50')
carro3.registrarCarro()

print(carro1.totalCarros) #3
print(carro2.totalCarros) #3
print(carro3.totalCarros) #3


        
