# Trek in die nodige pakette
from random import seed
from random import randint

# Lukraak getal kies met 'n saadgetal
seed(1)

# Kies die maaltafel
maaltafel = 9

for _ in range(10):
    value = randint(0, 10)
    vraag = str(maaltafel) + ' x ' + str(value) + ' = '
    antwoord  = input(vraag)

    if int(antwoord) == value * maaltafel:
        print('Reg')
    else:
        print('Verkeerd')