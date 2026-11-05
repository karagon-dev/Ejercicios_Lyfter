print("------ Clasificador de Nivel Gamer ------")
name = input("Ingrese su nombre: ")
hours = int(input("Ingrese la cantidad de horas que juega a la semana: "))
is_competitive = input("Juegas competitivo? (si/no)")

if hours < 10:
    category = "Novato"
    message = "Bienvenido al mundo gamer!"
elif hours < 50:
    category = "Casual"
    message = "Ya le estás agarrando el ritmo!"
elif hours < 200:
    category = "Gamer"
    print("Definitivamente sabes lo que haces.")
elif hours >= 200 and is_competitive == "si":
    category = "Pro"
    message = "Eres una leyenda viviente."
else:
    category = "Gamer"
    message = "Tienes la experiencia, pero aún no entras al competitivo"

print(f"{name}, tu categoría es: {category}")
print(message)
