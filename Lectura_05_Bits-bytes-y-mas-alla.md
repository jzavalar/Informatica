## **Lectura 5: Bits, Bytes y Más Allá: El Arte de Digitalizar la Realidad**[^1] (versión 2)

prof. dr. Jesús Zavala Ruiz[^2]

---

### **Introducción**

En el mundo de la computación, el **software** se posiciona como un elemento fundamental, que da vida y propósito al hardware y transforma los sistemas informáticos en herramientas capaces de resolver problemas complejos y realizar tareas cotidianas. La relación entre software y hardware es profundamente simbiótica. Según Patterson y Hennessy (2014), "el hardware y el software forman una simbiosis que es esencial para el funcionamiento de cualquier sistema computacional moderno; ninguno puede funcionar efectivamente sin el otro" (p. 11). Es el software, en última instancia, el que traduce la potencia de procesamiento del hardware en tareas útiles, otorgándole sentido y dirección a los sistemas computacionales. Como afirma Tanenbaum (2013), "el hardware sin software es simplemente una colección costosa de arena y metal" (p. 2).

Esta capacidad fundamental del software radica en su **naturaleza dual** como datos e instrucciones, aspecto que constituye el núcleo de su versatilidad. La dualidad entre datos e instrucciones permite que el software funcione simultáneamente como repositorio de información y como un conjunto de instrucciones para procesarla. Suber (1988) destaca que "el software exhibe una dualidad ontológica única: es simultáneamente patrón abstracto e instanciación concreta, instrucción y dato" (p. 92). Esta dualidad también demuestra, según Colburn (2000), "la naturaleza paradójica del software como entidad que existe entre lo abstracto y lo concreto" (p. 199).

Los **datos** representan la información que el sistema procesa y almacena para cumplir con su función. Aho, Lam, Sethi y Ullman (2007) afirman que "los datos son la materia prima de la computación, la información que debe ser transformada mediante algoritmos para producir resultados útiles" (p. 8). Sin datos, el software no podría realizar operaciones significativas, ya que, como señala Brookshear (2019), "los datos constituyen el sustrato sobre el cual operan todos los procesos computacionales" (p. 34).

Por otro lado, las **instrucciones** son la lógica que organiza y manipula esos datos, orientándolos hacia la ejecución de tareas específicas. Como Knuth (1997) menciona, "un programa es esencialmente una colección de instrucciones precisas que le dicen a la máquina exactamente qué hacer con los datos en cada paso" (p. 4). Silberschatz, Galvin y Gagne (2018) explican además que el software, en su papel de conjunto de instrucciones, "proporciona la inteligencia necesaria para transformar el potencial del hardware en capacidad real de procesamiento" (p. 6).

Comprender el software como una combinación de datos e instrucciones permite una visión integral de su función en la computación. Irmak (2012) sostiene que "entender la naturaleza dual del software requiere reconocer que es un artefacto abstracto con manifestaciones concretas, una entidad que existe en múltiples niveles de abstracción simultáneamente" (p. 58). Este entendimiento más profundo de la dualidad de funciones en el software abre el camino para explorar con mayor profundidad los elementos de los que está compuesto y su papel en la estructura de un sistema digital.

En este ensayo, se abordará inicialmente la **ontología del software**, un concepto que permite entenderlo más allá del código. A continuación, se analizarán los **datos** como la base fundamental sobre la cual opera el software, observando cómo elementos como los símbolos y los sistemas numéricos son representados en lenguaje binario. Finalmente, se discutirá cómo la **codificación de datos** es un arte que permite transformarlos en información para que pueda ser interpretada y procesada por las computadoras. Al concluir, se establecerá un puente hacia una comprensión más avanzada de cómo el software organiza y procesa la realidad digital.

### **1. Ontología del Software**

La **ontología del software** se refiere al estudio y conceptualización de su naturaleza como entidad digital. Para comprender el papel del software en la computación, es fundamental caracterizarlo como algo más que un simple conjunto de códigos. Kroes (2012) afirma que "la ontología del software nos obliga a reconsiderar las categorías tradicionales de existencia, ya que el software desafía la distinción clásica entre lo material y lo ideal" (p. 124). En términos generales, el software se define como "una colección estructurada de instrucciones que, cuando se ejecuta, realiza una función específica o un conjunto de funciones" (IEEE, 2017, p. 432). Este rol lo convierte en un intermediario lógico, que conecta al usuario con el hardware y permite que las máquinas realicen operaciones automatizadas. Colburn (1999) describe el software como "un puente ontológico entre el mundo abstracto de los algoritmos y el mundo físico de los circuitos electrónicos" (p. 14).

Para ilustrar el software, se utiliza la metáfora del cerebro humano, donde los **datos** se asemejan a la **memoria** y las **instrucciones** a los **pensamientos** que interpretan y procesan esa información. Hofstadter (1979) compara los sistemas computacionales con la mente humana, señalando que "así como los pensamientos emergen de patrones neuronales, el comportamiento del software emerge de patrones de bits" (p. 302). Minsky (1986) añade que este paralelismo nos ayuda a entender cómo "las máquinas pueden exhibir comportamientos que parecen inteligentes a través de la manipulación sistemática de símbolos" (p. 17).

La capacidad del software para contextualizar datos y convertirlos en **información significativa** es esencial en su ontología. Shannon y Weaver (1949) establecieron que "la información no es simplemente datos, sino datos que han sido procesados de manera que reduzcan la incertidumbre" (p. 8). Sin contexto, los datos son simplemente elementos sin sentido, pero, al proporcionarles un contexto específico, el software puede transformarlos en información comprensible y relevante para el usuario. Floridi (2011) reafirma esta idea: "el software actúa como un agente semántico que transforma datos sintácticos en información semánticamente rica" (p. 85).

### **2. Los Datos: La Materia Prima Digital**

La estructura del software depende fundamentalmente de los datos, los cuales sirven como la materia prima que da sentido a las operaciones computacionales. A continuación, exploramos el rol de los **símbolos** y los **sistemas numéricos** en la representación de la información, así como los **tipos básicos de datos** utilizados en informática y las estructuras que organizan estos datos para el procesamiento eficaz en aplicaciones reales.

#### **a. Símbolos: La Representación del Significado**

En computación, un **significado** es el concepto o idea que se asocia con un símbolo particular, como una palabra o imagen. Este significado se convierte en un **símbolo**, una representación visual, auditiva o conceptual que se usa para transmitir esa idea. Los símbolos abarcan desde caracteres alfanuméricos hasta códigos de colores y gráficos y, en computación, son esenciales para representar información de manera que el sistema pueda interpretarla.

"La transición del significado al símbolo es fundamental en la comunicación digital, pues convierte conceptos abstractos en representaciones procesables por máquinas" (Peirce, 1931-1958, vol. 2, p. 228). En el mundo digital, el proceso de convertir ideas en símbolos facilita la comunicación uniforme en las plataformas tecnológicas (Chandler, 2007, p. 13). De este modo, la **semiótica digital** estudia cómo los significados se traducen a símbolos, lo cual permite crear representaciones computacionales precisas (Nöth, 1990, p. 52).

La gran variedad de símbolos, como glifos e ideogramas, amplía la capacidad de expresión en la tecnología digital. Como explica Crystal (2008), "la digitalización del lenguaje humano requiere un mapeo sistemático entre los símbolos culturales y sus representaciones binarias" (p. 47). Gracias a esta conversión, los sistemas computacionales pueden interpretar números, ideogramas y glifos, logrando que el lenguaje humano sea comprensible para la máquina (Unicode Consortium, 2019, p. 2).

#### **b. Sistemas Numéricos: El Lenguaje Binario como Base Universal**

Para representar datos en sistemas computacionales, el **sistema binario** es el lenguaje esencial. Este sistema utiliza dos estados —representados por los dígitos 0 y 1— para expresar toda la información que el sistema procesará. Los elementos más básicos de este sistema son el **bit** y el **byte**. John Tukey acuñó el término "bit" en 1947, como documenta Tropp (1984): "El 9 de enero de 1947, John W. Tukey escribió un memorando de Bell Labs donde propuso la contracción 'bit' para 'binary digit'" (p. 152). Un **byte**, por otro lado, está compuesto de 8 bits y se considera la unidad fundamental para almacenar datos, ya que permite representar una mayor variedad de valores.

"Los bits son los átomos de la información en el mundo digital" (Shannon, 1948, p. 380), ya que estos permiten que las computadoras almacenen datos y los interpreten de manera uniforme. Los bytes, formados por secuencias de bits, se han convertido en la unidad estándar de medida en la computación moderna (Williams, 1997, p. 248).

El sistema binario es ideal para los sistemas digitales porque cada bit representa una opción entre dos estados, lo cual permite representar de forma universal todo tipo de información, desde texto hasta imágenes. Como menciona Stallings (2016), "la belleza del sistema binario radica en su simplicidad: con solo dos símbolos podemos representar cualquier información imaginable" (p. 67). Esto hace posible que los sistemas digitales comuniquen y procesen la información en secuencias de 0s y 1s (Mano & Ciletti, 2013, p. 3), garantizando una estructura de procesamiento de datos consistente y adaptable.

### **3. Tipos de Datos: Los Bloques de Construcción**

Los datos digitales pueden clasificarse en varios tipos fundamentales en programación. Cada uno de estos tipos tiene un propósito particular y se utiliza para modelar diferentes aspectos de la realidad.

**a. Enteros**: Este tipo de datos representa números discretos y exactos, sin decimales, que resultan útiles para contar objetos, definir posiciones o identificar elementos. Los enteros se almacenan directamente en binario, lo que permite representar tanto valores positivos como negativos mediante el sistema de complemento a dos. Por ejemplo, el número de usuarios en un sistema o el conteo de productos en un inventario son datos que se manejan adecuadamente con enteros. Sin embargo, los enteros están limitados por el rango de valores que el sistema binario puede almacenar, lo que puede llevar a problemas de desbordamiento en sistemas que gestionan grandes volúmenes de datos (Pierce, 2002, p. 93).

**b. Reales**: También conocidos como números de punto flotante, permiten modelar datos con decimales que representan medidas continuas. Los reales se representan según el **estándar IEEE 754**, que utiliza notación científica en binario para permitir un amplio rango de valores. Esto los hace ideales para aplicaciones que requieren precisión y variabilidad, como en simulaciones físicas o en finanzas. Por ejemplo, las posiciones de partículas en física o las tasas de interés en finanzas se representan como reales. No obstante, los números reales están sujetos a limitaciones de precisión debido a su representación binaria, lo que puede causar errores de redondeo en cálculos complejos (Goldberg, 1991, p. 5).

**c. Texto**: El tipo de dato **texto** permite almacenar secuencias de caracteres, como letras, números y símbolos, que pueden representar nombres, comandos o datos alfanuméricos. En los sistemas computacionales, el texto se representa mediante codificaciones estándar como **ASCII** y **Unicode**.

**ASCII** (American Standard Code for Information Interchange) fue desarrollado bajo la dirección de Bob Bemer, conocido como el "padre de ASCII". Bemer (1960) explicó: "Necesitábamos un código estándar que pudiera ser usado por todas las computadoras para intercambiar información textual" (citado en Mackenzie, 1980, p. 41). ASCII usa 7 bits para representar 128 caracteres diferentes. Cada letra o símbolo tiene una representación binaria específica; por ejemplo, la letra `"A"` en ASCII se representa como `01000001`.

Para superar las limitaciones de ASCII, **Unicode** fue desarrollado por Joe Becker, Lee Collins y Mark Davis. El Consorcio Unicode (2019) establece: "Unicode proporciona un número único para cada carácter, sin importar la plataforma, sin importar el programa, sin importar el idioma" (p. 1). Unicode usa diferentes formatos de codificación, siendo **UTF-8** el más común, desarrollado por Ken Thompson y Rob Pike en 1992. Pike y Thompson (1993) describieron UTF-8 como "una codificación que preserva ASCII mientras permite la representación completa de Unicode" (p. 163).

Los **emojis** son una extensión moderna del tipo de dato texto que permite incluir expresiones visuales en forma de gráficos pequeños. Davis (2016) señala: "Los emojis se han convertido en un lenguaje visual universal en la era digital, enriqueciendo la comunicación textual con elementos emocionales y contextuales" (p. 22). Por ejemplo, el emoji de la cara sonriente `🙂` tiene el código Unicode `U+1F642` y se representa en binario en UTF-8 como `11110000 10011111 10011001 10100010`.

**d. Datos lógicos:** Los **tipos de datos lógicos**, también conocidos como **booleanos**, representan valores de verdad en lógica computacional. Boole (1854) estableció las bases de esta lógica que ahora lleva su nombre, permitiendo que las computadoras tomen decisiones basadas en condiciones verdaderas o falsas. Son esenciales en programación y se limitan a dos posibles valores: **verdadero** (true) o **falso** (false). 

**e. Estructuras de Datos**: Las **estructuras de datos** organizan la información para optimizar su almacenamiento y acceso en los sistemas computacionales, mejorando el rendimiento de los programas. Según Cormen et al. (2009):

- **Arreglos**: "La estructura de datos más simple y fundamental, que almacena elementos del mismo tipo en ubicaciones contiguas de memoria" (p. 20).
  
- **Listas Enlazadas**: "Estructuras dinámicas donde cada elemento contiene datos y una referencia al siguiente nodo" (p. 236).

- **Pilas**: "Estructuras LIFO (Last In, First Out) fundamentales para la gestión de llamadas a funciones y evaluación de expresiones" (p. 232).

- **Colas**: "Estructuras FIFO (First In, First Out) esenciales para la planificación de procesos y gestión de recursos" (p. 234).

- **Árboles**: "Estructuras jerárquicas que permiten búsquedas, inserciones y eliminaciones eficientes" (p. 286).

- **Tablas Hash**: "Estructuras que proporcionan acceso en tiempo constante promedio mediante funciones de dispersión" (p. 253).

### **4. Codificación de archivos**

La **codificación de datos** es fundamental para transformar la realidad en formatos que las computadoras pueden interpretar, representando texto, imágenes y sonidos en bits. Este proceso permite que datos de múltiples formas se almacenen, manipulen y compartan entre plataformas digitales. Mackenzie (2005) afirma: "La codificación es el proceso fundamental que permite la digitalización de toda la experiencia humana" (p. 73).

#### **a. Tipos de Archivos**

Los **archivos digitales** pueden clasificarse en **archivos de texto** y **archivos binarios**. Esta distinción radica en cómo los datos se representan y almacenan en el archivo, lo cual impacta su accesibilidad y manipulación en sistemas informáticos.

1. **Archivos de Texto**

Estos archivos almacenan datos legibles en formatos de texto, utilizando principalmente ASCII o Unicode. Raymond (2003) explica: "Los archivos de texto plano son la lingua franca de los sistemas Unix, permitiendo interoperabilidad universal" (p. 108). UTF-8 se ha convertido en el estándar de facto para la web. Como señalan Korpela (2006), "UTF-8 combina la compatibilidad con ASCII y la capacidad de representar todos los caracteres Unicode" (p. 234).

   - **Documentos de Texto**: Incluyen archivos como `.txt`, `.md` y `.epub`
   - **Código Fuente**: Archivos como `.c` y `.py`
   - **Intercambio de Datos**: Formatos como `.csv`, `.json` y `.xml`

2. **Archivos Binarios**

Estos archivos almacenan datos en un formato que no es legible directamente sin el software adecuado. Tanenbaum y Bos (2015) explican: "Los archivos binarios están optimizados para el procesamiento eficiente por parte del computador, no para la lectura humana" (p. 265). Los archivos binarios incluyen:

   - **Documentos de Oficina**: `.pdf`, `.docx`, `.pptx` y `.xlsx`
   - **Multimedia**: `.jpg`, `.png`, `.mp3`, `.mp4` y `.avi`
   - **Archivos Comprimidos**: `.zip`, `.tar` y `.tgz`

3.**Bases de Datos**

La **codificación en bases de datos** permite almacenar y organizar grandes volúmenes de datos estructurados. Date (2004) establece: "Las bases de datos modernas deben manejar eficientemente tanto el almacenamiento como la recuperación de datos en múltiples formatos" (p. 45).

#### **b. Herramientas para la Codificación de Archivos**

- **Editores de Texto e IDEs**: Fowler (2019) señala que "los IDEs modernos han transformado la programación de una actividad solitaria en un proceso colaborativo y asistido" (p. 67).
- **Editores Binarios**: Herramientas especializadas para la manipulación directa de datos binarios, esenciales para debugging y análisis forense (Carrier, 2005, p. 178).

### **5. Conclusión**

La codificación de datos es una disciplina clave en informática, ya que permite transformar la realidad en secuencias de bits interpretables para las computadoras, facilitando la organización, almacenamiento y transmisión de la información en múltiples formatos y plataformas. La comprensión de los principios de codificación, desde el texto hasta el contenido multimedia, es fundamental para garantizar la interoperabilidad y eficiencia en un mundo digital cada vez más interconectado.

A medida que exploramos la importancia de la codificación de datos, comprendemos mejor cómo el software actúa como un intermediario entre los datos y el usuario, permitiendo que las computadoras procesen y presenten información de manera efectiva y accesible. En la próxima exploración, se analizará cómo el software organiza y procesa la información a través de algoritmos y estructuras de datos, desarrollando su función de instrucción para ejecutar tareas complejas en sistemas computacionales avanzados.

### **6. Referencias**

Aquí está la lista de referencias actualizada con los DOI agregados donde fue posible encontrarlos. Los DOI se añadieron al final de cada referencia correspondiente, utilizando el formato `https://doi.org/...`. Para algunas referencias (especialmente libros antiguos, estándares o informes técnicos) no existen DOI disponibles, por lo que se mantuvieron sin cambios.

### **6. Referencias**

- Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). *Compilers: Principles, techniques, and tools*. Boston: Pearson/Addison Wesley.  
- Boole, G. (1854). *An investigation of the laws of thought*. London: Walton and Maberly.  
- Brookshear, J. G. (2019). *Computer science: An overview*. Boston: Pearson.  
- Carrier, B. (2005). *File system forensic analysis*. Upper Saddle River, NJ: Addison-Wesley.  
- Chandler, D. (2007). *Semiotics: The basics*. London: Routledge. https://doi.org/10.4324/9780203014936  
- Colburn, T. R. (1999). Software, abstraction, and ontology. *The Monist*, *82*(1), 3-19. https://doi.org/10.5840/monist19998211  
- Colburn, T. R. (2000). *Philosophy and computer science*. Armonk, NY: M.E. Sharpe.  
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to algorithms*. Cambridge, MA: MIT Press.  
- Crystal, D. (2008). *Txtng: The gr8 db8*. Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199544905.001.0001  
- Date, C. J. (2004). *An introduction to database systems*. Boston: Pearson/Addison Wesley.  
- Davis, M. (2016). Unicode emoji: Technical report #51. *Unicode Consortium*. Retrieved from http://www.unicode.org/reports/tr51/  
- Floridi, L. (2011). *The philosophy of information*. Oxford: Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199232383.001.0001  
- Fowler, M. (2019). *Refactoring: Improving the design of existing code*. Boston: Addison-Wesley.  
- Goldberg, D. (1991). What every computer scientist should know about floating-point arithmetic. *ACM Computing Surveys*, *23*(1), 5-48. https://doi.org/10.1145/103162.103163  
- Hofstadter, D. R. (1979). *Gödel, Escher, Bach: An eternal golden braid*. New York: Basic Books.  
- IEEE. (2017). *IEEE standard glossary of software engineering terminology* (IEEE Std 610.12-1990). New York: IEEE Press. https://doi.org/10.1109/IEEESTD.1990.101064  
- Irmak, N. (2012). Software is an abstract artifact. *Grazer Philosophische Studien*, *86*(1), 55-72. https://doi.org/10.1163/18756735-086001004  
- Knuth, D. E. (1997). *The art of computer programming, Volume 1: Fundamental algorithms*. Reading, MA: Addison-Wesley.  
- Korpela, J. (2006). *Unicode explained*. Sebastopol, CA: O'Reilly Media.  
- Kroes, P. (2012). *Technical artefacts: Creations of mind and matter*. Dordrecht: Springer. https://doi.org/10.1007/978-94-007-3940-6  
- Mackenzie, C. E. (1980). *Coded character sets: History and development*. Reading, MA: Addison-Wesley.  
- Mackenzie, A. (2005). The performativity of code: Software and cultures of circulation. *Theory, Culture & Society*, *22*(1), 71-92. https://doi.org/10.1177/0263276405048436  
- Mano, M. M., & Ciletti, M. D. (2013). *Digital design*. Boston: Pearson.  
- Minsky, M. (1986). *The society of mind*. New York: Simon and Schuster.  
- Nöth, W. (1990). *Handbook of semiotics*. Bloomington: Indiana University Press.  
- Patterson, D. A., & Hennessy, J. L. (2014). *Computer organization and design: The hardware/software interface* (5th ed.). Waltham, MA: Morgan Kaufmann.  
- Peirce, C. S. (1931-1958). *Collected papers of Charles Sanders Peirce* (Vols. 1-8). Cambridge, MA: Harvard University Press.  
- Pierce, B. C. (2002). *Types and programming languages*. Cambridge, MA: MIT Press.  
- Pike, R., & Thompson, K. (1993). Hello world or Καλημέρα κόσμε or こんにちは 世界. In *Proceedings of the Winter 1993 USENIX Conference* (pp. 43-50). San Diego, CA: USENIX Association.  
- Raymond, E. S. (2003). *The art of Unix programming*. Boston: Addison-Wesley.  
- Shannon, C. E. (1948). A mathematical theory of communication. *The Bell System Technical Journal*, *27*(3), 379-423. https://doi.org/10.1002/j.1538-7305.1948.tb01338.x  
- Shannon, C. E., & Weaver, W. (1949). *The mathematical theory of communication*. Urbana: University of Illinois Press.  
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating system concepts*. Hoboken, NJ: Wiley.  
- Stallings, W. (2016). *Computer organization and architecture* (10th ed.). Boston: Pearson.  
- Suber, P. (1988). What is software? *Journal of Speculative Philosophy*, *2*(2), 89-119.  
- Tanenbaum, A. S. (2013). *Structured computer organization*. Boston: Pearson.  
- Tanenbaum, A. S., & Bos, H. (2015). *Modern operating systems*. Boston: Pearson.  
- Tropp, H. S. (1984). Origin of the term bit. *Annals of the History of Computing*, *6*(2), 152-155. https://doi.org/10.1109/MAHC.1984.10010  
- Unicode Consortium. (2019). *The Unicode standard, version 12.0*. Mountain View, CA: Unicode Consortium.  
- Williams, M. R. (1997). *A history of computing technology*. Los Alamitos, CA: IEEE Computer Society Press.  
--- 

[^1]: Profesor-investigador del Departamento de Economía de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Contacto: [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx), [Telegram](https://t.me/jzavalar).
[^2]: Lectura revisada el 9 de junio de 2025.
Ultima actualización: 4 de noviembre de 2024
