import csv

def import_csv():
    while True:
        try:
            path = path_finder()
            with open(path, 'r', encoding='utf-8') as file:
                reader = list(csv.DictReader(file))
                if reader == []:
                    print(f"El CSV que importón está vacío. Intente con otro archivo o actualice el que utilizó.")
                else:
                    return reader
        except FileNotFoundError as error:
            print(f"No fue posible encontrar el archivo. Error: {error}")

def export_csv(students):
    path = path_finder()
    try:
        if students == []:
            print("La lista está vacía. Agregue estudiantes primero.")
            return
        with open(path, 'w', encoding='utf-8', newline='') as file:
            headers = students[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(students)
        selection = input("Desea vaciar la lista de estudiantes del programa? 1. Sí 2. No")
        if selection == '1':
            students.clear()
            print("Lista vacía.")
        elif selection != '1' and selection != '2':
            print("Selección inválida.")
    except PermissionError as error:
        print(f"No se tiene acceso al directorio ingresado. Error: {error}")
    except FileNotFoundError as error:
        print(f"Directorio o archivo no encontrado. Error: {error}")
    except IndexError as error:
        print(f"La lista que intenta exportar está vacía. Intente agregar estudiantes primero. Error: {error}")

def path_finder():
    while True:
        try:
            path = (input("Ingrese la ruta absoluta de donde desea crear el CSV: ")+r"\students.csv")
            if path == r"\students.csv":
                raise InvalidEntry
            else:
                return path
        except InvalidEntry as error:
            print(error)

class InvalidEntry(Exception):
    def __init__(self):
        super().__init__("No puede ingresar una ruta vacía.")