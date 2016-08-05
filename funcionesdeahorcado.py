
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
			print ("Adios")

