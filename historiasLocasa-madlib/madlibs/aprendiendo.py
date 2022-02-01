# En este primer proyecto aprenderemos la concatenacion de caracteres en python usando diferentes metodos
# Para esto haremos un proyecto sencillo llamado "historias locas" (del ingles "madlib") en el cual
# pediremos al usuario que escriba verbos, adjetivos, etc. segun corresponda para armar una historia graciosa.

# Existen diferentes maneras de concatenar en python, estas son 3 de las mas comunes

# Declaramos una variable
# canalYouTube = "Drago Do"  #Alguna cadena de texto

#print("Subscribete al canal " + canalYouTube)
#print("Subscribete al canal {}".format(canalYouTube))
#print(f"Subscribete al canal {canalYouTube}")


def madlib():
# Ahora vamos a hacer el juego
# Primero le daremos las instrucciones al jugador
  print("Escribe las palabras que se te ocurran segun lo que corresponda \
      ")

  sujeto1 = input("Una persona: ")
  sujeto2 = input("Una persona: ")
  adjetivo1 = input("Un adjetivo calificativo:")
  verbo1 = input("Un verbo: ")
  verbo2 = input("Un verbo: ")
  adjetivo2 = input("Un adjetivo calificativo: ")
  madlib = f"Hola, yo soy {sujeto1}. Hoy estoy aprendiendo a programar con {sujeto2},  es muy {adjetivo1}. Mañana tendre que {verbo1} la casa, mi perro intenta {verbo2} su cola, y mi gato esta comiendo algo muy {adjetivo2}"
  print(madlib)


