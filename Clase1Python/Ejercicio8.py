
nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad: "))

nota1 = float(input("Ingrese la primera calificación: "))
nota2 = float(input("Ingrese la segunda calificación: "))
nota3 = float(input("Ingrese la tercera calificación: "))

promedio = (nota1 + nota2 + nota3) / 3

print("\n--- RESULTADOS ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Promedio:", promedio)

if promedio >= 71:
    print("Aprobado")
else:
    print("No aprobado")
