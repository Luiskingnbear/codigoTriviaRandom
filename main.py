import time
import math

import random

print("*** Bienvenidos 'Random Batle' ***\n")

jugadores = []

jugador1 = input("Ingresa el nombre del jugador 1: ")
jugador2 = input("Ingresa el nombre del jugador 2: ")

jugadores.append(jugador1)
jugadores.append(jugador2)

jugador_1_puntos = 20
jugador_2_puntos = 20

jugador_1_turnos = []
jugador_2_turnos = []

jugador_1_acumulado = []
jugador_2_acumulado = []

turnos = 0
jugar = True

while jugar == True:
  print(
      "\n Hola responde la siguientes preguntas escribiendo la letra de la alternativa y presionanado enter para enviar tu respuesta: \n"
  )

  print("Bienvenido a mi trivia sobre Futbol")
  print("pondremos a prueba tus conocimientos")

  print("Que seleccion es campeona del mundo")
  print("a)Argentina")
  print("b)Chile")
  print("c)Bolivia")
  print("c)Paraguay")

  print("Nacionalidad de Cristiano ronaldo")
  print("a)Portugal")
  print("b)Chile")
  print("c)Peru")
  print("d)Bolivia")

  print("Cuanto mide Messi")
  print("a)1.71")
  print("b)1.52")
  print("c)1.98")
  print("d)1.64")

  print("¿Qué jugador disputó más partidos en la historia de LaLiga?")
  print("a)Andoni Zubizarreta (622 entre 1981 y 1998)")
  print("b)Figo")
  print("c)Ronaldo")
  print("d)Pique")

  print(
      "¿Quién es el jugador que más veces vio la tarjeta roja en la historia de LaLiga?"
  )
  print("a)Sergio Ramos (19)")
  print("b)Pique")
  print("c)pepe")
  print("d)Carvajal")

  print(
      "¿Quién es el segundo máximo goleador de la historia de LaLiga, por detrás de Messi (438)?"
  )
  print("a)Cristiano Ronaldo (311)")
  print("b)Pedro")
  print("c)Villa")
  print("d)Carvajal")

  print(
      "¿Cuándo se jugó la primera edición de la Primera División del fútbol español?"
  )
  print("a)1928-29")
  print("b)1924-25")
  print("c)1923-24")
  print("d)1920-21")

  print("¿Quién fue el primer campeón en la Primera División?")
  print("a)FC Barcelona ")
  print("b)Real Madrid")
  print("c)Mallorca")
  print("d)Atletico de Madrid")

  print(
      "¿Qué equipo ha sumado más puntos a lo largo de las 89 temporadas de LaLiga?"
  )
  print("a)Real Madrid (4529)")
  print("b)Atletico de Madrid")
  print("c)FC Barcelona")
  print("d)Mallorca")

  print("¿A partir de qué temporada se implantó el VAR?")
  print("a)2018/19")
  print("b)2016/17")
  print("c)2015/16")
  print("d)2014/15")
  
  correcto = "la respuesta es correcta"
  incorrecto = "la respuesta es incorrecta"
  secreto = "este es un mensaje secreto,tienes un bono"
  mensaje = ""
  puntos = 0
  
  acabar = ""
  #---------------PREGUNTAS
  i = True
  intentos = 0
  jugador_1_acumulado1 = 0
  j1 = 0
  j2 = 0
  intentosA = 0
  intentosB = 0
  while i == True:
      # puntos=0
  
      nombreJugador = jugadores[int(random.randint(0, 1))]
      print("EMPIEZA EL JUGADOR : ", nombreJugador)
      if (nombreJugador == jugadores[0]):
          intentosA += 1
          jugador_1_turnos.append(intentosA)
          print("\nINTENTO: ", jugador_1_turnos[intentosA - 1])
      elif (nombreJugador == jugadores[1]):
          intentosB += 1
          jugador_2_turnos.append(intentosB)
          print("\nINTENTO: ", jugador_2_turnos[intentosB - 1])
  
      campeon = input("\nTu respuesta a la primera pregunta: ")
      while campeon not in ("a", "b", "c", "d", "x"):
          campeon = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
              jugador_1_acumulado.append(jugador_1_puntos)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)

      elif nombreJugador == jugadores[1]:
          if campeon == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon1 = input("\nTu respuesta a la segunda pregunta: ")
      while campeon1 not in ("a", "b", "c", "d", "x"):
          campeon1 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon1 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon1 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon1 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon2 = input("\nTu respuesta a la tercera pregunta: ")
      while campeon2 not in ("a", "b", "c", "d", "x"):
          campeon2 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon2 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon2 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon2 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon2 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon3 = input("\nTu respuesta a la cuarta pregunta: ")
      while campeon3 not in ("a", "b", "c", "d", "x"):
          campeon3 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon3 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon3 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon3 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon3 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon4 = input("\nTu respuesta a la quinta pregunta: ")
      while campeon4 not in ("a", "b", "c", "d", "x"):
          campeon4 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon4 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon4 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon4 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon4 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon5 = input("\nTu respuesta a la sexta pregunta: ")
      while campeon5 not in ("a", "b", "c", "d", "x"):
          campeon5 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon5 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon5 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon5 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon5 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon6 = input("\nTu respuesta a la septima  pregunta: ")
      while campeon6 not in ("a", "b", "c", "d", "x"):
          campeon6 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon6 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon6 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon6 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon6 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon7 = input("\nTu respuesta a la ocatava pregunta: ")
      while campeon7 not in ("a", "b", "c", "d", "x"):
          campeon7 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon7 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon7 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon7 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon7 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon8 = input("\nTu respuesta a la novena pregunta: ")
      while campeon8 not in ("a", "b", "c", "d", "x"):
          campeon8 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon8 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon8 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon8 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon8 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon9 = input("\nTu respuesta a la decima pregunta: ")
      while campeon9 not in ("a", "b", "c", "d", "x"):
          campeon9 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon9 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon9 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon9 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon9 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      campeon10 = input("\nTu respuesta a la onceava pregunta: ")
      while campeon10 not in ("a", "b", "c", "d", "x"):
          campeon10 = input("Debes responder a,b,c,d.\n Responde: ")
      if nombreJugador == jugadores[0]:
          if campeon10 == "a":
              mensaje = correcto
              jugador_1_puntos -= int(random.randint(0, 5))
              jugador_1_acumulado.append(jugador_1_puntos)
          elif campeon10 == "x":
              mensaje = secreto
              jugador_1_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_1_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_1_puntos)
  
      elif nombreJugador == jugadores[1]:
          if campeon10 == "a":
              mensaje = correcto
              jugador_2_puntos -= int(random.randint(0, 5))
              jugador_2_acumulado.append(jugador_2_puntos)
          elif campeon10 == "x":
              mensaje = secreto
              jugador_2_puntos -= random.randint(0, 10)
          else:
              mensaje = incorrecto
              jugador_2_puntos += int(random.randint(0, 5))
          print(mensaje, "y tu puntaje es : ", jugador_2_puntos)
  
      time.sleep(0.0005)
      
        
      if nombreJugador == jugadores[0]:
          if jugador_1_puntos <= 0:
            print("\nHey: ", nombreJugador, "GANASTE")
            print("ESTE ES TU PUNTAJE Y TUS INTENTOS",
                  jugador_1_turnos[intentosA - 1])
            print("HISTORIAL DE PUNTAJE")
            for x in range (0,11):
              print("TU PUNTAJE",jugador_1_acumulado[x])
              
            #print(jugador_1_acumulado[intentosB-1])
            print("EL PROGRAMA SE ACABÓ")
            i = False
            jugar = False
          else:
            acabar = input("\nSi quieres acabar el programa escribe: salir ,si no presiona enter \n")
    
      

      if acabar == "salir":
            print("EL PROGRAMA SE ACABÓ")
            i = False
            jugar = False
        
      if nombreJugador == jugadores[1]:
          if jugador_2_puntos <= 0:
              print("\nHey: ", nombreJugador, "GANASTE")
              print("TUS INTENTOS", jugador_2_turnos[intentosB - 1])
              print("HISTORIAL DE PUNTAJE")
              for x in range (0,11):
                print(jugador_2_acumulado[x])
              print("EL PROGRAMA SE ACABÓ")
              i = False
              jugar = False

          else:
            acabar = input("\nSi quieres acabar el programa escribe: salir ,si no presiona enter \n")
        
          if acabar == "salir":
                print("EL PROGRAMA SE ACABÓ")
                i = False
                jugar = False

      





        
