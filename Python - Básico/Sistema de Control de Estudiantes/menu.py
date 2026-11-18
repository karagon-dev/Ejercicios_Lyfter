import actions
import data

def menu():
    students = []
    while True:
        print("Sistema de Control de Estudiantes")
        print("1. Ingresar información de estudiantes.")
        print("2. Ver información de todos los estudiantes.")
        print("3. Ver los mejores 3 estudiantes.")
        print("4. Ver el promedio general de los estudiantes.")
        print("5. Exportar información de estudiantes en CSV.")
        print("6. Importar información de estudiantes desde CSV.")
        print("q. Salir.")
        choice = input("Ingrese el número de la opción que desea seleccionar (o 'q' para salir): ")
        try:
            if choice == '1':
                actions.enter_student_data(students)
            elif choice == '2':
                actions.get_students_data(students)
            elif choice == '3':
                print(actions.get_top(students))
            elif choice == '4':
                print(actions.get_students_average(students))
            elif choice == '5':
                data.export_csv(students)
            elif choice == '6':
                students = data.import_csv()
                print("Lista de estudiantes importada al programa.")
                print("Puede continuar editandola para exportarla después.")
            elif choice == 'q':
                print("Saliendo del programa.")
                break
            else:
                raise ValueError()
        except ValueError as error:
            print(f"Opción inválida. Por favor, ingrese un número del 1 al 6 o 'q' para salir. Error: {error}")