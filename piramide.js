var altura = 5;
var x = altura - 1;
var p = 1

for( var i=0; i < altura; i++){
	console.log(" ".repeat(x), "* ".repeat(i))
	x-= 1
};

for( var y = 0; y < p; y++){
	console.log(" ".repeat(altura-2), "*")
}
