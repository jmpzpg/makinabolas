''' clase principal '''
MONEDA = 'Euro_1'
BOLA = 'Bola entregada'
CAPACIDAD = 100 # numero de bolas que caben en el deposito

class MakinaBolas():
    ''' Clase que representa la máquina '''
    def __init__(self) -> None:
        ''' Constructor de la clase '''
        self.deposito = CAPACIDAD
        self.monedero = 0

    def aceptar_moneda(self, moneda_insertada):
        ''' el metodo para aceptaruna moneda y devuelve True o False
        dependiendo de si es un euro o no '''
        return moneda_insertada == MONEDA
        #if moneda_insertada == MONEDA:
        #    return True
        #else:
        #    return False
    def girar_manivela(self, giro):
        ''' Simula el giro de la manivela despues de introducir la moneda.
        Solo funciona con giros de 360'''
        return giro == 360

    def soltar_bola(self):
        ''' Si se ha insertado una moneda valida y se ha girado la manivela.
        Entonces deja caer la bola en el agujero.
        Se decrementa el numero de bolas e incrementa el numero de monedas'''
        self.deposito -= 1
        self.monedero += 1
        return BOLA
