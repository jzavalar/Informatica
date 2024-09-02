# **Estudio de Caso: Análisis de Datos con RStudio**

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

   El paquete `rio` permite convertir un archivo directamente, sin cargarlo en memoria. A continuación se va a convertir el Archivo CSV a los tres tipos de archivo de datos más frecuentes.

   **Instrucciones**:

   a. **Instalar el Paquete `rio`**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
      ```R
      install.packages("rio")
      ```
      - Asegúrate de que el paquete esté instalado correctamente.

   b. **Convierte el archivo CSV a un archivo Excel**:
      ```R
      convert("analisis_ventas.csv", "analisis_ventas_exportado.xlsx")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   c. **Convierte el Archivo CSV a un archivo JSON**:
      ```R
      convert("analisis_ventas.csv", "analisis_ventas_exportado.json")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   d. **Convierte el Archivo CSV a un archivo XML**:
      ```R
      convert("analisis_ventas.csv", "analisis_ventas_exportado.xml")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   **Instrucciones Adicionales**:
   Asegúrate de publicar el pantallazo del directorio con los archivos exportados y convertidos en el grupo de Telegram.

2. **Carga del Archivo CSV**

   En esta sección, se cargará el archivo CSV en RStudio.

   **Instrucciones:**

   a. **Abrir RStudio**:
      - Inicia el programa RStudio.

   b. **Cargar el Archivo CSV**:
      - Ve a la pestaña "Archivo" y selecciona "Importar datos".
      - Selecciona el archivo "analisis_ventas.csv" que se generó anteriormente.
      - Asegúrate de que el tipo de archivo sea "CSV (Comma delimited)" y haz clic en "Aceptar".

   **Explicación:** Al cargar el archivo CSV, RStudio puede leer los datos y prepararlos para el análisis. Esta sección es fundamental para obtener los datos correctos para el análisis.

3. **Carga del Archivo CSV con `rio`**

   En esta sección, vamos a cargar el archivo CSV "analisis_ventas.csv" en RStudio.

   **Instrucciones:**

   a. **Cargar el Archivo CSV**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
      ```R
      library(rio)
      ventas <- read_csv("analisis_ventas.csv")
      ```
      - Asegúrate de que el archivo se haya cargado correctamente como un dataframe llamado `ventas`.

   b. **Importar el Archivo CSV**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
      ```R
      ventas_imp <- import("analisis_ventas.csv")
      ```
      - Asegúrate de que el archivo se haya cargado correctamente como un dataframe llamado `ventas_imp`.

   **Explicación:** La función `read_csv` es utilizada para leer archivos CSV y crear un dataframe en R. El paquete `rio` es una herramienta poderosa para importar y exportar archivos en R.

4. **Exportación de Dataframes**

   Una vez que el dataframe está en la memoria (`ventas`), este se puede exportar. Van tres ejemplos de cómo exportar a los tres tipos de archivo de datos más frecuentes.

   **Instrucciones**:

   a. **Convierte el dataframe en memoria y el archivo CSV a un archivo Excel**:
      ```R
      write_xlsx(ventas, "analisis_ventas.xlsx")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   b. **Convierte el Archivo CSV a un archivo JSON**:
      ```R
      write_json(ventas, "analisis_ventas.json")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   c. **Convierte el Archivo CSV a un archivo XML**:
      ```R
      write_xml(ventas, "analisis_ventas.xml")
      ```
      - Asegúrate de que el archivo se haya creado correctamente.

   d. También puede usarse el paquete `rio`, con la función `export(dataframe, "archivo_de_salida.formato")`, por ejemplo:
      ```R
      export(ventas_imp, "analisis_ventas_exportado.xlsx")
      ```

5. **Visualizar los Datos**

   En esta sección, se visualizarán los datos cargados en RStudio.

   **Instrucciones:**

   a. **Visualizar los Datos**:
      - Una vez que se haya cargado el archivo CSV, ve a la pestaña "Explorador" y selecciona el archivo "analisis_ventas.csv".
      - Haz clic en el botón "Visualizar" y selecciona la opción "Tabla" para visualizar los datos.

   **Explicación:** Al visualizar los datos, podemos verificar que los datos estén bien cargados y que no haya errores en la sintaxis. Esto es importante para asegurarnos de que los datos sean correctos para el análisis.

6. **Calcular el Total de Ventas**

   En esta sección, se calculará el total de ventas por cada producto utilizando la función `summarise` del paquete `dplyr`; recuerde que se debe instalar y/o cargar el paquete, previamente.

   **Pregunta**: ¿Cuál fue la venta total generada por cada producto?

   **Instrucciones:**

   a. **Calcular el Total de Ventas**:
      - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción para calcular el total de ventas por cada producto:
      ```R
      library(dplyr)
      sales <- read_csv("analisis_ventas.csv")
      sales_total <- sales %>%
      group_by(Producto) %>%
      summarize(Total = sum(Precio_Unitario * Cantidad))
      ```
      - Asegúrate de que los datos estén bien cargados y que no haya errores en la sintaxis.

      **Explicación:** La función `summarise` agrupa los datos por cada producto y calcula el total de ventas para cada grupo. Esto nos permite obtener la venta total generada por cada producto.

b. **Crear una Tabla Dinámica con RStudio**

   En esta sección, se creará una tabla dinámica utilizando la función `kable` del paquete `knitr`.

   **Instrucciones:**

   a. **Crear una Tabla Dinámica con RStudio**:
      - Para crear una tabla dinámica similar a la que se generó en Excel, puedes utilizar la función `kable` del paquete `knitr`:
      ```R
      library(knitr)
      kable(sales_total)
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

Puedes automatizar el proceso de carga de un archivo CSV, la generación de una tabla dinámica y la creación de una gráfica en R utilizando los paquetes `dplyr`, `tidyverse` y `ggplot2`. A continuación, se ilustra eso con un script completo que realiza estas tareas. El script en R incluye la validación de la existencia de los paquetes, con la carga condicional de los mismos y mensajes informativos al usuario sobre el nombre del script, su objetivo, los prerrequisitos y los procesos que realiza:

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
