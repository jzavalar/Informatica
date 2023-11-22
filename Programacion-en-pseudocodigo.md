<img src="https://github.com/jzavalar/2211088-informatica/blob/main/images/conjunto-baseIzt.png" alt="UAM Iztapalapa" width="60%"/>

## Programación de Computadoras con Pseudocódigo PSeInt

**Profesor:** dr. Jesús Zavala Ruiz

**Contacto**:
- **Correo electrónico:** [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx)
- **Telegram:** <img src="https://github.com/jzavalar/2211088-informatica/blob/main/images/images/telegram_logo.svg" alt="Telegram" width="3%"/> [jzavalar.t.me](https://jzavalar.t.me)

Ultima actualización: 21 de noviembre de 2023. 

### 1. Introducción

Estas notas de clase pretenden servir para estudiar programación y la conversion de pseudocódigo a un lenguaje de programación real como R. 

La *programación de computadoras* es la creación, escritura o o *codificación* de programas de computadora que permiten darle instrucciones precisas, que permiten realizar las cuatro funciones básicas de la computadora : (1) lectura, (2) escritura, (3) almacenamiento y (4) procesamiento de datos. De manera general, existen dos tipos de lenguajes de programación: el pseudocódigo y los lenguajes de programación.

El *pseudocódigo* (*pseudocode*) es un lenguaje artificial que permite dar instrucciones a la computadora en lenguaje natural que tiene una sintaxis relativamente laxa y no estandarizada es fácil de leer y permite enfocarse en la abstracción lógica de un algoritmo. El pseudocódigo se utiliza para aprender programación y para diseñar los algoritmos, una tarea que precede a su implantación en un verdadero lenguaje de programación. Existen distintas herramientas automatizadas que implantan pseudódigo, pero en su mayoría en el idioma inglés, por lo que la existencia del Intérprete de Pseudocódigo [*PseInt*](https://pseint.sourceforge.net/)[^1] en español, es una gran ventaja para los estudiantes hispanohablantes. La obra clásica de algoritmos (en pseudocódigo) es la obra *The art of computer programming*, en 5 volúmenes, de Donald E. Knuth.

Los *verdaderos lenguajes de programación* o simplemente lenguajes de programación son lenguajes artificiales que se utilizan para programar computadoras y, por lo tanto, están basados en una sintaxis estricta. El primer lenguaje de programación fue ForTran (*For*mula *Tran*slating system) en 1957 para el cálculo científico y el segundo fue CoBol en 1959, que siguen vigentes y relativamente actualizados. Desde entonces se han desarrollado lenguajes de programación con gramáticas formales, conocidas como Backus-Naar Form o BNF. En la actualidad, se reportan entre 600 y 2500 u 8945 lenguajes de programación creados[^2], dependiendo de la fuente, la mayoría desconocidos; sin embargo, con conocer uno es suficiente. Existen también, muchas herramientas de programación: editores, compiladores, intérpretes, debuggers e IDEs para el desarrollo de software profesional.


### 2. Algoritmo en pseudocódigo

El _código fuente_ se escribe con las instrucciones del *algoritmo* según las reglas estrictas de la *sintaxis* del lenguaje, en cualquier editor de texto o en un entorno de desarrollo integrado (EDI), creando un *programa* y un _archivo fuente_.

El *pseudocódigo* es un lenguaje intermedio entre el lenguaje natural y un verdadero lenguaje de programación como R o Python, que es utilizado para dar instrucciones a una computadora con fines didácticos. Cuando el pseudocódigo se implanta en un intérprete como [*PseInt*](https://pseint.sourceforge.net/)[^3], puede verse en acción la ejecución de cada instrucción, como si fuera un verdadero *lenguaje de programación*. _PSeInt_ es la contracción de "*PSe*udocode *Int*erpreter" (Intérprete de Pseudocódigo). Inicialmente, _PSeInt_ fue el resultado de un proyecto final para la materia Programación I, de la carrera de Ingeniería en Informática, de la Facultad de Ingeniería y Ciencias Hídricas de la Universidad Nacional del Litoral (FICH-UNL) en Argentina. PSeInt fue desarrollado por el Ing. Pablo Novara, entonces estudiante, en diciembre de 2003[^4]. El PSeInt tomó como base el pseudocódigo usado por sus profesores, el Ing. Horacio Loyarte y el Dr. Diego Milone (idem). Las premisas del pseudocódigo PSeInt son:

-   Programación estructurada con:
    -   Un programa principal o *Algoritmo o Proceso*,
    -   *Subprocesos* o *funciones*.
-   Una sintaxis sencilla y, relativamente flexible, en español.
-   Entrada y salida de datos en una consola.
-   Solo tres *tipos de datos* básicos o simples:
    -   `Numéricos`, `Enteros` y `Reales`.
    -   Alfanuméricos: `Caracteres` o `Cadenas` de caracteres y
    -   `Logicos`.
-   Una sola estructura de datos:
    -   `Arreglo`.
-   Las principales estructuras básicas de control del flujo de control son:
    -   *Condicionales:*
        -   Simple: `Si ... Entonces ... FinSi`
        -   Doble: `Si ... Entonces ... SiNo ... FinSi`
        -   Múltiple: `Segun`
    -   *Repetitivas:*
        -   `Mientras`
        -   `Repetir`
        -   `Para`

Las *instrucciones* se construyen con los siguientes elementos básicos: *palabras reservadas*, *variables*, *operadores* y signos de puntación como punto y coma ( `;` ) para identificar el final de una instrucción. Las *palabras reservadas*, *palabras clave* o *keywords* en pseudocódigo PSeInt son identificadores predefinidos que tienen un significado especial y constituyen la _gramática del lenguaje_ y sirven para crear las instrucciones, en un programa. Un *programa* en pseudocódigo consta de ninguna, una o varias funciones o subprocesos y/o, por lo menos, un procedimiento principal llamado `Algoritmo` o `Proceso`, con la siguiente estructura general:

```
    // Se usan dos diagonales `//` para declarar un comentario, que es una línea que no se ejecuta

    // La estructura de un algoritmo puede organizarse
    // en Funciones o Subprocesos y un bloque de código
    // principal llamado Proceso o Algoritmo

    // Declaración de una Funcion o Subproceso

    // Funcion
    // Cabecera
    Funcion <variable_de_retorno> <- <nombre_de_la_función>( [ <lista_de_parámetros_formales> ] )
       // Declaraciones
       // Cuerpo
       <bloque_de_instrucciones>
    FinFuncion

    // SubProceso
    // Cabecera
    SubProceso <nombre_del_procedimiento>( [ <lista_de_parámetros_formales> ] )
       // Declaraciones
       // Cuerpo
       <bloque_de_instrucciones>
    FinSubProceso

    // Declaración del proceso principal o del algoritmo principal:

    // Cabecera
    Proceso <nombre_del_proceso>
       // Declaraciones
       // Cuerpo
       <bloque_de_instrucciones>
    FinProceso

    // o declaración del algoritmo principal
    // Cabecera
    Algoritmo <nombre_del_algoritmo>
       // Declaraciones
       // Cuerpo
       <bloque_de_instrucciones>
    FinAlgoritmo
```

En pseudocódigo, cuando no se definen funciones ni suprocesos, el programa en pseudocódigo sólo incluye la palabra reservada `Algoritmo` o `Proceso`, seguida del *nombre del algoritmo* que es utilizada para definir el inicio de un algoritmo. Luego, le sigue una *secuencia de instrucciones* y finaliza con la palabra reservada `FinAlgoritmo` o `FinProceso`. Por lo tanto, un algortimo es un bloque de instrucciones que inicia con la palabra `Algoritmo` y termina con `FinAlgoritmo` o inicia con `Proceso` y termina con `FinProceso`, tal como se ilustra más delante. El ejemplo más simple de esta construcción es el programa *Suma.psc* de la Ayuda de PSeInt, un pequeño algoritmo que *pide al usuario dos números* para *sumarlos* y, después, *muestra el resultado* de la operación suma, al cual se le han hecho alguna adecuaciones para señalar las partes del algoritmo y el nombre de las variables en minúsculas:

```
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
```

Descargue el archivo [suma.psc](https://github.com/jzavalar/Informatica/blob/main/suma.psc) y cárguelo y pruébelo en PSeInt.

Este ejemplo sirve para mostrar la estructura básica de un algoritmo o programa que contiene, esencialmente, las tres partes que coinciden con las cuatro funciones de la computadora:
1. Carga de datos (*Entrada*)
2. Cálculo (*Almacenamiento* y *Procesamiento*)
3. Presentación de resultados (*Salida*)

A continuación se describe la sintáxis del Pseudocódigo PSeInt que permite la implantación de esas cuatro funciones de la computadora.

### 3. Almacenamiento de datos

#### 3.1. Comentarios

En los *lenguajes de programación verdaderos* existen varios elementos básicos que son necesarios para que funcione la programación.

Uno de estos elementos son los *comentarios*, que son instrucciones que no se ejecutan, sino que ayudan a entender el código. En este sentido es una buena práctica documentar el código con información, entre otras cosas, como el nombre del algoritmo, el objetivo, el nombre del autor y sus datos de contacto, la fecha de realización, así como comentarios más explícitos que aclaren la lógica del algoritmo, para reinterpretarlo en el futuro.

En pseudocódigo PSeInt un comentario se define con dos diagonales, seguidas del comentario, como sigue:

```
    // Comentario

    c <- a + b; // Cálculo


    // Ejemplo

    // Archivo: suma.psc

    // Algoritmo: suma
    // Objetivo: Solicita dos numeros, los suma y muestra el resultado

    // Autor: Ayuda de PSeInt
    // Fecha: 2003
    // Modificado por: prof. J Zavala
    // e-mail: jzr\@xanum.uam.mx
```

#### 3.2. Variables

Una *variable* en un algoritmo es una posición o almacenamiento de memoria donde se puede guardar un dato, representada por un nombre o *identificador.*

En otras palabras, en pseudocódigo PSeInt, una variable se nombra con las siguientes reglas básicas:
-   Consta de uno o más *caracteres*, con *letras* del alfabeto inglés, el carácter *guión bajo* ( `_` ) o *dígitos* del 0 al 9, por lo que no está permitido el uso de las letras `ñ` y `Ñ`, ni puede contener *acentos*, ni *diéresis*.
-   El primer carácter debe ser una *letra* o el carácter *guión bajo* ( `_` ).
-   El nombre de una variable es *único* dentro de un algoritmo, es decir, debe ser distinto de los nombres de los subprocesos o funciones y distinto de las palabras reservadas y operadores.

Aunque, en PSeInt se pueden usar de manera indistinta las letras mayúsculas y minúsculas como identificadores equivalentes, es una muy buena práctica usar letras o palabras minúsculas, separadas por el carácter *guión bajo* ( `_` ), para identificar a las variables. Ejemplos de identificadores válidos son: `a`, `b`, `c`, `lado_1`, `_total`, `nombre_y_apellido`, `direccion_de_correo`.

#### 3.3. Constantes

Como su nombre lo indica, el *valor almacenado* en una *variable* puede ir variando a medida que el algoritmo se ejecuta o *corre*; sin embargo, también hay *constantes* que son variables que no cambian durante la ejecución del programa. Los identificadores de las *constantes* están sujetos a las mismas reglas de nombramiento que las variables, con la particularidad de que es una buena práctica utilizar letras o palabras MAYÚSCULAS para los nombres de las constantes, por ejemplo: `TOPE`, `MES`, `NUMERO_PI` y `NUMERO_E`.

#### 3.4. Tipos de datos

En PSeInt, las variables (y las constantes) tienen un *tipo de dato* asociado que también se definen con palabras reservadas, tal como se indica a continuación:
-   `Numerico` o `Numericos` para declarar el tipo de dato numérico, indistintamente, de entero o real, tales como `5` y `3.14`.
-   `Entero` o `Enteros` para declarar específicamente el tipo de dato entero, usado para *contar*, tales como `12`, `23`, incluyendo el cero ( `0` ) y valores negativos como `-3`.
-   `Real` o `Reales` para declarar el tipo de dato real, es decir, valores decimales o fraccionarios de unidades que *se miden*, positivos, el cero y negativos, tales como `1.0`, `-2.3`, `0.0` y `3.141592`.
-   Los tipos alfanuméricos pueden ser de dos tipos:
    -   `Caracter` o `Caracteres` para representar caracteres y se acostumbra usar un caracter entre apóstrofes ( `'` ), para distinguirlo de las cadenas, tales como `'H'`, `'\'` y `'a'`.
    -   `Cadena` o `Cadenas` para declarar *cadenas de caracteres* que se usa para almacenar valores alfanuméricos, tales como nombres, etiquetas y descripciones, por lo que se acostumbra encerrar los valores entre comillas ( `"` ), tales como `"Hola!"`, `"Hola Mundo!"`, `"123"` y `"Juan Pérez"`.
-   `Logico` o `Logicos` para declarar el tipo de dato lógico, que puede tomar uno de los dos valores posibles:
    -   `Falso`, `F` o `0` para indicar el valor `FALSO` o *No*.
    -   `Verdadero`, `V` o `1` para indicar el valor `VERDADERO` o *Si*.

Cada tipo de dato tiene asociada una serie de operaciones válidas. Por ejemplo, los datos *Numericos* se pueden usar para realizar operaciones matemáticas, los datos alfanuméricos (*Cadenas* o *Caracteres*) pueden concatenarse u obtenerse una subcadena y con los datos *Logicos* se pueden realizar operaciones lógicas de conjunción, disyunción y negación.


#### 3.4. Declaración de variables y constantes

Las variables tienen un *alcance* (*scope*) o validez global o local, dependiendo del lugar donde son declaradas; es decir, si las variables están declaradas dentro de un bloque de código son *variables locales*.

En pseudocódigo PSeInt no se pueden declarar variables fuera de un bloque de código, por lo que sólo permite variables locales. Por lo tanto, las variables que están dentro del bloque principal 
```
    Algoritmo 
    ... 
    FinAlgoritmo`
```
se comportan como *variables globales*.

En PseInt, las variables y las constantes se declaran explícitamente antes de usarse en un bloque de código, con el nombre de la variable y el tipo de dato, según la siguiente sintaxis general:

```
    // Declaración de las variables
    Definir <nombre_de_la_variable_1>, <nombre_de_la_variable_2>, ... Como <tipo_de_dato>;
```

Ejemplos de declaración de variables:

```
    Definir a Como Numerico;
    Definir cajas, zapatos, lonas Como Enteros;
    Definir peso Como Real;
    Definir letra Como Caracter;
    Definir nombre Como Cadena;
    Definir es_estudiante Como Logico;
```

Las *constantes* también se declaran según las mismas reglas que se aplican a las variables, sólo que con identificadores en letras MAYUSCULAS, según la siguiente sintaxis general:

```
    // Declaración de las constantes
    Definir <NOMBRE_DE_LA_CONSTANTE_1>, <NOMBRE_DE_LA_CONSTANTE_2>, ... Como <tipo_de_dato>;
```
Ejemplos de constantes:

```
    Definir TOPE, MES Como Enteros;
    Definir NUMERO_PI, NUMERO_E Como Reales;
    Definir LETRA, NUM, SIGNO, ESPACIO_EN_BLANCO Como Caracteres;
    Definir CADENA_VACIA, TITULO, AUTOR Como Cadenas;
    Definir ESTADO, INTERRUPTOR Como Logico;
```

Si se utiliza el *perfil de lenguaje* por defecto (*Flexible*), la definición explícita es opcional, pero se puede configurar el lenguaje para que sea obligatoria.

#### 3.5. Declaración de estructuras de datos

La *estructura de datos* es una forma de organización de datos para un manejo y procesamiento eficaz, como arreglos (*arrays*), listas (*lists*), pilas (*heaps*), colas (*queues*), árboles binarios (*binary* *trees*) y tablas (*tables* o *dataframes*), entre otras.

El pseudocódigo PSeInt sólo permite la declaración de una *estructura de datos*: el *arreglo* (o *array*) que es una lista de valores de tamaño fijo, del *mismo tipo de dato*; por lo que puede haber arreglos de tipo *Numerico*, *Entero*, *Real*, *Caracter* o *Logico*. Además, los arreglos pueden tener *una o más dimensiones*; es decir, arreglos unidimensionales, bidimensionales (matrices) o n-dimensionales. Después de declarar una variable con el tipo de dato, se debe declarar que esa variable es un arreglo de un tamaño y dimensiones específicas, con la siguiente sintaxis general:

```
    // Arreglo unidimensional (vector):
    Dimension <nombre_del_arreglo>[ <tamaño> ];
    Dimension <nombre_del_arreglo_1>[ <tamaño> ], <nombre_del_arreglo_2>[ <tamaño> ];

    // Arreglo bidimensional (matriz):
    Dimension <nombre_del_arreglo>[ <filas>, <columnas> ];

    // Arreglo multi-dimensional:
    Dimension <arreglo_1>[ <tamaño_1> ], <arreglo_2>[ <tamaño_1>, <tamaño_2> ], ..., <arreglo_n>[ <tamaño_1>, <tamaño_2>, ..., <tamaño_n> ] ];
```

Ejemplos:

```
    // Declaración de las variables
    Definir id, matriz, tridimensional como Entero;
    Definir descripcion como Caracter;
    Definir precio_unitario, total como Reales;
    Definir es_Soltero como Logico;

    // Declaracion de vectores (unidimensionales) de 10 elementos:
    Dimension id[10], descripcion[10], precio_unitario[10], total[10], es_Soltero[10];

    // Declaracion de de un arreglo bidimensional (matriz) de 10 x 2 elementos:
    Dimension matriz[10,20];

    // Declaracion de de un arreglo tridimensional de 10 x 20 x 30 elementos:
    Dimension tridimensional[10,20,30];
```

#### 3.6. Inicialización de variables

Después de declarar las variables, éstas deben *inicializarse*, es decir, deben almacenar un primer valor, con la restricción de que *siempre debe guardar datos* del *tipo de dato*, declarado previamente.

En PSeInt, por ejemplo, si una variable se declaró como tipo `Numerico`, ésta se utiliza para guardar *números* y no puede utilizarse para guardar valores de otro tipo, como `Cadena` o `Logico`. Las variables pueden *inicializarse* de dos formas:

1.  Mediante la *lectura* de un dato, que implica capturar el valor desde el teclado y asignarlo a una variable, con la instrucción `Leer` seguida de la lista de variables.
2.  Con una operación de *asignación* `<-` que permite guardar un valor, por ejemplo: `a <- 1; o` si la variable es producto de una operación, almacena el resultado, como `c <- a + b;`.

Por estas características se dice que la *lectura* y la *asignación* son *acciones constructivas*, es decir, de creación de datos, sin embargo, dado que con la asignación el valor de una variable es reemplazado por otro, se dice que es una *operación destructiva*.

Una vez inicializada, la variable puede utilizarse en cualquier instrucción, expresión o cálculo.

### 3.7. Inicialización de constantes

Las constantes se declaran igualmente que las variables, sin embargo, éstas sólo se inicializan y no vuelven a cambiar su valor, por lo menos durante la ejecución del programa.

A continuación se muestran algunos ejemplos de inicialización de constantes en pseudocódigo PSeInt, con la siguiente sintaxis general:

```
    // Inicializacion de una constante
    <NOMBRE_DE_LA_CONSTANTE> <- <expresión>;
```

Ejemplos:

```
    // Inicializacion de constantes enteras
    TOPE <- -5;
    MES <- 10;

    // Inicializacion de constantes reales
    NUMERO_PI <- 3.141592;
    NUMERO_E <- 2.718281;

    // Inicializacion de constantes alfanumericas
    // Tipo Caracter
    LETRA <- 's';
    NUM <- '9';
    SIGNO <- '-';
    ESPACIO_EN_BLANCO <- ' ';

    // Tipo Cadena
    CADENA_VACIA <- "";
    TITULO <- "El arte de escuchar";
    AUTOR <- "Erich Fromm";

    // Inicializacion de constantes logicas
    ESTADO <- Verdadero;
    INTERRUPTOR <- Falso;
```

### 4. Entrada de datos

La entrada de datos es una función principal de la computadora y, en un programa, es una instrucción primitiva que permite la lectura de un flujo de datos o (*stream*), mediante la captura de datos desde el teclado, un archivo, un sensor o cualquier dispositivo de entrada de datos.

En pseudocódigo PSeInt sólamente se pueden capturar bytes desde el teclado con la palabra reservada `Leer` con la siguiente sintaxis general:

```
    // Lectura de datos e inicializacion de variables
    Leer <variable_1>, ..., <variable_n>;
```

Ejemplos:

```
    // Leer e inicializar las variables
    Leer nombre;
    Leer apellidos;
    Leer edad;

    // Otra posibilidad es:
    Leer nombre, apellidos, edad;
```

Además, en PseInt se puede capturar un teclazo con la palabra reservada `Esperar Tecla` para esperar hasta que el usuario *presione cualquier tecla*. Se usa la siguiente sintaxis general:
```
    Esperar Tecla; 
```

En PseInt, existe una funcionalidad similar a la anterior, que con la palabra reservada `Esperar` puede utilizarse para *suspender temporalmente el algoritmo*, durante un tiempo definido en segundos o milisegundos, con la siguiente sintaxis general:

```
    // Esperar
    Esperar <tiempo> [Segundos | Milisegundos];
```

Ejemplos:

```
    Esperar 3 Segundos;
    Esperar 250 Milisegundos;
```

### 5. Salida de datos

La *salida de datos* es otra función principal de la computadora que consiste en exponer la respuesta, presentación de algún dato, poner a funcionar un dispositivo de salida como una señal, un motor o un actuador.

#### 5.1. Impresión de mensajes

En PSeInt, hay varias acciones de salida de datos que se pueden realizar, dependiendo de las necesidades del usuario. En primer lugar, se pueden *escribir mensajes* en la pantalla, con la palabra reservada `Escribir`, bajo la siguiente sintaxis general:

```
    // Imprimir mensajes
    Escribir <expresion_l> , <expresion_2> , ... , <expresion_N>;
```

Ejemplo:

```
    Escribir nombre, " ", apellidos, " tiene ", edad, "años.";  
```

#### 5.2. Impresión sin salto de línea

En PSeInt pueden usarse las palabras reservadas `Sin Saltar` para imprimir un mensaje y evitar el salto de línea con la siguiente sintaxis general:

```
    // Opción 1:
    Escribir Sin Saltar <exprl> , ... , <exprN>;

    // OPción 2:
    Escribir <exprl> , ... , <exprN> Sin Saltar;
```

Ejemplo:

```
    Escribir Sin Saltar "Nombre? ";
```

#### 5.3. Borrar pantalla

En pseudocódigo PSeInt se puede usar la palabra reservada `Borrar Pantalla` o `Limpiar Pantalla` para limpiar la pantalla o terminal de salida y colocar el cursor en la esquina superior izquierda, con la siguiente sintaxis general:

```
    Borrar Pantalla;
```

#### 5.4. Salida y entrada de datos

Es frecuente utilizar las instrucciones de salida y de entrada de datos de manera simultánea para la captura de datos eficaz, como en el siguiente ejemplo:

```
    // Declaración de variables
    Definir nombre, apellidos Como Cadenas;
    Definir edad Como Entero;

    // Leer o inicializar las variables, una por una
    Escribir "Introduce el nombre";
    Leer nombre;

    Escribir "Introduce los apellidos";
    Leer apellidos;

    // Otra posibilidad de entrada de datos, varios a la vez, es la siguiente:
    Escribir "Introduce el nombre y apellidos";
    Leer nombre, apellidos;

    // Otra posibilidad de entrada es:
    Escribir "Introduce el nombre y apellidos";
    Leer nombre, apellidos;

    Escribir "Introduce la edad de ",nombre, " ",apellidos;  
    Leer edad;

    // Otra posibilidad es:
    Leer nombre, apellidos, edad;

    // Salida
    Escribir nombre, " ", apellidos, " tiene ", edad, "años.";  
```

### 6. Procesamiento de datos

El *almacenamiento de datos* es otra función importante de la computadora, que ocurre cuando se almacenan los datos en las variables y las constantes, sin embargo, en la estructura de un algoritmo el almacenamiento es una función primaria que posibilita el *procesamiento de datos*, que es la implantación de los algoritmos y, por lo mismo, es la función de la computadora que tiene más variedad y versatilidad.

A continuación se exponen las operaciones que están implantadas en pseudocódigo PSeInt.

#### 6.1. Expresiones

Las expresiones se elaboran combinando las variables y los operadores con una sintaxis estricta.

El pseudolenguaje PSeInt tiene operadores de varios tipos: relacionales, lógicos y algebráicos.

Los *operadores relacionales* permiten comparar dos valores o variables numéricas o alfanuméricas y el resultado es un valor lógico, según la siguiente tabla:

Tabla 1. Operadores relacionales en pseudocódigo PSeInt
| Operador |    Significado    |    Ejemplo      | Resultado            |
|:--------:|:-----------------:|:---------------:|:--------------------:|
|    \>    |     Mayor que     |     3 \> 2      | VERDADERO            |
|    \<    |     Menor que     | 'ABC' \< 'abc'  | VERDADERO            |
|    =     |     Igual que     |     4 = 3       |   FALSO              |
|   \<=    | Menor o igual que |  'a' \<= 'b'    | VERDADERO            |
|   \>=    | Mayor o igual que |    4 \>= 5      |   FALSO              |
|   \<\>   |   Distinto que    |  'a' \<\> 'b'   | VERDADERO            |

Los *`operadores lógicos`* permiten hacer operaciones lógicas, es decir, relacionar variables lógicas son los siguientes y se puede usar el símbolo o la palabra y el resultado es evaluado según las tablas de verdad para cada operación:

Tabla 2. Operadores lógicos en pseudocódigo PSeInt
| Operador      | Significado   | Ejemplo       | Resultado             |
|:-------------:|:-------------:|:-------------:|:---------------------:|
| &             | Conjunción    | A & B         | V & V -\> V ERDADERO  |
| Y             |               | A Y B         | V & F -\> FALSO       |
|               |               |               | F & V -\> FALSO       |
|               |               |               | F & F -\> FALSO       |
| \|            | Disyunción    | A \| B        | V \| V -\> V ERDADERO |
| O             |               | A O B         | V \| F -\> V ERDADERO |
|               |               |               | F \| V -\> V ERDADERO |
|               |               |               | F \| F -\> FALSO      |
| \~ NO         | Negación      | \~A NO A      | \~F -\> V ERDADERO    |
|               |               |               | \~V -\> FALSO         |

Los operadores algebraicos permiten realizar las operaciones algebraicas básicas:

Tabla 3. Operadores algebraicos en pseudocódigo PSeInt
| Operador      | Significado                   | Ejemplo                       |
|:-------------:|:-----------------------------:|:-----------------------------:|
| \+            | Suma                          | total \<- cant1 + cant2       |
| \-            | Resta                         | total \<- cant1 - cant2       |
| \*            | Multiplicación                | area \<- base \* altura       |
| /             | División                      | porc \<- 100 \* parte / total |
| \^            | Potenciación                  | sup \<- 3.41 \* radio \^ 2    |
| \%            | Módulo                        | resto \<- num % div           |
| MOD           | (resto de la división entera) | resto \<- num MOD div         |

#### 6.2. Funciones interconstruidas

Todos los lenguajes de programación tienen implantadas algunas funciones básicas con distintos mecanismos como librerías, módulos, paquetes o cualquier otro nombre.

Las funciones en pseudocódigo PSeInt se utilizan en cualquier expresión. A continuación se listan las funciones disponibles para datos *Numericos* y alfanuméricos o tipo *Cadena*:

Tabla 4. Funciones en pseudocódigo PSeInt
| Función             | Significado                                            |
|:-------------------:|:------------------------------------------------------:|
| ABS(X)              | Devuelve el valor absoluto de X                        |
| TRUNC(X)            | Devuelve la parte entera de X                          |
| REDON(X)            | Devuelve el entero más cercano a X                     |
| RC(X) RAIZ(X)       | Devuelve la raíz cuadrada de X                         |
| SEN(X)              | Devuelve el seno de X                                  |
| COS(X)              | Devuelve el coseno de X                                |
| TAN(X)              | Devuelve la tangente de X                              |
| ASEN(X)             | Devuelve el arcoseno de X                              |
| ACOS(X)             | Devuelve el arcocoseno de X                            |
| ATAN(X)             | Devuelve el arcotangente de X                          |
| LN(X)               | Devuelve el logaritmo natural de X                     |
| EXP(X)              | Devuelve la función exponencial de X                   |
| AZAR(X)             | Devuelve el entero aleatorio en el rango [0,X-1]       |
| ALEATORIO(A,B)      | Devuelve el entero aleatorio en el rango [A,B]         |
| LONGITUD(S)         | Devuelve la cantidad de caracteres de la cadena S      |
| SUBCADENA(S,X,Y)    | Devuelve una cadena que consiste en la parte de la cadena S que va desde la posición X hasta la posición Y, incluyendo ambos extremos. La primer letra será la 0 o la 1 de acuerdo al perfil del lenguaje utilizado. |
| CONCATENAR(S1,S2)   | Devuelve una cadena que resulta de unir las cadenas S1 y S2|
| CONVERTIRANUMERO(X) | Devuelve el valor numérico de la cadena de caracteres que contiene un número|
| CONVERTIRATEXTO(S)  | Devuelve la cadena de una variable numérica con la representación como cadena de caracteres de dicho real |
| MAYUSCULAS(S)       | Devuelve una copia de la cadena S con todos sus caracteres en mayúsculas               | MINUSCULAS(S)       | Devuelve la cadena S con todos sus caracteres en minúsculas |

#### 6.3. Control del flujo de control

El *flujo de control* es el orden en el que se ejecutan las instrucciones de un programa, donde las propias instrucciones son las que lo controlan. En el flujo natural de un programa, las instrucciones siempre se ejecutan secuencialmente, una detrás de otra, en orden de aparición, de izquierda a derecha y de arriba a abajo, a menor que el flujo de control se modificado por *instrucciones de control*.

##### 6.3.1. Control alternativo

Una instrucción de *control alternativo* permite modificar el flujo de control de un programa eligiendo las instrucciones a ejecutar de entre varias posibilidades: doble, simple y múltiple.

En primer lugar, en pseudocódigo PSeInt se tiene la instrucción de ***control alternativo simple*** que permite la ejecución de *un bloque de instrucciones* siempre y cuando la `<expresión_lógica>` resulte evaluada como VERDADERA. Si la `<expresión_lógica>` es FALSA, continúa con la siguiente instrucción, fuera de la estructura.

La instrucción de *control alternativo simple* 
```
    Si ... Entonces 
        ... 
    FinSi
``` 

En PSeInt tiene la siguiente sintaxis general:

```
    // Control alternativo simple
    Si \<expresión_lógica\> Entonces
        // Se ejecuta si \<expresión_lógica\> es VERDADERA
        \<bloque_de_instrucciones_1\>
    FinSi
    \<siguiente_instruccion\>
```

Ejemplo:

```
    Si (nota >= 6) Entonces
      Escribir "APROBADO";
    FinSi
    // Siguiente instrucción
```

En segundo lugar, la instrucción de ***control alternativo doble*** permite evaluar una condición mediante una `<expresión_lógica>` para elegir alternativamente un bloque de instrucciones a ejecutar, entre dos opciones. Si la condición evaluada en la `<expresión_lógica>` es VERDADERA, se ejecuta el `<bloque_de_instrucciones_1>` y si la `<expresión_lógica>` es FALSA, se ejecuta el `<bloque_de_instrucciones_2>`.

En pseudocódigo PSeInt, la instrucción de control alternativo doble `Si ... Entonces ... SiNo ... FinSi` tiene la siguiente sintaxis general:

```
    // Control alternativo doble
    Si <expresión_lógica> Entonces
        // Se ejecuta si <expresión_lógica> es VERDADERA
        <bloque_de_instrucciones_1>
    SiNo
        // Se ejecuta si <expresión_lógica> es FALSA
        <bloque_de_instrucciones_2>
    FinSi
```

Ejemplo:

```
    Si (nota >= 6) Entonces
      Escribir "APROBADO";
    SiNo
      Escribir "NO APROBADO";
    FinSi
```

En tercero y último lugar, la instrucción de ***control alternativo múltiple*** permite evaluar una condición mediante una `<expresión>` para elegir alternativamente un bloque de instrucciones a ejecutar, entre múltiples opciones. El resultado de evaluar la `<expresión>` debe ser un valor finito y ordenado, es decir, `Entero`, `Logico`, `Caracter`, enumerado o rango.

En pseudocódigo PSeInt, se puede escribir una instrucción de *control alternativo múltiple* 

```
    Segun ... 
    ...
    FinSegun
```

Si la <expresión> evaluada en la `<expresión_lógica>` es VERDADERO, se ejecuta el `<bloque_de_instrucciones_1>`, pero si la `<expresión_lógica>` es FALSO, se ejecuta el `<bloque_de_instrucciones_2>`, mediante la siguiente sintaxis:

```
    // Control alternativo múltiple
    Segun <expresión> Hacer

      <lista_de_valores_1>:
          // Ejecutar este bloque 
          // si la <expresión> evaluada ESTÁ en la <lista_de_valores_1> 
          <bloque_de_instrucciones_1>
          
      <lista_de_valores_2>:
          <bloque_de_instrucciones_2>
      ...
      
      <lista_de_valores_n>:
          <bloque_de_instrucciones_n>

      [ De Otro Modo: 
          // Ejecutar este bloque 
          // si la <expresión> evaluada NO ESTÁ 
          // en alguna de las <listas_de_valores_previas> 
          <bloque_de_instrucciones_n+1> ]
    FinSegun
```

Ejemplo:
```
    // Menú
            
    // mostrar menu
    Escribir "Menú de recomendaciones";
    Escribir "   1. Literatura";
    Escribir "   2. Cine";
    Escribir "   3. Salir";

    // ingresar una opcion
    Escribir "Elija una opción (1-3): ";
    Leer elecion;
            
    // procesar esa opción
    Segun elecion Hacer
        1:
          Escribir "Lecturas recomendables:";
            Escribir " El Principito";
        2:
          Escribir "Películas recomendables:";
            Escribir "Matrix (1999)";
        3:
          Escribir "Gracias. Salir!";
        De otro modo:
          Escribir "Opción no válida";
    FinSegun
```

##### 6.3.2. Control repetitivo

Una instrucción de ***control repetitivo***, también conocida como bucle, ciclo o lazo, permite ejecutar un bloque de instrucciones, ninguna, una o varias veces, dependiendo de la evaluación de las condición. Existen tres tipos de instrucciones repetitivas: `Mientras`, `Repetir` (Hacer) y `Para`.

En primer lugar, el *ciclo `Mientras` evalúa la `<expresión_lógica>` y, si resulta `VERDADERO`, entonces ejecuta el ciclo y si la `<expresión_lógica>` es FALSA, el ciclo `Mientras` no se ejecuta y el control del flujo continúa con la siguiente instrucción fuera del ciclo `Mientras`. Por lo tanto, las variables involucradas en la `<expresión_lógica>` deben haber sido inicializadas o actualizadas previamente su evaluación.

En pseudocódigo PSeInt, una instrucción repetitiva `Mientras ... FinMientras` se escribe bajo la siguiente sintaxis general:

```
    // Ciclo Mientras

    // Las variables involucradas en la <expresión_lógica> 
    // deben haber sido inicializadas antes de ser evaluada  

    Mientras <expresión_lógica> Hacer
        // Ejecuta el ciclo si la <expresión_lógica> es VERDADERA
        <bloque_de_instrucciones>
    FinMientras
    <siguiente_instruccion_fuera_del_ciclo>
```

Ejemplo:

```
    // Inicialización de las variables involucradas en el ciclo Mientras
    Escribir "Adivine el numero (de 1 a 100):";
    Leer num_ingresado;
    intentos <- 10;
    num_secreto <- azar(100)+1;

    // La expresión lógica es una conjunción (&) que evalua dos comparaciones:
    // Si el num_secreto es distinto del num_ingresado: (num_secreto <> num_ingresado)
    // el todavía quedan intentos, es decir, si el numero de intentos es mayor a 1: (intentos > 1)
    // el ciclo se ejecutará

    Mientras ((num_secreto <> num_ingresado) & (intentos > 1)) Hacer
        Si num_secreto > num_ingresado Entonces
            Escribir "Muy bajo";
        SiNo 
            Escribir "Muy alto";
        FinSi
            
        // Actualiza el valor de intentos
        intentos <- intentos - 1;
        Escribir "Le quedan ",intentos," intentos:";
            
        // Actualiza el valor de num_ingresado
        Leer num_ingresado;
    FinMientras
```

En segundo lugar, el *ciclo `Repetir`* se ejecuta por lo menos una vez y varias veces, mientras la `<expresión_lógica>` sea FALSA. Por lo tanto, si al final del ciclo `Repetir`, la `<expresión_lógica>` se evalúa como VERDADERA, el ciclo termina y el control del flujo continúa con la siguiente instrucción fuera del ciclo `Repetir`.

En pseudocódigo PSeInt, una instrucción repetitiva `Repetir` se escribe bajo la siguiente sintaxis general:

```
    // Ciclo Repetir
    Repetir
       <bloque_de_instrucciones>
    Hasta Que <expresión_lógica>
    <siguiente_instruccion_fuera_del_ciclo>
```

En tercer y último lugar, el *ciclo `Para`* es una instrucción repetitiva con un número conocido de repeticiones, que controla mediante una variable acumuladora o `<contador>` de ciclos o iteraciones, desde un `<valor_inicial>`, hasta un `<valor final>`. Al final del ciclo, el `<contador>` se incrementa, por defecto, con un `<incremento>` de uno en uno o distinto. Cuando finaliza una iteración, el valor del `<contador>` se actualiza sumándole el `<incremento>`. El ciclo `Para` termina cuando el `<contador>` supera el <valor_final>. El ciclo `Para` es pertinente para operaciones secuenciales con un número de repeticiones conocido, como recorrer una estructura de datos de manera secuencial para leer, inicializar o actualizar los valores de un arreglo, para ordenamientos, etc.

En pseudocódigo PSeInt, una instrucción repetitiva `Para` se puede escribir con la siguiente sintaxis general:

```
    // Ciclo Para
    Para <contador> <- <valor_inicial> Hasta <valor_final> [ Con Paso <incremento> ] Hacer
       <bloque_de_instrucciones>
    FinPara
    <siguiente_instruccion_fuera_del_ciclo>

    // Ejemplo
    // Para poder ejecutar correctamente este ejemplo debe tener
    // habilitada la sintaxis flexible en su perfil de lenguaje

    Proceso arreglo 

        // Declara las variables
        Definir a,i,elemento Como Enteros;
        
        // Declara una variable como un arreglo de 10 elementos
        Dimension a[10];
        
        
        // Primera sintaxis del ciclo Para  
        
        // Recorre los 10 elementos y asigna enteros aleatorios
        Para cada elemento de a Hacer
            // <elemento> toma el contenido de cada posicion del arreglo
            // e inicializa cada elemento del arreglo
            elemento <- azar(100);
        FinPara
        Escribir "Los elementos del arreglo son:";
        
        
        // Segunda sintaxis del ciclo Para
        
        // Recorre los 10 elementos utilizando subindices y los muestra en pantalla
        // Comienza a contar en 0 y termina en 9 (n-1)
        Para i desde 0 hasta 9 Hacer
            escribir "Posición " i ": " A[i];
        FinPara
        Escribir ""; // deja una linea en blanco
        
        // Segunda sintaxis del ciclo Para, con incremento distinto a 1
        
        // Recorre los 10 elementos utilizando subindices y los muestra en pantalla
        // pero de 2 en 2
        // Comienza a contar en 0 y termina en 9 (n-1)
        Para i desde 0 hasta 9 Con Paso 2 Hacer
            escribir "Posición " i ": " A[i];
        FinPara
        Escribir ""; // deja una linea en blanco
        
        Escribir "En orden inverso:";
        
        
        // Segunda sintaxis del ciclo Para
        
        // recorre los 10 elementos en orden inverso y los muestra en una misma linea
        para i desde 9 hasta 0 Hacer
            escribir sin bajar A[i] " ";
        FinPara
        
    FinProceso
```

Ejemplo integral, `OrdenaLista.psc` de la Ayuda de PseInt:

```
OrdenaLista.psc
//   Se ingresa una lista de nombres (la lista termina
// cuando se ingresa un nombre en blanco) no permitiendo
// ingresar repetidos y luego se ordena y muestra

Proceso OrdenaLista
	
	Definir nombre,lista,aux Como Cadenas;
	Definir se_repite Como Logico;
	Definir cant,i,j,pos_menor Como Enteros;
	Dimension lista[200];
	
	Escribir "Ingrese los nombres (enter en blanco para terminar):";
	
	// leer la lista
	cant <- 0;
	Leer nombre;
	Mientras nombre <> "" Hacer
		lista[cant] <- nombre;
		cant <- cant + 1;
		Repetir // leer un nombre y ver que no este ya en la lista
			Leer nombre;
			se_repite <- Falso;
			Para i <- 0 Hasta cant - 1 Hacer
				Si nombre = lista[i] Entonces
					se_repite <- Verdadero;
				FinSi
			FinPara
		Hasta Que ~ se_repite
	FinMientras
	
	// ordenar
	Para i <- 0 Hasta cant - 2 Hacer
		// busca el menor entre i y cant
		pos_menor <- i;
		Para j <- i + 1 Hasta cant - 1 Hacer
			Si lista[j]<lista[pos_menor] Entonces
				pos_menor <- j;
			FinSi
		FinPara
		// intercambia el que estaba en i con el menor que encontro
		aux <- lista[i];
		lista[i] <- lista[pos_menor];
		lista[pos_menor] <- aux;
	FinPara	
	
	// mostrar como queda la lista
	Escribir "La lista ordenada es:";
	Para i <- 0 Hasta cant - 1 Hacer
		Escribir "   ", lista[i];
	FinPara
	
FinProceso
```

## Referencias 
[^1]: PseInt. <https://pseint.sourceforge.net/>
[^2]: Online historical encyclopaedia of programming languages. <https://hopl.info/>
[^3]: PseInt. <https://pseint.sourceforge.net/>
[^4]: Ibañez Reyes, K. D., Lemus Véliz, G. M., Mcknight Cuyuche, K. P., & Villareal Santos, D. J. (s.f.). Historia de Pseint. Blog. Consultado en <https://sites.google.com/site/portafolio4bd8/historia-de-pseint>.
