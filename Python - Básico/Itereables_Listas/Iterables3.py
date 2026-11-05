my_list = [12, 23, 45, 67, 78, 3, 1, 4, 6, 76, 54]
first_digit = my_list[0]
last_digit = my_list[len(my_list) - 1]

my_list[0] = last_digit
my_list.pop(len(my_list) - 1)
my_list.append(first_digit)

print(my_list)