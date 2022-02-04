'''
Será el código de la función principal de la máquina
'''
import makinabolas
from makinabolas import BOLA

makina = makinabolas.MakinaBolas()
SEGUIR = True
while SEGUIR:
    moneda = input('Introduce una moneda válida, ejemplo: "Euro_1":  ')
    if makina.aceptar_moneda(moneda):
        try:
            giro = int(input('Introduce el giro (360=OK): '))
        except ValueError:
            print('Solo se admiten números enteros.')
            giro = 0
        if makina.girar_manivela(giro):
            print(makina.soltar_bola())
            print(f'Quedan {makina.deposito} bolas')
            print(f'Hay {makina.monedero} monedas')
        else:
            print('Debe girar 360 grados si quiere la bola. Operación cancelada')
            continue
    else:
        print('Debe introducir una moneda de 1 euro')
        continue
    resp = input('Quieres más bolas? (s/n): ').upper()
    if resp == 'N':
        SEGUIR = False
