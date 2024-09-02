# Estudio de Caso: Análisis de Datos con Excel

## Parte Teórica

### Introducción
Las bases de datos son colecciones estructuradas de información que permiten almacenar, gestionar y recuperar datos eficientemente. Excel, aunque no es un sistema de gestión de bases de datos en sí mismo, ofrece potentes herramientas para analizar conjuntos de datos mediante sus funciones, gráficos y tablas dinámicas. En el contexto de administración, el análisis de datos se vuelve fundamental para la toma de decisiones empresariales informadas.

### Preguntas Guía
1. **¿Cómo influye la organización de los datos en la efectividad de su análisis?**
   - Reflexiona sobre la estructura de tus datos y cómo una mala organización podría dificultar la obtención de resultados valiosos.
  
2. **¿De qué manera puede el uso de herramientas como Excel optimizar el proceso de toma de decisiones en el ámbito empresarial?**
   - Considera cómo la visualización y análisis de datos pueden impactar en la estrategia de una empresa.
  
3. **¿Qué desafíos pueden surgir al trabajar con grandes volúmenes de datos en softwares como Excel?**
   - Piensa en limitaciones de Excel como software y en qué casos sería más provechoso usar bases de datos más robustas, por ejemplo, cuando miles o millones de regsitros.

## Parte Práctica

### Datos
Para ilustrar el uso de Excel en el análisis de datos, vamos a considerar los siguientes registros de ventas de un pequeño negocio:

| ID Venta | Producto    | Cantidad | Precio Unitario | Fecha       |
|----------|-------------|----------|------------------|-------------|
| 1        | Camiseta    | 5        | 20               | 2023-10-01  |
| 2        | Pantalón    | 3        | 30               | 2023-10-02  |
| 3        | Chaqueta    | 2        | 50               | 2023-10-03  |
| 4        | Zapatos     | 4        | 40               | 2023-10-04  |
| 5        | Sombrero    | 7        | 10               | 2023-10-05  |

### Instrucciones

A continuación se dan las instrucciones paso a paso para procesar los datos en Excel.

1. **Abrir Excel**:
   - Inicia el programa Microsoft Excel.

2. **Crear una Nueva Hoja de Cálculo**:
   - Selecciona 'Libro en blanco' para comenzar con una hoja de trabajo nueva.

3. **Ingresar los Datos**:
   - Copia y pega la tabla de datos anterior en tu nueva hoja de Excel. Asegúrate de que las columnas estén bien alineadas.
   - Verifica que las fechas estén en formato de fecha.

4. **Calcular el Total de Ventas**:
   - Añade una nueva columna llamada "Total" al final de la tabla.
   - En la celda correspondiente a la primera venta (por ejemplo, en la columna F2), ingresa la fórmula: `=C2*D2`, donde C corresponde a Cantidad y D a Precio Unitario. Esto calculará el total de esa venta.
   - Arrastra la fórmula hacia abajo para calcular los totales para las demás filas.

5. **Crear una Tabla Dinámica**:
   Ahora vamos a ver cómo se puede consultar una tabla de datos utilizando una tabla dinámica.
   - Selecciona toda la tabla, incluida la nueva columna de "Total".
   - Ve a la pestaña "Insertar" y selecciona "Tabla Dinámica".
   - En el cuadro de diálogo que aparece, selecciona "Nueva Hoja de Cálculo" y haz clic en "Aceptar".

7. **Configurar la Tabla Dinámica**:
   - En el panel de campo de la tabla dinámica, arrastra "Producto" a las filas y "Total" a los valores. Asegúrate de que se esté calculando la suma de los totales.
   
8. **Guardar el Libro de Excel**:
   - Ve a la pestaña "Archivo" y selecciona "Guardar Como".
   - Elige la ubicación donde deseas guardar el archivo.
   - En el campo "Nombre del archivo", ingresa un nombre (por ejemplo, "Análisis_Ventas").
   - Asegúrate que el formato sea "Libro de Excel (*.xlsx)" y haz clic en "Guardar".

10. **Guardar como CSV**:
   A continuación, se guardan los datos en formato CSV (valores separados por comas), un formato prácticamente universal, para guardar tablas de datos.
   - Con el libro aún abierto, vuelve a la pestaña "Archivo".
   - Selecciona "Guardar Como" y elige la misma ubicación que antes.
   - En el campo "Nombre del archivo", puedes usar el mismo nombre pero con la extensión "csv" (por ejemplo, "Análisis_Ventas.csv").
   - En el menú desplegable de “Tipo”, elige "CSV (Comma delimited) (*.csv)" y haz clic en "Guardar".
   - Si aparece un mensaje advirtiendo que algunas características de Excel no se guardarán en el formato CSV, haz clic en "Sí". Esto es normal, ya que CSV solo guarda texto y números.

### Pregunta para Responder con la Tabla Dinámica
**¿Cuál fue la venta total generada por cada producto?**
Crea un pantallazo de tu tabla dinámica y publícala en el chat de Telegram del grupo.

## Solución
Comprueba que, después de seguir los pasos anteriores, la tabla dinámica debería verse así:

| Producto    | Suma de Total |
|-------------|---------------|
| Camiseta    | 100           |
| Chaqueta    | 100           |
| Pantalón    | 90            |
| Sombrero    | 70            |
| Zapatos     | 160           |
| **Total**   | 620           |

### Reflexión
Este ejercicio ilustra la importancia del análisis de datos en la administración. Al manipular estos datos en Excel y guardarlos tanto en formato de Excel como en CSV, los estudiantes no solo dominan herramientas prácticas, sino que también se preparan para enfrentar problemas reales en el ámbito empresarial usando datos para tomar decisiones más informadas. El formato CSV es especialmente útil para la interoperabilidad con otras aplicaciones y sistemas de gestión de datos.
