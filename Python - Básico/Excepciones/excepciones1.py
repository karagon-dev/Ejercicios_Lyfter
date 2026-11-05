def main ():
    try:
        menu()
    except Exception as error:
        print(f"Ocurrió un error: {error}")

def menu(actual_number = 0):
    print("============= Calculadora =============")
    option_selected = 0 
    while option_selected != 6:
        try: 
            print(" 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Borrar resultado \n 6. Salir")
            option_selected = int(input("Ingrese la operación que desea realizar: "))
            if option_selected == 6:
                print("Saliendo del programa...")
            if option_selected > 6 or option_selected < 1:
                raise InvalidOptionError(option_selected)
            else:
                match option_selected:
                    case 1:
                        entered_number = float(input("Ingrese el número: "))
                        actual_number = sum_numbers(entered_number, actual_number)
                    case 2:
                        entered_number = float(input("Ingrese el número: "))
                        actual_number = extract_numbers(entered_number, actual_number)
                    case 3:
                        entered_number = float(input("Ingrese el número: "))
                        actual_number = multiply_numbers(entered_number, actual_number)
                    case 4:
                        entered_number = float(input("Ingrese el número: "))
                        actual_number = divide_numbers(entered_number, actual_number)
                    case 5:
                        actual_number = 0
                        print("El resultado ha sido borrado.")
                print (f"El resultado actual es: {actual_number}")
        except ValueError as error:
            print(f"No se pudo convertir el valor ingresado a número. Error: {error}")
        except TypeError as error:
            print(f"Intentaste calcular una cadena de texto con un número. Error: {error}")
        except ZeroDivisionError as error:
            print(f"No se puede dividir un número entre 0. Error: {error}")
        except InvalidOptionError as error:
            print(error)

def sum_numbers(number, actual_number):
    return actual_number + number
def extract_numbers(number, actual_number):
    return actual_number - number

def multiply_numbers(number, actual_number):
    return actual_number * number

def divide_numbers(number, actual_number):
    return actual_number /  number

class InvalidOptionError(Exception):
    def __init__(self, option_selected):
        super().__init__(f"La selección {option_selected} no es válida")

if __name__ == "__main__":
    main()
