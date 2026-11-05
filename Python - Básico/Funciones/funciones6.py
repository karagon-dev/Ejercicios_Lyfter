def sort_string(my_string):
    divided_words = []
    word = ""
    my_string += "-"
    for index in range(0, len(my_string), 1):
        if my_string[index] != "-":
            word += my_string[index]
        elif my_string[index]:
            divided_words.append(word)
            word = ""
    return list_to_string(sorted(divided_words))

def list_to_string(my_list):
    my_sorted_string = ""
    for index in range(0, len(my_list), 1):
        if index == 0:
            my_sorted_string += my_list[index]
        else: my_sorted_string += "-" + my_list[index]
    return my_sorted_string

my_string = "elefante-computadora-murcielago-zapato-biblioteca-guitarra-mariposa-ventana"
result = sort_string(my_string)
print(result)