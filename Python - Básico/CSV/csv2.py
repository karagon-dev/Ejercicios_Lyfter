import csv

def main():
    collect_game_data()

def collect_game_data():
    games_list = []
    sentinel = 1
    while sentinel != 2:
        try:
            games_dict = {}
            games_dict['Nombre'] = input("Ingrese el nombre del juego que desea registrar: ")
            games_dict['Género'] = input("Ingrese el género del juego: ")
            games_dict['Desarrollador'] = input("Ingrese el desarrollador del juego: ")
            games_dict['ESRB'] = input("Ingrese la calificación: ")
            games_list.append(games_dict)
            sentinel = int(input("Juego guardado. \nDesea agregar otro juego? \n 1. Sí \n 2. No \n"))
            if sentinel > 2 or sentinel < 1:
                raise InvalidOptionError()
        except ValueError as error:
            print(f"No se pudo convertir el valor ingresado a número. Error: {error}")
        except InvalidOptionError as error:
            print(error)
    list_to_csv(games_list)

def list_to_csv(games):
    file_path = (input("Ingrese la ruta absoluta: ")+r"\games.csv")
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            headers = games[0].keys()
            writer = csv.DictWriter(file, fieldnames=headers, delimiter='\t')
            writer.writeheader()
            writer.writerows(games)
    except PermissionError as error:
        print(f"No se tiene acceso al directorio ingresado. Error: {error}")
    except FileNotFoundError as error:
        print(f"Directorio o archivo no encontrado. Error: {error}")

class InvalidOptionError(Exception):
    def __init__(self):
        super().__init__("La opción ingresada no es válida.")

if __name__  == "__main__":
    main()