my_list = [1, 3, 5, 7, 2, 4, 6]
i = 0

while i < len(my_list):
    if my_list[i] % 2 != 0:
        my_list.pop(i)
    else:
        i += 1
print(my_list)

