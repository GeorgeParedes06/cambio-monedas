def calcular_monedas(denominaciones, monto):

    denominaciones.sort(reverse=True)

    cantidades = []
    monto_restante = monto
    
    for moneda in denominaciones:
        cantidad = monto_restante // moneda
        cantidades.append(cantidad)
        monto_restante = monto_restante % moneda
        
    return cantidades

def main():
 
    denominaciones = [100, 50, 20, 10, 5, 2, 1]
    
    try:
        monto_usuario = int(input("Ingrese el monto a pagar: "))
        if monto_usuario < 0:
            print("El monto no puede ser negativo.")
            return

        resultado_lista = calcular_monedas(denominaciones, monto_usuario)
        
        print("\nDenominaciones disponibles:", denominaciones)
        print("Lista de cantidades a usar:", resultado_lista)
        
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

main()
