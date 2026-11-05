def main():
    try:
        path_existing_txt = r"Manejo de archivos\songs.txt"
        path_new_txt = r"Manejo de archivos\sorted_songs.txt"
        sorted_songs_list = sort_file(path_existing_txt)
        if len(sorted_songs_list) == 0:
            raise EmptyListError()
        write_file(path_new_txt, sorted_songs_list)
    except EmptyListError as error:
        print(error)

def sort_file(path):
    sorted_songs = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            sorted_songs = sorted(file.readlines())
    except PermissionError as error:
        print(f"No se tienen los permisos para accesar al archivo. Error: {error}")
    except FileNotFoundError as error:
        print(f"El archivo no existe. Error: {error}")
    return sorted_songs

def write_file(path, songs):
    try:
        with open(path, 'w', encoding='utf-8') as file:
            for index in range(0, len(songs), 1):
                if not songs[index].endswith("\n"):
                    songs[index] += "\n"
                    file.write(songs[index])
                else:
                    file.write(songs[index])
    except PermissionError as error:
        print(f"No se tienen los permisos para accesar al archivo. Error: {error}")

class EmptyListError(Exception):
    def __init__(self):
        super().__init__("La lista de canciones está vacía.")

if __name__ == "__main__":
    main()