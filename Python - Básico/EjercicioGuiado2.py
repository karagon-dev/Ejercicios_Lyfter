print("===== Simulacro de ahorro =====")

name = input("Ingrese su nombre:")
monthly_savings = float(input("Cuántos dólares ahorras al mes?"))
months = int(input("Cuántos meses deseas acumular?"))
total = 0

for month in range(1, months + 1):
    total = total + monthly_savings
    print(f"Mes {month}: total acumulado = {total}")

print(f"{name}, en {months} meses habrás ahorrado = {total}")