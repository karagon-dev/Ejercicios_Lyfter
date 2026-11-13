def enter_student_data(students=None):
    if students == None:
        students = []
    try:
        while True:
            student = {}
            student["name"] = input("Ingrese el nombre del estudiante: ")
            student["age"] = int(input("Ingrese la edad del estudiante: "))
            student["class"] = input("Ingrese la sección del estudiante: ")
            print("*** Español")
            student["spanish_grade"] = get_grade()
            print("*** Inglés")
            student["english_grade"] = get_grade()
            print("*** Estudios sociales")
            student["social_studies_grade"] = get_grade()
            print("*** Ciencias")
            student["science_grade"] = get_grade()
            print(
                f"Datos del estudiante ingresado: "
                f"\nNombre: {student['name']}, "
                f"\nEdad: {student['age']}, \nSección: {student['class']}, "
                f"\nEspañol: {student['spanish_grade']}, "
                f"\nInglés: {student['english_grade']}, "
                f"\nCiencias Sociales: {student['social_studies_grade']}, "
                f"\nCiencias: {student['science_grade']}"
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
        print(student)

def get_students_average(students_list):
    students_average = []
    for student in students_list:
        student_dict = {}
        spanish = float(student.get('spanish_grade'))
        english = float(student.get('english_grade'))
        social_studies = float(student.get('social_studies_grade'))
        science = float(student.get('science_grade'))
        student_average = (spanish + english + social_studies + science) / 4
        student_dict['name'] = student.get('name')
        student_dict['class'] = student.get('class')
        student_dict['average'] = student_average
        students_average.append(student_dict)
    return students_average

def get_top(students_list):
    all_grades = []
    for student in students_list:
        grade_per_student = {}
        grades_average = (float(student.get('spanish_grade')) + float(student.get('english_grade')) + float(student.get('social_studies_grade')) + float(student.get('science_grade'))) / 4
        grade_per_student['name'] = student.get('name')
        grade_per_student['class'] = student.get('class')
        grade_per_student['grade_average'] = grades_average
        all_grades.append(grade_per_student)
    all_grades.sort(key=get_average, reverse=True)
    return all_grades[:3]

def get_average(student):
    return student['grade_average']

def get_grade():
    while True:
        try:
            grade = float(input("Ingrese la calificación del estudiante: "))
            if grade > 100 or grade < 0:
                print("Ingrese un número válido (entre 0 y 100).")
            else: return grade
        except ValueError as error:
            print(f"Ingresó un valor no numérico. Error: {error}")