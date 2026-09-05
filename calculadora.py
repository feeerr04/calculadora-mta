def sumar(a, b):
    """Retorna la suma de dos numeros."""
    return a + b


def restar(a, b):
    """Retorna la resta de dos numeros."""
    return a - b


def multiplicar(a, b):
    """Retorna la multiplicacion de dos numeros."""
    return a * b


def dividir(a, b):
    """Retorna la division de dos numeros. Lanza error si b es 0."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def mostrar_menu():
    print("\n--- Calculadora Basica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion (1-5): ")

        if opcion == "5":
            print("Hasta luego.")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opcion invalida, intenta de nuevo.")
            continue

        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))

        if opcion == "1":
            print(f"Resultado: {sumar(num1, num2)}")
        elif opcion == "2":
            print(f"Resultado: {restar(num1, num2)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicar(num1, num2)}")
        elif opcion == "4":
            try:
                print(f"Resultado: {dividir(num1, num2)}")
            except ValueError as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    main()
