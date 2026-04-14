# ============================================================
#  FUNDAMENTOS DE PROGRAMACIÓN - TEMA N°2
#  Modularidad en la Programación: Funciones en Python
# ============================================================

# ── ETAPA 2: Funciones simples ───────────────────────────────

def saludar(nombre):
    """Recibe un nombre y saluda al usuario."""
    print(f"  Hola, {nombre}! Bienvenido al sistema.")


# ── ETAPA 3: Funciones con retorno de valores ────────────────

def sumar(a, b):
    """Recibe dos números y devuelve su suma."""
    return a + b


def multiplicar(a, b):
    """Recibe dos números y devuelve su producto."""
    return a * b


def es_par(numero):
    """Devuelve True si el número es par, False si es impar."""
    return numero % 2 == 0


# ── ETAPA 4: Funciones para el menú modular ──────────────────

def ingresar_datos():
    """Solicita nombre y edad al usuario y los devuelve."""
    print("\n  -- Ingreso de datos --")
    nombre = input("  Ingresa tu nombre : ")
    while True:
        try:
            edad = int(input("  Ingresa tu edad   : "))
            break
        except ValueError:
            print("  ✗ Por favor ingresa un número entero válido.")
    return nombre, edad


def es_mayor_de_edad(edad):
    """Devuelve True si la edad es mayor o igual a 18."""
    return edad >= 18


def mostrar_resultados(nombre, edad):
    """Muestra los datos del usuario y si es mayor de edad."""
    print("\n  -- Resultados --")
    print(f"  Nombre : {nombre}")
    print(f"  Edad   : {edad} años")
    if es_mayor_de_edad(edad):
        print("  Estado : Mayor de edad ✓")
    else:
        print("  Estado : Menor de edad ✗")


def menu_operaciones():
    """Submenú de operaciones matemáticas."""
    print("\n  -- Operaciones matemáticas --")
    while True:
        try:
            a = float(input("  Primer número  : "))
            b = float(input("  Segundo número : "))
            break
        except ValueError:
            print("  ✗ Ingresa números válidos.")

    resultado_suma = sumar(a, b)
    resultado_mult = multiplicar(a, b)
    print(f"\n  Suma        : {a} + {b} = {resultado_suma}")
    print(f"  Producto    : {a} × {b} = {resultado_mult}")

    while True:
        try:
            num = int(input("\n  Ingresa un entero para verificar par/impar: "))
            break
        except ValueError:
            print("  ✗ Ingresa un número entero.")

    if es_par(num):
        print(f"  El número {num} es PAR.")
    else:
        print(f"  El número {num} es IMPAR.")


# ── PROGRAMA PRINCIPAL ───────────────────────────────────────

def main():
    nombre_usuario = None
    edad_usuario   = None

    while True:
        print("\n" + "=" * 40)
        print("   MENÚ PRINCIPAL - LabFunciones")
        print("=" * 40)
        print("  1. Saludar al usuario")
        print("  2. Operaciones matemáticas")
        print("  3. Ingresar datos personales")
        print("  4. Mostrar resultados del usuario")
        print("  0. Salir")
        print("-" * 40)

        opcion = input("  Selecciona una opción: ").strip()

        if opcion == "1":
            # Etapa 2: función simple de saludo
            nombre = input("\n  ¿Cómo te llamas? ")
            saludar(nombre)

        elif opcion == "2":
            # Etapa 3: operaciones con retorno de valores
            menu_operaciones()

        elif opcion == "3":
            # Etapa 4: ingreso de datos
            nombre_usuario, edad_usuario = ingresar_datos()
            print(f"\n  Datos guardados correctamente para '{nombre_usuario}'.")

        elif opcion == "4":
            # Etapa 4: mostrar resultados
            if nombre_usuario is None:
                print("\n  ✗ Primero debes ingresar tus datos (opción 3).")
            else:
                mostrar_resultados(nombre_usuario, edad_usuario)

        elif opcion == "0":
            print("\n  ¡Hasta luego! Programa finalizado.\n")
            break

        else:
            print("\n  ✗ Opción no válida. Intenta de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()