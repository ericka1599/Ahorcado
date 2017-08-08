//Encontrar el area de un rectangulo, un circulo y un triangulo 

var AreaTriangulo = function(dato_uno, dato_dos){
	return (dato_uno*dato_dos)/2;
}

var AreaRectangulo = function(dato_uno, dato_dos){
	return dato_uno*dato_dos;
}

var AreaCirculo = function(dato_uno){
	return (2*3.14*(dato_uno*dato_uno));
}

var Encontrar =function(forma, dato_uno, dato_dos){
	return forma(dato_uno, dato_dos)
}
forma = "circulo"
dato_uno = 2
dato_dos = 5

if (forma == "triangulo"){
	console.log(Encontrar(AreaTriangulo, dato_uno, dato_dos))
} 
if (forma == "rectangulo"){
	console.log(Encontrar(AreaRectangulo, dato_uno, dato_dos))
}
if (forma == "circulo"){
	console.log(Encontrar(AreaCirculo, dato_uno))
}