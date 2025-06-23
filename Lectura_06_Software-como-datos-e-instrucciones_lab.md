## Práctica de Laboratorio: Software como Datos e Instrucciones en RStudio.cloud
**Duración:** 30 minutos  
**Nivel:** Estudiantes universitarios de nuevo ingreso  
**Entorno:** RStudio.cloud  
**Modalidad:** Laboratorio de computación

### Objetivos de Aprendizaje

Al finalizar esta práctica, el estudiante será capaz de:

1. Distinguir conceptualmente entre software como datos y software como instrucciones
2. Experimentar prácticamente los procesos de interpretación inmediata y "compilación" de documentos
3. Analizar las diferencias entre código R, scripts y documentos R Markdown
4. Evaluar cómo el mismo código puede existir como archivo (datos) y como instrucciones ejecutables

### Antecedentes y Conocimientos Previos

#### Conocimientos que Utilizarás en Esta Práctica:

**Conceptos de Informática Básica:**
- **Archivo vs. Programa:** Recordar que un archivo puede contener información (datos) o ser ejecutable (instrucciones)
- **Sistemas Operativos:** El software necesita un sistema operativo para ejecutarse
- **Entrada → Procesamiento y Almacenamiento → Salida:** Las 4 operaciones básicas de la computadora (incluye almacenamiento de datos y código fuente)
- **Script vs. Código fuente:** Un script es código fuente diseñado para automatizar tareas

**Conceptos de Administración:**
- **Datos vs. Información:** Los datos se procesan para generar información útil para toma de decisiones
- **Documentación:** Importancia de documentar procesos para su reproducción
- **Reportes:** Transformación de análisis técnicos en documentos ejecutivos

**Experiencia Previa Esperada:**
- Uso básico de navegador web
- Operaciones básicas con archivos (guardar, abrir, copiar)
- Navegación en interfaces gráficas

> **Objetivo central:** Al final de esta práctica, comprenderás por qué el mismo código puede ser tanto información almacenada (datos) como órdenes ejecutables (instrucciones), concepto fundamental para entender cómo funcionan los sistemas de información empresariales.

### Preparación Inicial: Crear Cuenta y Acceder a RStudio.cloud (5 minutos)

#### Paso 0A: Crear Cuenta en RStudio.cloud

**Si ya tienes cuenta, salta al Paso 0B. Si no:**

1. Abrir navegador web (Chrome, Firefox, Safari, Edge)
2. Ir a: `https://rstudio.cloud`
3. Click en "Get Started" (botón en la parte superior)
4. Click en "Sign Up" 
5. Elegir método de registro:
   - **Opción A:** "Sign up with Google" (más rápido si tienes Gmail)
   - **Opción B:** "Sign up with GitHub" (si tienes cuenta GitHub)
   - **Opción C:** "Sign up with email" (crear cuenta nueva)

**Para registro con email:**
- **Email:** tu correo electrónico
- **Password:** contraseña segura (mínimo 8 caracteres)
- **First name:** tu nombre
- **Last name:** tu apellido
- Click en "Sign Up"
- Revisar tu email y click en el enlace de confirmación

6. Verificar acceso: Debes ver la página principal de RStudio.cloud

#### Paso 0B: Acceder y Crear Proyecto

1. Iniciar sesión en `https://rstudio.cloud` (si no estás ya dentro)
2. Crear nuevo proyecto:
   - Click en "New Project" (botón azul en la parte superior)
   - Seleccionar "New RStudio Project"
   - Esperar 60-90 segundos mientras se configura el entorno

**Verificación:** ¿Ves una interfaz dividida en paneles con código, consola, archivos, etc.? Si no, pide ayuda.

#### Paso 0C: Orientación del Entorno RStudio.cloud

**Concepto clave:** RStudio.cloud es un entorno de desarrollo integrado (IDE) que funciona en tu navegador, basado en Ubuntu Linux.

**Lo que verás al cargar:**
- **Panel superior izquierdo:** Editor de código (donde escribirás scripts)
- **Panel inferior izquierdo:** Consola R + Terminal Ubuntu Linux
- **Panel superior derecho:** Environment (variables) + History
- **Panel inferior derecho:** Files + Plots + Packages + Help

**Punto de atención:** Este entorno tiene dos sistemas operativos trabajando juntos:
- Tu computadora: Windows/Mac/Linux local
- RStudio.cloud: Ubuntu Linux en la nube

**Recordatorio:** Un IDE es como una "oficina completa" para programar, con todas las herramientas necesarias en un solo lugar, similar a como Microsoft Office integra Word, Excel y PowerPoint.

### Marco Conceptual Breve (5 minutos)

#### La Naturaleza Dual del Software en el Contexto de R

**Concepto central a aprender:** El software tiene una naturaleza dual que es fundamental para entender toda la informática moderna.

**Recordatorio:** Piensa en una receta de cocina:
- Como información: Es texto en papel que puedes leer, copiar o modificar
- Como instrucciones: Cuando la sigues paso a paso, produce un platillo real

En RStudio.cloud observaremos cómo el software manifiesta esta misma dualidad:

**Software como datos:**
- Archivos `.R` y `.Rmd` almacenados en el sistema Ubuntu Linux
- Scripts y código fuente que pueden ser editados, copiados, modificados (como texto)
- Información que ocupa espacio de almacenamiento en el servidor

**Software como instrucciones:**
- Comandos ejecutados en la consola de R
- Transformación de datos de entrada en resultados específicos
- Documentos R Markdown que se "compilan" a HTML/PDF

**Punto clave:** Durante esta práctica, observa cómo el mismo código puede existir en ambos estados simultáneamente.

---

### ACTIVIDAD 1: Explorando el Software como Datos (8 minutos)

**Concepto a observar:** En esta actividad verás cómo el código fuente de R es información almacenada que puedes manipular como cualquier archivo de texto.

**Antecedente:** Recuerda que todo archivo en una computadora es fundamentalmente datos hasta que algo lo interprete o ejecute. Un script es código fuente escrito para automatizar tareas específicas.

#### Paso 1: Crear un script R simple (3 minutos)

**Instrucciones detalladas:**

1. **Crear nuevo archivo R:**
   - Localizar la barra de menú superior
   - Click en "File" (primera opción del menú)
   - Mover cursor hacia abajo hasta "New File"
   - Aparecerá un submenú → Click en "R Script"
   - Resultado: Se abrirá una pestaña nueva llamada "Untitled1"

**Observa:** En este momento, aún no tienes "software" - solo tienes un archivo vacío esperando contenido.

2. **Escribir el código exactamente como aparece:**
   - Click en el área blanca del nuevo archivo
   - Copiar y pegar o escribir el siguiente código:

```r
## mi_primer_script.R
## Script para demostrar software como datos e instrucciones

## Solicitar nombre del usuario
nombre <- readline(prompt = "¿Cómo te llamas? ")

## Procesar información
mensaje <- paste("¡Hola", nombre, "! Bienvenido a la programación en R.")
num_caracteres <- nchar(nombre)

## Mostrar resultados
print(mensaje)
print(paste("Tu nombre tiene", num_caracteres, "caracteres."))

## Crear un pequeño análisis
datos_nombre <- data.frame(
  nombre = nombre,
  longitud = num_caracteres,
  vocales = stringr::str_count(tolower(nombre), "[aeiou]")
)

print("Análisis de tu nombre:")
print(datos_nombre)
```

3. **Guardar el archivo:**
   - Presionar: `Ctrl + S` (Windows) o `Cmd + S` (Mac)
   - Alternativa: Click en "File" → "Save"
   - Aparecerá ventana "Save File As"
   - En el campo "File name" escribir: `mi_primer_script.R`
   - Click en "Save" (botón azul)
   - Verificar: La pestaña ahora dice "mi_primer_script.R" (ya no "Untitled1")

**Momento clave:** Acabas de crear software como datos - el archivo existe en el sistema de archivos Ubuntu Linux de RStudio.cloud, pero aún no ha "hecho" nada.

**Verificación:** ¿Ves el nombre del archivo en la pestaña? Si no, repite el paso de guardar.

#### Paso 2: Observar el software como datos (5 minutos)

**Concepto a demostrar:** El software almacenado se comporta exactamente como información - puedes copiarlo, renombrarlo, moverlo, etc.

**Recordatorio:** En sistemas Unix/Linux (como Ubuntu que usa RStudio.cloud), todo es un archivo - incluso las instrucciones ejecutables son archivos especiales.

**Instrucciones detalladas para explorar archivos:**

1. **Localizar el panel "Files":**
   - Mirar hacia el panel inferior derecho de la pantalla
   - Buscar las pestañas: "Files", "Plots", "Packages", "Help"
   - Click en la pestaña "Files" si no está activa (debe verse resaltada)

**Observa:** Estás viendo el sistema de archivos Ubuntu Linux donde se ejecuta R. Es como explorar una carpeta en tu computadora, pero en la nube.

2. **Encontrar tu archivo:**
   - En la lista de archivos, buscar `mi_primer_script.R`
   - Verificar que aparece con un ícono de documento
   - Observar la columna "Size" (tamaño del archivo)
   - Anotar el tamaño: _________ bytes

**Punto clave:** Este archivo ocupa espacio de almacenamiento real en el servidor Ubuntu. Es datos físicamente almacenados.

3. **Experimentar con operaciones de archivo:**
   
   **Operación A - Renombrar:**
   - Click derecho sobre `mi_primer_script.R`
   - Seleccionar "Rename" del menú contextual
   - Escribir nuevo nombre: `copia_script.R`
   - Presionar Enter para confirmar
   - Verificar: Ahora tienes dos archivos (original + copia)

**Concepto demostrado:** Puedes manipular el script como información - copiarlo, renombrarlo, etc. Esto prueba que es software como datos.

   **Operación B - Ver propiedades:**
   - Click en el archivo `mi_primer_script.R` para seleccionarlo
   - Observar información en la parte inferior del panel Files
   - Anotar la fecha de modificación: _________________

   **Operación C - Abrir como texto:**
   - Click derecho en `mi_primer_script.R`
   - Seleccionar "View File"
   - Observar: Se abre una nueva pestaña mostrando el contenido
   - Pregunta: ¿Puedes leer el código fuente como texto normal? Sí / No

**Revelación importante:** El código fuente de R es simplemente texto legible almacenado en archivos. No hay "magia" - es información que los humanos pueden leer y editar.

4. **Completar tabla de reflexión:**

| Observación | ¿Qué significa? | Tu respuesta |
|-------------|-----------------|--------------|
| El archivo aparece en el explorador | Es datos almacenados en Ubuntu Linux | ✓ Sí / ✗ No |
| Se puede renombrar y copiar | Se comporta como información | ✓ Sí / ✗ No |
| El contenido es código fuente legible | Es script editable por humanos | ✓ Sí / ✗ No |
| No ha "hecho" nada aún | Está inactivo hasta ser ejecutado | ✓ Sí / ✗ No |

**Conexión con administración:** En empresas, los scripts de análisis de datos se almacenan como archivos, se respaldan, se versionan y se comparten - exactamente como cualquier documento administrativo.

**Checkpoint:** Antes de continuar, asegúrate de tener al menos un archivo `.R` visible en el panel Files.

---

### ACTIVIDAD 2: Experimentando la Interpretación en R (8 minutos)

**Concepto central:** Ahora transformarás el software como datos en software como instrucciones - verás la "magia" de la ejecución.

**Antecedente:** Un intérprete es un programa que lee código fuente línea por línea y lo ejecuta inmediatamente. R es un lenguaje interpretado (como Python o JavaScript).

**Contraste con lenguajes compilados:** A diferencia de C++ o Java, R no necesita ser "compilado" antes de ejecutarse - puede ejecutar scripts directamente desde archivos de código fuente.

#### Paso 1: Ejecutar como instrucciones (4 minutos)

**Instrucciones muy detalladas para ejecutar código:**

1. **Preparar el entorno (instalar paquete):**
   - Localizar la consola de R (panel inferior izquierdo)
   - Buscar el símbolo `>` (prompt de R)
   
**Nota técnica:** Esta consola ejecuta R dentro del sistema Ubuntu Linux de RStudio.cloud. También tienes acceso a una Terminal Ubuntu (pestaña "Terminal" junto a "Console") para comandos Linux directos si fuera necesario.

   - Click después del símbolo `>`
   - Escribir exactamente: `install.packages("stringr")`
   - Presionar Enter
   - Esperar 30-60 segundos (verás texto instalando el paquete)

**Observa:** El intérprete R está descargando e instalando código desde internet. El paquete se almacena en el sistema Ubuntu Linux.

   - Cuando reaparezca el `>`, escribir: `library(stringr)`
   - Presionar Enter

**Concepto:** `library()` carga el código del paquete en la memoria de R - transformando datos almacenados en funciones ejecutables.

**Si aparece error:** Levanta la mano para pedir ayuda.

2. **Volver al archivo de código:**
   - Click en la pestaña `mi_primer_script.R` (panel superior izquierdo)
   - Verificar que puedes ver todo tu script

3. **Ejecutar código de tres maneras:**

   **Método A - Línea por línea (interpretación pura):**
   
**Concepto clave:** Verás cómo R interpreta cada línea de código fuente inmediatamente, sin necesidad de compilar todo el programa primero.

   - Click al inicio de la primera línea con código (no comentario)
   - La línea es: `nombre <- readline(prompt = "¿Cómo te llamas? ")`
   - Presionar: `Ctrl + Enter` (Windows) o `Cmd + Enter` (Mac)
   
**Observa cuidadosamente:** 
   - ¿La línea se copió a la consola?
   - ¿Aparece una pregunta esperando tu respuesta?
   
   - ¿Aparece una pregunta? Sí / No
   - Escribir tu nombre en la consola y presionar Enter
   
**Momento revelador:** ¡El código inactivo se convirtió en instrucciones ejecutándose! R interpretó la línea y ejecutó la función `readline()`.

   **Continuar con las siguientes líneas:**
   - Click en la línea: `mensaje <- paste("¡Hola", nombre, "! Bienvenido a la programación en R.")`
   - Presionar: `Ctrl + Enter`
   
**Observa:** R tomó la variable `nombre` (almacenada en memoria) y creó una nueva variable `mensaje`.

   - Click en la línea: `print(mensaje)`
   - Presionar: `Ctrl + Enter`
   - ¿Apareció tu mensaje personalizado? Sí / No

**Revelación:** El mismo código que era texto inerte ahora está produciendo resultados - se transformó de datos a instrucciones.

   **Método B - Seleccionar varias líneas:**
   - Click y arrastrar para seleccionar estas 3 líneas juntas:
     ```r
     num_caracteres <- nchar(nombre)
     print(mensaje)
     print(paste("Tu nombre tiene", num_caracteres, "caracteres."))
     ```
   - Presionar: `Ctrl + Enter`
   - Observar resultados en consola

**Concepto:** R puede interpretar múltiples líneas secuencialmente, manteniendo el estado de las variables en memoria.

   **Método C - Todo el script:**
   - Presionar: `Ctrl + Shift + Enter` (ejecutar todo)
   - Nota: Como `readline` necesita interacción, esto puede no funcionar completamente

#### Paso 2: Análisis del proceso de interpretación (4 minutos)

**Objetivo analítico:** Documenta evidencia observable de la transformación de software-datos a software-instrucciones.

**Recordatorio:** En administración, entender procesos es clave. Aquí analizarás el proceso de interpretación como cualquier proceso empresarial.

**Instrucciones para documentar observaciones:**

1. **Completar tabla de observaciones:**
   - Mira cada panel de RStudio.cloud mientras ejecutas código
   - Completa la siguiente tabla marcando lo que observas:

| Panel RStudio | ¿Qué ves ahora? | Evidencia de interpretación |
|---------------|-----------------|----------------------------|
| **Source** (sup. izq.) | ☐ Código coloreado<br>☐ Cursor en líneas ejecutadas | Software como datos (texto estático) |
| **Console** (inf. izq.) | ☐ Comandos ejecutados<br>☐ Resultados mostrados<br>☐ Símbolo `>` activo | Software como instrucciones (ejecución dinámica) |
| **Environment** (sup. der.) | ☐ Variables creadas<br>☐ Valores almacenados | Resultados de la ejecución (memoria activa) |
| **Files** (inf. der.) | ☐ Archivos sin cambios<br>☐ Mismo tamaño | Software como datos (archivos inalterados) |

**Concepto revelado:** Los paneles muestran diferentes estados del mismo software simultáneamente:
- Source: Estado estático (datos)
- Console: Estado dinámico (instrucciones)
- Environment: Estado resultante (información procesada)

2. **Experimento controlado (detectar errores):**

**Objetivo:** Demostrar cuándo el intérprete detecta errores - concepto crucial para debugging.

   **Introducir error deliberado:**
   - En una línea nueva del script, escribir: `print(mensaje`
   - Nota: Falta el paréntesis de cierre `)` deliberadamente
   - Ejecutar esta línea: `Ctrl + Enter`
   
   **Documentar qué sucede:**
   - ¿Aparece error en consola? Sí / No
   - ¿Cuándo se detectó el error? 
     ☐ Al escribir el código (en el editor)
     ☐ Al intentar ejecutarlo (en la consola)
   - Escribe el mensaje de error: ___________________________

**Concepto clave:** Los lenguajes interpretados detectan errores en tiempo de ejecución, no en tiempo de escritura.

   **Corregir el error:**
   - Agregar el paréntesis que falta: `print(mensaje)`
   - Ejecutar nuevamente: `Ctrl + Enter`
   - ¿Ahora funciona? Sí / No

3. **Conclusión del experimento:**
   **Pregunta:** ¿En qué momento el intérprete R detecta los errores?
   ☐ Cuando escribo el código
   ☐ Cuando intento ejecutar el código
   ☐ Cuando guardo el archivo

**Implicación práctica:** En sistemas empresariales, los errores en scripts automatizados se detectan durante la ejecución, no antes. Por eso es importante probar todo código antes de ponerlo en producción.

**Comparación con otros sistemas:**
- Excel: Los errores se ven inmediatamente en las celdas
- R interpretado: Los errores se ven al ejecutar
- Sistemas compilados: Los errores se detectan antes de ejecutar

**Checkpoint:** Debes tener variables en el panel "Environment" antes de continuar.

---

### ACTIVIDAD 3: Explorando la "Compilación" con R Markdown (7 minutos)

**Concepto revolucionario:** Ahora verás un proceso híbrido - R Markdown combina texto + código y los "compila" en un documento final. Es como tener un reporte que se escribe solo.

**Antecedente:** A diferencia de la interpretación línea por línea, la "compilación" procesa todo el documento de una vez para crear un producto final diferente.

**Relevancia empresarial:** R Markdown automatiza la creación de reportes ejecutivos - imagina un reporte de ventas que se actualiza automáticamente cada mes con nuevos datos.

#### Paso 1: Crear documento R Markdown (3 minutos)

**Instrucciones muy detalladas:**

1. **Crear nuevo archivo R Markdown:**
   - Click en "File" (menú superior)
   - Mover cursor hacia "New File"
   - En el submenú, click en "R Markdown..."
   - Aparecerá ventana "New R Markdown"

**Nota:** R Markdown es una tecnología de programación literaria - combinas explicaciones en texto natural con código ejecutable.

2. **Configurar el documento:**
   - En "Title" escribir: `Mi Primer Reporte`
   - En "Author" escribir: tu nombre
   - Verificar que "HTML" esté seleccionado (debe estar marcado)
   - Click en "OK" (botón azul)

3. **Resultado esperado:**
   - Nueva pestaña llamada "Untitled1" se abre
   - Verás contenido predeterminado del template
   - Hay texto normal y bloques de código (fondo gris)

**Observa la diferencia:** Este archivo combina tres tipos de contenido:
- Metadatos (sección YAML al inicio)
- Texto narrativo (explicaciones en lenguaje natural)  
- Código fuente ejecutable (bloques con fondo gris)

4. **Reemplazar todo el contenido:**
   - Seleccionar todo: `Ctrl + A` (Windows) o `Cmd + A` (Mac)
   - Borrar el contenido seleccionado
   - Copiar y pegar el siguiente código fuente completo:

````markdown
---
title: "Análisis de Nombres - Mi Primer Reporte"
author: "Tu Nombre"
date: "`r Sys.Date()`"
output: html_document
---

### Introducción

Este documento demuestra cómo el mismo código R puede existir como:
- **Datos**: archivo .Rmd editable
- **Instrucciones**: código ejecutable  
- **Documento compilado**: reporte HTML final

### Análisis Interactivo

```{r setup, include=FALSE}
library(stringr)
```

```{r analisis}
## Código que se ejecutará y mostrará resultados
nombres_ejemplo <- c("María", "José", "Ana", "Carlos")

analisis_nombres <- data.frame(
  nombre = nombres_ejemplo,
  longitud = nchar(nombres_ejemplo),
  vocales = stringr::str_count(tolower(nombres_ejemplo), "[aeiou]"),
  consonantes = nchar(nombres_ejemplo) - stringr::str_count(tolower(nombres_ejemplo), "[aeiou]")
)

print("Análisis de nombres de ejemplo:")
analisis_nombres
```

### Visualización

```{r grafico}
barplot(analisis_nombres$longitud, 
        names.arg = analisis_nombres$nombre,
        main = "Longitud de Nombres",
        ylab = "Número de Caracteres",
        col = "lightblue")
```

### Conclusión

El software muestra su naturaleza dual: este documento existe como código fuente (datos) y genera un reporte interactivo (instrucciones ejecutadas).
````

5. **Guardar el archivo:**
   - Presionar: `Ctrl + S` (Windows) o `Cmd + S` (Mac)
   - En "File name" escribir: `mi_reporte.Rmd`
   - Click en "Save"
   - Verificar: La pestaña ahora dice "mi_reporte.Rmd"

**Momento clave:** Acabas de crear un documento fuente que combina:
- Datos (texto explicativo)
- Scripts (código fuente R)
- Metainstrucciones (comandos de formato para compilar)

**Verificación:** ¿Ves bloques de código con fondo gris en tu documento? Si no, revisa que hayas pegado todo el contenido correctamente.

#### Paso 2: Proceso de "compilación" (4 minutos)

**Concepto a observar:** La "compilación" de R Markdown es radicalmente diferente a la interpretación línea por línea de R. Aquí se procesa todo el documento para crear un producto completamente nuevo.

**Recordatorio:** En lenguajes tradicionales compilados (como C++), se convierte código fuente a código máquina. Aquí convertimos documento fuente a documento publicable.

**Instrucciones paso a paso para compilar:**

1. **Observar el archivo .Rmd antes de compilar:**
   - Ir al panel "Files" (inferior derecho)
   - Buscar `mi_reporte.Rmd` en la lista
   - Anotar el tamaño: _________ bytes
   - Pregunta: ¿Es un archivo de código fuente editable? Sí / No

**Estado actual:** El archivo es software como datos - código fuente almacenado en el sistema Ubuntu Linux.

2. **Iniciar el proceso de compilación:**
   - Asegúrate de estar en la pestaña `mi_reporte.Rmd`
   - Localizar el botón "Knit" en la barra de herramientas
     - Está cerca de la parte superior del panel de código
     - Tiene un ícono de ovillo de lana azul
   - Click en "Knit"
   - Alternativa: Presionar `Ctrl + Shift + K`

**Inicia la magia:** El sistema comenzará un proceso complejo de transformación.

3. **Observar el proceso de compilación:**

**Atención:** Verás múltiples pasos ejecutándose automáticamente:

   - Aparecerá pestaña "R Markdown" (panel inferior izquierdo)
   - Verás mensajes como:
     ```
     processing file: mi_reporte.Rmd
     |.....................| 100%
     ordinary text without R code
     ```
   - Esperar 30-90 segundos (no cerrar nada)

**Proceso en tiempo real:** 
1. knitr extrae y ejecuta el código R
2. R procesa las instrucciones y genera resultados
3. pandoc convierte todo a HTML con formato

   - El proceso termina cuando aparece: "Output created: mi_reporte.html"

**Diferencia clave:** A diferencia de la interpretación inmediata, este proceso requiere múltiples programas trabajando juntos en el sistema Ubuntu Linux.

4. **Verificar resultados:**
   - Nueva pestaña se abre automáticamente mostrando el reporte HTML
   - En panel "Files", ahora debes ver DOS archivos:
     - `mi_reporte.Rmd` (archivo original - datos)
     - `mi_reporte.html` (archivo compilado - producto final)

**Transformación completada:** El mismo contenido ahora existe en dos formas diferentes:
- Forma editable (.Rmd) - para desarrolladores/analistas
- Forma presentable (.html) - para ejecutivos/clientes

5. **Completar tabla de comparación:**

| Archivo | Estado | Tamaño | ¿Puedes editarlo? | ¿Necesita R? |
|---------|--------|---------|-------------------|--------------|
| **mi_reporte.Rmd** | Código fuente | _____ KB | ☐ Sí ☐ No | ☐ Sí ☐ No |
| **mi_reporte.html** | "Compilado" | _____ KB | ☐ Sí ☐ No | ☐ Sí ☐ No |

6. **Explorar el resultado compilado:**
   - En la pestaña HTML, desplázate hacia abajo
   - ¿Ves la tabla de datos? Sí / No
   - ¿Ves el gráfico de barras? Sí / No
   - ¿El código está visible o solo los resultados? _______________

**Revelación empresarial:** El archivo HTML puede enviarse a cualquier persona - no necesita R, RStudio, ni conocimientos técnicos. Solo un navegador web.

**Concepto final:** Has presenciado cómo software como datos (archivo .Rmd) se procesa para crear información consumible (archivo .html) a través de un proceso automatizado.

**Si aparece error:** Asegúrate de que el paquete `stringr` esté instalado. Si no funciona, levanta la mano.

**Checkpoint:** Debes tener un archivo HTML visible antes de continuar a la siguiente actividad.

---

### ACTIVIDAD 4: Comparación Crítica y Síntesis (5 minutos)

**Objetivo integrador:** Sintetiza toda tu experiencia para entender las implicaciones prácticas de la naturaleza dual del software en contextos empresariales.

**Conexión administrativa:** Como futuro administrador, trabajarás con sistemas que tienen estas mismas características - hojas de cálculo con macros, sistemas ERP, reportes automatizados, etc.

**Instrucciones para completar el análisis:**

#### Tabla Comparativa: Completar con tus observaciones

**Instrucciones analíticas:**
1. Revisar cada archivo que creaste
2. Completar la tabla basándote en tu experiencia directa
3. Relacionar con situaciones empresariales que conoces

| Aspecto | Script R (.R) | R Markdown (.Rmd) | HTML Compilado |
|---------|---------------|-------------------|----------------|
| **¿Se puede editar?** | ☐ Sí ☐ No | ☐ Sí ☐ No | ☐ Sí ☐ No |
| **¿Se ejecuta directamente?** | ☐ Sí ☐ No | ☐ Sí ☐ No | ☐ Sí ☐ No |
| **Tamaño aproximado** | _____ KB | _____ KB | _____ KB |
| **Necesita R para funcionar** | ☐ Sí ☐ No | ☐ Sí ☐ No | ☐ Sí ☐ No |
| **Se puede compartir fácilmente** | ☐ Sí ☐ No | ☐ Sí ☐ No | ☐ Sí ☐ No |

#### Preguntas de Reflexión Crítica:

**Aplicación empresarial - Responde basándote en tu experiencia:**

1. **¿Por qué es útil que el mismo código pueda existir en diferentes formatos?**
   Tu respuesta: ________________________________________________
   ____________________________________________________________

**Pista:** Piensa en diferentes audiencias (analistas vs. ejecutivos vs. clientes).

2. **Si fueras gerente y necesitas un reporte para una junta directiva, ¿qué formato usarías?**
   ☐ Script R (.R)
   ☐ R Markdown (.Rmd)  
   ☐ HTML compilado
   
   **¿Por qué?** _______________________________________________

**Considera:** ¿Qué conocimientos técnicos tienen los directivos?

3. **Si eres un analista que necesita actualizar los cálculos cada mes, ¿qué formato preferirías?**
   ☐ Script R (.R)
   ☐ R Markdown (.Rmd)
   ☐ HTML compilado
   
   **¿Por qué?** _______________________________________________

**Considera:** ¿Qué necesitas modificar regularmente?

#### Casos de Aplicación en Administración:

**Escenarios reales - Lee cada situación y marca la mejor opción:**

**Escenario A:** Necesitas analizar ventas mensuales y compartir resultados con el equipo directivo.
☐ Solo script R  ☐ Solo R Markdown  ☐ R Markdown + HTML compilado

**Escenario B:** Quieres que un colega continúe tu análisis y lo modifique.
☐ Solo script R  ☐ Solo R Markdown  ☐ Solo HTML compilado

**Escenario C:** Debes enviar un reporte a clientes que no saben programación.
☐ Solo script R  ☐ Solo R Markdown  ☐ Solo HTML compilado

**Reflexión avanzada:** ¿Cómo se relaciona esto con sistemas que ya conoces?

| Sistema Conocido | ¿Datos o Instrucciones? | ¿Se parece más a...? |
|------------------|-------------------------|----------------------|
| **Archivo Excel (.xlsx)** | ☐ Datos ☐ Instrucciones ☐ Ambos | ☐ Script R ☐ R Markdown ☐ HTML |
| **Macro de Excel ejecutándose** | ☐ Datos ☐ Instrucciones ☐ Ambos | ☐ Script R ☐ R Markdown ☐ HTML |
| **Reporte PDF final** | ☐ Datos ☐ Instrucciones ☐ Ambos | ☐ Script R ☐ R Markdown ☐ HTML |

**Conexión con Ubuntu Linux:** En RStudio.cloud, también tienes acceso a la Terminal Ubuntu Linux (pestaña "Terminal"). Esto te permitiría ejecutar comandos del sistema operativo directamente si fuera necesario para automatizaciones más avanzadas.

**Checkpoint:** Completa todas las respuestas antes de pasar a la síntesis final.

---

### Síntesis y Consolidación (Cierre - 2 minutos)

**Validación final:** Verifica que dominas los conceptos fundamentales que acabas de experimentar.

**Importancia:** Estos conceptos son la base para entender todos los sistemas de información empresariales que usarás en tu carrera profesional.

**Instrucciones para verificar aprendizaje:**

#### Lista de Verificación Final:

**Conceptos fundamentales experimentados:**

**✅ Software como Datos:**
- ☐ Creé archivos `.R` y `.Rmd` que puedo ver en el sistema Ubuntu Linux
- ☐ Renombré y copié archivos como información normal
- ☐ Observé que el código fuente es texto legible y editable
- ☐ Entiendo: Los scripts son datos almacenados hasta que algo los ejecute

**✅ Software como Instrucciones:**
- ☐ Ejecuté scripts línea por línea en la consola R
- ☐ Vi cómo las instrucciones transforman entradas en resultados
- ☐ Observé variables creadas en el panel Environment
- ☐ Entiendo: El código fuente ejecutándose son instrucciones activas que procesan información

**✅ Procesos de Transformación:**
- ☐ Experimenté interpretación inmediata con scripts R
- ☐ "Compilé" un documento R Markdown a HTML
- ☐ Comparé archivos fuente vs archivos procesados
- ☐ Entiendo: Diferentes procesos transforman el software de una forma a otra

**Diferencia clave experimentada:**
- **Interpretación:** Ejecución línea por línea, inmediata, flexible
- **"Compilación":** Procesamiento completo, producto final diferente, optimizado para consumo

#### Conceptos Clave Verificados:

**Autoevaluación rápida - Responde en una palabra:**

1. Los scripts `.R` en el sistema Ubuntu son software como: ____________
2. El código fuente ejecutándose en la consola es software como: ____________
3. R evalúa el código: ☐ Todo junto ☐ Línea por línea
4. Un archivo `.html` generado desde `.Rmd` es: ☐ Editable ☐ Solo para ver

**Aplicación inmediata:** En tu trabajo futuro, verás esta dualidad en:
- **Excel:** Hojas con datos (almacenados) vs. macros ejecutándose
- **Sistemas ERP:** Configuraciones guardadas vs. procesos en ejecución
- **Páginas web:** Código HTML (datos) vs. página renderizada (resultado)

#### Autoevaluación del Aprendizaje:

**Marca tu nivel de comprensión:**

| Concepto | No entendí | Entendí poco | Entendí bien | Entendí muy bien |
|----------|------------|--------------|--------------|------------------|
| Software como datos | ☐ | ☐ | ☐ | ☐ |
| Software como instrucciones | ☐ | ☐ | ☐ | ☐ |
| Diferencia interpretación/compilación | ☐ | ☐ | ☐ | ☐ |
| Aplicación en administración | ☐ | ☐ | ☐ | ☐ |

#### Verificación Final de Archivos:

**En tu panel Files debes tener:**
- ☐ `mi_primer_script.R` (script de R)
- ☐ `mi_reporte.Rmd` (documento fuente R Markdown)
- ☐ `mi_reporte.html` (documento compilado final)
- ☐ Posiblemente `copia_script.R` (script duplicado)

**Si te falta algún archivo:** Revisa los pasos anteriores o pide ayuda.

#### Meta-Comprensión Lograda:

**Pregunta final de integración:**

**Escribe en una oración cómo aplicarías este conocimiento en tu carrera de administración:**

_________________________________________________________________
_________________________________________________________________

**Ejemplos de respuestas esperadas:**
- "Automatizaría reportes financieros mensuales que se actualicen solos"
- "Crearía análisis de datos que otros puedan usar sin saber programar"
- "Entendería mejor cómo funcionan los sistemas empresariales"

#### Próximos Pasos en tu Formación:

**Acabas de experimentar conceptos que se conectan con:**
- **Algoritmos:** Cómo estructurar las instrucciones
- **Bases de datos:** Cómo almacenar y recuperar información
- **Sistemas de información:** Cómo integrar datos, procesos y tecnología
- **Análisis de datos empresariales:** Herramientas para toma de decisiones

**¡Felicitaciones!** 

Has completado exitosamente tu primera inmersión en los fundamentos conceptuales de las ciencias de la computación aplicadas a la administración, es decir, de la Informática.

**Logro desbloqueado:** Comprendes la naturaleza dual del software - una distinción que te acompañará durante toda tu carrera profesional en la era digital.

**Para entregar:** Todos tus archivos están guardados automáticamente en RStudio.cloud. El profesor puede revisarlos accediendo a tu proyecto.

---

### GUÍA DE SOLUCIÓN DE PROBLEMAS

#### Problemas Comunes y Soluciones:

**"No puedo ver mi archivo en Files"**
- Verifica que guardaste el archivo (`Ctrl + S`)
- Revisa que estés en la pestaña "Files" (panel inferior derecho)
- Actualiza la vista haciendo click en el ícono de actualizar

**"El código no se ejecuta"**
- Verifica que instalaste `stringr`: `install.packages("stringr")`
- Carga la librería: `library(stringr)`
- Asegúrate de seleccionar la línea completa antes de `Ctrl + Enter`

**"No funciona el botón Knit"**
- Verifica que el archivo esté guardado como `.Rmd`
- Revisa que hayas copiado todo el contenido del template
- Asegúrate de que `stringr` esté instalado

**"Aparecen errores rojos en la consola"**
- Lee el mensaje de error cuidadosamente
- Verifica que escribiste el código exactamente como aparece
- Revisa que no falten paréntesis o comillas

#### Si Nada Funciona:
1. Levanta la mano para pedir ayuda al profesor
2. Reinicia RStudio.cloud (cerrar pestaña y volver a abrir)
3. Crea un nuevo proyecto si es necesario

---

### Material de Apoyo Específico para RStudio.cloud

#### Requisitos Verificados:
- Cuenta activa en RStudio.cloud
- Navegador web actualizado (Chrome, Firefox, Safari, Edge)
- Conexión estable a internet
- Proyecto nuevo creado

#### Archivos que Debes Tener al Final:
- `mi_primer_script.R` - Script de R (código fuente)
- `mi_reporte.Rmd` - Documento R Markdown fuente
- `mi_reporte.html` - Documento compilado final
- Posiblemente `copia_script.R` - Script duplicado para experimentar

#### Shortcuts Útiles de RStudio.cloud:
- `Ctrl + S` (Windows) / `Cmd + S` (Mac): Guardar archivo
- `Ctrl + Enter` / `Cmd + Enter`: Ejecutar línea de código
- `Ctrl + Shift + Enter` / `Cmd + Shift + Enter`: Ejecutar todo el script
- `Ctrl + Shift + K` / `Cmd + Shift + K`: Compilar R Markdown (Knit)

#### Evaluación de la Práctica:

**El profesor evaluará:**
- ☐ Participación activa durante las actividades (40%)
- ☐ Archivos creados correctamente en RStudio.cloud (30%)
- ☐ Respuestas completas en tablas y preguntas de reflexión (20%)
- ☐ Comprensión demostrada en discusión grupal final (10%)

#### Conexión con el Programa de Informática UAM:

Esta práctica se conecta directamente con:
- **Fundamentos de computación** - Conceptos básicos del software
- **Manipulación de datos numéricos asistido por computadora** - Uso práctico de R
- **Sistemas de información** - Transformación de datos en información útil

#### Próximos Pasos en tu Aprendizaje:
- Algoritmos y estructuras de control en R
- Análisis de datos empresariales
- Bases de datos relacionales
- Sistemas de información gerencial

---

**Nota para el Profesor:** Esta práctica está diseñada para ser completamente autoguiada por estudiantes novatos. Los checkpoints y verificaciones permiten identificar rápidamente quién necesita ayuda adicional.
