from ejercicios import ejercicio1_cine
from ejercicios import ejercicio2_combustible

from ejercicios import ejercicio1_cine
from ejercicios import ejercicio2_combustible


def mostrarMenu():
    print("SEGUNDO PARCIAL")
    print("1. Venta de boletos de cine")
    print("2. Consumo de combustible")
    print("0. Salir")


def ejecutarEjercicio1():
    cantidad = ejercicio1_cine.leerCantidad()
    subtotal = ejercicio1_cine.calcularSubtotal(cantidad)
    descuento = ejercicio1_cine.calcularDescuento(cantidad, subtotal)
    ejercicio1_cine.mostrarCompra(cantidad, subtotal, descuento)


def ejecutarEjercicio2():
    distancia, litros = ejercicio2_combustible.leerDatos()
    rendimiento = ejercicio2_combustible.calcularRendimiento(
        distancia, litros
    )
    costo = ejercicio2_combustible.calcularCosto(litros)
    ejercicio2_combustible.mostrarResultados(
        distancia, litros, rendimiento, costo
    )


def ejecutarMenu():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción (0-2): ")

        if opcion == "1":
            ejecutarEjercicio1()
        elif opcion == "2":
            ejecutarEjercicio2()
        elif opcion == "0":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutarMenu()