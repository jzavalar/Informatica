## Laboratorio Guiado Paso a Paso
## **“De la hoja de cálculo al DBMS con IA como tutor”**  
## *Caso: Tortillería El Boleo*

> **Regla de oro**: Nunca pidas “el código completo”. Usa la IA para **validar tu lógica**, no para hacer el trabajo por ti.

---

### Introducción

El **Laboratorio Guiado Paso a Paso**, diseñado específicamente para que el estudiante **interactúe con la IA como tutor**, enviando sus avances, recibiendo retroalimentación conceptual (no soluciones directas) y corrigiendo errores en tiempo real.  

La guía sigue la progresión: **Google Sheets → Google Colab (DataFrame) → SQLite Online (DBMS + visualización)** y en cada etapa incluye:

- **Qué hacer tú**,  
- **Qué decirle a la IA** (con frases modelo),  
- **Qué esperar como retroalimentación útil**,  
- **Cómo verificar que vas por buen camino**.

### Fase 0: Preparación

#### Acciones del estudiante:
1. Crea un negocio ficticio simple (ej.: tortillería, papelería, cafetería).
2. Copia el conjunto de datos (dataset) proporcionado (`ventas_tortilleria.csv`) o crea uno similar con 10–15 registros.
3. Ten listas las herramientas:
   - [Google Sheets](https://sheets.google.com)
   - [Google Colab](https://colab.research.google.com)
   - [SQLite Online](https://sqliteonline.com/)

> No avances sin tener tu conjunto de datos listo. La IA no puede ayudarte si no tienes algo concreto que transformar.

### Fase 1: Diagnóstico en Google Sheets

#### Paso 1.1: Carga los datos
- Pega el CSV en una hoja nueva de Google Sheets.
- Observa visualmente: ¿hay nombres repetidos? ¿formatos distintos?

#### Paso 1.2: Envía a la IA
> **Mensaje al modelo:**  
> “Tengo una hoja de cálculo con ventas de mi tortillería. Aquí están mis datos:  
> ```csv  
> [pega aquí las primeras 5 filas]  
> ```  
> ¿Puedes identificar **tres problemas reales** que me impedirían escalar este negocio si sigo usando solo Sheets?”

#### Qué esperar:
- La IA debe señalar: inconsistencia en nombres, duplicados por formato, falta de identificador único, etc.
- **No debe darte SQL ni código aún**.

#### Paso 1.3: Verificación
- Si entiendes por qué “Juan Pérez” y “juan pérez” son un problema, estás listo para avanzar.


### Fase 2: Limpieza en Google Colab (DataFrame)

#### Paso 2.1: Sube el CSV a Colab
- En Colab, usa `from google.colab import files` o copia/pega como texto.

#### Paso 2.2: Diseña tu plan lógico
Antes de programar, escribe en tu cuaderno o en el notebook:

> “Voy a:  
> 1. Cargar el CSV en un DataFrame.  
> 2. Convertir todos los nombres a título (`str.title()`).  
> 3. Reemplazar ‘maiz’ por ‘maíz’.  
> 4. Convertir las colonias a minúsculas.  
> 5. Agrupar por teléfono para asegurar un cliente = un registro.  
> 6. Crear columna Total.”

#### Paso 2.3: Envía a la IA
> **Mensaje al modelo:**  
> “Quiero limpiar mi conjunto de datos en Pandas. Mi plan es: [pega tu lista].  
> No me des código todavía. Solo dime:  
> - ¿Es correcto usar el teléfono como identificador único en este contexto?  
> - ¿Debería corregir los acentos antes o después de agrupar?”

#### Qué esperar:
- Retroalimentación sobre la lógica, no el código.
- Posible advertencia: “El teléfono puede no ser único en otros contextos, pero aquí es razonable”.
- Confirmación de que corregir texto **antes** de agrupar es lo correcto.

#### Paso 2.4: Implementa y verifica
- Escribe el código tú mismo (puedes pedir ayuda en errores específicos).
- Al final, debes tener **6 clientes únicos**, **2 productos**, **15 ventas**.

> Si ves “maiz” o “CENTRO” en tu resultado final, algo falló.


### Fase 3: Diseño del modelo relacional

#### Paso 3.1: Define las tablas en papel
Dibuja o escribe:
- Tabla Clientes: ¿qué columnas?
- Tabla Productos: ¿qué columnas?
- Tabla Ventas: ¿qué columnas?

#### Paso 3.2: Envía a la IA
> **Mensaje al modelo:**  
> “Voy a crear una base de datos en SQLite. Mi diseño es:  
> - Clientes: ClienteID (PK), Nombre, Teléfono, Colonia  
> - Productos: ProductoID (PK), Nombre, PrecioUnitario  
> - Ventas: VentaID (PK), ClienteID (FK), ProductoID (FK), Fecha, Cantidad  
>  
> ¿Está bien usar Teléfono como campo único en Clientes?  
> ¿Debo incluir PrecioUnitario en Ventas o solo en Productos?”

#### Qué esperar:
- Confirmación: “El precio debe estar solo en Productos; así, si cambia, no afecta ventas pasadas”.
- Advertencia: “Si el precio varía con el tiempo, necesitarías otra estrategia, pero para este caso, está bien”.

#### Paso 3.3: Verificación
- Si entiendes por qué **no se repite el precio en Ventas**, estás listo.


### Fase 4: Implementación en SQLite Online

#### Paso 4.1: Crea las tablas
- Ve a [https://sqliteonline.com/](https://sqliteonline.com/)
- Usa la pestaña **“SQLite”** (no “MySQL” ni “PostgreSQL”).

#### Paso 4.2: Envía a la IA
> **Mensaje al modelo:**  
> “Voy a escribir mis comandos CREATE TABLE. Te mando mi primer intento:  
> ```sql  
> CREATE TABLE Clientes (  
>     ClienteID INTEGER PRIMARY KEY,  
>     Nombre TEXT,  
>     Telefono TEXT UNIQUE,  
>     Colonia TEXT  
> );  
> ```  
> ¿Está bien declarado el `UNIQUE` en Teléfono? ¿Necesito `NOT NULL`?”

#### Qué esperar:
- Sí, debería llevar `NOT NULL` para evitar clientes sin teléfono.
- Confirmación de que `INTEGER PRIMARY KEY` en SQLite auto-genera IDs.

#### Paso 4.3: Inserta datos de prueba (2–3 registros)
- No insertes los 15 de golpe. Prueba con uno.

> **Mensaje al modelo:**  
> “Voy a insertar un cliente y una venta. Te mando mi código:  
> ```sql  
> INSERT INTO Clientes (Nombre, Telefono, Colonia) VALUES ('Juan Pérez', '5551234567', 'centro');  
> INSERT INTO Ventas (ClienteID, ProductoID, Fecha, Cantidad) VALUES (1, 1, '2025-03-01', 5);  
> ```  
> ¿Qué pasa si ProductoID = 1 aún no existe en Productos?”

#### Qué esperar:
- “Fallará por **integridad referencial**. Debes insertar el producto antes de la venta.”

#### Paso 4.4: Verificación
- Si puedes hacer `SELECT * FROM Ventas` y ver los datos sin errores, sigues bien.


### Fase 5: Consultas y visualización

#### Paso 5.1: Escribe una consulta con JOIN
> **Mensaje al modelo:**  
> “Quiero saber el total gastado por colonia. Mi intento es:  
> ```sql  
> SELECT Colonia, SUM(Cantidad * PrecioUnitario) AS Total  
> FROM Ventas v  
> JOIN Clientes c ON v.ClienteID = c.ClienteID  
> JOIN Productos p ON v.ProductoID = p.ProductoID  
> GROUP BY Colonia;  
> ```  
> ¿Está bien el JOIN? ¿Necesito alias?”

#### Qué esperar:
- Confirmación: “Sí, los alias ayudan y los JOIN están bien si las FK existen”.

#### Paso 5.2: Convierte a gráfica en SQLite Online
> **Mensaje al modelo:**  
> “Voy a usar QBAR-SELECT. Mi intento es:  
> ```sql  
> QBAR-SELECT L_Colonia y_Total  
> FROM (  
>   -- mi consulta anterior  
> );  
> ```  
> ¿Es correcta la sintaxis? ¿Necesito renombrar las columnas del subquery?”

#### Qué esperar:
- “Sí, pero asegúrate de que la subconsulta devuelva exactamente las columnas `Colonia` y `Total`”.
- Recordatorio: “En SQLite Online, QBAR-SELECT solo funciona si las columnas tienen los prefijos correctos”.

#### Paso 5.3: Verificación final
- Si al ejecutar el QBAR-SELECT **aparece una gráfica de barras**, ¡lo lograste!


### Fase 6: Reflexión final (entregable)

Escribe un breve informe (5 líneas) como si se lo enviaras a tu jefe:

> “Con base en los datos de marzo, la colonia Centro genera el mayor ingreso ($276), seguida por Condesa ($210). Recomendamos reforzar promociones en Nápoles, que solo aporta $120. Este análisis fue posible gracias a una base de datos normalizada que evita errores por datos inconsistentes.”


### Cómo usar esta guía

- Dedica **máximo 45 minutos por fase**.
- Si te atasca más de 10 minutos, **envía tu intento a la IA** con la frase:  
  > “No me des la solución. Solo dime si mi lógica tiene sentido o me estoy torciendo.”
- Cada fase debe terminar con una **verificación concreta** (no “creo que sí”).

---

Con este laboratorio, el estudiante no solo aprende SQL o Pandas, sino a **pensar como un administrador que usa datos para tomar decisiones** y a **usar la IA como aliado estratégico**, no como muleta técnica.
