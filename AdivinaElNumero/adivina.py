from operator import truediv
import os
import random


print("Bienvenido a Adivina el número")

# Selecciona la dificultad
print("Selecciona la dificultad")
print("1. Fácil")
print("2. Medio")
print("3. Difícil")
while True:
  dificultad = int(input("Dificultad: "))
  if dificultad < 1 or dificultad > 4:
    print("Dificultad incorrecta, selecciona una dificultad entre 1 y 3")
  else:
    break

#Dificultad facil
if dificultad == 1:
  numero_secreto = random.randint(1, 10)
  limite =10
if dificultad == 2:
  numero_secreto = random.randint(1, 100)
  limite = 100
if dificultad == 3:
  numero_secreto = random.randint(1, 1000) 
  limite = 1000
while True:
   intentos = 5
   print(f"\nEstoy pensando en un número del 1 al {limite}")
   while True:
     numero_adivinar = int(input("Adivina un número: "))
     print("Te quedan: "+ str(intentos)+ " intentos")
     if numero_adivinar < 1 or numero_adivinar > limite:
       print(f"El número debe estar entre 1 y {limite}\n")
     if numero_adivinar < numero_secreto:
       print("El número es mayor\n")
     if numero_adivinar > numero_secreto:
       print("El número es menor\n")
     if numero_adivinar == numero_secreto:
      print("Has ganado\n")
      break
     if intentos == 0:
      print("Has perdido\n")
      print(f"El número era {numero_secreto}")
      break
     intentos -= 1
     


