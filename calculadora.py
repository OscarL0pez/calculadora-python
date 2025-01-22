def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División entre cero no permitida"

def calculadora():
    print("Bienvenido a la Calculadora en Python")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == "5":
            print("¡Gracias por usar la calculadora!")
            break

        if opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == "1":
                    print(f"Resultado: {sumar(num1, num2)}")
                elif opcion == "2":
                    print(f"Resultado: {restar(num1, num2)}")
                elif opcion == "3":
                    print(f"Resultado: {multiplicar(num1, num2)}")
                elif opcion == "4":
                    print(f"Resultado: {dividir(num1, num2)}")
            except ValueError:
                print("Error: Por favor, ingresa un número válido.")
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    calculadora()
