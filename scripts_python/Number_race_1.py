import os
from random import randint


def dices() :
    status = True

    while status :    
        os.system("clear")
        dice1 = randint(1,6)
        dice2 = randint(1,6)
        print("D1: ", dice1)
        print("D2: ", dice2)

        suma = 0

        resultado = dice1+dice2
        print("la suma es: ", resultado)
        suma += resultado
 

        if dice1 == dice2 :
            status = False
            print("Los dados son pares. El lanzamiento ha finalizado..")
        else :
            key = input(".:: Presiona cualquier tecla para lanzar los dados nuevamente ...")    

    
        
    print("suma total: ", suma)

#Main
dices()