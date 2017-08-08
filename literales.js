var jose ={
	edad: 18,
	altura: 175,
	direccion: {
		departamento: 'Guatemala',
		municipio: 'Cuidad',
		"la zona man": 16,
		residencia: {
			colonia: 'Santa Amelia',
			apartamento: '100',
			edificio: 5
		}
	}
};

console.log(jose.direccion["la zona man"]);
console.log(jose.direccion.municipio);