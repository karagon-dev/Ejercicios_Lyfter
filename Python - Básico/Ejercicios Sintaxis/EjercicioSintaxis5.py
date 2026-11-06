scores = []
passed_scores = []
failed_scores = []
answer = ""

while answer != "no":
    answer = input('Ingrese una nota. Si ya no desea ingresar más escriba "no": ')
    if answer != "no" and answer.isdigit() == False:
        print("Valor desconocido.")
    elif answer != "no" and int(answer) > 0 and int(answer) <= 100:
        scores.append(int(answer))
        print(scores)
    elif answer != "no":
        print("Ingrese una nota entre los rangos posibles (1 al 100) o 'no' si decía terminar")

i = 0
total_average = 0
for score in scores:
    if score < 70:
        failed_scores.append(scores[i])
    else:
        passed_scores.append(scores[i])
    i = i + 1

print(f"Notas aprobadas: {len(passed_scores)}")
print(f"Notas reprobadas: {len(failed_scores)}")

if len(scores) != 0:
    total_average = (sum(scores) / len(scores)) 
    print(f"Promedio total: {total_average}")
else:
    print("No hubieron notas registradas")

if len(passed_scores) != 0:
    print(f"El promedio de las notas aprobadas es: {sum(passed_scores)/len(passed_scores)}")
else:
    print("El promedio es 0 porque no hubieron aprobados.")

if len(failed_scores) != 0:
    print(f"El promedio de las notas reprobadas es: {sum(failed_scores)/len(failed_scores)}")
else:
    print("El promedio es 0 porque no hubieron reprobados.")
