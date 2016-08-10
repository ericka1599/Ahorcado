import random
des = 1
lista = [
"adolescente", "adulto", "agua", "aire", "alberca", "alcalde", "anciano", "arbol", "asfalto", "avion", "azucar", "azul", "balon", "barrio", "blanco", "bolsa", "boton", "brocha", "cabello", "cabeza", "cafe", "calle", "camara", "camion", "camisa", "cara", "caramelo", "casa", "cepillo", "cerveza", "chocolate", "cigarro", "ciudad", "clavo", "coche", "comida", "cortina", "cuaderno", "cuchara", "dedos", "disco", "dulce", "edificio", "ejercito", "electricidad", "espejo", "forma", "fuego", "gato", "goma", "gorra", "guante", "hombre", "jabon", "jardin", "joven", "labios", "lampara", "lapiz", "libreta", "libro", "llave", "lluvia", "luz", "manguera", "mano", "manta", "mesa", "mujer", "negro", "nina", "nino", "pan", "pantalon", "perro", "piedra", "pierna", "pintura", "pistola", "placa", "planta", "plato", "pluma", "pueblo", "puerta", "radio", "sal", "sarten", "silencio", "silla", "simbolo", "sol", "tornillo", "trapo", "tren", "vaso", "vecino", "ventana", "verde", "vino", "zapato", "muchos", "multa", "mugre", "mugir", "mudar", "multitud", "mutilar", "musitar", "muneca", "muela", "muelle", "mujer", "mural", "muralla", "mueble", "muerte", "mundo", "multiplicacion", "muerdago", "musgo", "mula", "mutuo", "muleta", "murcielago", "mutis", "muy", "mustia", "muslo", "musica", "musulman", "museo", "murmurar", "mucama", "mutante", "mullida", "comun", "amueble", "cumulo", "acumular", "amuleto", "camuflaje", "inmune", "bismuto", "tartamudo", "pomulo", "comunista", "comulgar", "formula", "escaramuza", "almuerzo", "disimular", "conmuevo", "limusina", "estimular", "transmutar", "remunerar", "comunicar", "emulsion", "permuta", "promulgar", "simular", "comuna", "bermuda", "conmutador", "cumulo", "enmudecer", "femur", "gamuza", "lemur", "salmuera", "rimu", "emu", "anamu", "temu", "samu", "jermu", "vermu", "sumu", "apersonamiento", "apersonarse", "apertar", "apertura", "aperturismo", "aperturista", "apesadumbrar", "apesaradamente", "apesarar", "apesgamiento", "apesgar", "apestar", "apestillar", "apestoso", "apetalo", "apetecedor", "apetecer", "apetecible", "apetencia", "apetente", "apetite", "apetitivo", "apetito", "apetitoso", "apex", "apezonado", "apezunar", "api", "apiadador", "alejandria", "alejandrinismo", "alejandrino", "alejandrita", "alejar", "alejija", "alejur", "alelado", "alelamiento", "alelar", "alelevi", "aleli", "alelo", "alelomorfico", "alelomorfo", "aleluya", "alema", "aleman", "alemanda", "alemanes", "alemanesco", "alemanico", "alemanisco", "alenguamiento", "alenguar", "alentada", "alentadamente", "brecha", "brechero", "brecol", "brecolera", "brega", "bregadura", "bregar", "breguero", "bren", "brena", "brenal", "brenar", "brenca", "brenoso", "breque", "bresca", "brescar", "bretador", "bretana", "brete", "breton", "bretoniano", "bretonica", "breva", "breval", "breve", "brevedad", "brevera", "brevete", "breviario", "brevipenne", "brezal", "brezar", "brezo", "briago", "brial", "briba", "bribar", "bribia", "bribiatico", "bribion", "bribon", "bribonada", "bribonear", "briboneria", "bribonesco", "bricbarca", "bricho", "bricolaje", "brida", "bridecu", "bridon", "briega", "brigada", "brigadero", "brigadier", "brigadiera", "brigantina", "brigantino", "bright", "brigola", "brijan", "brillador", "brillante", "brillantemente", "brillantez", "brillantina", "brillar", "brillazon", "brillo", "brilloso", "brin", "brincador", "brincar", "brincho", "brincia", "brinco", "brindador", "brindar", "brindis", "brinon", "brinquillo", "brinquino", "brinza", "brio", "briocense", "briofito", "briol", "brionia", "briosamente", "brioso", "briozoo", "briqueta", "brisa", "brisar", "brisca", "briscado", "briscar", "brisera", "brisotecaballerito", "caballeriza", "caballerizo", "caballero", "caballerosamente", "caballerosidad", "caballeroso", "caballerote", "caballeta", "caballete", "caballillo", "caballista", "caballito", "caballo", "caballon", "caballuno", "cabalmente", "cabalonga", "cabana", "cabanal", "cabanense", "cabanera", "cabaneria", "cabanero", "cabanga", "cabanil", "cabare", "cabaretero", "cabarga", "cabarra", "cabarron", "cabas", "cabaza", "cabdal", "cabdillazgo", "cabdillo", "cabe", "cabear", "cabeceado", "cabeceador", "cabeceamiento", "cabecear", "cabeceo", "cabecero", "cabeciancho", "cabeciduro", "cabecilla", "cabedero", "cabellado", "cabellar", "cabellera", "cabello", "cabelludo", "caber", "cabero", "cabestraje", "cabestrante", "cabestrar", "cabestrear", "cabestreria", "cabestrero", "cabestrillo", "cabestro", "cabete", "cabeza", "cabezada", "cabezaje", "cabezal", "cabezaleria", "cabezalero", "cabezazo", "cabezcaido", "cabezo", "cabezon", "cabezonada", "cabezoneria", "cabezorro", "cabezota", "cabezote", "cabezudamente", "cabezudo", "cabezuela", "cabido", "cabila", "cabildada", "cabildante", "cabildear", "cabildeo", "cabildero", "cabildo", "cabileno", "cabilla", "cabillero", "cabillo", "cabimiento", "cabina", "cabinera", "cabio", "cabizbajo", "cabizcaido", "cabizmordido", "cable", "cableado", "cablear", "cablegrafiar", "cablegrafico", "cablegrama", "cablero", "cablieva", "cabo", "caboral", "cabotaje", "caboverdiano", "cabra", "cabracho", "cabrada", "cabrahigadura", "cabrahigal", "cabrahigar", "cabrahigo", "cabrales", "cabrear", "cabreo", "cabreria", "cabrerizo", "cabrero", "cabrestante", "cabria", "cabrilla", "cabrillear", "cabrilleo", "cabrina", "cabrio", "cabriola", "cabriolar", "cabriole", "cabriolear", "cabrita", "cabritada", "cabritero", "cabritilla", "cabrito", "cabrituno", "cabro", "cabron", "cabronada", "cabrunar", "cabruno", "cabujon", "cabure", "cabuya", "cabuyera", "cabuyeria", "caca", "cacahual", "cacahuate", "cacahuatero", "cacahuero", "cacahuete", "cacalota", "cacalote", "cacan", "cacana", "cacao", "cacaotal", "cacaotero", "cacarana", "cacaranado", "cacareador", "cacarear", "cacareo", "cacarico", "cacarizo", "cacarro", "cacaste", "cacastle", "cacatua", "deterior", "deterioracion", "deteriorar", "deterioro", "determinable", "determinacion", "determinado", "determinante", "determinar", "determinativo", "determinismo", "determinista", "detersion", "detersivo", "detersorio", "detestable", "detestacion", "detestar", "detienebuey", "detinencia", "detonacion", "detonador", "detonante", "detonar", "detornar", "detorsion", "detraccion", "detractar", "detractor", "detraedor", "detraer", "detraimiento", "detras", "detrimento", "detritico", "detrito", "detritus", "deturpacion", "deturpar", "deuda", "deudo", "deudor", "deudosa", "deudoso", "deuteragonista", "deuterio", "deuteron", "deuton", "devalar", "devaluacion", "devaluar", "devanadera", "devanado", "devanador", "devanagari", "devanar", "devandicho", "devaneador", "devanear", "devaneo", "devant", "devantal", "devastacion", "devastador", "devastar", "develar", "develizar", "devengar", "devengo", "devenir", "deverbal", "deverbativo", "deviacion", "deviedo", "devieso", "devino", "devinto", "devisa", "devisar", "devisero", "devocion", "devocionario", "devodar", "devolucion", "devolutivo", "devolver", "devoniano", "devonico", "devorador", "devorar", "devoraz", "devoteria", "devoto", "esplendido", "esplendor", "esplendorosamente", "esplendoroso", "esplenectomia", "esplenetico", "esplenico", "esplenio", "esplenitis", "esplenomegalia", "espliego", "esplin", "esplique", "espolada", "espolazo", "espoleadura", "espolear", "espoleta", "espoliacion", "espoliador", "espoliar", "espolin", "espolinar", "espolio", "espolique", "espolista", "espolon", "espolonada", "espolonazo", "espolonear", "espolvorar", "espolvorear", "espolvoreo", "espolvorizar", "espondaico", "espondeo", "espondil", "espondilitis", "espondilo", "espondilosis", "espongiario", "espongiosidad", "espongioso", "esponja", "esponjado", "esponjadura", "esponjamiento", "esponjar", "esponjera", "esponjosidad", "esponjoso", "esponsales", "esponsalicio", "esponsorizacion", "esponsorizar", "espontaneamente", "espontanearse", "espontaneidad", "espontaneo", "esponton", "espontonada", "espora", "esporadico", "esporangio", "esporidio", "esporifero", "esporo", "esporocarpio", "esporofila", "esporofilo", "esporofito", "esporozoario", "esporozoo", "esportada", "esportear", "esportilla", "esportillero", "esportillo", "esportizo", "esporton", "esportonada", "esporulacion", "esporular", "esposa", "esposado", "esposar", "esposo", "esprintar", "esprinter", "espuela", "espuenda", "espuerta", "espulgadero", "espulgador", "espulgar", "espulgo", "espuma", "espumadera", "espumador", "espumaje", "espumajear", "espumajo", "espumajoso", "espumar", "espumarajo", "espumear", "espumeo", "espumero", "espumilla", "espumillon", "espumoso", "espumuy", "espundia", "espurio", "espurrear", "espurriar", "espurrir", "esputar", "esputo", "esquebrajar", "esquejar", "esqueje", "esquela", "esqueletado", "esqueletico", "esqueleto", "esquema", "esquematicamente", "esquematico", "esquematismo", "esquematizacion", "esquematizar", "esquena", "esquenanto", "esquero", "esqui", "esquiador", "esquiar", "esquiciar", "esquicio", "esquifada", "esquifar", "esquifazon", "esquife", "esquijama", "esquila", "esquilada", "flauta", "flautado", "flauteado", "flautero", "flautillo", "flautin", "flautista", "flautos", "flavo", "flebil", "flebitis", "flebotomia", "flebotomiano", "flecadura", "flecha", "flechador", "flechadura", "flechar", "flechaste", "flechazo", "flechera", "flecheria", "flechero", "flechilla", "fleco", "flegma", "flegmatico", "flegmonoso", "fleja", "flejar", "fleje", "flema", "flematico", "fleme", "flemon", "flemonoso", "flemoso", "flemudo", "fleo", "flequillo", "fleta", "fletacion", "fletador", "fletamento", "fletante", "fletar", "flete", "fletear", "fleteo", "fletero", "flexibilidad", "flexibilizar", "flexible", "flexion", "flexional", "flexionar", "flexivo", "flexo", "flexor", "flexuoso", "flexura", "flictena", "flipar", "flirtear", "flirteo", "flocadura", "floculacion", "flocular", "floema", "flogistico", "flogisto", "flogosis", "flojamente", "flojear", "flojedad", "flojel", "flojera", "flojo", "flojuelo", "flojura","floqueado","flor","flora","tequila","traicion","traicionar","traicionero","traido","traidor","traidoramente","trailer","trailla","traillar","traina","trainera","traite","trajano","traje","trajeado","trajear","trajelar","trajin","trajinante","trajinar","trajinera","trajineria","trajinero","trajino","tralhuen","tralla","trallazo","trama","tramador","tramar","tramilla","tramitacion","tramitador","tramitar","tramite","tramitologia","tramitomania","tramo","tramojo","tramontano","tramontar","tramoya","tramoyista","tramoyon","trampa","trampal","trampantojo","trampazo","trampeador", "trampear","tramperia","trampero","trampilla","trampista","trampolin","tramposo","tranca","trancada","trancahilo","trancanil","trancar","trancazo","trance","trancelin","trancha","tranchea","tranchete","trancho","tranco","trangallo","tranquear","tranquera","vodka","vodu","voduismo","voila","volada","voladero","voladito","voladizo","volado","volador","voladura","volandas","volandero","volandillas","volando","volanta","volante","volantear","volantin","volanton","volapie","volapuk","volar","volateo","volateria","volatero","volatil","volatilidad","volatilizable","volatilizacion","volatilla","volatin","volatinero","volatizar","volaverunt","volcan","volcanico","volcanismo","volcanologia","volcanologo","volcar","volea","volear","voleibol","voleo","volframio","volicion","volido","volitar","volitivo","volovan","volquearse","volqueta","volquetazo","volquete","volquetero", "volsco","volt","voltaico","voltaje","voltametro","voltariedad","voltario","whisky","ron","rona","ronal","ronar","ronca","roncadera","roncador","roncal","roncales","roncamente","roncar","ronce","roncear","ronceria","roncero","roncha","ronchar","ronchon","ronco","roncon","ronda","rondador","rondalla","rondana","rondar","rondel","rondeno","rondin","rondis",
]

mu = [
"""
  _______
 |       
 |
 | 
 |""",

"""
  _______
 |       |
 |
 | 
 |""",

"""
  _______
 |       |
 |     (._.)
 | 
 |""",

"""
  _______
 |       |
 |     (._.)
 |       ¦
 |""",

"""
  _______
 |       |
 |     (._.)
 |      -¦
 |""",

"""
  _______
 |       |
 |     (._.)
 |      -¦-
 |""",


"""
  _______
 |       |
 |     (._.)
 |      -¦-
 |      /  """,

"""
  _______
 |       |
 |     (._.)
 |      -¦-
 |      / \ """
] 

print ("Hola! Empecemos a jugar")
while des != 2:
    if des == 1:

        numero = random.randrange(0 , 1000)
        palabra = lista[numero] 
        guiones = [ ]
        for i in palabra:
            palabra = str(palabra)
            guiones.append ("_")
        print (guiones)

        intento = input ("Ingresa una letra: ")
        encontrado = False
        error = False
        errores = 0
        
        if intento in palabra:
            for i in range(len(palabra)):
                    if palabra[i] == intento: 
                        guiones[i] = intento
                        if palabra == guiones:
                            print("")
                            print(" ".join(guiones))
                            print("")
                            print("Ganaste!")

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