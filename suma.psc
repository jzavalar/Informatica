// suma.psc

// El ejemplo más simple de la Ayuda de PSeInt (2023)
// Solicita dos numeros, los suma y muestra el resultado

// Inicia el proceso principal
Proceso Suma
	// Parte 1: Declarar las variables y su tipo de dato 
	Definir a, b, c como Reales;
	
	// Parte 2: Cargar los datos de entrada 
	// Se le muestra un mensaje al usuario con la instrucción Escribir, y 
	// luego se lee y almacena cada dato, al mismo tiempo, con la instrucción Leer, 
	// el primero en la variable a y el segundo en la variable b. 
	
	Escribir "Ingrese el primer número:";
	Leer a;
	
	Escribir "Ingrese el segundo número:";
	Leer b;
	
	// Parte 3: Calcular o procesar los datos
	// Se calcula la suma y se guarda el resultado en la
	// variable c mediante la operación de asignación ( <- )
	
	c <- a + b;
	
	// Parte 4: Salida de resultados
	// Finalmente, se muestra el resultado para avisar al usuario,
	// precedido de un mensaje
	Escribir "El resultado de sumar ", a , " + " , b , " es: ", c;
	
    // Termina el proceso
FinProceso