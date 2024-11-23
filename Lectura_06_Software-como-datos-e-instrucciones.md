## Lectura 6. El Software como Datos e Instrucciones[^1]

prof. dr. Jesús Zavala Ruiz[^2]

---

### Introducción

En un mundo cada vez más impulsado por la tecnología, comprender el software como un ente que es, a la vez, datos e instrucciones resulta esencial. Los datos, en su estado más puro, son la representación de la información, mientras que las instrucciones, cuidadosamente elaboradas en programas de computadora, transforman esos datos en información, en la forma de sistemas de información que resuelven problemas reales. Este ensayo explora cómo se representan, almacenan en distintos formatos y estructuras. También, se abordan los principios que están detrás de codificación y las tecnologías que crean las aplicaciones que  procesan los datos, mediante lenguajes de programación. Se ilustran los dos procesos fundamentales que llevan a la ejecución del software: la interpretación y la compilación del código fuente, para que revelen sus secretos. Al final, se abordan los elementos básicos para integrar un ecosistema básico de desarrollo para practicar la codificación y ejecución de scripts en Python y R, como base para una práctica complementaria.


### 1. Tipos de datos y codificación

Un **dato** es un valor crudo, *la representación de un hecho aislado* que describe una característica o una observación sin contexto de un objeto de interés, como un número, una palabra o una medición específica (por ejemplo, "25", "rojo" o "12/11/2024"). Por sí solo, un dato no proporciona significado. La **información**, en cambio, es el resultado de dotar de sentido al dato al darl contexto y significado para el usuario. Por ejemplo, al asociar "25" con "grados Celsius", obtenemos información que indica la medición de una temperatura; el "rojo" de un semáforo está asociado al significado de "alto" al tránsito y el dato "12/11/2024" puede ser la fecha de nacimiento de una persona. Así, comprobamos que los representan significados o información para los ususarios. Por lo tanto, los datos son la materia prima de la información. Dicho de otra manera, la información es un dato contextualizado o con significado. Los datos deben ser organizados y procesados para transformarse en información útil, que puede ser utilizada para tomar decisiones, resolver problemas o adquirir conocimientos.

Un **tipo de dato** define su naturaleza y cómo puede ser manipulado dentro de un algoritmo o de un sistema de información. Los **tipos de datos básicos** incluyen **números enteros** y los **números reales** o decimales (que sirven para realizar operaciones matemáticas), **cadenas de texto** (o datos alfanuméricos) y **caracteres** (cadenas de tamaño 1) para describir características, datos **lógicos** (para representar el valor `verdadero` o `falso`)) y tipos especiales de datos como el **dato nulo** (que sirve para representar datos faltantes o perdidos). Los tipos de datos determinan qué operaciones se pueden realizar con ellos, cómo se almacenan en la memoria y qué significado tienen cuando se capturan o se presentan al usuario. 

Para que la computadora maneje los datos éstos deben codificarse. La **codificación de datos** se refiere a la forma en que los datos se representan digitalmente para ser almacenados o procesados por la computadora. *Todos los tipos de datos se representan internamente en binario*, es decir, como combinaciones de ceros y unos. Esta representación es clave para que el hardware pueda procesar cualquier tipo de dato. 

**1.1. Números enteros**

Los **números enteros** (*integer*), que sirven para **contar**, se codifican directamente en sistema binario. Un número como 5, en base decimal, se representa como `0101` en binario, utilizando 4 bits y un número 255 se representa como `11111111`, es decir, 8 bits, en binario. Para los números negativos, se emplea una técnica llamada complemento a dos, que ajusta los valores binarios para permitir operaciones matemáticas con signos.

**1.2. Números reales**

En el caso de los **números reales** (*float point*), que sirven para representar **mediciones** de distintas magnitudes, su representación es más compleja. Siguiendo el estándar IEEE 754, ese formato divide los bits en tres partes: el *signo* (positivo o negativo), el *exponente* (que ajusta la escala del número) y la *mantisa* (que almacena los dígitos significativos). Así, un número como 2.5 se descompone y codifica en un formato binario preciso: *signo*: `0`, *exponente*: `10000000` y *mantisa*: `01000000000000000000000`, es decir, la representación binaria completa es: `0 10000000 01000000000000000000000` (32 bits). La precisión de los números reales es dependiente de la arquitectura de hardware: 8, 16, 32 o 64 bits. 

Las *operaciones básicas* sobre datos numéricos son matemáticas y estadísticas.

**1.3. Cadenas de texto**

En cuanto a las **cadenas de texto** (*string*), también llamados **datos alfanuméricos**, que sirven para representar la *descripción de los atributos* de los objetos de interés, cada **carácter** individual se convierte a binario según sistemas de codificación como el **ASCII** (Acrónimo de *A*merican *S*tandard *C*ode for *I*nformation *I*nterchange) (que permite representar hasta 256 símbolos con un byte) o el **Unicode** (que permite representar caracteres más complejos, como un emoji, con uno a tres bytes), codificados como **UTF-8** (*8-bit Unicode Transformation Format*). Lo mismo aplica para una cadena de tamaño unitario se llama *carácter* o *símbolo alfanumérico*.

Por ejemplo, la palabra **"Hola"** se codifica carácter por carácter, en **ASCII**, como **H** (`01001000`), **o** (`01101111`), **l** (`01101100`) y **a** (`01100001`) y la palabra completa **"Hola"** en binario (ASCII) sería `01001000 01101111 01101100 01100001`. Para este proceso se usa la llamada *Tabla ASCII*. Y, en código **Unicode**, el emoji **"😊"** (cara sonriente con ojos felices) se codifica con 4 bytes como `11110000 10011111 10011000 10101010`, que corresponde al código `U+1F60A` (en hexadecimal). Esto permite que Unicode maneje una gama mucho más amplia de caracteres, desde letras de alfabetos internacionales o antiguos, hasta símbolos complejos como los emojis.

Los datos alfanuméricos son los más abundantes y tienen una gran versatilidad de uso, desde la comunicación con la computadora, hasta la construcción dinámica de mensajes y el formateo de reportes. 

Las *operaciones básicas* que se realizan con datos alfanuméricos son: concatenación, extracción de subcadenas, reemplazo, búsqueda, comparación, división,  formateo, eliminación de espacios, longitud y verificación de patrones.

**1.4. Datos lógicos**

Para los **datos lógicos** (también llamados *booleanos* o *boolean*), como `True` (verdadero) y `False` (falso), la codificación es directa: `1` y `0`, respectivamente. Este tipo de dato sirve para representar comparaciones entre valores y tomar decisiones en el flujo de procesamiento. 

Las *operaciones básicas* con datos lógicos son: unión (`Y` o `AND`), disyunción (`O` u `OR`) y negación (`NO` o `NOT`).   

**1.5. Dato nulo** 

Por último, el tipo especial **nulo**, que sirve para representar un dato perdido o inexistente, no tiene un valor binario directo. En su lugar, el sistema usa punteros que indican un espacio vacío o un objeto especial predefinido que representa "sin valor". Es decir, la computadora sabe que un valor es **null** (nulo) (ausencia de un valor) mediante representaciones específicas que dependen del lenguaje de programación y del sistema operativo subyacente. Por lo general, se usa un valor `0` en 8 a 64 bits, dependiendo de la arquitectura de la computadora.

**1.6. Datos especiales**

De manera análoga como se codifican los datos básicos, se procede igual con ciertos datos especiales como los **sonidos** y los **colores**, que permiten codificar el audio, las imágenes y el video de archivos multimedia. Los datos básicos multimedia también tiene operaciones básicas mediante software especializado. 

El tipo de dato de **fecha y hora** (*datetime*) es otro tipo de datos especial que se codifica de acuerdo con un estándar o sistema que permite representar momentos en el tiempo de manera precisa y eficiente. Uno de los métodos más comunes es mediante una marca de tiempo (*timestamp*), que almacena el número de segundos transcurridos desde un punto de referencia llamado **Epoch** (generalmente el 1 de enero de 1970 a las 00:00:00 UTC). El *UTC* (*Coordinated Universal Time*, *Tiempo Universal Coordinado*) es el estándar de tiempo global utilizado como referencia para sincronizar relojes y medir el tiempo en todo el mundo.

La fecha es un caso típico de un **tipo de dato complejo** porque tiene *tres componentes*: fecha, hora y marca de tiempo. Los componentes de una **fecha** (año, mes, día) pueden representarse en números enteros; por ejemplo, el 18 de noviembre de  2024, se codifica en binario como año (`11111100100`), mes (`1011`), día (`10010`). Hay funciones de cómputo que calculan la fecha correcta, considerando los años bisiestos. La **hora** tiene también tres componentes: hora, minuto y segundo) que también se representan como enteros; por ejemplo, las 14:30:45 se representan como `1110`, `11110` y `101101`. Y, la **marca de tiempo** o **timestamp** combina la fecha y la hora en un único número que representa los segundos desde el Epoch. Este número se almacena como un *entero en binario*; por ejemplo, la fecha y hora `2024-11-18 14:30:45` tiene una marca de tiempo timestamp (asumiendo UTC) de 1,731'940,245 segundos desde el Epoch, que en binario es: `1100110110110100001001010101`. 

Este tipo de codificación permite realizar cálculos rápidos, como encontrar la diferencia entre dos momentos o convertir entre zonas horarias. La fecha y la hora es un tipo de dato muy especial, tanto que está en los metadatos de todos los archivos.

La fecha y hora se usa para crear *bitácoras* o *log* de eventos en todos los sistemas operativos y en los sistemas de información, para marcar el momento de la realización de las operaciones, detectar errores y otros múltiples usos. Por eso, los sistemas operativos deben estar sincronizados con la hora exacta. Para ello, se usa el protocolo *NTP*, que es el estándar para sincronizar el tiempo en sistemas informáticos, asegurando precisión y consistencia. Implementarlo es esencial en entornos donde el tiempo exacto es crucial, como en transacciones financieras, comunicaciones y redes distribuidas. 


### 2. Estructuras de datos

Los datos individuales, como números, cadenas o valores lógicos, son la base de cualquier algoritmo o sistema informático. Sin embargo, cuando necesitamos manejar grandes cantidades de información o datos interrelacionados, es necesario organizarlos de manera eficiente. Aquí es donde entran las estructuras de datos, que permiten agrupar, almacenar y manipular múltiples datos de forma organizada. Estas estructuras no solo optimizan el acceso y la gestión de la información, sino que también sirven como puente para operaciones más complejas en programación.

Formalmente, las **estructuras de datos** son herramientas fundamentales diseñadas para almacenar, organizar y manipular datos de manera eficiente. Estas estructuras no solo optimizan el rendimiento y la escalabilidad de los programas de cómputo, sino que también facilitan la resolución de problemas complejos y la implementación de complejos sistemas de información como los sistemas empresariales. Hay distintos **tipos de estructuras de datos**: estructuras lineales, jeráquicas, tabulares y avanzadas.


**2.1. Estructuras lineales**

Las estructuras lineales organizan los datos de forma secuencial. Entre estas se encuentran los vectores, las listas, las pilas, las colas y las matrices, con múltiples aplicaciones. Las estructuras de datos se pueden considerar como **datos complejos** compuestos de **datos simples**.

Los **vectores** son una colecciones de datos homogéneos (del mismo tipo de dato) organizada en una dimensión, donde cada elemento tiene una posición única accesible mediante un índice. Los vectores se utilizan en hojas de cálculo como Excel para representar columnas de datos, como los valores diarios de acciones. Los vectores pueden almacenar cualquiera de los datos básicos, pero sólo de un tipo, por ejemplo, vectores de enteros o vectores de cadenas. Por ejemplo, un vector puede almacenar todos los códigos postales alfanuméricos de una ciudad y otro vector de números reales puede almacenar las mediciones de temperaturas de una estación meteorológica.

Las **listas** son colecciones ordenadas que pueden contener datos de diferentes tipos y permiten el acceso mediante índices. Por ejemplo, las listas se utilizan para organizar tareas, en actividades pendientes y completadas. Dos ejemplos prácticos son la codificación de los datos de un contacto como: nombre, apellidos, edad, domicilio, teléfono y correo electrónico o el mismo domicilio que tiene una estructura predeterminada.   

Las **pilas** son estructuras que operan bajo el principio LIFO (*L*ast *I*n, *F*irst *O*ut: último en entrar, primero en salir) que son útiles para gestionar elementos en orden inverso; por ejemplo, para implementar la función "deshacer" en los editores de texto o gráficos.

Las **colas** son estructuras que siguen el principio FIFO (*F*irt *I*nt, *F*irts *O*ut, primero en entrar, primero en salir), que se utilizan para procesar elementos en orden de llegada. Por ejemplo, se usan para administran las colas de impresión en oficinas, enviando los trabajos en el orden en que llegaron.

Las **matrices** son vectores n-dimensionales que, para el caso de dos dimensiones, organiza los datos en filas y columnas. Por ejemplo, las matrices se usan para representar las imágenes, donde cada píxel se representa como un elemento de una matriz, con colores o intensidades.


**2.2. Estructuras jerárquicas**

Los **árboles** son estructuras de *datos* donde cada nodo tiene un padre y puede tener múltiples hijos, organizados de forma jerárquica. Estas estructuras se usan, por ejemplo, para representan los sistemas de archivos, donde las carpetas son nodos que contienen subcarpetas y archivos.

Los **grafos** son conjuntos de nodos conectados mediante aristas que pueden tener direcciones o ser bidireccionales, con mútiples aplicaciones. Por ejemplo, los grafos se usan para modelar redes de todo tipo, las redes sociales, donde los nodos son usuarios y las aristas son sus conexiones o las redes de vialidad que definen las rutas de tránsito en aplicaciones como Google Maps o Waze.

**2.3. Estructuras tabulares y avanzadas**

Los **dataframes** y las **tablas** son estructuras tabulares bidimensionales que combinan etiquetas para filas y columnas, con soporte para tipos de datos heterogéneos, es decir, las filas son vectores y las filas son listas. Los dataframes se utilizan por analistas financieros para consolidar y analizar información como ingresos y gastos por trimestre o realizar análisis estadísticos. Comunmente, los dataframes se graban como archivos delimitados por comas (`.csv`) para su intercambio.

En cambio, las **tablas** se usan para crear las enormes y complejas *bases de datos relacionales* que utilizan los sistemas empresariales (como los ERP y los CRM) en las empresas. Los ERP (*Planificación de Recursos Empresariales*) son sistemas de software que gestionan y automatizan los procesos centrales de una empresa, como contabilidad, finanzas, recursos humanos, producción, inventario y cadena de suministro. Y los CRM (*Gestión de las Relaciones con los Clientes*) son sistemas de software que ayudan a las empresas a gestionar las interacciones con sus clientes, desde la prospección hasta la postventa.

Las **tablas hash** son estructuras que almacenan datos en pares clave-valor, permitiendo búsquedas rápidas. Las tablas hash se utilizan en los diccionarios de idiomas digitales para buscar palabras y sus definiciones rápidamente y en los buscadores web se usan para indexar las páginas web, según los términos codificados en cada una de ellas.

Como puede verse, comprender la existencia y uso de las estructuras de datos es esencial para cualquier profesional que busque optimizar procesos o resolver problemas de manera eficiente, especialmente en contextos donde el manejo y análisis de información es clave. Su correcta aplicación impacta directamente en la elección de algoritmos y en el desempeño general de las soluciones tecnológicas. Un administrador puede usar estos conocimientos para participar en las mejoras tecnológicas en empresas y el gobierno.


### 3. Archivos 

Hoy en día, se emplean miles de **tipos de archivos**, cada uno adaptado a necesidades específicas, desde la gestión de documentos hasta el diseño gráfico o la transmisión de datos, donde se codifican distintos tipos de datos básicos y estructuras de datos. A continuación, se presenta una panorámica de los distintos tipos de archivos, desde esta perspectiva.

**3.1. Documentos** 

Los **documentos** son arvchivos complejos, desde **archivos de texto** hasta **hojas de cálculo**, que son esenciales en los entornos laborales. Archivos como `.txt` permiten manejar texto sin formato, mientras que archivos `.docx` (Microsoft Word) y `.pdf` (documentos portátiles) son fundamentales para informes y presentaciones. Por otro lado, los archivos `.xlsx` (Microsoft Excel) y `.csv` (datos separados por comas) son ideales para el análisis de datos y la gestión administrativa.

**3.2. Multimedia** 

Los **formatos multimedia** son cruciales para la comunicación visual y auditiva. Las imágenes `.jpg` y `.png` son ampliamente utilizadas en fotografía y diseño gráfico, mientras que `.svg` permite manejar gráficos vectoriales escalables, esenciales en el diseño web. En el ámbito del audio, `.mp3` y `.wav` son estándares para compresión y calidad profesional, respectivamente. Para video, formatos como `.mp4` y `.mkv` se destacan por su calidad y capacidad de integrar pistas de audio y subtítulos. 

**3.3. Bases de datos**

En el **manejo de datos**, formatos como `.json` y `.xml` facilitan el intercambio de información estructurada y los archivos `.sql`, son esenciales para las bases de datos. Los archivos `.sav` (SPSS), `.sas`  (SAS) o `.RData` (R) son esenciales para almacenar bases de datos para análisis estadísticos.

**3.4. Diseño y manufactura**

En **ingeniería, arquitectura y manufactura**, archivos como `.dwg` (AutoCAD) y `.stl` (modelos 3D) son estándar para planos y prototipos. Estos formatos permiten la colaboración eficiente y la implementación de proyectos complejos.

**3.5. Software**

Para la **creación o desarrollo de software**, hay archivos con scripts como `.py` (Python), `.c` (Lenguaje C), `.js` (JavaScript) y `.html` y `.css` (páginas web) son herramientas fundamentales para programadores y diseñadores web.

**3.6. Otros usos** 

Para usos especiales como  **almacenamiento y distribución**, los formatos como `.zip` y `.tar.gz` son comunes, mientras que los archivos `.log` son esenciales para las bitácoras en sistemas y las imágenes de discos `.iso` son vitales para la distribución de software y la instalación de sistemas operativos, por ejemplo.

En general, los datos se codifican en archivos, en formato de **texto plano** o **en binario**, con  **editores** que permiten crear, abrir, modificar y guardar los distintos tipos de archivos. Para todos los tipos de archivos hay **editores**, por ejemplo, de audio, video, imágenes y documentos; pero también hay **lectores** y **reproductores** (*players*) que sólo muestran el contenido de los archivos en algún medio de salida. Y no faltan los **convertidores de archivos** que son aplicaciones que transforman tipos de archivos compatibles, según el tipo de datos que contengan. 

Es importante comprender que cada tipo de archivo tiene un propósito único y un rol clave en diversos sectores. Su conocimiento y manejo adecuado permiten optimizar procesos y mejorar la eficiencia en cualquier entorno profesional. 

### 4. Programación de computadoras y su aprendizaje

Hasta ahora, hemos explorado cómo el software puede representar los datos de una variedad de tipos y estructuras de datos, tales como enteros, reales, cadenas, datos lógicos y especiales, además de estructuras de datos como vectores, listas, registros, matrices, dataframes y tablas, cómo éstos se codifican en archivos. Para que estos conceptos se integren en una aplicación práctica, se utiliza el **software** en la forma de **instrucciones**. De aquí en delante exploraremos la forma en que se crean las órdenes que permiten que una computadora procese datos y realice tareas específicas.

De manera formal, se llama **programar** o **programación** al acto de *escribir instrucciones* en un lenguaje de programación que una computadora pueda entender y ejecutar. Hay que recordar que la computadora realiza cuatro funciones básicas: entrada, salida, almacenamiento y procesamiento de datos (ESAP) y todo lenguaje de programación implementa esas funciones. Además, considérese que *programar es una habilidad muy bien valorada*, sobre todo en aquellos profesionistas que no están ligados a la informática. De ahí que aprender a programar computadoras sea muy importante. 

Sin embargo, *aprender a programar es un viaje lleno de desafíos*, especialmente para los principiantes que se enfrentan, por primera vez, a algo completamente desconocido y misterioso. Hay dos aspectos a considerar: aprender el arte de programar y aprender a enfrentar la frustración ante los tropiezos en este camino.

Dominar **el arte de programar** comienza por emprender uno o ambos caminos: (1) aprender pseudocódigo (como PSeInt) o (2) aprender, por lo menos, un lenguaje de programación. El **pseudocódigo** es una *herramienta didáctica* para aprender los conceptos de programación o crear conceptualmente los algoritmos, en el idioma natural. Se pueden usar varias herramientas de spoyo, por ejemplo, el [PSeInt](https://pseint.sourceforge.net/) (*PSe*udocódigo *Int*erprete), es la mejor aplicación para los estudiantes de habla hispana. Para aquellos de ustedes que quieran seguir este camino, he desarrollado un tutorial, mismo que pueden consultar [aquí](https://github.com/jzavalar/Informatica/blob/main/Programacion-en-pseudocodigo.md). En cambio, el **lenguaje de programación** es la herramienta que permite crear las instrucciones de tal forma que la computadora resuelva problemas mediante el **manejo de datos**. Este camino es un viaje más desafiante, pero lleno de oportunidades para practicar la programación. Veamos cómo es posible hacer esto.

El *conjunto completo de instrucciones* que la computadora puede ejecutar, se llama **programa de computadora** para llevar a cabo una tarea específica, es decir, para implementar un algoritmo. Un **algoritmo** es un conjunto de instrucciones o pasos claramente definidos que se siguen para resolver un problema o realizar una tarea específica al procesar datos. Los algoritmos pueden ser simples o complejos y se aplican en muchos contextos, desde las matemáticas, hasta en actividades cotidianas de las empresas. 

Los programas de computadora se almacenan en archivos que contienen las instrucciones para la computadora y éstos tienen dos presentaciones de codificación: en *texto plano* y en *binario*. A esos archivos se les llama, genéricamente, código, un tema que vermos en la siguiente sección. 

En cambio, el desafío de **aprender a manejar los desafíos psicológicos** que implica resolver los errores de sintaxis y ejecución incomprensibles, que impiden continuar. Estos errores, a menudo acompañados de mensajes poco claros y muy técnicos, no ponen a prueba el conocimeinto del usuario, sino su paciencia y capacidad para manejar su frustración al no saber cómo resolverlos. Los principiantes carecen del conocimiento necesario para interpretar estos mensajes en inglés, un idioma que no dominan, y terminan atrapados en *ciclos de prueba y error* irresolubles. Hay que reconocer que esto no solo ralentiza su progreso, sino que también puede hacerlos sentir incompetentes, debilitando la autoconfianza en su capacidad para aprender programación. Aquí es donde herramientas basadas en inteligencia artificial pueden ser aliadas poderosas al ofrecer explicaciones claras y soluciones personalizadas, si se usan como un tutor personalizado.

La *frustración* del usuario se agrava por expectativas poco realistas, ya que muchos aprendices creen que la programación debería surgir de forma natural o ser más intuitiva. Cuando los errores comienzan a acumularse, la percepción de la programación como algo inalcanzable lleva a la desmotivación y, en la mayoría de los casos, al abandono total. Sin el apoyo de mentores o comunidades o principiantes desconfiados para preguntar, pueden sentirse aislados y atrapados. Sin embargo, la inteligencia artificial puede cambiar este panorama. 

Sistemas de inteligencia artificial como *ChatGPT*, *DeepAI* o *Claude* pueden *analizar errores, ofrecer posibles causas y guiar a los estudiantes paso a paso*, en el propio idioma del usuario y de manera interactiva, reduciendo significativamente la sensación de aislamiento y la curva de aprendizaje. Superar estas barreras con el apoyo de estas herramientas puede ser transformador porque *no hay otro camino más que aprender a prueba y error*. Esto hace que los errores no sean el final del camino, sino oportunidades para aprender, de una vez y para siempre, y mejorar progresivamente. Resolver un error fortalece la confianza y demuestra que la programación no se trata de evitar errores, sino de aprender a enfrentarlos, con resiliencia y mucha paciencia. Con el apoyo de la inteligencia artificial y entornos de aprendizaje amigables, los principiantes pueden encontrar en la programación una habilidad poderosa que no solo les permite resolver problemas, sino también motivante. Esta lectura es un principio para ello.


### 5. Del código fuente al código ejecutable

Volvamos a los aspectos técnicos. Formalmente, el **código** es la esencia de cualquier programa, compuesto por instrucciones escritas en *un lenguaje* que las computadoras pueden entender y ejecutar. Se trata de la materialización de un algoritmo en un formato procesable. Sin embargo, el código adopta distintas formas, a lo largo del *ciclo de producción de software*, desde su creación hasta su ejecución final.

El código base para crear un programa de computadora es el **código fuente**, ése que escribe una persona en su rol de programador o desarrollador. Ese código fuente, también llamado *programa* o *script* se guarda en un archivo de texto plano que luego se procesa mediante dos procesos: interpretación o compilación. En la **interpretación**, el código fuente se traduce y ejecuta, línea por línea, en tiempo real, de tal forma que el usuario puede observar el software en ejecución. En cambio, en la **compilación**, el código fuente se transforma en un archivo ejecutable que, después debe ejecutarse directamente. A continuación te explico un poco más a detalle ambos procesos. 

El **proceso de interpretación** es un enfoque dinámico y directo para ejecutar el código fuente, donde las instrucciones se traducen y ejecutan, línea por línea, en tiempo real, observándose los resultados. Este método utiliza un intérprete que actúa como intermediario entre el código del programador y el hardware de la computadora.

El **intérprete** toma el código fuente y lo analiza, una línea a la vez. Primero, *verifica la sintaxis* de cada instrucción. Si el intérprete detecta un *error*, como una palabra clave mal escrita o un paréntesis sin cerrar, detiene inmediatamente la ejecución y muestra un mensaje de error. Esto permite al programador investigar la soluciòn y corregirlo en tiempo real, lo que es una ventaja significativa durante el desarrollo. 

Luego, *traduce las instrucciones* a un formato intermedio, como **bytecode**, en el caso de Python. Este bytecode es una representación simplificada del código que el intérprete puede ejecutar rápidamente. Finalmente, el intérprete *maneja la ejecución del programa*, resolviendo variables, calculando resultados y controlando el flujo de ejecución según las instrucciones dadas.

Este enfoque es ideal para pruebas rápidas y prototipos, ya que permite modificar y ejecutar el código de inmediato. Sin embargo, puede ser más lento que la compilación, ya que cada instrucción debe traducirse en tiempo de ejecución. Aun así, su flexibilidad y simplicidad lo convierten en una opción popular para lenguajes de scripting como Python o R, aplicaciones web y análisis de datos.

En cambio, la **compilación** es un proceso de varias etapas que, mediante un software llamado **compilador** genera diferentes tipos de códigos intermedios, cada uno con un propósito específico. A continuación, te lo explico de forma sencilla y clara.

El **código fuente**, escrito por el programador, se proporciona como entrada al compilador. En la primera etapa, se realiza el **análisis léxico**, que descompone el código en partes más pequeñas llamadas **tokens** (palabras clave, identificadores, operadores, etc.). A continuación, el compilador lleva a cabo el **análisis sintáctico**, verificando que los tokens cumplan con las reglas gramaticales del lenguaje. Luego, realiza el **análisis semántico**, asegurándose de que el significado del código sea válido, por ejemplo, comprobando la compatibilidad de los tipos de datos.

Tras estas fases de análisis o **preprocesamiento**, el **ensamblador** del compilador genera un **código intermedio** llamado **código ensamblador** (archivo `.s`), que no está asociado directamente al hardware y que puede optimizarse más fácilmente. Posteriormente, se realiza una **optimización** para mejorar la eficiencia del código, minimizando recursos o acelerando su ejecución. En la etapa siguiente, este código intermedio se traduce en **código máquina** o **código objeto** (archivo `.o` o `.obj`), que contiene instrucciones en binario específicas para el hardware de destino.

Finalmente, el **enlazador** toma todos los fragmentos de código máquina y los combina en un solo archivo ejecutable en binario (`.exe`, `.out` o sin extensión) que contiene el **código ejecutable**, listo para ser ejecutado directamente por el sistema operativo en la computadora. Cuando el archivo ejecutable se ejecuta o **corre**, entonces se lleva a cabo el **procesamiento de datos**. 

Este flujo de transformación asegura que el programa sea eficiente, portátil y funcional, facilitando la comunicación entre el lenguaje de alto nivel del programador y el lenguaje de bajo nivel que entiende la computadora. Este viaje desde la idea hasta la ejecución es la esencia de la programación eficiente y confiable.


### 6. El lenguaje de programación

Retomemos el lenguaje de programación de una manera más técnica. Todo lenguaje de programación se construye sobre tres fundamentos esenciales: gramática, sintaxis y semántica. Estos elementos trabajan juntos para garantizar que el código no solo sea válido y ejecutable, sino también lógico y funcional. Entender estos pilares es crucial para escribir programas claros y efectivos.

**6.1. Gramática**

La **gramática** de un lenguaje de programación establece las *reglas formales* que determinan *cómo se estructuran las instrucciones*. Al igual que las reglas gramaticales en los idiomas humanos, la gramática de un lenguaje de programación define qué construcciones son válidas para que las computadoras puedan procesarlas. A diferencia del lenguaje natural que tiene elementos como artículo, sujeto, verbo y complemento, la gramática de un lenguaje de programción define otras piezas elementales:  

- Los **tokens**, son las piezas fundamentales del código, que incluyen:
  - **Palabras clave** o **reservadas** que tienen un propósito específico y no pueden usarse como identificadores.
  - **Identificadores**, que dan nombres a elementos como **variables**, **constantes** y **funciones** y deben seguir ciertas reglas, como comenzar con una letra o guion bajo (_) y no coincidir con palabras clave.
  - **Operadores**, que realizan operaciones matemáticas, comparaciones entre valores u operaciones lógicas.
  - **Símbolos de puntuación**, como llaves `{}`, paréntesis `()`, puntos `.` y comas `,`, que estructuran y organizan el código.

- Las **reglas de formación** describen *cómo combinar tokens para formar instrucciones válidas*. Por ejemplo, para asignar un valor a una variable necesitas un identificador, un operador de asignación (`=`) y un valor, como `altura = 3.5` o algo parecido.

- La **producción de sentencias** se refiere a *estructuras completas que definen una instrucción* como declaraciones de variables, bucles (ciclos de repetición) o funciones, en todas sus variaciones posibles. Es el equivalente de la creación de oraciones correctas en un lenguaje natural. 

**6.2. Sintaxis**

La **sintaxis** dicta *cómo deben organizarse los tokens y las estructuras gramaticales* para que el código sea interpretado correctamente por el compilador o el intérprete. Es como la ortografía y la gramática de un idioma, pero aplicada a un lenguaje de programación. Por ejemplo, el uso de paréntesis de apertura y de cierre en la posición correcta. Si la estructura no es precisa, se produce un *error de sintaxis* y el programa o el script ya no continuará su proceso hasta la ejecución. 

Las estructuras sintácticas comunes incluyen:
- **Declaraciones de variables**, que definen el nombre de las variables y el tipo de dato asociado y su valor durante la inicialización.
- **Condicionales**, que controlan decisiones en el flujo del programa a través de variables o valores lógicos. 
- **Ciclos** de repetición, también llamados **bucles** que repiten bloques de código, dada una condición, determinada por una variable o valor lógico.

La sintaxis asegura que el código sea "gramaticalmente correcto", permitiendo que el programa pueda avanzar a la siguiente fase del procesamiento. 

Hay que destacar que el incumplimiento estricto de las reglas de sintaxis del lenguaje de programación que se esté usando es la mayor fuente de errores, durante la interpretación o compilación del código fuente. Conviene usar herramientas de IA para ayudar a encontrar la solución, cuando no se tiene mucha experiencia.

**6.3. Semántica**

La **semántica** se centra en el *significado* del código y en validar si las instrucciones tienen sentido lógico, es decir, si el código resuelve el problema para el que creó el programa o el script. Aunque un programa tenga una sintaxis correcta, no garantiza que haga lo que se espera. Aquí es donde entra la semántica para verificar la lógica del programa. Por ejemplo, un *error semántico* puede ocurrir si intentas realizar una operación imposible o no definida, como dividir un número entre cero o sumar una variable de texto con un número; aunque el código esté correctamente escrito, su lógica será incorrecta.

La semántica es crucial para garantizar que el programa no solo sea ejecutable, sino también funcional y preciso en lo que debe realizar. Aquí es donde entra en juego lo que se llama "testing" o prueba del algoritmo, con datos y procedimiento validados.

En resumen, la gramática, la sintaxis y la semántica trabajan juntas para garantizar que el código esté bien escrito y sea correcto, por lo tanto, sea ejecutable. La gramática establece las reglas fundamentales, la sintaxis asegura que las instrucciones sean válidas y la semántica verifica que tengan sentido. Comprender estos conceptos no solo mejora tu habilidad para programar, sino que también fomenta la creación de software confiable y eficiente. Crea tus programas una vez y úsalo muchas veces.


### 7. Entorno para programación

En la actualidad, el ecosistema tecnológico ofrece miles de **aplicaciones** de **software privativo** y **software libre o abierto**, muchas de ellas gratuitas. Plataformas como [AlternativeTo](https://alternativeto.net/) permiten explorar y comparar opciones para necesidades específicas en tecnología, negocios, educación, redes sociales, entre otras áreas. Estas herramientas hacen más accesible encontrar soluciones que se ajusten a cualquier requerimiento, particularmente para estudiantes que buscan recursos de calidad sin costos adicionales.

Dentro de estas herramientas de **software libre** destacan los *sistemas operativos* como Fedora, los *entornos de desarrollo integrados* (IDE) como RStudio, *intérpretes* de lenguajes como Python y R, y los *compiladores* como **GCC** (*GNU Compiler Collection*). Este último es una colección de compiladores que permite trabajar con múltiples lenguajes como C, C++ y Fortran, entre otros, siendo una herramienta esencial para transformar código fuente en ejecutable y en los códigos intermedios: código ensamblador y código objeto o código máquina. Estas *soluciones con software libre* eliminan prácticamente todas las barreras económicas y tecnológicas al ofrecer recursos gatuitos para que estudiantes y profesionales en administración y otras disciplinas, puedan capacitarse y desarrollar habilidades de programación.

**7.1. Lenguajes de programación**

En cuanto a los lenguajes de programación, el panorama es diverso, dependiendo del propósito. Por ejemplo, hay **lenguajes generalistas** como Python que son altamente versátiles para tareas como desarrollo web, análisis de datos y automatización. Por otro lado, los **lenguajes especializados**, como R o SQL, responden a necesidades concretas como el análisis estadístico o las bases de datos. 

Los lenguajes también se dividen en **lenguajes de alto nivel** (como Python, que son fáciles de aprender, como por estar muy cercanos a la gramática del lenguaje natural) y **lenguajes de bajo nivel** (como el Ensamblador que están más cercanos al hardware). Destaca el Lenguaje C que, siendo un lenguaje de alto nivel, tiene la capacidad de interactuar directamente con el hardware a bajo nivel y, por eso, es el lenguaje usado para crear sistemas operativos como Unix o Linux.

Además, los lenguajes de programación se clasifican según los **paradigmas de programación**, que representan diferentes enfoques para resolver problemas. Uno de los más comunes es el **paradigma imperativo**, que se centra en describir *cómo* se debe resolver un problema mediante una secuencia de instrucciones; ejemplos de este tipo son *COBOL*, usado principalmente en sistemas administrativos, financieros y bancarios y *Ensamblador*, usado en programación de bajo nivel para hardware específico. Por otro lado, el **paradigma funcional** prioriza el uso de funciones matemáticas puras y se enfoca en *qué* resolver, evitando el estado mutable; ejemplos destacados son *Haskell*, ideal para análisis matemático y trabajos que requieren concurrencia y *Erlang*, usado en telecomunicaciones y sistemas distribuidos. El **paradigma orientado a objetos** organiza el código en clases y objetos que modelan entidades del mundo real, promoviendo la reutilización y modularidad; *Ruby* (on Rails) que es usado en desarrollo web, automatización y scripts pertenece a esta categoría. Otros paradigmas incluyen el **lógico**, como Prolog, que utiliza reglas y hechos para derivar conclusiones y el **declarativo**, como SQL, que describe *qué* se quiere obtener sin especificar cómo lograrlo. Hay que considerar que cada paradigma ofrece herramientas únicas que se adaptan a diferentes tipos de problemas y estilos de programación. 

Dado que Python y R son dos lenguajes de programación multiparadigma, es relevante aprovechar las fortalezas de ambos como una oportunidad única de combinar lo mejor de dos mundos, en el análisis de datos, la automatización de procesos y la generación de reportes visuales. Ambos lenguajes tienen características complementarias que, cuando se integran en un flujo de trabajo, potencian enormemente las capacidades administrativas y estratégicas.

**Python** destaca por su versatilidad y facilidad para automatizar tareas repetitivas, ampliar las funciones de Excel y conectar con diversas fuentes de datos. Librerías como `pandas` permiten manejar datos de manera eficiente, facilitando operaciones como filtrado, pivoteo y resúmenes. Esto resulta ideal para automatizar reportes financieros o análisis de tendencias. Además, herramientas como `openpyxl` y `xlsxwriter` ofrecen la personalización necesaria para generar hojas de cálculo visualmente atractivas y profesionales. Python también sobresale en el ámbito de la visualización con librerías como `matplotlib` y `seaborn`, que ayudan a crear gráficos impactantes para respaldar decisiones estratégicas. En escenarios más avanzados, `numpy` y `scipy` son ideales para simulaciones financieras, y `pywin32` permite automatizar el manejo directo de Excel, maximizando la eficiencia operativa.

Por otro lado, **R** es insuperable cuando se requiere un análisis estadístico profundo y visualizaciones avanzadas y reproducibles. Paquetes como `tidyverse`, con herramientas como `dplyr` para manipulación de datos y `ggplot2` para gráficos personalizables, ofrecen un enfoque integral para el análisis y la presentación de datos. Además, la capacidad de R para manejar grandes volúmenes de datos con `data.table` o su capacidad de conectarse a bases de datos locales y remotas con `DBI` o `RPostgres` y la posibilidad de realizar análisis de series temporales con `forecast` lo convierten en una *elección ideal para predicciones* de ventas, demandas y *proyecciones financieras*. Su capacidad para generar *dashboards interactivos* con `shiny` y *reportes dinámicos* con `RMarkdown` lo posiciona como una herramienta fundamental para comunicar resultados de manera clara y efectiva.

La *verdadera ventaja* surge al combinar las fortalezas de ambos lenguajes. Python puede utilizarse para tareas de preprocesamiento y automatización, como integrar datos desde múltiples fuentes y estructurarlos en formatos utilizables. Luego, estos datos pueden ser analizados en profundidad en R, aprovechando sus paquetes avanzados para estadísticas y predicciones. Adicionalmente, Python y R tienen herramientas que permiten integrarlos fácilmente, como los paquetes `reticulate` en R o bibliotecas como `rpy2` en Python, haciendo posible un flujo de trabajo sin interrupciones.

En resumen, Python y R ofrecen una combinación perfecta para estudiantes de administración. Python sobresale en la automatización, la manipulación de datos y la conexión con otras herramientas, mientras que R brilla en el análisis estadístico y la presentación de resultados. Juntos, brindan a los estudiantes la posibilidad de abordar problemas administrativos de manera integral, potenciando tanto la eficiencia operativa como la toma de decisiones estratégicas basada en datos.

**7.2. Entorno de desarrollo**

**RStudio**, tanto en su versión de escritorio como en la plataforma en la nube [RStudio.cloud](https://posit.cloud), es un *entorno de desarrollo integrado (IDE)* excepcionalmente versátil que facilita el aprendizaje de la programación, especialmente para usuarios que desean iniciarse en el uso de R y Python, en un único espacio de trabajo. Esto permite explorar desde análisis estadísticos hasta automatización de tareas, con aplicaciones prácticas directamente relacionadas con su campo.

Una de las principales fortalezas de RStudio es su *interfaz intuitiva y organizada*, que guía a los principiantes a medida que exploran conceptos básicos de programación. Con un *editor* que incluye autocompletado, resaltado de sintaxis y herramientas de depuración, los estudiantes pueden escribir y corregir scripts de manera eficiente. La consola interactiva permite ejecutar comandos en tiempo real, lo que fomenta el aprendizaje a través de prueba y error, mientras que el entorno de trabajo visualiza las variables y objetos en memoria, ayudando a comprender cómo se procesan los datos en un programa. Además, el visor de gráficos integrado facilita la visualización inmediata de resultados, lo que es esencial para el análisis y la toma de decisiones basada en datos.

RStudio no solo es una herramienta eficaz para aprender R, sino que también permite trabajar con Python a través de herramientas como **reticulate** y Jupyter Notebooks, que pueden integrarse en proyectos dentro del IDE. Esta compatibilidad amplía las posibilidades, permitiendo a los estudiantes usar R para análisis estadísticos y Python para tareas como automatización, machine learning o integración con sistemas externos. Esto resulta especialmente útil para estudiantes de administración, ya que pueden aprender las fortalezas de ambos lenguajes en un entorno controlado y accesible.

RStudio soporta una amplia variedad de tipos de archivos, que facilitan el trabajo en análisis de datos, programación y generación de reportes. En el ámbito de la **programación**, RStudio permite trabajar con archivos de código como los scripts de R (`.R`), R Markdown (`.Rmd`) y notebooks de R (`.nb.html`), que combinan código, texto y resultados en documentos dinámicos. Además, soporta scripts de Python (`.py`) y formatos como Quarto (`.qmd`), ofreciendo un entorno integrador para lenguajes complementarios.

En cuanto a los datos, RStudio admite formatos tabulares como archivos de **texto plano** (`.txt`, `.csv`, `.tsv`), hojas de cálculo (`.xlsx`, `.xls`), y datos estructurados en jerarquías como JSON (`.json`) y XML (`.xml`). También se adapta perfectamente a los formatos nativos de R, como **archivos de datos** (`.rds`) y **espacio de trabajo** (`.RData`). Para quienes manejan **bases de datos**, RStudio permite conectarse y trabajar con formatos como SQLite (`.db`, `.sqlite`) y otras, facilitando análisis más avanzados.

En la generación de **reportes** y presentación de resultados, RStudio destaca con su compatibilidad con formatos como HTML (`.html`), PDF (`.pdf`), Microsoft Word (`.docx`), y documentos científicos creados con LaTeX (`.tex`). Además, en el ámbito visual, RStudio soporta formatos de gráficos como PNG (`.png`), JPEG (`.jpg`), SVG (`.svg`) y TIFF (`.tiff`), ideales para la comunicación visual de datos.

Para la organización y configuración de **proyectos**, RStudio utiliza archivos específicos como proyectos de RStudio (`.Rproj`), junto con archivos de **configuración** (`.Renviron` y `.Rprofile`), que establecen variables de entorno y ajustes personalizados para sesiones. También integra **scripts** de otros lenguajes, como shell scripts (`.sh`) y scripts SQL (`.sql`), ampliando las posibilidades de automatización y conexión con bases de datos locales y remotas.

Por último, RStudio facilita la **documentación** con formatos como Markdown (`.md`), usado para crear documentación clara y estructurada, y YAML (`.yaml`), común en configuraciones avanzadas de proyectos. Esta capacidad para manejar una amplia variedad de archivos lo convierte en una herramienta integral, ideal para trabajar con datos y análisis en un entorno colaborativo y productivo.

En resumen, RStudio es más que un IDE; es un entorno de aprendizaje integral que equipa a los estudiantes con las habilidades necesarias para abordar problemas administrativos mediante el análisis de datos y la programación. Su diseño accesible, sus capacidades avanzadas y su compatibilidad con R y Python lo hacen una herramienta imprescindible para quienes desean integrar la programación como parte fundamental de su formación profesional.

### 8. Conclusiones

El software, en su esencia, es una entidad dual: datos e instrucciones que, bien estructurada para resolver problemas con el manejo de datos y realizar tareas concretas. Este ensayo ha demostrado cómo los datos, cuando se codifican y organizan adecuadamente en estructuras de datos eficientes, pueden ser manipulados y procesados por instrucciones para producir resultados significativos. Hemos hecho un repaso de los elementos de todo lenguaje de programación. Además, se ha explicado el ciclo completo que recorre el código, desde su concepción como código fuente hasta su transformación en código ejecutable, ilustrando los procesos de interpretación y compilación. Este recorrido conceptual permite que cualquier estudiante pueda comprender y estudiar, por su cuenta, cómo usar Python, R en RStudio, como un pequeño ecosistema tecnológico potente y versátil. No me cabe la menor duda, que si logran dominar esas tres tecnologías, pueden mejorar sus habilidades en el procesamiento automatizado de datos en sus otras UEAs y egresar como profesionistas bien capacitados.

Para ustedes, estudiantes de administración, comprender esta interacción entre datos e instrucciones no solo es una habilidad técnica, sino también una habilidad estratégica. Ya sea para optimizar flujos de trabajo, tomar decisiones basadas en datos en su campo profesional, esta comprensión es fundamental. El software, al integrar datos e instrucciones, no solo facilita la resolución de problemas, sino que también abre un mundo de posibilidades en la automatización, el análisis de información y la creación de análisis innovadores. La capacidad de entender y aprovechar estos conceptos los posiciona como individuos privilegiados en la economía nacional.

He desarrollado una práctica paralela para practicar y aterrizar los conceptos.

--- 

[^1]: Profesor-investigador del Departamento de Economía de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Contacto: [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx), [Telegram](https://t.me/jzavalar).
[^2]: Lectura leída el 11, 18 y 25 de noviembre de 2024.

Ultima actualización: 22 de noviembre de 2024
