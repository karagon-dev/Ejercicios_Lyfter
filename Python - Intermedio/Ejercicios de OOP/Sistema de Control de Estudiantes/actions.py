from models import Student

def enter_student_data(students=None):
    if students == None:
        students = []
    while True:
        try:
            name = input("Ingrese el nombre del estudiante: ")
            age = int(input("Ingrese la edad del estudiante: "))
            class_ = input("Ingrese la sección del estudiante: ")
            print("*** Español")
            spanish_grade = get_grade()
            print("*** Inglés")
            english_grade = get_grade()
            print("*** Estudios sociales")
            social_studies_grade = get_grade()
            print("*** Ciencias")
            science_grade = get_grade()
            student = Student(name, age, class_, spanish_grade, english_grade, social_studies_grade, science_grade)
            print(
                f"Datos del estudiante ingresado: "
                f"\nNombre: {student.name}, "
                f"\nEdad: {student.age}, \nSección: {student.class_}, "
                f"\nEspañol: {student.spanish_grade}, "
                f"\nInglés: {student.english_grade}, "
                f"\nCiencias Sociales: {student.social_studies_grade}, "
                f"\nCiencias: {student.science_grade}"
            )
            students.append(student)
            sentinel = input("Desea ingresar otro estudiante? \n 1. Sí \n 2. No")
            if sentinel != '1' and sentinel != '2':
                raise ValueError()
            elif sentinel == '2':
                break
            return
        except ValueError as error:
            print(f"El valor que ingresó no es válido. Error {error}")

def get_students_data(students):
    for student in students:
        print(f"\nNombre: {student.name}, "
            f"\nEdad: {student.age}, \nSección: {student.class_}, "
            f"\nEspañol: {student.spanish_grade}, "
            f"\nInglés: {student.english_grade}, "
            f"\nCiencias Sociales: {student.social_studies_grade}, "
            f"\nCiencias: {student.science_grade}")

def get_students_average(students):
    try: 
        students_average = 0.00
        for student in students:
            students_average += student.get_average()
        students_average = students_average / len(students)
        return students_average
    except  ZeroDivisionError as error:
        print(f"Error al dividir por cero. No hay estudiantes registrados. Error: {error}")

def get_top(students):
    students.sort(key=lambda student: student.get_average(), reverse=True)
    return students[:3]

def get_grade():
    while True:
        try:
            grade = float(input("Ingrese la calificación del estudiante: "))
            if grade > 100 or grade < 0:
                print("Ingrese un número válido (entre 0 y 100).")
            else: return grade
        except ValueError as error:
            print(f"Ingresó un valor no numérico. Error: {error}")