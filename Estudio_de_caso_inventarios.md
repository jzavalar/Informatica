# Estudio de Caso: Automatización de la Gestión de Inventarios

## Contexto

Usted es un estudiante de nuevo ingreso a la licenciatura en administración. Se le ha solicitado que ayude a una pequeña tienda de abarrotes llamada “El Ahorro” a gestionar su inventario de manera más eficiente. La tienda actualmente utiliza un sistema manual que es propenso a errores y consume demasiado tiempo.

El propietario de la tienda, Don Carlos, ha mencionado que le gustaría emplear alguna solución tecnológica que le ayude a realizar un seguimiento más efectivo de sus productos y ventas. Sin embargo, Don Carlos no tiene conocimientos de tecnología ni programación. 

## Escenario

La tienda tiene un inventario reducido de productos (aproximadamente 50 artículos). Los productos se registran manualmente en hojas de papel, lo que lleva a errores humanos y desactualización frecuente de los niveles de stock.

Don Carlos le pregunta: “¿Hay alguna manera de que podamos automatizar esto?”.

## Preguntas para Reflexionar

1. **¿Qué tipo de información es esencial para llevar un control adecuado del inventario?**
   - Reflexione sobre los datos necesarios: nombre del producto, cantidad, precio, fecha de ingreso, etc.
   - Haga el análisis de datos.

2. **¿Cómo podría una hoja de cálculo simplificar este proceso?**
   - Considere las ventajas de estructurar los datos y la capacidad de realizar cálculos automáticos.
   - Compare entre usar Excel o una aplicación de manejo de inventarios.

3. **¿Qué funciones básicas deberíamos incluir en una solución tecnológica para satisfacer las necesidades de ‘El Ahorro’?**
   - Enlista funciones de altas, bajas y cambios para manejar el inventario
   - Proponga la manera de darle seguimiento a las ventas con algunos reportes de inventario.
   - Desarrolle conceptualmente los reportes.

4. **Si tuviéramos que programar una pequeña aplicación, ¿qué lenguaje de programación sería más adecuado para este caso y por qué?**
   - Reflexione sobre lenguajes como Python, Excel/VBA o R.

5. **¿Qué desafíos podrían surgir al implementar esta solución en la tienda?**
   - Considere la resistencia al cambio, la capacitación del personal para el uso del nuevo sistema y problemas técnicos.

### Habilidades a desarrollar

Para realizar esta actividad, Usted debe enfocarse en las siguientes habilidades:

1. **Lógica de Programación**: Iniciado con la identificación de tareas, secuenciación de procesos y manejo de condiciones.
2. **Uso de Hojas de Cálculo**: Aprender a utilizar funciones básicas (SUMA, CONTAR, SI) y fórmulas.
3. **Resolución de Problemas**: Identificar errores comunes en el manejo manual de inventarios y crear un flujo de trabajo eficiente.
4. **Comunicación**: Presentar su solución al resto de la clase y recibir retroalimentación.

## Recursos Recomendados

- **“Excel para Dummies”** de Greg Harvey: Excelente introducción al uso de Excel, incluyendo fórmulas y funciones.
- **“Automate the Boring Stuff with Python”** de Al Sweigart: Si se desea ir un paso más allá hacia la programación con Python.

## Conclusión

El estudio de caso de “El Ahorro” resalta la importancia de la programación y el manejo de datos en la administración moderna. A través de un enfoque práctico, los estudiantes no solo desarrollarán habilidades técnicas, sino también resolverán problemas del mundo real, lo que les permitirá apreciar la utilidad de la tecnología en la gestión empresarial. La comprensión de herramientas como hojas de cálculo es esencial en su formación, y les servirá como base para futuros avances en el ámbito tecnológico y administrativo.

## Anexo 1. Proyecto: Desarrollo del sistema de inventarios

En grupos de 3 estudiantes, utilicen [ChatGPT](https://deepai.org/chat) como una herramienta para crear una pequeña aplicación como un prototipo simplificado de un sistema de inventario con las siguientes especificaciones:

1. Estudiante con el **menor número de matrícula** será responsable de lo siguiente:

   - Crear el libro en **Excel** `inventario.xlsx`
   - Desarrollar las macros que incluyan las siguientes funcionalidades:
       - Registrar los productos en la hoja `inventario`.
       - Actualizar cantidades.
       - Mostrar un informe de los productos con bajo inventario.
       - Registrar la historia del inventario en el archivo de texto en la hoja: `historial`.
       - Mostrar la historia del inventario de un periodo de fechas en formato DD-MM-YYYY
   - Genere otras macros para que usen el archivo `inventario.db` con SQLite como base de datos.
   - Ponga en funcionamiento las dos aplicaciones.
   - Genere una presentación de su aplicación que incluya sus propias reflexiones NO generadas por IA y las dificultades que tuvo y cómo las resolvió.
   - Preséntela en un video de 5 minutos grabando la pantalla de su computadora y su voz.
   - Haga una compilación de los prompts que le permitieron generar su aplicación. 
   - Genere un archivo comprimido con todos los archivos de su proyecto y entréguelo por chat al profesor.

2. Estudiante con el número de matrícula medio será responsable de lo siguiente:

   - Generar el script `inventario.py` en lenguaje **Python**.
   - Implementar las siguientes funcionalidades:
       - Registrar los productos en un archivo `inventario.csv` como almacén de persistencia de datos.
       - Actualizar cantidades.
       - Mostrar un informe de los productos con bajo inventario.
       - Registrar la historia del inventario en el archivo de texto en la hoja: `historial.txt`.
       - Mostrar la historia del inventario de un periodo de fechas en formato DD-MM-YYYY.
   - Genere el script en Python `inventario_sqlite.py` modificado para que use el archivo `inventario.db` con SQLite, en lugar del archivo `inventario.csv` como base de datos.
   - Ponga en funcionamiento las dos aplicaciones.
   - Genere una presentación de su aplicación que incluya sus propias reflexiones NO generadas por IA y las dificultades que tuvo y cómo las resolvió.
   - Preséntela en un video de 5 minutos grabando la pantalla de su computadora.
   - Haga una compilación de los prompts que le permitieron generar su aplicación. 
   - Genere un archivo comprimido con todos los archivos de su proyecto y entréguelo por chat al profesor.
   
3. Estudiante con el mayor número de matrícula responsable de lo siguiente:

   - Genere el script `inventario.R` en **lenguaje R**.
   - Implemente las siguientes funcionalidades:
       - Registrar los productos en SQLite en un archivo `inventario.db`.
       - Actualizar cantidades.
       - Mostrar un informe de los productos con bajo inventario.
       - Registrar la historia del inventario en el archivo de texto en la hoja: `historial.txt`.
       - Mostrar la historia del inventario de un periodo de fechas en formato DD-MM-YYYY
   - Genere el script en Python `inventario_sqlite.R` modificado para que use el archivo `inventario.db` con SQLite, en lugar del archivo `inventario.csv` como base de datos.
   - Ponga en funcionamiento las dos aplicaciones.
   - Genere una presentación de su aplicación que incluya sus propias reflexiones NO generadas por IA.
   - Preséntela en un video de 5 minutos grabando la pantalla de su computadora.
   - Haga una compilación de los prompts que le permitieron generar su aplicación. 
   - Genere un archivo comprimido con todos los archivos de su proyecto y entréguelo por chat al profesor. 

## Anexo 2: Datos de prueba

A continuación, se presenta un ejemplo de los 50 datos que Don Carlos podría estar registrando manualmente para llevar el control de su inventario en la tienda de abarrotes "El Ahorro". Cada registro contendrá información esencial sobre los productos disponibles, permitiéndole a Don Carlos tener una visión clara de su inventario. A continuación se muestra un ejemplo de los datos registrados.

| ID  | Nombre del Producto        | Categoría        | Cantidad en Stock | Precio Unitario | Fecha de Ingreso | Proveedor              |
|-----|---------------------------|------------------|-------------------|-----------------|-------------------|------------------------|
| 1   | Arroz (kg)                | Granos           | 20                | $15.00          | 01/01/2024        | Proveedor A            |
| 2   | Frijoles Negros (kg)      | Granos           | 15                | $18.00          | 01/01/2024        | Proveedor B            |
| 3   | Azúcar (kg)               | Endulzantes      | 10                | $13.00          | 02/01/2024        | Proveedor A            |
| 4   | Harina de Trigo (kg)      | Granos           | 25                | $14.00          | 02/01/2024        | Proveedor C            |
| 5   | Sal (kg)                  | Condimentos      | 10                | $5.00           | 02/01/2024        | Proveedor B            |
| 6   | Aceite Vegetal (litro)    | Aceites          | 8                 | $45.00          | 03/01/2024        | Proveedor D            |
| 7   | Salsa de Tomate (litro)   | Salsas           | 5                 | $20.00          | 03/01/2024        | Proveedor E            |
| 8   | Mayonesa (litro)          | Salsas           | 4                 | $35.00          | 04/01/2024        | Proveedor E            |
| 9   | Pasta (kg)                | Granos           | 12                | $22.00          | 05/01/2024        | Proveedor A            |
| 10  | Galletas Dulces           | Snacks           | 30                | $12.00          | 05/01/2024        | Proveedor F            |
| 11  | Cereales de Maíz          | Desayunos        | 25                | $20.00          | 05/01/2024        | Proveedor F            |
| 12  | Leche (litro)             | Lácteos          | 18                | $14.00          | 06/01/2024        | Proveedor G            |
| 13  | Yogur (litro)             | Lácteos          | 10                | $35.00          | 06/01/2024        | Proveedor G            |
| 14  | Huevos (docena)           | Lácteos          | 12                | $35.00          | 07/01/2024        | Proveedor H            |
| 15  | Pan de Caja (paquete)     | Panadería        | 20                | $25.00          | 07/01/2024        | Proveedor I            |
| 16  | Tortillas (paquete)       | Panadería        | 15                | $20.00          | 08/01/2024        | Proveedor J            |
| 17  | Café (kg)                 | Bebidas          | 5                 | $70.00          | 08/01/2024        | Proveedor K            |
| 18  | Té (caja)                 | Bebidas          | 10                | $40.00          | 09/01/2024        | Proveedor K            |
| 19  | Sopa Instantánea          | Snacks           | 20                | $10.00          | 09/01/2024        | Proveedor F            |
| 20  | Chicles (paquete)         | Snacks           | 50                | $5.00           | 10/01/2024        | Proveedor L            |
| 21  | Jabón en Barra            | Limpieza         | 30                | $10.00          | 10/01/2024        | Proveedor M            |
| 22  | Detergente Líquido        | Limpieza         | 15                | $30.00          | 11/01/2024        | Proveedor M            |
| 23  | Pasta Dental              | Higiene          | 20                | $25.00          | 11/01/2024        | Proveedor N            |
| 24  | Papel Higiénico           | Higiene          | 24                | $35.00          | 12/01/2024        | Proveedor O            |
| 25  | Toallas Desechables       | Higiene          | 50                | $22.00          | 12/01/2024        | Proveedor O            |
| 26  | Champú                    | Higiene          | 15                | $50.00          | 12/01/2024        | Proveedor P            |
| 27  | Acondicionador            | Higiene          | 10                | $60.00          | 13/01/2024        | Proveedor P            |
| 28  | Desodorante               | Higiene          | 20                | $40.00          | 13/01/2024        | Proveedor Q            |
| 29  | Crema Hidratante          | Higiene          | 15                | $80.00          | 14/01/2024        | Proveedor Q            |
| 30  | Limpiador Multiusos       | Limpieza         | 10                | $30.00          | 14/01/2024        | Proveedor R            |
| 31  | Discos de Algodón         | Higiene          | 25                | $15.00          | 15/01/2024        | Proveedor S            |
| 32  | Hojas de Papel            | Oficina          | 100               | $10.00          | 15/01/2024        | Proveedor T            |
| 33  | Bolígrafos                | Oficina          | 50                | $2.00           | 16/01/2024        | Proveedor T            |
| 34  | Marcadores                | Oficina          | 30                | $25.00          | 16/01/2024        | Proveedor U            |
| 35  | Carpetas                  | Oficina          | 40                | $10.00          | 17/01/2024        | Proveedor U            |
| 36  | Gomas de Borrar           | Oficina          | 20                | $3.00           | 17/01/2024        | Proveedor V            |
| 37  | Regla                     | Oficina          | 15                | $5.00           | 18/01/2024        | Proveedor V            |
| 38  | Tinta para Impresora      | Oficina          | 5                 | $150.00         | 18/01/2024        | Proveedor W            |
| 39  | Puntas para Lápiz         | Oficina          | 10                | $2.00           | 19/01/2024        | Proveedor X            |
| 40  | Plumas para Escritura      | Oficina          | 30                | $10.00          | 19/01/2024        | Proveedor X            |
| 41  | Cinta Adhesiva            | Oficina          | 25                | $8.00           | 20/01/2024        | Proveedor Y            |
| 42  | Cartulina                  | Oficina          | 15                | $12.00          | 20/01/2024        | Proveedor Y            |
| 43  | Fideos Instantáneos       | Snacks           | 30                | $2.00           | 21/01/2024        | Proveedor Z            |
| 44  | Sopa de Fideos            | Snacks           | 20                | $3.50           | 21/01/2024        | Proveedor Z            |
| 45  | Dulces Variados           | Snacks           | 50                | $20.00          | 22/01/2024        | Proveedor AA           |
| 46  | Frutas en Conserva        | Alimentos        | 5                 | $18.00          | 22/01/2024        | Proveedor AB           |
| 47  | Verduras en Conserva      | Alimentos        | 6                 | $20.00          | 23/01/2024        | Proveedor AC           |
| 48  | Conservas de Pescado      | Alimentos        | 8                 | $30.00          | 23/01/2024        | Proveedor AD           |
| 49  | Salsa Picante             | Salsas           | 12                | $25.00          | 24/01/2024        | Proveedor AE           |
| 50  | Gelatina Instantánea       | Postres          | 20                | $10.00          | 24/01/2024        | Proveedor AF           |

Este conjunto de datos incluye diversas categorías de productos que son comunes en una tienda de abarrotes, así como información relevante para la gestión del inventario. Don Carlos podría utilizar esta información para hacer un seguimiento de las existencias, planificar pedidos y prevenir faltantes en su tienda.
