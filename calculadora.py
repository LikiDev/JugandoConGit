def sumar(a, b):
    // devuelve la suma
    return 0

def restar(a, b):
    // devuelve la resta
    return 0

def multiplicar(a, b):
    // devuelve la multiplicacion
    return 0

while True:
    print("\nMini Calculadora")
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")

    opcion = input("Introduzca el número de la operación deseada: ")

    if opcion == '4':
        break

    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = sumar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == '2':
        resultado = restar(num1, num2)
        print("El resultado es:", resultado)
    elif opcion == '3':
        resultado = multiplicar(num1, num2)
        print("El resultado es:", resultado)
    else:
        print("Opción no reconocida. Por favor, elija una opción válida.")
