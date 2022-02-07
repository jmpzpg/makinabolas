'''
Pruebas de la clase MakinaBolas
'''

import unittest
from makinabolas import MakinaBolas, MONEDA, BOLA, CAPACIDAD, ARCHIVO
#import makinabolas as mkb

class TestMakina(unittest.TestCase):
    ''' pruebas de la clase '''
    def test_constructor_por_defecto(self):
        '''  pruebas del constructor por defecto '''
        makina = MakinaBolas()
        self.assertIsNotNone(makina)

    def test_moneda_1e_es_valida(self):
        ''' prueba de que un euro es valido '''
        makina = MakinaBolas()
        resp = makina.aceptar_moneda(MONEDA)
        self.assertEqual(resp, True)

    def test_moneda_50cent_es_invalida(self):
        ''' prueba de que una moneda de 0,50 NO es valida '''
        makina = MakinaBolas()
        resp = makina.aceptar_moneda('Cent_50')
        self.assertEqual(resp, False)

    def test_giro_manivela_correcto(self):
        ''' Si gira una vuelta completa es True '''
        makina = MakinaBolas()
        giro = 360
        resp = makina.girar_manivela(giro)
        self.assertEqual(resp, True)

    def test_giro_manivela_incorrecto(self):
        ''' Si gira menos d euna vuelta completa es False '''
        makina = MakinaBolas()
        giro = 90
        resp = makina.girar_manivela(giro)
        self.assertEqual(resp, False)

    def test_moneda_y_giro_correctos_soltar_bola(self):
        ''' Si se ha insertado una moneda valida y se ha girado la manivela.
        Entonces deja caer la bola en el agujero'''
        makina = MakinaBolas()
        dep = makina.deposito
        mon = makina.monedero
        resp = makina.soltar_bola()
        self.assertEqual(resp, BOLA)
        self.assertEqual(makina.deposito, dep-1)
        self.assertEqual(makina.monedero, mon+1)

    def test_lectura_correcta_del_archivo_de_configuracion(self):
        ''' hola '''
        makina = MakinaBolas()
        self.assertEqual(makina.deposito, 73)
        self.assertEqual(makina.monedero, 27)