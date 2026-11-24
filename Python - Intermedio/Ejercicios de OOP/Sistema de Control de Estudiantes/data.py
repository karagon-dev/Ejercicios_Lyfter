import csv
import os
from models import Student

def import_csv():
    while True:
        students = []
        try:
            path = path_finder()
            with open(path, 'r', encoding='utf-8') as file:
                reader = list(csv.DictReader(file))
                if reader == []:
                    print(f"El CSV que importó está vacío. Intente con otro archivo o actualice el que utilizó.")
                else:
                    for row in reader:
                        student = Student(row.get('name'), int(row.get('age')), row.get('class_'), float(row.get('spanish_grade')), float(row.get('english_grade')), float(row.get('social_studies_grade')), float(row.get('science_grade')))
                        students.append(student)
                    return students
        except FileNotFoundError as error:
            print(f"No fue posible encontrar el archivo. Error: {error}")
        except TypeError as error:
            print(error)
        except ValueError as error:
            print(error)

def export_csv(students):
    if students == []:
        print("La lista está vacía. Agregue estudiantes primero.")
        return
    else: path = path_finder()
    try:
        with open(path, 'w', encoding='utf-8', newline='') as file:
            headers = vars(students[0])
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for index in range(0, len(students)):
                writer.writerow(vars(students[index]))
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

def path_finder():
    while True:
        try:
            path = input("Ingrese la ruta del CSV: ")
            path = os.path.join(path, 'students.csv')
            return path
        except FileNotFoundError as error:
            print(f"No se encontró un archivo. Error: {error}")