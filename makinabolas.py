''' clase principal '''

from genericpath import exists


MONEDA = 'Euro_1'
BOLA = 'Bola entregada'
CAPACIDAD = 100 # numero de bolas que caben en el deposito
ARCHIVO = 'estado_makina.csv'

class MakinaBolas():
    ''' Clase que representa la máquina '''
    def __init__(self) -> None:
        ''' Constructor de la clase '''
        if not exists(ARCHIVO):
            self.deposito = CAPACIDAD
            self.monedero = 0
        else:
            self.__leer_estado()

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
        self.__salvar_estado()
        return BOLA
    
    def __salvar_estado(self):
        with open(ARCHIVO, 'w') as manejador:
            datos = f'{self.deposito}, {self.monedero}\n'
            manejador.writelines(datos)

    def __leer_estado(self):
        with open(ARCHIVO, 'r') as manejador:
            datos = manejador.readline().split(',')
            self.deposito = int(datos[0])
            self.monedero = int(datos[1])

