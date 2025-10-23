import random

# Generar número secreto entre 1 y 50
numero_secreto = random.randint(1, 50)

# Inicializar contador de intentos
intentos = 0
max_intentos = 5

print("Bienvenido al juego: ¡Adivina el Número!")
print("Tenés que adivinar un número entre 1 y 50.")
print(f"Tenés {max_intentos} intentos. ¡Suerte!")

# Bucle principal del juego
while intentos < max_intentos:
    intento_texto = input(f"\nIntento {intentos + 1} - Ingresá un número entre 1 y 50: ")

    # Validar que sea un número
    if intento_texto.isdigit():
        intento = int(intento_texto)

        # Validar que esté dentro del rango permitido
        if 1 <= intento <= 50:
            intentos += 1

            if intento == numero_secreto:
                print("¡Felicitaciones! Adivinaste el número secreto.")
                break
            elif intento < numero_secreto:
                print("El número secreto es mayor.")
            else:
                print("El número secreto es menor.")
        else:
            print("El número debe estar entre 1 y 50. No se cuenta como intento.")
    else:
        print("Entrada inválida. Por favor, ingresá un número válido.")

# Si no lo adivinó en 5 intentos
if intentos == max_intentos and intento != numero_secreto:
    print("\nAgotaste tus 5 intentos.")
    print(f"El número secreto era: {numero_secreto}")
