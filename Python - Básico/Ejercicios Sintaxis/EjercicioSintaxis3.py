import random

print("--- Bienvenido al juego del número secreto ---")
print("--- Instrucciones: El sistema va a seleccionar un número aleatorio del 1 al 10. ---")
print(" ")
guess_number = 0
secret_number = random.randint(1, 10)
while guess_number != secret_number:
    guess_number = int(input("Ingrese su número: "))
    while guess_number > 10 or guess_number <= 0:
        print(f"El número {guess_number} está fuera de rango.")
        guess_number = int(input("Ingrese uno del 1 al 10: "))
    if guess_number != secret_number:
        print("Número fallido, intente con otro.")

print(f"Felicidades! El número {guess_number} era el correcto.")
