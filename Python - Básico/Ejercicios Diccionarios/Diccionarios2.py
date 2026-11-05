list_a = ["first_name", "last_name", "role"]
list_b = ["Kenny", "Aragón", "Junior Software Engineer"]
lists = {}
for index in range(0, len(list_a)):
    lists[list_a[index]] = list_b[index]
print(lists)