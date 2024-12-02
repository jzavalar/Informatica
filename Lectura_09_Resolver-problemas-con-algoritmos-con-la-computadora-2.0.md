## **Lectura 9. Resolver Problemas con Algoritmos con la Computadora 2.0**[^1]

prof. dr. Jesús Zavala Ruiz[^2]

---

### **1. Introducción**

Los algoritmos son la base del pensamiento computacional y del desarrollo de software. Constituyen secuencias claras y precisas de pasos diseñadas para resolver problemas o realizar tareas específicas. Desde cálculos matemáticos simples hasta la gestión de sistemas complejos, los algoritmos nos permiten descomponer problemas en componentes manejables y crear soluciones eficientes.

Esta lectura se centra en cómo diseñar y aplicar algoritmos para resolver problemas de manera estructurada. Abordaremos las etapas desde el planteamiento del problema hasta su implementación en pseudocódigo y su posterior traducción a Python. También exploraremos cómo la inteligencia artificial (IA) puede servir como una herramienta para generar, optimizar y validar algoritmos.

El propósito de este texto es equipar a los lectores con los fundamentos necesarios para abordar problemas de programación de forma organizada y eficiente. Asimismo, aprenderán a aprovechar herramientas modernas para fortalecer su pensamiento lógico y sus habilidades técnicas.

### **2. Fundamentos**

En este apartado, exploraremos conceptos básicos sobre qué es un algoritmo, su relevancia, el rol de la semántica y la relación con la sintaxis, así como la integración de herramientas modernas, como la inteligencia artificial, para facilitar su desarrollo.

Un **algoritmo** es un conjunto finito y ordenado de pasos o instrucciones que se siguen para resolver un problema o realizar una tarea específica. Cada paso del algoritmo debe ser *claro*, *preciso* y *ejecutable*, lo que garantiza que, al aplicarlo, se obtenga un resultado correcto o esperado, siempre que se sigan las condiciones iniciales definidas. 

Más a detalle, las *características principales de un algoritmo* son las siguientes:
1. **Finitud**: Un algoritmo debe tener un *número limitado de pasos* y llegar a una solución en un tiempo finito.
2. **Definición**: Cada paso del algoritmo debe estar *claramente definido* y *no dejar lugar a ambigüedades*.
3. **Entradas**: Puede recibir uno o varios *datos iniciales* (entradas), aunque no siempre es necesario.
4. **Salidas**: Debe proporcionar al menos un *resultado* (salida) relacionado con el problema a resolver.
5. **Efectividad**: Todas las operaciones del algoritmo deben *ser realizables* en un tiempo razonable con los recursos disponibles.
6. **Generalidad**: Un algoritmo debe ser *aplicable a un conjunto de problemas similares*, no solo a uno en particular.

Hay algoritmos de procedimientos cotidianos, como *Preparar una taza de té*:  

**Algoritmo**:
1. Poner agua en una tetera.
2. Calentar el agua hasta que hierva.
3. Colocar una bolsita de té en una taza.
4. Verter el agua caliente en la taza.
5. Esperar 3 minutos para que el té se infusione.
6. Retirar la bolsita de té.
7. Opcional: Agregar azúcar o leche según preferencias.
8. Servir y disfrutar.

Sin embargo, los algoritmos que nos interesan en informática son aquellos que pueden implementarse con el uso de la computadora, ya que sirven como el *modelo lógico* para diseñar programas de computadora que resuelvan problemas de manera eficiente. En otro sentido, *los algoritmos son una extensión de las capacidades de la calculadora*, en problemas matemáticos, pero más allá: problemas del uso y manejo de datos para tomar decisiones. Por ejemplo, los algoritmos permiten optimizar recursos, como tiempo de ejecución y uso de memoria, en el diseño de soluciones computarizadas y son la base de muchas aplicaciones modernas, desde búsquedas en Internet hasta el desarrollo de la inteligencia artificial (IA). 

De hecho, no es descabellado decir que *los algoritmos ya gobiernan el mundo*, especialmente en una era dominada por la tecnología y el *big data*. Los algoritmos no solo son herramientas que ejecutan instrucciones en sistemas computacionales, sino que, siendo creados y ajustados por humanos, están influyendo de manera invisible pero determinante en nuestras decisiones, interacciones y acceso a recursos. Los algoritmos *toman decisiones complejas e influyen en nuestras elecciones cotidianas*, pues el teléfono celular ha puesto al alcance de todos, aplicaciones prácticamente para cualquier finalidad, como hacer pagos bancarios o elegir la mejor ruta para llegar de un lugar a otro. Esa es una actividad tan adictiva que mantiene a las personas "*pegadas al teléfono*". Nada más voleen a su alrededor mientras viajan en el transporte público, para comprobarlo.

Por eso, el diseño e implementación de algoritmos es una habilidad esencial en cualquier carrera profesional. Los algoritmos no solo representan el núcleo de cualquier aplicación de software, sino que también son herramientas fundamentales para estructurar y organizar soluciones de manera eficiente. 

### **3. Metodología de Programación**

En el mundo de la programación, resolver problemas requiere un enfoque sistemático y organizado. La metodología de programación establece un marco de pasos claros para abordar desafíos computacionales, desde la definición del problema hasta su implementación y optimización. A continuación, exploraremos cada etapa del proceso, con ejemplos prácticos y explicaciones claras para principiantes.

#### **3.1. Planteamiento del Problema**

El primer paso en la resolución de cualquier problema computacional es *entender claramente qué se desea resolver*. Un planteamiento mal definido lleva a soluciones incompletas o erróneas. En informática hay un dicho que ejemplifica esto: *Basura entra, basura sale*. 

**Paso 1: Definir el problema de forma clara**: Debe responder a preguntas como: ¿Qué se necesita resolver? ¿Cuál es el objetivo final? Debe evitarse vaguedades o generalizaciones. 

Por ejemplo, "*Crear un programa que determine si un número es par o impar*".

#### **3.2. Diseño del Algoritmo**

La planificación previa a la escritura del código ayuda a minimizar errores y mejora la claridad de las soluciones. Antes de escribir código, es esencial estructurar el problema en pasos simples y verificables. Un *buen diseño* evita redundancias, mejora la eficiencia y facilita la depuración. El segundo paso es *desglosar el problema en pasos claros* es fundamental para avanzar hacia la siguiente etapa: el diseño del algoritmo. 

Se puede usar lenguaje natural para plantear el problema inicial.

**Paso 2: Identificar entradas, procesos y salidas**: 
   - **Entradas**: ¿Qué datos necesita el programa para funcionar? 
   - **Procesos**: ¿Qué operaciones se deben realizar con esos datos? 
   - **Salidas**: ¿Qué resultados o acciones debe generar o hacer el programa?

Por ejemplo, para *Crear un programa que determine si un número es par o impar*, estos son sus tres elementos: 
   - **Entradas**: *Un **número entero** ingresado por el usuario*; 
   - **Procesos**: *Verificar si el número es* **divisible entre 2**; 
   - **Salidas**: **Imprimir** *"Es par" o "Es impar" según corresponda*.

Luego, se puede usar pseudocódigo. 

#### **3.3. Diseño del Algoritmo en Pseudocódigo**

El **pseudocódigo** es una herramienta intermedia entre el lenguaje humano y el lenguaje de programación. Es una representación simplificada del algoritmo que no sigue la sintaxis de un lenguaje específico, pero describe con precisión la lógica del problema. Las ventajas del pseudocódigo son, entre otras: facilitar la *comprensión y comunicación de ideas*, ayuda a *visualizar la solución antes* de implementarla y servir como *guía para escribir código* en un lenguaje de programación. Una de las herramientas de pseudocódigo más recomendadas es **PSeInt**, una herramienta gratuita que permite escribir, depurar y validar programas en pseudocódigo, en una interfaz amigable ideal para principiantes. 

**Paso 3: Diseñar el algoritmo en pseudocódigo**: Diseñemos el algoritmo para el problema *"Determinar si un número es par o impar"*, a partir de lo definido en lenguaje natural, en el paso previo:

**Pseudocódigo en PSeInt:**
```plaintext
// es_par_o_impar.psc
// Algoritmo: Determinar si un número es par o impar
// Autor: profe J. Zavala
// Fecha: 2 de diciembre de 2014
Inicio
   // Definir variables y tipos de datos
   Definir numero como entero; 
   
   // Entrada:
   Escribir "Ingresa un número entero:";
   Leer numero; 
   
   // Proceso
   residuo <- numero % 2;
   Si (residuo == 0) Entonces
      // Salida:
      Escribir "El número ", numero, "es par.";
   Sino
      // Salida:
      Escribir "El número ", valor, "es impar.";
   Fin Si
Fin
```

#### **3.4. Probar el Algoritmo**

La **prueba de un algoritmo** es el proceso de verificar que el algoritmo *funcione correctamente*, en diversas condiciones. Esto incluye probarlo con diferentes entradas para asegurarse de que produce los resultados esperados y manejar casos límite, errores o condiciones inesperadas, es decir, que el algoritmo no tenga errores semánticos. Las pruebas evalúan:

1. **Exactitud**: ¿El algoritmo produce los resultados correctos para todas las entradas válidas? Si así ocurre, no hay errores de semántica.
2. **Robustez**: ¿Cómo maneja el algoritmo entradas inválidas o casos extremos? Esto es el manejo de errores de captura de datos de entrada.
3. **Eficiencia**: ¿El algoritmo utiliza recursos de manera óptima (tiempo, memoria)?
4. **Confiabilidad**: ¿Produce resultados consistentes en múltiples ejecuciones?

Para probar un algoritmo, se desarrollan definiendo **casos de prueba** para cada escenario posible. Estos casos incluyen:

1. **Entradas válidas normales**:
   - Datos estándar que cumplen con los requisitos.
   - Ejemplo: Si el algoritmo calcula si un número es par o impar, usar valores como `5` y `10`.

2. **Casos límite**:
   - Valores cercanos al rango permitido; en este caso no aplica, pero si se esperara un número entre `0` y `100`, probar con `0`, `100` y valores intermedios.

3. **Entradas inválidas**:
   - Datos fuera del rango esperado o de tipo incorrecto.
   - Ejemplo: En lugar de un número, ingresar una cadena o un valor vacío.

4. **Casos excepcionales**:
   - Condiciones inusuales, como divisiones por cero o listas vacías.

Para el ejemplo, se debe verificar si un número es par o impar en los siguiente **casos de prueba**:

- **Entrada válida normal**: `10` -> Salida: "Es par".
- **Caso límite**: `0` -> Salida: "Es par".
- **Entrada inválida**: Letras ele y O mayúscula: `lO` -> Salida: "Error: Entrada no válida".
- **Caso excepcional**: Número negativo como `-3` -> Salida: "Es impar".

Para llevar el control de las pruebas de un algoritmo se puede desarrollar un **formato de registro de casos de prueba**, como el siguiente:

| **ID del Caso de Prueba** | **Descripción**               | **Entrada**    | **Acción esperada**        | **Salida esperada**          | **Resultado**  |
|---------------------------|-------------------------------|----------------|----------------------------|-----------------------------|----------------|
| CP-001                   | Entrada válida normal         | `10` y `5`           | Verificar si es par o impar | "Es par"                    |                |
| CP-002                   | Caso límite                   | `0`            | Verificar si es par o impar | "Es par"                    |                |
| CP-003                   | Entrada inválida              | `lO`  (letras ele y o)         | Verificar si la entrada es válida y determinar paridad | "Error: Entrada no válida" |                |
| CP-004                   | Caso excepcional              | `-3`           | Verificar si es par o impar | "Es impar"                  |                |

**Instrucciones para completar el registro:**

1. **Ejecutar el caso de prueba**:
   - Utilizar el algoritmo para procesar la entrada indicada.
   - Anotar la salida obtenida en la columna **Resultado**.
2. **Comparar la salida obtenida con la salida esperada**:
   - Si coinciden, marcar como **Correcto**.
   - Si no coinciden, anotar el problema detectado.
3. **Registrar observaciones adicionales**:
   - Documentar cualquier comportamiento inesperado o área de mejora.

A continuación se muestra el pseudocódigo PSeInt corregido y mejorado para que funcione correctamente en todos los casos de prueba. Se han añadido validaciones para manejar entradas inválidas y casos excepcionales:

```pseint
// es_par_o_impar_mejorado.psc
// Algoritmo: Determinar si un número es par o impar, con validaciones
// Version 2
// Autor: profe J. Zavala
// Fecha: 2 de diciembre de 2024
Inicio
   // Definir variables y tipos de datos
   Definir numero como entero;
   Definir es_valido como lógico;
   es_valido <- Falso;

   // Entrada:
   Mientras No es_valido Hacer
      Escribir "Ingresa un número entero:";
      Leer numero;

      // Validación de entrada
      Si EsNumero(numero) Entonces
         es_valido <- Verdadero;
      Sino
         Escribir "Error: Entrada no válida. Por favor, ingresa un número entero.";
      Fin Si
   Fin Mientras

   // Proceso
   Si (numero % 2 == 0) Entonces
      // Salida:
      Escribir "El número ", numero, " es par.";
   Sino
      // Salida:
      Escribir "El número ", numero, " es impar.";
   Fin Si
Fin
```

**Cambios al pseudocódigo inicial:**

1. **Validación de entrada:**
   - Se agregó un bucle `Mientras` para validar que el usuario ingrese un número entero.
   - Se utiliza la función `EsNumero(numero)` para verificar que la entrada sea válida.

2. **Corrección de errores semánticos:**
   - Se corrigió el nombre de la variable en la salida de `valor` a `numero`.

3. **Casos excepcionales:**
   - El pseudocódigo ahora maneja adecuadamente números negativos y garantiza que no se procesen entradas no válidas. 

4. **Robustez mejorada:**
   - El algoritmo solicita al usuario corregir su entrada hasta que se ingrese un valor válido.

Una vez que ya está validado el algoritmo, ahora se traduce a un lenguaje de programación, por ejemplo, a Python:
   
#### **3.5. Traducción del Pseudocódigo a un Lenguaje de Programación**

Traducir un algoritmo a un lenguaje de programación implica convertir las instrucciones escritas en un lenguaje entendible para los humanos, como el pseudocódigo **PSeInt**, a un lenguaje que pueda ser procesado y ejecutado por una computadora, por ejemplo, con **Python**. Este proceso debe respetar tanto la lógica del algoritmo como la sintaxis del lenguaje elegido, manteniendo correspondencia directa entre las instrucciones. Sin embargo, hay que considerar que se pueden presentar algunos problemas durante este proceso, como los siguientes:

1. **Errores de Sintaxis:** La estructura del pseudocódigo no siempre tiene un equivalente directo en el lenguaje de programación, por lo que los programadores deben adaptarse a las reglas gramaticales del lenguaje.
   
2. **Errores de Lógica:** Una mala interpretación del pseudocódigo puede alterar la lógica y causar resultados incorrectos. Debe ser cuidadoso en este aspecto.

3. **Diferencias Semánticas:** Algunas funciones o estructuras del pseudocódigo no tienen una traducción directa al lenguaje de programación, porque no existen y requieren desarrollar alternativas.

4. **Falta de Validaciones:** En pseudocódigo, las validaciones suelen ser más implícitas; en código real, deben ser explícitas.

5. **Errores de Tipo de Datos:** Los lenguajes de programación tienen reglas estrictas para manejar tipos de datos que deben ser respetadas.

A continuación se muestra el código Python equivalente (línea por línea), que traduce estrictamente el pseudocódigo proporcionado, con comentarios para explicar los ajustes realizados. No se realizan optimizaciones; el objetivo es preservar la estructura original y la lógica del pseudocódigo, que el el script se muestra como un comentario.

```python
# es_par_o_impar_mejorado.py
# Algoritmo: Determinar si un número es par o impar, con validaciones
# Versión 2
# Autor: profe J. Zavala
# Fecha: 2 de diciembre de 2024

# Inicio del algoritmo (No tiene equivalente directo en Python, solo se comenta)

# Definir variables y tipos de datos
numero = None  # En Python, las variables no necesitan declaración previa
es_valido = False  # Inicializar la variable lógica como Falso

# Entrada
while not es_valido:  # Mientras No es_valido Hacer
    print("Ingresa un número entero:")  # Escribir "Ingresa un número entero:"
    try:
        numero = int(input())  # Leer numero; Se intenta convertir la entrada a entero
        
        # Validación de entrada
        # Si EsNumero(numero) Entonces
        es_valido = True  # Si la conversión tiene éxito, es válida
    except ValueError:
        # Sino
        print("Error: Entrada no válida. Por favor, ingresa un número entero.")  # Escribir "Error..."
    # Fin Si (El bloque try-except reemplaza esta parte)
# Fin Mientras (El bucle termina aquí)

# Proceso
if numero % 2 == 0:  # Si (numero % 2 == 0) Entonces
    # Salida:
    print(f"El número {numero} es par.")  # Escribir "El número ", numero, " es par."
else:
    # Salida:
    print(f"El número {numero} es impar.")  # Escribir "El número ", numero, " es impar."
# Fin Si (Fin del condicional)

# Fin del algoritmo (No tiene equivalente directo en Python, solo se comenta)
```

### **Explicación de la traducción línea por línea:**

1. **Definición de variables:**
   - `Definir numero como entero` y `Definir es_valido como lógico` -> Traducido a `numero = None` y `es_valido = False`. En Python no es necesario declarar el tipo de variable, pero se inicializa explícitamente.

2. **Bucle de entrada:**
   - `Mientras No es_valido Hacer` -> Traducido a `while not es_valido`.
   - `Escribir` -> Traducido a `print()`.
   - `Leer numero` -> Traducido a `input()` y convertido a entero con `int()`.

3. **Validación de entrada:**
   - `Si EsNumero(numero)` -> Implementado con un bloque `try-except` en Python para manejar la conversión a entero y detectar errores.

4. **Condicional para determinar par o impar:**
   - `Si (numero % 2 == 0) Entonces` -> Traducido a `if numero % 2 == 0:`.
   - `Escribir` -> Traducido a `print()`.

5. **Bloques sin equivalente directo en Python:**
   - `Inicio` y `Fin` no tienen equivalentes directos en Python, por lo que se indican como comentarios.

Este código es fiel al pseudocódigo original. La optimización y mejora de la implementación en Python se realizará en un paso posterior.

#### **3.6. Optimización del Algoritmo con IA**

Optimizar un código implica más que simplemente reducir líneas o hacer que se ejecute más rápido. Es un proceso integral que busca mejorar la eficiencia, legibilidad, adaptabilidad y robustez del programa, sin comprometer su funcionalidad. La optimización de un programa o script, aplicando principios de buenas prácticas en desarrollo de software incluye las siguientes tareas:

**1. Modularización del Código**
   - *Tarea*: Dividir el código en funciones pequeñas y específicas que realizan una tarea concreta.
   - *Por qué es importante*: La modularización mejora la legibilidad, facilita el mantenimiento y permite la reutilización de componentes en otros programas.

**2. Validaciones Robustas**
   - *Tarea*: Implementar validaciones de entrada que manejan escenarios excepcionales y aseguran que los datos procesados sean válidos.
   - *Por qué es importante*: Garantiza que el programa funcione correctamente incluso en condiciones inesperadas, mejorando la confiabilidad.

**3. Mejora de la experiencia del usuario**
   - *Tarea*: Diseñar mensajes claros y educativos que informan al usuario sobre el progreso del programa y cómo corregir errores en caso de entradas no válidas.
   - *Por qué es importante*: La interacción fluida y comprensible con el usuario hace que el programa sea más accesible, especialmente para principiantes.

**4. Adherencia a Estándares de Estilo**
   - *Tarea*: Usar las directrices del *PEP 8* para garantizar un código limpio y bien estructurado.
   - *Por qué es importante*: Un código que cumple con estándares es más fácil de leer y entender, tanto para el autor como para otros desarrolladores.

**5. Documentación Clara**
   - *Tarea*: Incluir comentarios significativos y docstrings para explicar la lógica y el propósito de cada parte del código.
   - *Por qué es importante*: La documentación es esencial para facilitar la comprensión y el mantenimiento del programa a largo plazo.

**6. Eficiencia y Escalabilidad**
   - *Tarea*: Identificar posibles cuellos de botella y simplificar la lógica para que el programa utilice menos recursos.
   - *Por qué es importante*: Un código eficiente puede manejar datos más grandes y escenarios más complejos sin afectar el rendimiento.

**7. Flexibilidad para Extensiones Futuras**
   - *Tarea*: Diseñar el código de manera que sea fácil de modificar o ampliar con nuevas funcionalidades.
   - *Por qué es importante*: Los programas rara vez permanecen estáticos; una buena base permite adaptarse a nuevas necesidades.

A continuación, muestro el ejemplo de un conjunto  de instrucciones, llamado **prompt**, claro y completo, para solicitar la optimización del script en Python, usando ChatGPT, que ustedes pueden copiar y probar:

```markdown
Optimiza el siguiente script en Python manteniendo su funcionalidad original pero mejorando su eficiencia, legibilidad y adaptabilidad. Asegúrate de:

1. Usar las mejores prácticas de programación en Python (e.g., nombres descriptivos, estructura clara, PEP 8).
2. Minimizar el código redundante y simplificar la lógica donde sea posible.
3. Implementar validaciones robustas para entradas.
4. Mejorar la experiencia del usuario con mensajes claros.
5. Documentar el código con comentarios significativos.
6. Considerar posibles escenarios excepcionales y manejarlos adecuadamente.

Aquí está el script original:

```python
# es_par_o_impar_mejorado.py
# Algoritmo: Determinar si un número es par o impar, con validaciones
# Versión 2
# Autor: profe J. Zavala
# Fecha: 2 de diciembre de 2024

# Inicio del algoritmo (No tiene equivalente directo en Python, solo se comenta)

# Definir variables y tipos de datos
numero = None  # En Python, las variables no necesitan declaración previa
es_valido = False  # Inicializar la variable lógica como Falso

# Entrada
while not es_valido:  # Mientras No es_valido Hacer
    print("Ingresa un número entero:")  # Escribir "Ingresa un número entero:"
    try:
        numero = int(input())  # Leer numero; Se intenta convertir la entrada a entero
        
        # Validación de entrada
        # Si EsNumero(numero) Entonces
        es_valido = True  # Si la conversión tiene éxito, es válida
    except ValueError:
        # Sino
        print("Error: Entrada no válida. Por favor, ingresa un número entero.")  # Escribir "Error..."
    # Fin Si (El bloque try-except reemplaza esta parte)
# Fin Mientras (El bucle termina aquí)

# Proceso
if numero % 2 == 0:  # Si (numero % 2 == 0) Entonces
    # Salida:
    print(f"El número {numero} es par.")  # Escribir "El número ", numero, " es par."
else:
    # Salida:
    print(f"El número {numero} es impar.")  # Escribir "El número ", numero, " es impar."
# Fin Si (Fin del condicional)

# Fin del algoritmo (No tiene equivalente directo en Python, solo se comenta)
```

Por favor, devuelve el código optimizado acompañado de una explicación de los cambios realizados y cómo mejoran el script. 

```

Este *prompt*, diseñado para obtener una versión mejorada del código con una justificación detallada de las optimizaciones aplicadas, generó la siguiente respuesta de ChatGPT:

```markdown
Aquí tienes la versión optimizada del script, seguida de una explicación detallada de los cambios realizados:

### **Script Optimizado**
```python
"""
es_par_o_impar_optimizado.py
Algoritmo: Determinar si un número es par o impar, con validaciones.
Versión optimizada
Autor: profe J. Zavala
Fecha: 2 de diciembre de 2024
"""

def obtener_numero_entero():
    """
    Solicita al usuario un número entero con validación robusta.
    Retorna:
        int: El número entero ingresado por el usuario.
    """
    while True:
        try:
            numero = int(input("Ingresa un número entero: "))
            return numero  # Retorna el número si es válido
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingresa un número entero.")


def determinar_paridad(numero):
    """
    Determina si un número es par o impar.
    Parámetros:
        numero (int): Número a evaluar.
    """
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")


def main():
    """
    Función principal que coordina la ejecución del programa.
    """
    print("Bienvenido al programa para determinar si un número es par o impar.")
    numero = obtener_numero_entero()  # Solicita un número entero al usuario
    determinar_paridad(numero)  # Evalúa la paridad del número
    print("Gracias por usar el programa. ¡Hasta la próxima!")


if __name__ == "__main__":
    main()
```

---

### **Explicación de los Cambios y Mejoras**

1. **Estructuración en funciones**:
   - Dividí el código en funciones bien definidas para mejorar la modularidad y legibilidad:
     - `obtener_numero_entero`: Encargada de solicitar y validar la entrada del usuario.
     - `determinar_paridad`: Evalúa si el número es par o impar y muestra el resultado.
     - `main`: Coordina el flujo principal del programa.
   - Esto facilita la reutilización del código y permite realizar pruebas unitarias fácilmente.

2. **Validación robusta de entradas**:
   - La función `obtener_numero_entero` incluye un bucle `while` infinito que garantiza que el programa no avanzará hasta que el usuario ingrese un número entero válido.
   - El mensaje de error es claro y educativo para una mejor experiencia del usuario.

3. **Uso de `try`-`except` para manejo de excepciones**:
   - Permite manejar entradas no válidas (como cadenas o valores vacíos) sin que el programa se cierre inesperadamente.

4. **Separación de lógica y presentación**:
   - La lógica de determinar si un número es par o impar está en `determinar_paridad`.
   - Los mensajes están centralizados, lo que facilita su modificación en el futuro (por ejemplo, para traducciones).

5. **Adherencia a PEP 8**:
   - El código sigue el estándar de estilo de Python:
     - Uso de nombres descriptivos para funciones y variables.
     - Espaciado adecuado entre bloques de código.
     - Comentarios y docstrings para describir funciones y el propósito general del script.

6. **Mejora de la experiencia del usuario**:
   - Se añadió un mensaje de bienvenida y de despedida en la función `main` para hacer el programa más amigable.

7. **Flexibilidad y adaptabilidad**:
   - El diseño modular permite añadir fácilmente nuevas funcionalidades, como probar múltiples números en una sola ejecución o evaluar listas de números.

---

Con esta optimización, el script es más claro, eficiente y fácil de mantener, mientras conserva la funcionalidad original.
```

La metodología de programación esbozada proporciona un marco claro y efectivo para resolver problemas computacionales. Desde el planteamiento del problema hasta la optimización y documentación, cada paso es esencial para garantizar soluciones robustas y funcionales. Con herramientas modernas como la IA, este proceso se vuelve más accesible y eficiente, permitiendo concentrarse en lo más importante: resolver problemas y crear soluciones innovadoras.

### **4. Conclusiones**

Resolver problemas con algoritmos no solo es un pilar en la programación, sino también una habilidad clave en la resolución de problemas en general. Al seguir una metodología clara y estructurada, es posible desglosar problemas complejos en pasos simples y manejables. Esta lectura destacó los siguientes aspectos clave:

1. **Importancia de los Algoritmos**: Los algoritmos son esenciales para estructurar el pensamiento lógico y encontrar soluciones eficientes. Desde la vida cotidiana hasta los sistemas avanzados, son herramientas universales.
2. **Papel del Pseudocódigo**: Sirve como puente entre la lógica humana y los lenguajes de programación. Herramientas como PSeInt son valiosas para aprender y practicar.
3. **Traducción al Lenguaje de Programación**: Convertir pseudocódigo a un lenguaje como Python es un paso crucial, que requiere atención a la lógica y la sintaxis específicas.
4. **Pruebas y Optimización**: Validar y optimizar algoritmos asegura que las soluciones sean precisas, robustas y eficientes. La IA es un aliado poderoso en este proceso.
5. **Habilidades Transferibles**: El diseño de algoritmos fomenta habilidades que trascienden la programación, como el análisis crítico, la creatividad y la resolución de problemas.

La integración de herramientas modernas y el aprendizaje continuo permiten que los estudiantes no solo dominen los fundamentos, sino que también estén preparados para abordar desafíos más complejos en el futuro.

### **5. Bibliografía Indispensable**

A continuación, las referencias indispensables para aprender a programar y resolver problemas de programación, incluyendo análisis de datos y el uso de herramientas modernas como ChatGPT. Estas referencias abarcan desde fundamentos básicos hasta enfoques aplicados, tanto en español como en inglés, y son ideales para estudiantes que buscan desarrollar habilidades de resolución de problemas mediante la programación.


1. Bravo, C., & Plaza, S. (2020). *Introducción a la programación con Python: Resolución de problemas con aplicaciones prácticas*. Madrid: Editorial Paraninfo.  
   Este libro ofrece una introducción amigable al lenguaje Python, con énfasis en resolver problemas prácticos, incluyendo casos aplicados al análisis de datos y la toma de decisiones.

2. Deitel, P., & Deitel, H. (2020). *Cómo programar en Python*. Ciudad de México: Pearson Educación.  
   Un enfoque moderno en Python que incluye ejercicios orientados a la resolución de problemas reales, especialmente útiles para estudiantes que buscan desarrollar habilidades aplicadas.

3. Evkaya, O., & de Carvalho, M. (2024). Decoding AI: The inside story of data analysis in ChatGPT. *arXiv*. Cornell University. [https://arxiv.org/abs/2404.08480](https://arxiv.org/abs/2404.08480)  
   Este trabajo analiza las capacidades de ChatGPT para resolver problemas de análisis de datos, desde la creación de pipelines automatizados hasta la interpretación de resultados. También ofrece una visión crítica sobre las limitaciones y consideraciones éticas al usar herramientas de IA en el análisis de grandes conjuntos de datos.

4. Marzal, A. & Gracia, I. (2003). *Introducción a la programación con Python*. España: Universitat Jaume I. [http://persoal.citius.usc.es/eva.cernadas/informaticaparacientificos/material/libros/ippython.pdf](http://persoal.citius.usc.es/eva.cernadas/informaticaparacientificos/material/libros/ippython.pdf).
   Este texto combina teoría con práctica, enfatizando el aprendizaje progresivo y el análisis de problemas desde una perspectiva algorítmica. Es una excelente guía para quienes comienzan en la programación y desean explorar dos lenguajes con enfoques complementarios: Python y Lenguaje C. Más de 480 ejercicios diseñados para reforzar conceptos y fomentar la práctica activa.

--- 

[^1]: Profesor-investigador del Departamento de Economía de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Contacto: [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx), [Telegram](https://t.me/jzavalar).
[^2]: Lectura leída el 2 de diciembre de 2024.

Ultima actualización: 2 de diciembre de 2024.
