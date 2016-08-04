import funciones
des = 1

print ("Hola! Empecemos a jugar")
while des != 2:
    if des == 1:
        print (guiones)
        intento = input ("Ingresa una letra: ")
        encontrado = False
        error = False
        errores = 0
        for j in range(len(palabra)):
            if intento == palabra[j]:
                guiones[j] = letra
                encontrado = True

                print (" ".join(encontrado))
                print ("")

            else:
                error = True 
                errores = errores + 1
                for j in errores:
                    j = errores - 1
                    print (mu [j])

        muere = False
        while errores < 7:
            muere = False 
        else:
            muere = True
            print ("Perdiste")
            print ("La palabra era " + palabra)
            des = int(input("1. Volver a jugar" '\n' "2. Salir"))
            if des == 1:
                muere == False
                errores = 0
            else: 
                print ("Adios ☺")