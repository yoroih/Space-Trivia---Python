#PRUEBA GIT
#ALUMNO: ROY CRISTHOPHER QUISPE PEÑA
#USO DE LIBRERIAS

import random
import time

#COLORES

#PRUEBA GIT

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[035m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

#CICLOS 

ini_triv = True
intentos = 0

#BIENVENIDA Y TIMERS
print(UNDERLINE+BOLD+GREEN,"BIENVENIDO A MI TRIVIA 'ODISEA EN EL ESPACIO'\n",RESET+END)
time.sleep(2)
print(YELLOW+"Mi nombre es Roy y te acompañaré en este viaje, estas muy cerca al sol, tu nave se ha descompuesto y necesitas abordar una capsula de emergencia.")
print("Para abordar identificate con tu nombre y presiona 'Enter':\n"+RESET)

#INPUTS
name = input(BOLD+BLUE+"Nombre: "+RESET+END)

#NUMEROS ALEATORIOS
comb_act = 0
comb = random.randint(20000,50000)
comb_2 = random.randint(2000,6000)
comb_3 = random.randint(6000,8000)

#INICIO - REPETICIÓN CON CICLOS WHILE
while ini_triv == True:
	intentos += 1
	
#CONTADOR DE REPETICIÓN

	print(BLUE+"Número de viajes: "+str(intentos)+RESET)

#INSTRUCCIONES
	
	print("")
	print(YELLOW+"Hola oficial",name,"que gusto que se encuentre bien! \n")
	time.sleep(2)
	print("Antes de iniciar el viaje, le informo que el piloto automático se ha dañado, pero podemos marcar el camino a casa.\n")
	time.sleep(4)
	print("Para eso tiene que decirme hacía donde ir, tenga cuidado porque si se equivoca perderemos combustible y se quedara flotando en el espació para siempre.\n"+RESET)
	
	input(GREEN+"Presione 'ENTER' para arrancar los motores\n"+RESET)

#USO DE CICLO FOR
	
	print(RED+"Arrancando motores...")
	
	for carga in range (5,0,-1):
		print(carga)
		time.sleep(1)
	
	print("Empezamos el viaje\n"+RESET)
	time.sleep(1)

##### PRIMERA PREGUNTA #####
	
	print(YELLOW+"1. No tenemos mucho combustible, tenemos que impulsarnos con la gravedad del planeta más cercano al sol, indiqueme por favor:"+RESET)
	print(BOLD+YELLOW+"¿cuál es el planeta más cercano al sol?: ")
	print("a) Urano")
	print("b) Mercurio")
	print("c) Neptuno")
	print("d) Venus\n"+RESET+END)

#CONTADOR DE PUNTOS EN BASE A NÚMEROS ALEATORIOS Y CORRECCIÓN DE TIPO DE DATO
	
	print(RED+"Nivel de Combustible: "+str(comb)+" Litros\n"+RESET)
	rpta1 = input(GREEN+"Ingrese tu respuesta: "+RESET)

#VALIDACIÓN DE RESPUESTA CON CICLO WHILE
	
	while rpta1 not in ("a", "b", "c", "d"):
		rpta1 = input(RED+"Oficial "+name+" debe responder con a, b, c o d. Ingrese nuevamente su respuesta: \n"+RESET)

#TIMER
	print(YELLOW+"Procesando...\n"+RESET)
	time.sleep(1)

#USO DE "IF-ANIDADO" PARA RESPUESTAS VARIADA
	
	if rpta1 == "b":
	    comb_act = comb + comb_2 #OPERADORES
	    print(YELLOW+"Bien hecho oficial",name,"ha elegido la ruta más adecuada y ha ganado",comb_2,"Litros de combustible"+RESET)
	    print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
		
	elif rpta1 == "d":
	    if comb >= 30000:
	      comb_act = comb
	      print(YELLOW+"Ha elegido el segundo planeta más cercano al sol, por suerte tenemos más de 30 000 Litros de combustible, este planeta nos servirá también.\n"+RESET)
	      print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
	    else:
	      print(YELLOW+"Ha elegido el segundo planeta más cercano al sol, necesita más de 30 000 Litros para llegar allí y no los tenemos, aquí termina su viaje. \n"+RESET)
	      exit()
				
	else:
		print(YELLOW+"Oficial",name,"este planeta esta incluso más lejos que la tierra, lo siento, aquí termina su viaje.\n"+RESET)
		exit()
				
	input(GREEN+"Presione 'ENTER' para continuar el viaje\n"+RESET)
	    
##### SEGUNDA PREGUNTA #####
	
	print(YELLOW+"2. Oficial! estamos cerca, pero veo un problema, falta velocidad, tendra que gastar combustible y ajustar la velocidad a 1/10 de la velocidad de la luz, necesito que me diga: "+RESET)
	print(BOLD+YELLOW+"¿Cuál es la velocidad de la luz?")
	
	print("a) 299 792.48 km/s")
	print("b) 3*10^-2")
	print("c) 300 000 Km/s")
	print("d) 30 000 m/s \n"+RESET+END)

#CONTADOR DE PUNTOS EN BASE A NÚMEROS ALEATORIOS Y CORRECCIÓN DE TIPO DE DATO
	
	print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)

#VALIDACIÓN DE RESPUESTA CON CICLO WHILE
	
	rpta2 = input(GREEN+"Ingrese tu respuesta: "+RESET)
	while rpta2 not in ("a", "b", "c", "d"):
	  rpta2 = input(RED+"Oficial "+name+" debe responder con a, b, c o d. Ingrese nuevamente su respuesta: \n"+END)

#USO DE CICLO FOR

	for carga in range (2,0,-1):
		print(YELLOW+"Procesando...\n"+RESET)
		time.sleep(1)

#IF ANIDADO PARA RESPUESTA VARIADA
	
	if rpta2 == "a":
	    print(YELLOW+"Bien hecho oficial",name,"es la velocidad exacta, podré hacer calculos más precisos y no gastaremos combustible demás, todo listo para el impulso"+END)
	    print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+END)
		
	elif rpta2 == "c":
	    comb_act = comb_act - comb_3 #OPERADORES
	    print(YELLOW+"Bien Oficial",name,"aunque pudo haber sido más preciso, debido a la diferencia tendra que gastar",comb_3,"Litros de combustible extra, de todas formas, todo listo para el impulso"+RESET)
	    print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
		
	else:
	    comb_act = comb_act - 12000 #OPERADORES
	    if comb_act >= 22000:
	      print(YELLOW+"Oficial",name,"esa no es la velocidad de la luz, los calculos salieron mal, su viaje continuará si solo le quedan más de 22 000 Litros de combustible."+RESET)
	      print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros \n"+RESET)
				
	    else:
	      print(YELLOW+"Oficial",name,"lamentablemente esa no es la velocidad de la luz, los calculos salieron mal, necesita al menos 22 000 Litros de combustible, y solo tiene",str(comb_act),"lo siento, no podrá regresar a casa.\n"+RESET)
	      exit()
	
	input(GREEN+"Presione 'ENTER' para continuar el viaje\n"+RESET)   
##### TERCERA PREGUNTA #####
	print(YELLOW+"3. Oficial",name,"ese impulso gravitacional salió bien, ahora necesito hacer unos reajustes a la gravedad de la capsula, para eso necesito que me diga: "+RESET)
	print(BOLD+YELLOW+"¿cuál es la gravedad de la tierra?")
	
	print("a) 9.8 m/s^2")
	print("b) 10 m/s^2")
	print("c) 15 m/s^2")
	print("d) 100 km/s^2 \n"+END+RESET)

#CONTADOR DE PUNTOS EN BASE A NÚMEROS ALEATORIOS
	
	print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)

#VALIDACIÓN DE RESPUESTA CON CICLO WHILE
	
	rpta3 = input(GREEN+"Ingrese tu respuesta: "+RESET)
	while rpta3 not in ("a", "b", "c", "d"):
	  rpta3 = input(RED+"Oficial "+name+" debe responder con a, b, c o d. Ingrese nuevamente su respuesta: \n"+RESET)

	for carga in range (2,0,-1):
		print(YELLOW+"Procesando...\n"+RESET)
		time.sleep(1)

#RESPUESTA CON OPERADORES NÚMERICOS
	
	if rpta3 == "a":
	  comb_act = comb_act * 2 #OPERADOR PRODUCTO
	  print(YELLOW+"Muy bien oficial",name,"eso me permite aprovechar recursos y duplicar la duración del combustible."+RESET)
	  print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
	elif rpta3 == "b":
	  comb_act = comb_act + 5000 #OPERADOR SUMA
	  print(YELLOW+"Muy bien oficial",name,"no fue muy preciso, pero es como si tuvieramos más combustible"+RESET)
	  print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
	elif rpta3 == "c":
	  comb_act = comb_act - 5000 #OPERADOR RESTA
	  print(YELLOW+"Oficial",name,"esa es más gravedad de la necesaria, vamos a perder combustible"+RESET)
	  print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
	else:
	  comb_act = comb_act / 2 #OPERADOR DIVISIÓN
	  print(YELLOW+"Oficial",name,"esa gravedad es 10 veces más que la tierra, con este ajuste el combustible se reducirá a la mitad"+RESET)
		
#VERIFICACIÓN DE PUNTAJE
		
	  print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
	
	input(GREEN+"Presione 'ENTER' para continuar el viaje\n"+RESET)

##### CUARTA PREGUNTA #####

#LISTAS
	
	print(YELLOW+"Muy bien oficial",name,"ahora le voy a pedir una serie de datos para poder hacer más ajustes, estos se guardaran en una lista\n"+RESET)
	
	datos = []
	print(BLUE+"")
	datos.append(int(input("Ingrese edad: ")))
	datos.append(int(input("Ingrese peso (Kg): ")))
	datos.append(int(input("Ingrese estatura(cm): ")))        
	datos.append(int(input("Ingrese número de tripulantes: ")))
	print(""+RESET)

	print(YELLOW+"Bien oficial, estos datos me serviran para ajustar los niveles de oxigeno, compruebelos por favor, si hay alguno mal, modifiquelo según las instrucciones: \n")
	
	print("Edad: ",datos[0])
	print("Peso: ",datos[1])
	print("Estatura: ",datos[2])
	print("Tripulantes:\n",datos[3])
	print(""+RESET)
	
	modi=input(RED+"¿Desea modificar algún dato?, Responda 'si' o 'no': \n"+RESET)

	if modi == "si":
		print(YELLOW+"1. Edad")
		print("2. Peso")
		print("3. Estatura")
		print("4. Tripulantes"+RESET)

		print(BLUE+"Ingrese el número de dato que desea cambiar: "+RESET)
		i = int(input())
		print(BLUE+"Ingrese nuevo dato: "+RESET)
		val = int(input())
		
		datos[i]=val
		print(YELLOW+"Dato cambiado satisfactoriamente\n")

	elif modi == "no":
		print("Muy bien oficial, continuemos")			

	input(GREEN+"Presione 'ENTER' para continuar el viaje\n"+RESET)

##### ULTIMA PREGUNTA #####
	
	print(YELLOW+"4. Oficial "+name+"nos estamos acercando mucho, solo necesito un dato más para optimizar más el viaje, necesito que me diga: "+RESET)
	print(BOLD+YELLOW+"¿Cuál es la forma más común para medir distancias en el espacio?")
	
	print("a) Unidades Astronomicas")
	print("b) Años luz")
	print("c) Pársecs")
	print("d) Número Match \n"+RESET+END)
	
	print(RED+"Nivel de Combustible: "+str(comb_act)+" Litros\n"+RESET)
	
	rpta5 = input(GREEN+"Ingrese tu respuesta: "+RESET)
	while rpta5 not in ("a", "b", "c", "d"):
	  rpta5 = input(RED+"Oficial "+name+" debe responder con a, b, c o d. Ingrese nuevamente su respuesta: \n"+RESET)
	
	for carga in range (3,0,-1):
		print(YELLOW+"..."+RESET)
		time.sleep(1)

#RESPUESTAS CON IF ANIDADOS PARA DEFINIR SEGÚN EL PUNTAJE
		
	if rpta5 == "b":
	  comb_act = comb_act + comb_2 #OPERADORES NUM
	  if comb_act >= 22000:
	    print(YELLOW+"Necesitamos 22000 Litros de combustible para llegar a la tierra y usted tiene",str(comb_act),"Litros de combustible")
	    print("Bien hecho oficial",name,"ahora podrá llegar a la tierra sano y salvo, disfrute del viaje, no falta mucho para llegar\n")
	    print("Gracias por Jugar"+RESET)
	    exit()
			
	  else:
	    print(YELLOW+"Necesitamos 22000 Litros de combustible para llegar a la tierra, lamentablemente usted solo tiene",str(comb_act),"Litros de combustible")
	    print("El combustible no es suficiente oficial "+name+", pero se encuentra muy cerca de la tierra, enviaré una señal de emergencia y vendran a rescatarlo. \n")
	    print("Gracias por Jugar"+END)
	    exit()
			
	else:
	  if comb_act >= 22000:
	    print(YELLOW+"Necesitamos 22000 Litros de combustible para llegar a la tierra")
	    print("Bien hecho oficial",name,"no sé como pero tenemos combustible suficiente, pronto llegaremos.\n"+END)
	    print("Gracias por Jugar"+END)
	    exit()
	  else:
	    print(YELLOW+"Necesitamos 22000 Litros de combustible para llegar a la tierra\n")
	    print("Es una pena que se haya quedado tan cerca oficial",name,"no esta lo suficientemente cerca para enviar una señal de auxilio. Creo que aquí termina su viaje.\n"+RESET)

#FINAL - REPETICIÓN CON CICLOS
	
	print(RED+"Un segundo oficial",name,"puedo ver un agujero de gusano el cual nos llevará al inicio del viaje, ¿DESEA VOLVER A INICIAR \n"+RESET)
	rep_triv = input(YELLOW+"Ingrese 'si' para repetir, o presione cualquier tecla para terminar el viaje: \n"+RESET).lower()

#MENSAJE FINAL
	
	if rep_triv != "si":
	  print(BOLD+YELLOW+"Ha sido un gran viaje Oficial",name,", hasta pronto!"+RESET+END)
	  ini_triv = False 
	
	