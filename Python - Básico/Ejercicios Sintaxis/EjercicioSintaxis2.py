name = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
age = int(input("Ingrese su edad: "))

if age <= 2:
    print(f"{name} {last_name}, usted es un bebé.")
elif age <= 11:
    print(f"{name} {last_name}, usted es un niño.")
elif age <= 13:
    print(f"{name} {last_name}, usted es un preadolescente.")
elif age <= 19:
    print(f"{name} {last_name}, usted es un adolescente.")
elif age <= 30:
    print(f"{name} {last_name}, usted es un adulto joven.")
elif age <= 55:
    print(f"{name} {last_name}, usted es un adulto.")
else:
    print(f"{name} {last_name}, usted es un adulto mayor.")