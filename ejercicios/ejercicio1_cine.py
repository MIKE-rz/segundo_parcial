"""
PROBLEMA:
Calcular el importe total de una compra de boletos de cine,
aplicando un descuento cuando se compran cuatro boletos o más.
"""

#ENTRADAS:
#cantidad: número entero mayor que cero, correspondiente
#a la cantidad de boletos que desea comprar el usuario.

#SALIDAS:
#- Cantidad de boletos adquiridos.
#- Precio unitario del boleto.
#- Subtotal de la compra.
#- Descuento aplicado.
#- Total a pagar.
#Los importes se muestran en pesos mexicanos con dos decimales.

#REGLAS Y SUPUESTOS:
#- Cada boleto cuesta $75.00.
#- Si se compran 4 boletos o más, se aplica un descuento del 10%
#  sobre el subtotal.
#- Si se compran menos de 4 boletos, no se aplica descuento.
#- La cantidad de boletos debe ser un entero mayor que cero.
#- El total se calcula restando el descuento al subtotal.
#- Los importes se muestran con dos decimales.
#- Se utiliza tabulate para presentar los resultados en una tabla.

#ALGORITMO:
#1. Solicitar la cantidad de boletos.
#2. Calcular el subtotal multiplicando la cantidad por $75.00.
#3. Si la cantidad es mayor o igual a 4, calcular el descuento
#   multiplicando el subtotal por 0.10.
#4. Si la cantidad es menor que 4, establecer el descuento en cero.
#5. Calcular el total restando el descuento al subtotal.
#6. Mostrar la cantidad, precio unitario, subtotal, descuento
#   y total a pagar mediante una tabla.

#CASOS DE PRUEBA:
#Caso 1:
#Entrada: 1 boleto.
#Subtotal: 1 * 75 = $75.00.
#Descuento: $0.00.
#Total: $75.00.

#Caso 2:
#Entrada: 3 boletos.
#Subtotal: 3 * 75 = $225.00.
#Descuento: $0.00.
#Total: $225.00.

#Caso 3:
#Entrada: 4 boletos.
#Subtotal: 4 * 75 = $300.00.
#Descuento: 300 * 0.10 = $30.00.
#Total: $270.00.

#Caso 4:
#Entrada: 6 boletos.
#Subtotal: 6 * 75 = $450.00.
#Descuento: 450 * 0.10 = $45.00.
#Total: $405.00.

#RESTRICCIONES PARA EL AGENTE:
#- La única biblioteca externa permitida es tabulate.
#- No agregar bibliotecas externas adicionales.
#- Respetar las funciones indicadas en el contrato.
#- No modificar el precio unitario ni las reglas del descuento.
#- Mostrar los resultados mediante tabulate.

#CONTRATO DE FUNCIONES:
#leerCantidad():
#Lee y retorna la cantidad de boletos como un entero mayor que cero.

#calcularSubtotal(cantidad):
#Recibe la cantidad de boletos y retorna el subtotal de la compra.

#calcularDescuento(cantidad, subtotal):
#Recibe la cantidad de boletos y el subtotal.
#Retorna el 10% del subtotal si la cantidad es mayor o igual a 4;
#en caso contrario, retorna cero.

#mostrarCompra(cantidad, subtotal, descuento):
#Recibe la cantidad, el subtotal y el descuento.
#Calcula el total a pagar y muestra todos los resultados mediante tabulate.
from tabulate import tabulate

def leerCantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de boletos a comprar (entero mayor que cero): "))
            if cantidad > 0:
                return cantidad
            else:
                print("Error: La cantidad debe ser un entero mayor que cero.")
        except ValueError:
            print("Error: Entrada inválida. Por favor, ingrese un número entero.")

def calcularSubtotal(cantidad):
    precio_unitario = 75.00
    subtotal = cantidad * precio_unitario
    return subtotal            

def calcularDescuento(cantidad, subtotal):
    if cantidad >= 4:
        return subtotal * 0.10
    else:
        return 0

def mostrarCompra(cantidad, subtotal, descuento):
    total = subtotal - descuento
    tabla = [
        ["Cantidad de boletos", cantidad],
        ["Precio unitario", "$75.00"],
        ["Subtotal", f"${subtotal:.2f}"],
        ["Descuento", f"${descuento:.2f}"],
        ["Total a pagar", f"${total:.2f}"]
    ]
    print(tabulate(tabla, headers="firstrow", tablefmt="grid"))

