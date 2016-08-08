from funcionesdeahorcado import eleccion, intentar
des = 1

print ("Hola! Empecemos a jugar")
while des != 2:
    if des == 1:

        print (eleccion)

        intento = input ("Ingresa una letra: ")
        encontrado = False
        error = False
        errores = 0
        
        print (intentar)

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
                print ("Adios ")