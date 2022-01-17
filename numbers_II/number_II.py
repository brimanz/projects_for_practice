import random


def adivina_el_numero_compu(x):

    print("==================")
    print("Bienvenido al juego")
    print("==================")

    #utilizando f-string
    print(f"Seleccione un número entre 1 y {x} para comenzar")

    limite_inferior = 1
    limite_superior = x
    respuesta = ""

    while respuesta != "c":
        #generando prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior,limite_superior)
        else:
            prediccion: limite_inferior

        #generando respuesta del usuario
        respuesta = input(f"Mi prediccion es: {prediccion}. Si es muy alta, ingresa(A). Si es muy baja, ingresa(B). Si es correcto, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion -1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"Numero adivinado correctamente: {prediccion}")


adivina_el_numero_compu(5)