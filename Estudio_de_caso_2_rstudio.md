# **Estudio de Caso 2: Bases de Datos con RStudio**

## **Introducción**

En R, las **bases de datos** se manejan a través de *estructuras de datos* conocidas como *dataframes*. Un **dataframe** es un tipo de estructura de datos que se utiliza para almacenar y manipular grandes cantidades de datos en R. Los dataframes pueden ser creados a partir de archivos de texto, como CSV, o mediante la carga de datos desde bases de datos externas.

Ambas herramientas tienen sus ventajas y desventajas, y la elección entre usar R o Excel dependerá de las necesidades específicas del usuario y la naturaleza del proyecto en cuestión.

## **Preguntas guía**

1. **¿Cuáles son las ventajas y desventajas de utilizar R en comparación con Excel para el análisis de datos, y en qué situaciones es preferible usar cada herramienta?**

2. **¿Qué pasos son necesarios para cargar y manipular un archivo CSV en R, y cómo se pueden convertir los datos a otros formatos, como Excel, JSON y XML?**

3. **¿Cómo se calcula el total de ventas por producto utilizando R, y qué métodos se pueden emplear para visualizar y presentar estos resultados de manera efectiva?**

## **Comparación entre R y Excel**

Excel es una herramienta popular para el análisis de datos, pero tiene algunas *limitaciones* en cuanto a la cantidad de datos que puede manejar. **Excel** es más accesible para trabajos que no requieren procesamiento intensivo de datos y es una herramienta práctica para realizar análisis básicos o presentaciones visuales de datos. Sin embargo, tiene limitaciones significativas en el manejo de grandes volúmenes de datos y funcionalidades avanzadas.

**R** es una herramienta poderosa para el análisis de datos y ofrece una amplia variedad de paquetes y funcionalidades para *importar*, *convertir* y *exportar* archivos. Algunos ejemplos de paquetes incluyen `readr` para leer archivos de texto, `writexl` para exportar a archivos Excel y `rio` para interactuar con archivos de datos. **R** es una herramienta más robusta y versátil para análisis de datos, especialmente cuando se trabaja con grandes conjuntos de datos. La capacidad del dataframe para manejar más filas y columnas de manera eficiente, así como su flexibilidad para realizar cálculos y análisis complejos, hace que sea la opción preferida en entornos académicos y de investigación.

A continuación se presenta una comparación entre R (específicamente sus dataframes) y Excel en cuanto a los límites de un libro y una hoja, destacando las características y limitaciones de cada uno.

| **Característica**              | **Excel**                                            | **R (Dataframe)**                          |
|----------------------------------|----------------------------------------------------|--------------------------------------------|
| **Límite de Filas por Hoja**    | 1,048,576 filas                                    | Teóricamente limitado solamente por la memoria disponible. |
| **Límite de Columnas por Hoja**  | 16,384 columnas                                     | Teóricamente limitado solamente por la memoria disponible. |
| **Límite de Hojas por Libro**    | 255 hojas                                          | No hay límite práctico, pero depende de la memoria. |
| **Estructura de Datos**          | Hojas con celdas y fórmulas                        | Dataframes (filas y columnas)             |
| **Tamaño de Archivo**            | Depende de la memoria                              | Dinámico y se ajusta a la memoria disponible |
| **Manipulación de Datos**        | Grandes conjuntos puede ser engorroso y por la interfaz gráfica. | Manipulación de datos potente mediante código. |
| **Análisis Complejo**            | Análisis con tablas dinámicas y gráficos, pero limitado. | Análisis estadísticos avanzados, visualizaciones personalizadas ambas reproducibles. |
| **Lectura y Escritura de Archivos**| Varios formatos pero lenta para archivos grandes. | Múltiples formatos, rápidamente y grandes volúmenes de datos. |

## **Práctica**

1. **Conversión de archivos**

   El paquete `rio` (R Input/Output) se considera una *"Navaja Suiza para la entrada y salida de datos"* que permite convertir un archivo directamente, sin cargarlo en memoria. A continuación se va a convertir el archivo CSV a los tres tipos de archivo de datos más frecuentes.

   **Instrucciones**:

   a. **Instalar el Paquete `rio`**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
      ```R
      install.packages("rio")
      ```
      - Asegúrate de que el paquete esté instalado correctamente.

      Para que puedas utilizar la funcionalidad de un paquete en R, requieres cargarlo a tu proyecto. Por ejemplo, después de instalar el paquete `rio`, debes asegurarte de instalar los formatos con los siguientes comandos: 
      ```R
      library(rio)
      install_formats()
      ```

   b. **Convierte el archivo CSV a un archivo Excel**:
      Ahora sí estás en condiciones de usar `rio` para convertir un archivo que está en tu directorio de trabajo o que esté en cualquier otra ubicación, incluso desde Internet, con el siguiente comando general: `convert("ruta/al/archivo/a/covertir", "ruta/local/al/archivo/covertido.tipo")`, donde `tipo` es la extención del archivo covertido, por ejemplo, xlsx, csv, dbf, dta, sas, etc. Por ejemplo:  
      ```R
      # convertir a a un archivo Excel
      convert("analisis_ventas.csv", "analisis_ventas_exportado.xlsx")

      # convertir a un archivo JSON
      convert("analisis_ventas.csv", "analisis_ventas_exportado.json")

      # convertir a un archivo XML
      convert("analisis_ventas.csv", "analisis_ventas_exportado.xml")
      ```
      - Asegúrate de que el archivo se haya convertido correctamente.

   **Instrucciones Adicionales**:
   Asegúrate de publicar el pantallazo del directorio con los archivos exportados y convertidos en el grupo de Telegram.

1. **Carga del Archivo CSV**

   En esta sección, se cargará el archivo CSV en RStudio.

   **Instrucciones:**

   a. **Abrir RStudio**:
      - Inicia el programa RStudio.

   b. **Cargar el Archivo CSV**:
      - Ve a la pestaña "Archivo" y selecciona "Importar datos".
      - Selecciona el archivo "analisis_ventas.csv" que se generó anteriormente.
      - Asegúrate de que el tipo de archivo sea "CSV (Comma delimited)" y haz clic en "Aceptar".

   **Explicación:** Al cargar el archivo CSV, RStudio puede leer los datos y prepararlos para el análisis. Esta sección es fundamental para obtener los datos correctos para el análisis.

2. **Carga del Archivo CSV con `rio`**

   En esta sección, vamos a cargar el archivo CSV `analisis_ventas.csv` a la memoria, en un *dataframe* con un nombre dado, en RStudio.

   **Instrucciones:**

   a. **Cargar el Archivo CSV**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
      ```R
      # Se carga el paquete rio
      library(rio)

      # Se carga el archivo analisis_ventas.csv al dataframe llamado ventas
      ventas <- read_csv("analisis_ventas.csv")

      # Se muestra el dataframe en RStudio
      View(ventas)
      ```
      - Asegúrate de que el archivo se haya cargado correctamente como un dataframe llamado `ventas`.

   b. **Importar el Archivo CSV**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
      ```R
      ventas_imp <- import("analisis_ventas.csv")
      ```
      - Asegúrate de que el archivo se haya cargado correctamente como un dataframe llamado `ventas_imp`.

   **Explicación:** La función `read_csv` es utilizada para leer archivos CSV y crear un dataframe en R. El paquete `rio` es una herramienta poderosa para importar y exportar archivos en R.

3. **Exportación de Dataframes**

   Una vez que el dataframe está en la memoria (`ventas`), éste se puede exportar. Van tres ejemplos de cómo exportar a los tres tipos de archivo de datos más frecuentes.

   **Instrucciones**:

   a. **Convierte el dataframe en memoria y el archivo CSV a un archivo Excel**:

   Se puede usar la función `write_xlsx(dataframe, "archivo.xlsx")` del paquete `writexl`. Si ya se instaló `rio` ya no es necesario, si no, debe instalarse
      ```R
      # Paso 1: Instalar el paquete
      install.packages("writexl")

      # Paso 2: Cargar el paquete
      library(writexl)

      # Paso 3: Validar que el data frame 'ventas' esté en memoria

      # Paso 4: Escribir el data frame en un archivo de Excel
      write_xlsx(ventas, "analisis_ventas.xlsx")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   b. **Convierte el Archivo CSV a un archivo JSON**:
      La función `write_json()` se utiliza en R para escribir datos en formato JSON (JavaScript Object Notation) y es parte del paquete `jsonlite`.
      ```R
      # Paso 1: Instalar el paquete
      install.packages("jsonlite")

      # Paso 2: Cargar el paquete
      library(jsonlite)

      # Paso 3: convertir el archivo
      write_json(ventas, "analisis_ventas.json")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   c. **Convierte el Archivo CSV a un archivo XML**:
      La función `write_xml()` se utiliza en R para escribir datos en formato XML (Extensible Markup Language) y ésta es parte del paquete `xml2`.
      ```R
      # Paso 1: Instalar el paquete xml2 (si aún no lo has hecho)
      install.packages("xml2")

      # Paso 2: Cargar el paquete
      library(xml2)

      # Paso 3: Convertir el archivo
      write_xml(ventas, "analisis_ventas.xml")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   d. También puede usarse el paquete `rio`, con la función `export(dataframe, "archivo/de/salida.formato")`, por ejemplo:
      ```R
      # Paso 1: Instalar el paquete rio (si aún no lo has hecho)
      install.packages("rio")

      # Paso 2: Cargar el paquete
      library(rio)

      # Paso 3: Convertir el archivo
      export(ventas_imp, "analisis_ventas_exportado.dbf")
      ```

5. **Visualizar los Datos**

   En esta sección, se visualizarán los datos cargados en RStudio.

   **Instrucciones:**

   a. **Visualizar los Datos**:
      - Una vez que se haya cargado el archivo CSV, ve a la pestaña "Explorador" y selecciona el archivo "analisis_ventas.csv".
      - Haz clic en el botón "Visualizar" y selecciona la opción "Tabla" para visualizar los datos.
  
   b. **Visualizar los Datos con código**:
   Puedes usar la función  `View(dataframe)` o darle doble click al dataframe `analisis_ventas`.
   ```
   View(analisis_ventas)
   ```
 
   **Explicación:** Al visualizar los datos, podemos verificar que los datos estén bien cargados y que no haya errores en la sintaxis. Esto es importante para asegurarnos de que los datos sean correctos para el análisis.

6. **Calcular el Total de Ventas**

   **Pregunta**: ¿Cuál fue la venta total generada por cada producto?

   En esta sección, se calculará el total de ventas por cada producto utilizando la función `summarise` del paquete `dplyr`; recuerda que se debes instalar y/o cargar el paquete, previamente.

   **Instrucciones:**

   a. **Calcular el Total de Ventas**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción para calcular el total de ventas por cada producto:
      ```R
      # Cargar el paquete dplyr para manipulación de datos
      library(dplyr)
      
      # Leer el archivo CSV que contiene los datos de ventas
      ventas <- read_csv("analisis_ventas.csv")

      # Agrupar los datos por la columna 'Producto' y calcular el total de ventas
      # Cargar el paquete dplyr (asegúrate de que esté instalado)

      # Calcular las ventas totales por producto
      ventas_total <- ventas %>% # Al dataframe ventas se le hace lo siguiente:
         group_by(Producto) %>%  # Agrupar por la columna 'Producto'
         summarize(Total = sum(Precio_Unitario * Cantidad))  # Calcular el total de ventas

      # Mostrar el resultado
      print(ventas_total)
      ```
      
   b. **Crear una Tabla Dinámica con RStudio**

   En esta sección, se creará una tabla dinámica equivalente, utilizando la función `kable` del paquete `knitr`.

   **Instrucciones:**

   a. **Crear una Tabla Dinámica con RStudio**:
      - Para crear una tabla dinámica similar a la que se generó en Excel, puedes utilizar la función `kable` del paquete `knitr`:
      ```R
      library(knitr)
      kable(ventas_total)
      ```
      - Asegúrate de que la tabla se muestre correctamente y que los valores estén bien calculados.

   **Explicación:** La función `kable` crea una tabla dinámica que puede ser utilizada para visualizar los resultados del análisis. Esto es similar a la tabla dinámica generada en Excel.

## **Solución**

Después de seguir los pasos anteriores, la tabla dinámica debería verse así:

| Producto    | Total |
|-------------|-------|
| Camiseta    | 100   |
| Chaqueta    | 100   |
| Pantalón    | 90    |
| Sombrero    | 70    |
| Zapatos     | 160   |
| **Total**   | 620   |

## **Automatización del Análisis**

Se puede automatizar el proceso de carga de un archivo CSV, la generación de una tabla dinámica y la creación de una gráfica en R utilizando los paquetes `dplyr`, `tidyverse` y `ggplot2`. A continuación, se ilustra eso con un script completo que realiza estas tareas. El script en R incluye la validación de la existencia de los paquetes, con la carga condicional de los mismos y mensajes informativos al usuario sobre el nombre del script, su objetivo, los prerrequisitos y los procesos que realiza:

**Script en R**

```R
# Nombre del Script: analisis_ventas.R
# Objetivo: Automatizar la carga de un archivo CSV, 
# calcular el total de ventas por producto y generar una gráfica correspondiente.
# Prerrequisitos: El archivo 'analisis_ventas.csv' debe estar en el directorio actual.

# Mensaje informativo al usuario
cat("=== Script: analisis_ventas.R ===\n")
cat("Objetivo: Automatizar la carga de un archivo CSV,\n")
cat("calcular el total de ventas por producto y generar una gráfica correspondiente.\n")
cat("Asegúrate de tener el archivo 'Análisis_Ventas.csv' en el directorio actual.\n")
cat("===================================\n\n")

# Función para instalar y cargar paquetes
load_packages <- function(packages) {
  for (pkg in packages) {
    if (!require(pkg, character.only = TRUE)) {
      install.packages(pkg, dependencies = TRUE)
      library(pkg, character.only = TRUE)
      cat(paste("Instalado y cargado:", pkg, "\n"))
    } else {
      library(pkg, character.only = TRUE)
      cat(paste("Cargado:", pkg, "\n"))
    }
  }
}

# Listar los paquetes requeridos
required_packages <- c("tidyverse", "dplyr", "ggplot2")

# Cargar los paquetes
load_packages(required_packages)

# 1. Cargar el archivo CSV
file_path <- "analisis_ventas.csv"  # Ajusta la ruta al archivo CSV si es necesario
ventas <- read_csv(file_path)

# 2. Validar si el archivo se ha cargado correctamente
if (is.null(ventas) || nrow(ventas) == 0) {
  stop("Error: No se pudo cargar el archivo 'analisis_ventas.csv'. Verifica que la ruta y el nombre del archivo sean correctos.")
}

# 3. Generar la tabla dinámica
ventas_total <- ventas %>%
  group_by(Producto) %>%
  summarise(Total_Ventas = sum(Precio_Unitario * Cantidad, na.rm = TRUE), .groups = 'drop')

# Mostrar la tabla dinámica
cat("\nTabla dinámica generada:\n")
print(ventas_total)

# 4. Generar la gráfica correspondiente
ggplot(ventas_total, aes(x = Producto, y = Total_Ventas, fill = Producto)) +
  geom_bar(stat = "identity") +
  labs(title = "Total de Ventas por Producto",
       x = "Producto",
       y = "Total de Ventas") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# 5. Guardar la gráfica
ggsave("grafico_total_ventas.png", width = 8, height = 6)
cat("\nGráfica guardada como 'grafico_total_ventas.png'.\n")
```

**Explicación del script**

1. **Mensajes Informativos**: Al inicio del script, se incluyen mensajes que informan al usuario sobre el propósito del script, su objetivo, y los requerimientos necesarios (el archivo CSV debe estar presente).

2. **Función `load_packages`**: Esta función se encarga de verificar si cada paquete está instalado. Si no lo está, lo instala y lo carga; si ya está instalado, simplemente lo carga. Esto se hace de manera que se eviten errores al ejecutar el script.

3. **Validación de Carga de Datos**: Después de intentar cargar el archivo CSV, se añade una validación para asegurar que los datos se han cargado correctamente (verificando que no sea `NULL` y que contenga filas). En caso contrario, se genera un mensaje de error y se detiene el script.

4. **Mensajes para el Usuario**: Se incluyen mensajes que indican qué sucede en cada etapa del proceso, especialmente al finalizar la carga y generación de la gráfica.

**Ejecución**

Para ejecutar el script:
- Asegúrate de que el archivo `analisis_ventas.csv` esté en la ubicación correcta que especificaste en `file_path`.
- Copia y pega el código en un archivo `.R` o ejecútalo directamente en la consola de R. 

Este script es relativamente robusto y proporciona una mejor experiencia al usuario al indicar el estado de las operaciones que se están llevando a cabo.

## **Conclusión**

Este ejercicio ilustra la importancia del análisis de datos en la administración. Al manipular estos datos en RStudio y generar la tabla dinámica similar a la que se generó en Excel, no solo se adquiere el dominio de herramientas prácticas más potentes como R y RStudio, sino que también se está preparado para enfrentar problemas reales en el ámbito empresarial usando datos para tomar decisiones más informadas.
