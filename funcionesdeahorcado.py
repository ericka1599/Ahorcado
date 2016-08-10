import random


def eleccion ():
	numero = random.randrange(0 , 1000)
	palabra = lista[numero] 
	guiones = [ ]
	for i in palabra:
		palabra = str(palabra)
		guiones.append ("_")
	print (guiones) 


def intentar ():
	pl = palabra.split()
	leng = len(pl)
	l = [pl]
	for j in range (leng):
		if intento == l[j]:
			guiones[j] = intento
			encontrado = True

			print (" ".join(intento))
			print ("")

		else:
			error = True 
			errores = errores + 1
			dib = errores - 1
			print (mu[dib])



