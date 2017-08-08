var saludoFormal = function(nombre){
	return "Buenas tardes" + nombre + "gusto en saludarlo";
}

var saludoInformal = function(nombre){
	return "como estas " + nombre + "?";
}

var saludar = function(saludo, nombre) {
	return saludo(nombre);
}

var persona = "Ericka";


if (persona == "Ericka"){
	console.log(saludar(saludoInformal, persona))
} else{
	console.log(saludar(saludoFormal, persona))
}