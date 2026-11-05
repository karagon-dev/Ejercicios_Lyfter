def sum_list(my_list):
    if isinstance(my_list, list):
        total_sum = 0
        for index in range(0, len(my_list)):
            total_sum += my_list[index]
        return total_sum
    else: print("Se ingresó un tipo de dato no soportado.")

my_list1 = [100,20,30,50,5,-5,4]

print(sum_list(my_list1))