numbers = []
i = 0

while i < 3:
    numbers.append(int(input("Ingrese un número: ")))
    i = i + 1

if numbers[0] >= numbers[1] and numbers[0] >= numbers[2]:
    print(f"El número mayor de los tres ingresados es: {numbers[0]}")
elif numbers[1] >= numbers[0] and numbers[1] >= numbers[2]:
    print(f"El número mayor de los tres ingresados es: {numbers[1]}")
else:
    numbers[2] >= numbers[0] and numbers[2] >= numbers[1]
    print(f"El número mayor de los tres ingresados es: {numbers[2]}")
