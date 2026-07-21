print("====== PROMEDIO DE TRES NOTAS ======")

nombre = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3

print("\nNombre:", nombre)
print("Promedio:", round(promedio, 2))

if promedio >= 6:
    print("Estado: Aprobado")
else:
    print("Estado: Reprobado")