#%%
# Trek in die nodige pakette
from random import seed
from random import randint
from playsound import playsound


# pip install playsound==1.2.2 
# Die 1.2.2 weergawe moet gebruik word, 
# want latere weergawes werk nie

#%%
# Lukraak getal kies met 'n saadgetal
seed(1)

# Kies die maaltafel
maaltafel = 2
aantalvrae = 15
aantalreg = 0


for _ in range(aantalvrae):
    value = randint(0, 10)
    vraag = str(maaltafel) + ' x ' + str(value) + ' = '
    antwoord  = input(vraag)

    if int(antwoord) == value * maaltafel:
        print('Reg')       
        playsound('Reg.mp3')

        aantalreg += 1
    else:
        print('Verkeerd')
        playsound('Verkeerd.mp3')
        
# %%

print('Punt is ' + str(aantalreg) + ' uit ' + str(aantalvrae))