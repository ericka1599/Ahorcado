import random
import lipalabras
def palabra (palabras):
	palabra = random.randrage(palabras)

def guiones ():
	guiones = [ ]
	for i in palabra(len(palabra)):
		guiones.append ("_")
	print (guiones)	


def intentos (intento):
	encontrado = False
	error = False
	errores = 0
	for j in range(len(palabra)):
		if intento == palabra[j]:
			guiones[j] = letra
			encontrado = True
		else:
			error = True 
			errores = errores + 1
			print ("Ingresa una letra: ")


def hombresito (errores):
	mu =[
	print (" ———————" ) 
	print("ǀ") 
	print("ǀ") 
	print("ǀ") 
	print("ǀ") ,

	print (" ———————" ) 
	print("ǀ       ǀ  ") 
	print("ǀ ") 
	print("ǀ ") 
	print("ǀ ") ,

	print (" ———————" ) 
	print("ǀ       ǀ  ") 
	print("ǀ     (•˛•)  ") 
	print("ǀ ") 
	print("ǀ ") , 

	print (" ———————" ) 
	print("ǀ       ǀ  ") 
	print("ǀ     (•˛•)  ") 
	print("ǀ       ¦   ") 
	print("ǀ       ") ,

	print (" ———————" ) 
	print("ǀ       ǀ  ") 
	print("ǀ     (•˛•)  ") 
	print("ǀ      ―¦   ") 
	print("ǀ      ") ,

	print (" ———————" ) 
	print("ǀ       ǀ  ") 
	print("ǀ     (•˛•)  ") 
	print("ǀ      ―¦―   ") 
	print("ǀ      ") ,

	print (" ———————" ) 
	print("ǀ       ǀ  ") 
	print("ǀ     (•˛•)  ") 
	print("ǀ      ―¦―   ") 
	print("ǀ      ┘ ") ,

	print (" ———————" ) 
	print("ǀ       ǀ  ") 
	print("ǀ     (•˛•)  ") 
	print("ǀ      ―¦―   ") 
	print("ǀ      ┘ └")


	] 
	

def ahorcado (errores):
	muere = False
	while errores < 7:
		muere = False 
	else:
		muere = True
		return "Perdiste"
		print ("La palabra era " + palabra)
		des = int(input("1. Volver a jugar" '\n' "2. Salir"))
		if des == 1:
			muere == False
			errores = 0
		else: 
			print ("Adios ☺")