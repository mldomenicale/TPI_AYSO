# Actividad. Ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrar el promedio de cada alumno.

print("¡Hola!\n")

#Validación de que un valor sea un número

lista_completa_notas={}
promedios={}

def probar_numero(n):
    try: 
        n=float(n)
        return True
    except ValueError:
        return False

#Cacular promedio de cada estudiante
def calcular_promedio(lista):
    suma=0
    for nota in lista:
        suma+=nota
    return suma / len(lista)

# Solicitar los tres nombre y notas
for i in range(3):
    #Solicitar el nombre del alumno al usuario y validar que no esté vacio
    nombre=input("¿Cuál es el nombre del estudiante que querés agregar?: ").strip().title()
    while nombre=="":
        print("\nEl nombre no puede estar vacío, vuelve a intentarlo...")
        nombre=input("¿Cuál es el nombre del estudiante que querés agregar?: ").strip().title()
    
    #Solicitar las notas de cada alumno y armar la tupla
    lista_notas=[]
    for j in range(1,4):
        nota=-1
        while nota<1 or nota>10:
            nota_texto=input(f"Nota {j} de {nombre}: ").strip()
            while not probar_numero(nota_texto):
                print("\nDebes ingresar un valor numérico, intenta nuevamente...")
                nota_texto=input(f"Nota {j} de {nombre}: ").strip()
            nota=float(nota_texto)
            if nota<1 or nota>10:
                print("La nota debe ser un valor entre 1 y 10, intenta nuevamente...")
        lista_notas.append(nota)
    tupla_notas=tuple(lista_notas)

    #Armar un diccionario para guardar todas las notas correspondientes a cada estudiante
    lista_completa_notas[nombre]=tupla_notas
    print(f"\nLas notas de {nombre} son {tupla_notas}\n")
      
    #Calcular promedios y registrarlos en un diccionario:
    promedio=calcular_promedio(lista_notas)
    print(f"El promedio de las notas de {nombre} es {promedio:.2f}\n")

    promedios[nombre]=round(promedio,2)

#Mostrar los resultados
print(f"\nLas notas registradas son:")
for alumno, nota in lista_completa_notas.items():
    print(f"{alumno}: {nota} ")   
print(f"\nLos promedios registrados son:")  
for alumno, media in promedios.items():
    print(f"{alumno}: {media} ")

print("\n¡Muchas gracias y hasta luego!\n")