class Carro:
    marca = ''
    color = ''
    year = ''
    estado_inicial = True

    def atributos(self, color, ano, marca):
        print (self.atributos)

    def enceder (self):
     if estado == False:
        estado = True
        print (self.encender)
     else: 
        print(self.encender)

    def apagar (self):
     if estado == True:
        estado = False
        print (self.encender)
     else: 
        print(self.encender)

    def estado(self):
        if estado_inicial == True:
            return False
            print (self.estado)
        else: 
            return True
            print (self.estado)

carro1 = Carro()
carro1.atributos = ('Negro', 'Mercedes Benz')
carro1.enceder = False
carro1.apagar = True

print (carro1.atributos)
print (carro1.enceder)
print (carro1.apagar)
print (carro1.estado)



def nombre(a,b,c,d):
    print (a)


f = nombre('Maria','Maria','Maria','Maria')
print (f)






def escribe_media():
    media = (a + b) / 2
    print(f"La media de {a} y {b} es: {media}")
    return

a = 3
b = 5
escribe_media()
print("Programa terminado")