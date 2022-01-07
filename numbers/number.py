#module imports
import random


def numbers(x):
    print("=======================")
    print("  Bienvenido al juego  ")
    print("=======================")

    print("Tu objetivo es obtener el numero.")

    #random number 1 to x
    random_number= random.randint(1, x)

    prediction = 0
    while prediction != random_number:
        prediction = int(input(f'Get a number 1 to {x}: '))

        if prediction < random_number:
            print('Try again please...')
        elif prediction > random_number:
            print('Try again please...')

    print(f'Lo lograste el numero es {random_number}')


numbers(5)