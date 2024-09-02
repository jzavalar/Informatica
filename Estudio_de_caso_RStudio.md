## **Estudio de Caso: Análisis de Datos con RStudio**
=============================

### **Introducción**
------------

En R, las **bases de datos** se manejan a través de *estructuras de datos* conocidas como *dataframes*. Un **dataframe** es un tipo de estructura de datos que se utiliza para almacenar y manipular grandes cantidades de datos en R. Los dataframes pueden ser creados a partir de archivos de texto, como CSV, o mediante la carga de datos desde bases de datos externas. 

Ambas herramientas tienen sus ventajas y desventajas, y la elección entre usar R o Excel dependerá de las necesidades específicas del usuario y la naturaleza del proyecto en cuestión.

Excel es una herramienta popular para el análisis de datos, pero tiene algunas *limitaciones* en cuanto a la cantidad de datos que puede manejar. **Excel** es más accesible para trabajos que no requieren procesamiento intensivo de datos y es una herramienta práctica para realizar análisis básicos o presentaciones visuales de datos. Sin embargo, tiene limitaciones significativas en el manejo de grandes volúmenes de datos y funcionalidades avanzadas.

R es una herramienta poderosa para el análisis de datos y ofrece una amplia variedad de paquetes y funcionalidades para *importar*, *convertir* y *exportar* archivos. Algunos ejemplos de paquetes incluyen `readr` para leer archivos de texto, `writexl` para exportar a archivos Excel y `rio` para interactuar con archivos de datos. **R** es una herramienta más robusta y versátil para análisis de datos, especialmente cuando se trabaja con grandes conjuntos de datos. La capacidad del dataframe para manejar más filas y columnas de manera eficiente, así como su flexibilidad para realizar cálculos y análisis complejos, hace que sea la opción preferida en entornos académicos y de investigación. 

A continuación se presenta una comparación entre R (específicamente sus dataframes) y Excel en cuanto a los límites de un libro y una hoja, destacando las características y limitaciones de cada uno.

### Comparación entre R y Excel

| **Característica**              | **Excel**                                            | **R (Dataframe)**                          |
|----------------------------------|----------------------------------------------------|--------------------------------------------|
| **Límite de Filas por Hoja**    | 1,048,576 filas) | Teóricamente limitado solamente por la memoria disponible. |
| **Límite de Columnas por Hoja**  | 16,384 columnas             | Teóricamente limitado solamente por la memoria disponible. |
| **Límite de Hojas por Libro**    | 255 hojas                                          | No hay límite práctico, pero depende de la memoria. |
| **Estructura de Datos**          | Hojas con celdas y fórmulas  | Dataframes (filas y columnas) |
| **Tamaño de Archivo**             | Depende de la memoria | Dinámico y se ajusta a la memoria disponible |
| **Manipulación de Datos**        | Grandes conjuntos puede ser engorroso y por la interfaz gráfica. | Manipulación de datos potente mediante código. |
| **Análisis Complejo**            | Análisis con tablas dinámicas y gráficos, pero limitado. | Análisis estadísticos avanzados, visualizaciones personalizadas ambas reproducibles. |
| **Lectura y Escritura de Archivos**| Varios formatos pero lenta para archivos grandes. | Múltiples formatos, rápidamente y grandes volúmenes de datos. |


### **Práctica**

1. **Conversión de archivos**

El paquete  `rio` permite convertir un archivo directamente, sin cargarlo en memoria. A continuación se vas a convertir el Archivo CSV a los tres tipos de archivo de datos más frecuentes.

**Instrucciones**:

a. **Instalar el Paquete rio**:
   - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
   ```R
   install.packages("rio")
   ```
   - Asegúrate de que el paquete esté instalado correctamente.

b. **Convierte el archivo CSV a un archivo Excel**
```R
convert("Análisis_Ventas.csv", "Análisis_Ventas_exportado.xlsx")
```
Asegúrate de que el archivo se haya creado correctamente.

c. **Convierte el Archivo CSV a un archivo JSON**
```R
convert("Análisis_Ventas.csv", "Análisis_Ventas_exportado.json")
```
Asegúrate de que el archivo se haya creado correctamente.

d. **Convierte el Archivo CSV a un archivo XML**
```R
convert("Análisis_Ventas.csv", "Análisis_Ventas_exportado.xml")
```
Asegúrate de que el archivo se haya creado correctamente.

Instrucciones Adicionales:
Asegúrate de publicar el pantallazo del directorio con los archivos exportados y convertidos en el grupo de Telegram.

2. **Carga del Archivo CSV**
En esta sección, se cargará el archivo CSV en RStudio.

**Instrucciones:**

a. **Abrir RStudio**:
   - Inicia el programa RStudio.

b. **Cargar el Archivo CSV**:
   - Ve a la pestaña "Archivo" y selecciona "Importar datos".
   - Selecciona el archivo "Análisis_Ventas.csv" que se generó anteriormente.
   - Asegúrate de que el tipo de archivo sea "CSV (Comma delimited)" y haz clic en "Aceptar".

**Explicación:** Al cargar el archivo CSV, RStudio puede leer los datos y prepararlos para el análisis. Esta sección es fundamental para obtener los datos correctos para el análisis.

2. **Carga del Archivo CSV con `rio`**
En esta sección, vamos a cargar el archivo CSV "Análisis_Ventas.csv" en RStudio.

**Instrucciones:**

a. **Cargar el Archivo CSV**:
   - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
   ```R
   library(rio)
   ventas <- read_csv("Análisis_Ventas.csv")
   ```
   - Asegúrate de que el archivo se haya cargado correctamente como un dataframe llamado `ventas`.

b. **Importar el Archivo CSV**:
   - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción:
   ```R
   library(rio)
   ventas_imp <- import("Análisis_Ventas.csv")
   ```
   - Asegúrate de que el archivo se haya cargado correctamente como un dataframe llamado `ventas_imp`.

**Explicación**
La función `read_csv` es utilizada para leer archivos CSV y crear un dataframe en R. El paquete `rio` es una herramienta poderosa para importar y exportar archivos en R: 

3. **Exportación de datafames**
Una vez que el dataframe está en la memoria (`ventas`) éste se puede exportar. Van tres ejemplos de cómo exportar a los tres tipos de archivo de datos más frecuentes.

Copie y ejecute el código en la consola.

**Instrucciones**:

a. **Convierte el dataframe en memoria y el archivo CSV a un archivo Excel**
   ```R
   write_xlsx(ventas, ""Análisis_Ventas.xlsx")
   ```
   Asegúrate de que el archivo se haya creado correctamente.

b. **Convierte el Archivo CSV a un archivo JSON**
   ```R
   write_json(ventas, "Análisis_Ventas.json")
   ```
   Asegúrate de que el archivo se haya creado correctamente.

c. **Convierte el Archivo CSV a un archivo XML**
   ```R
   write_xml(ventas, "ventas.xml")
   ```
   Asegúrate de que el archivo se haya creado correctamente.

d. También puede usarse el paquete `rio`, con la función `export(dataframe, "archivo_de_salida.formato")`, por ejemplo:
   ```R
   library(rio)
   export(ventas_imp, "Análisis_Ventas_exportado.xlsx")
   ```

4. **Visualizar los Datos**
En esta sección, se visualizarán los datos cargados en RStudio.

**Instrucciones:**

a. **Visualizar los Datos**:
   - Una vez que se haya cargado el archivo CSV, ve a la pestaña "Explorador" y selecciona el archivo "Análisis_Ventas.csv".
   - Haz clic en el botón "Visualizar" y seleccióna la opción "Tabla" para visualizar los datos.

**Explicación:** Al visualizar los datos, podemos verificar que los datos estén bien cargados y que no haya errores en la sintaxis. Esto es importante para asegurarnos de que los datos sean correctos para el análisis.

5. **Calcular el Total de Ventas**
En esta sección, se calculará el total de ventas por cada producto utilizando la función `summarise` del paquete `dplyr`; recuerde que se debe instalar y/o cargar el paquete, previamente.

**Instrucciones:**

a. **Calcular el Total de Ventas**:
   - En la ventana de "Consola" de RStudio, ingresa la siguiente instrucción para calcular el total de ventas por cada producto:
   ```R
   library(dplyr)
   sales <- read_csv("Análisis_Ventas.csv")
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

### Pregunta para Responder con la Tabla Dinámica
**¿Cuál fue la venta total generada por cada producto?**

**Solución del Ejercicio Práctico:**
Después de seguir los pasos anteriores, la tabla dinámica debería verse así:

| Producto    | Total |
|-------------|-------|
| Camiseta    | 100  |
| Chaqueta    | 100  |
| Pantalón    | 90   |
| Sombrero    | 70   |
| Zapatos     | 160  |
| **Total**   | 620  |

**Reflexión Final:** Este ejercicio ilustra la importancia del análisis de datos en la administración. Al manipular estos datos en RStudio y generar una tabla dinámica similar a la que se generó en Excel, los estudiantes no solo dominan herramientas prácticas, sino que también se preparan para enfrentar problemas reales en el ámbito empresarial usando datos para tomar decisiones más informadas.
