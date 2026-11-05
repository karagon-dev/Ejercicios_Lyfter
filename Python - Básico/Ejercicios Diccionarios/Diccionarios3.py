list_of_keys = ["access_level", "age", "email"]
employee = {
    "name": "Kenny",
    "last_name": "Aragón",
    "age": 25,
    "position": "Junior Software Engineer", 
    "access_level": 4
}
for keys in range(0, len(list_of_keys)):
    if employee.get(str(list_of_keys[keys])) != None:
        employee.pop(list_of_keys[keys])
print(employee)