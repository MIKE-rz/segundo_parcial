"""
PROBLEMA:
Calcular el rendimiento de combustible de un vehículo y el costo
del combustible consumido durante un recorrido.
"""
#ENTRADAS:
#distancia: número real mayor que cero, expresado en kilómetros.
#litros: número real mayor que cero, correspondiente a los litros
#de combustible consumidos.

#SALIDAS:
#- Distancia recorrida en kilómetros.
#- Cantidad de litros consumidos.
#- Precio por litro de combustible.
#- Rendimiento del vehículo en kilómetros por litro.
#- Costo total del combustible consumido.
#El rendimiento y el costo se muestran con dos decimales.

#REGLAS Y SUPUESTOS:
#- El precio por litro de combustible es de $24.00.
#- La distancia debe ser mayor que cero.
#- Los litros consumidos deben ser mayores que cero.
#- El rendimiento se calcula dividiendo la distancia entre los litros.
#- El costo se calcula multiplicando los litros por $24.00.
#- El rendimiento se expresa en kilómetros por litro.
#- Los importes monetarios se muestran en pesos mexicanos
#  con dos decimales.
#- Se utiliza tabulate para presentar los resultados en una tabla.

#ALGORITMO:
#1. Solicitar la distancia recorrida en kilómetros.
#2. Solicitar la cantidad de litros consumidos.
#3. Calcular el rendimiento dividiendo la distancia entre los litros.
#4. Calcular el costo multiplicando los litros por $24.00.
#5. Mostrar la distancia, los litros, el precio por litro,
#   el rendimiento y el costo total mediante una tabla.

#CASOS DE PRUEBA:
#Caso 1:
#Entrada: 120 km y 10 litros.
#Rendimiento: 120 / 10 = 12.00 km/L.
#Costo: 10 * 24 = $240.00.

#Caso 2:
#Entrada: 250 km y 20 litros.
#Rendimiento: 250 / 20 = 12.50 km/L.
#Costo: 20 * 24 = $480.00.

#Caso 3:
#Entrada: 180 km y 15 litros.
#Rendimiento: 180 / 15 = 12.00 km/L.
#Costo: 15 * 24 = $360.00.

#Caso 4:
#Entrada: 300 km y 25 litros.
#Rendimiento: 300 / 25 = 12.00 km/L.
#Costo: 25 * 24 = $600.00.

#RESTRICCIONES PARA EL AGENTE:
#- La única biblioteca externa permitida es tabulate.
#- No agregar bibliotecas externas adicionales.
#- Respetar las funciones indicadas en el contrato.
#- Mantener el precio del combustible en $24.00 por litro.
#- No dividir entre cero.
#- Mostrar los resultados mediante tabulate.

#CONTRATO DE FUNCIONES:
#leerDatos():
#Solicita y retorna la distancia recorrida y los litros consumidos.
#Ambos valores deben ser mayores que cero.

#calcularRendimiento(distancia, litros):
#Recibe la distancia en kilómetros y los litros consumidos.
#Retorna el rendimiento calculado como distancia / litros.

#calcularCosto(litros):
#Recibe los litros consumidos y retorna el costo total
#calculado como litros * 24.

#mostrarResultados(distancia, litros, rendimiento, costo):
#Recibe la distancia, los litros, el rendimiento y el costo.
#Muestra todos los resultados mediante tabulate.
from tabulate import tabulate

def leerDatos():
    while True:
        try:
            distancia = float(input("Ingrese la distancia recorrida en kilómetros (mayor que cero): "))
            if distancia <= 0:
                print("La distancia debe ser mayor que cero. Intente nuevamente.")
                continue
            litros = float(input("Ingrese la cantidad de litros consumidos (mayor que cero): "))
            if litros <= 0:
                print("Los litros consumidos deben ser mayores que cero. Intente nuevamente.")
                continue
            return distancia, litros
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")


def calcularRendimiento(distancia, litros):
    return distancia / litros


def calcularCosto(litros):
    return litros * 24


def mostrarResultados(distancia, litros, rendimiento, costo):
    tabla = [
        ["Distancia recorrida (km)", distancia],
        ["Litros consumidos", litros],
        ["Precio por litro ($)", 24],
        ["Rendimiento (km/L)", rendimiento],
        ["Costo total ($)", costo]
    ]
    print(tabulate(tabla, headers="firstrow", tablefmt="grid"))
