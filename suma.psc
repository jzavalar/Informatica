// suma.psc

// El ejemplo m�s simple de la Ayuda de PSeInt (2023)
// Solicita dos numeros, los suma y muestra el resultado

// Inicia el proceso principal
Proceso Suma
	// Parte 1: Declarar las variables y su tipo de dato 
	Definir a, b, c como Reales;
	
	// Parte 2: Cargar los datos de entrada 
	// Se le muestra un mensaje al usuario con la instrucci�n Escribir, y 
	// luego se lee y almacena cada dato, al mismo tiempo, con la instrucci�n Leer, 
	// el primero en la variable a y el segundo en la variable b. 
	
	Escribir "Ingrese el primer n�mero:";
	Leer a;
	
	Escribir "Ingrese el segundo n�mero:";
	Leer b;
	
	// Parte 3: Calcular o procesar los datos
	// Se calcula la suma y se guarda el resultado en la
	// variable c mediante la operaci�n de asignaci�n ( <- )
	
	c <- a + b;
	
	// Parte 4: Salida de resultados
	// Finalmente, se muestra el resultado para avisar al usuario,
	// precedido de un mensaje
	Escribir "El resultado de sumar ", a , " + " , b , " es: ", c;
	
    // Termina el proceso
FinProceso