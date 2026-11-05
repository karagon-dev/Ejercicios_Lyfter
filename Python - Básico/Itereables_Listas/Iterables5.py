my_list = []
i = 0
print("A continuación, ingrese 10 números.")
while len(my_list) < 10:
    my_list.append(int(input(f"Número #{i + 1}:")))
    i += 1
    highest_number = my_list[0] 
for index in range(0, len(my_list)):
    if my_list[index] > highest_number:
        highest_number = int(my_list[index])
print(f"Lista de números ingresados: {my_list}")
print(f"El número más alto es: {highest_number}")