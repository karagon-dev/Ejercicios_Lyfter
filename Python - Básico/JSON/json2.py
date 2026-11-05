import json

def main():
    pokemon_dict, path = import_json()
    add_pokemon_to_json(pokemon_dict, path)

def import_json():
    sentinel = 1
    while sentinel != 2:
        try:
            path = input("Ingrese la ruta del archivo JSON: ")
            with open(path, 'r', encoding='utf-8') as file:
                pokemon_dict = json.load(file)
                sentinel = 2
        except PermissionError as error:
            print(f"No se cuentan con permisos para accesar al archivo. Error: {error}")
            sentinel = 1
        except FileNotFoundError as error:
            print(f"Archivo no encontrado. Error: {error}")
            sentinel = 1
        except json.JSONDecodeError as error:
            print(f"Error al decodificar el archivo JSON. Error: {error}")
            sentinel = 1
    return pokemon_dict, path

def add_pokemon_to_json(pokemon_dict, path):
    try:
        sentinel = 1
        while sentinel != 2:
            name = input("Ingrese el nombre del pokemon: ")
            pokemon_type = input("Ingrese el tipo del pokemon: ")
            level = int(input("Ingrese el nivel del pokemon: "))
            weight_kg = float(input("Ingrese el peso del pokemon: "))
            is_shiny = int(input("El pokemon es shiny? 0. No 1. Sí : "))
            if is_shiny not in [0, 1]:
                raise ValueError("El valor ingresado para 'is_shiny' no es válido. Debe ser 0 o 1.")
            else:
                is_shiny = bool(is_shiny)
            held_item = input("Tiene algún objeto equipado? Deje vacío si no. ")
            if held_item == "":
                held_item = None
            stats = {}
            stats['hp'] = int(input("Ingrese la cantidad de HP del pokemon: "))
            stats['attack'] = int(input("Ingrese la cantidad de Attack del pokemon: "))
            stats['defense'] = int(input("Ingrese la cantidad de Defense del pokemon: "))
            stats['sp_attack'] = int(input("Ingrese la cantidad de Special Attack del pokemon: "))
            stats['sp_defense'] = int(input("Ingrese la cantidad de Special Defense del pokemon: "))
            stats['speed'] = int(input("Ingrese la cantidad de Speed del pokemon: "))
            skills = []
            while sentinel != 2:
                skill = input("Ingrese una habilidad del pokemon. Deje vacío si no desea agregar más habilidades. ")
                if skill == "":
                    sentinel = 2
                else:
                    skills.append(skill)
            sentinel = 1
            continue_adding = input("Desea agregar otro pokemon? 1. Sí 2. No :")
            if continue_adding == "1":
                sentinel = 1
            else:
                sentinel = 2
            new_pokemon = {
                "name": name,
                "type": pokemon_type,
                "level": level,
                "weight_kg": weight_kg,
                "is_shiny": is_shiny,
                "held_item": held_item,
                "stats": stats,
                "skills": skills
            }
            pokemon_dict.append(new_pokemon)
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(pokemon_dict, file)
    except TypeError as error:
        print(f"Error de tipo. Error: {error}")
    except ValueError as error:
        print(f"Error de valor. Error: {error}")

if __name__ == "__main__":
    main()  