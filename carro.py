class Contador(object):

  def __init__(self, inicial=0):
    self.numero = inicial

  def siguiente(self):
    self.numero += 1
    return self.numero

cuenta = Contador()




class Carro:
    color = ''
    year = ''
    estado_inicial = False

    def encender(self):
        estado_inicial = True
        return ('Carro encendido')
        
    def apagar(self):
        estado_inicial=False
        return ('Carro apagado')

    def acelerar(self):
        estado_inicial=True
        for i in range(100):
            print(cuenta.siguiente())

    def frenar(self):
        estado_inicial=False
        return ('Carro frenando')


enriqueta = Carro()
print (enriqueta.encender())
print (enriqueta.acelerar())
print (enriqueta.frenar())

print (enriqueta.apagar())



