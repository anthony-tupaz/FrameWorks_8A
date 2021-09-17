# descripcion: Script Python que permite identificar el mayor de dos numeros ingresados por consola


import os

os.system("clear")


print("ingrese primer numero: ")
n1 = int(input())


n2 = int(input("ingrese segundo numero: "))

if n1 > n2 :
    print("El mayor es: ", n1)
elif n1 < n2:
    print("el mayor es: ", n2)
else:
    print("Los numeros son iguales")