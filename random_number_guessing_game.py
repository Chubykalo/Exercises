import random

secretNumber = random.randint(1,20)
#print('DEBUG: Secret number is ' + str(secretNumber))

#variables para 6 intentos range(1,7)
min = 1
max = 7
guess = 0

print('Hola, ¿cómo te llamas?')
name = input()

print('Bien, ' + name + ', estoy pensando en un número entre 1 y 20.')

for guessesTaken in range(min, max):
    print('Prueba a adivinar cual!')
    guess = int(input())

    if guess < secretNumber:
        print('Demasiado bajo!')
    elif guess > secretNumber:
        print('Demasiado alto!')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    if guessesTaken > 1:
        print('Buen trabajo, ' + name + '! Has adivinado mi número en ' + str(guessesTaken) + ' intentos!')
    else:
        print('Buen trabajo, ' + name + '! Has adivinado mi número a la primera!')
else:
    print('Nooo. El número en el que estaba pensando era ' + str(secretNumber) + '!')




