var num = 10;
var cont = num - 1;

while(cont>1){
	if(num%cont== 0){
		console.log("No es primo")
		break
	};
	cont = cont - 1;
}

if(cont==1){
	console.log("Es primo")
}