import funciones
des = 1

print ("Hola! Empecemos a jugar")
while des != 2:
	if des == 1:
		print (funciones.guiones)
		intento = input ("Ingresa una letra: ")
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

		print (funciones.hombresito)