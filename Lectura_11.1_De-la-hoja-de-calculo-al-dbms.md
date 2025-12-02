## **De la hoja de cálculo al DBMS: Gestión de datos para estudiantes de Administración**  
## **Caso práctico: “Tortillería El Boleo”**

### OBJETIVO GENERAL

Transformar un conjunto de datos desordenado en una **base de datos relacional funcional**, comprendiendo cómo y por qué escalar desde una hoja de cálculo hasta un sistema gestor de bases de datos (DBMS) y cómo usar esa base para generar **información gerencial visual y confiable**.

### ETAPA 1: GOOGLE SHEETS – EL PUNTO DE PARTIDA (Y SUS LÍMITES)

#### Dataset inicial (`ventas_tortilleria.csv`)

```csv
Fecha,Cliente,Telefono,Colonia,Producto,Cantidad,PrecioUnitario
2025-03-01,Juan Pérez,5551234567,centro,Tortilla de maíz,5,12.00
2025-03-01,juan pérez,5551234567,CENTRO,Tortilla de maiz,3,12.00
2025-03-02,Maria Lopez,5559876543,roma,Tortilla de trigo,4,15.00
2025-03-02,María López,5559876543,Roma,Tortilla de trigo,2,15.00
2025-03-03,Pedro Sanchez,5511223344,condesa,Tortilla de maíz,10,12.00
2025-03-03,Pedro Sánchez,5511223344,Condesa,Tortilla de maiz,5,12.00
2025-03-04,Laura Gómez,5544556677,polanco,Tortilla de trigo,6,15.00
2025-03-04,Laura Gomez,5544556677,Polanco,Tortilla de trigo,2,15.00
2025-03-05,Carlos Ruiz,5522334455,centro,Tortilla de maíz,8,12.00
2025-03-05,carlos ruiz,5522334455,CENTRO,Tortilla de maiz,4,12.00
2025-03-06,Ana Martínez,5566778899,napoles,Tortilla de trigo,3,15.00
2025-03-06,Ana Martinez,5566778899,Nápoles,Tortilla de trigo,5,15.00
2025-03-07,Juan Pérez,5551234567,centro,Tortilla de trigo,2,15.00
2025-03-08,Maria Lopez,5559876543,roma,Tortilla de maíz,7,12.00
2025-03-09,Pedro Sanchez,5511223344,condesa,Tortilla de trigo,4,15.00
```

#### Actividad:
1. Copia estos datos en una hoja nueva de **Google Sheets**.
2. Intenta responder:
   - ¿Cuánto ha gastado Juan Pérez en total?
   - ¿Cuántas unidades de “tortilla de maíz” se vendieron?
   - ¿Qué colonia genera más ingresos?

> **Reflexión crítica**: ¿Qué problemas enfrentaste? ¿Fue fácil filtrar “centro” si aparece como “centro”, “CENTRO” y “Centro”?


### ETAPA 2: GOOGLE COLAB – AUTOMATIZAR LA LIMPIEZA CON DATAFRAMES

#### Conceptos aplicados:
- **Dato vs. información**: El mismo número puede ser un dato aislado o parte de una métrica útil.
- **Consistencia**: Usamos reglas para estandarizar texto (mayúsculas, acentos, ortografía).
- **Identificador único**: El teléfono se usa como clave lógica para agrupar clientes.

#### Objetivo del análisis:
Convertir el dataset caótico en una tabla limpia, reproducible y lista para cargar en una base de datos.

#### Flujo lógico esperado de la **limpieza de datos**:
1. Cargar el CSV.
2. Estandarizar nombres: `.str.title()`.
3. Corregir “maiz” → “maíz”.
4. Normalizar colonias: `.str.lower()` y eliminar acentos.
5. Agrupar por teléfono para asegurar unicidad del cliente.
6. Calcular columna `Total = Cantidad * PrecioUnitario`.

> **Nota**: No se busca copiar código, sino **diseñar la lógica antes de programar**.


### ETAPA 3: SQLITE ONLINE – EL DBMS PARA DECISIONES CONFIABLES

#### Herramienta: [SQLiteOnline](https://sqliteonline.com/)

Entorno gratuito en navegador que permite:
- Ejecutar SQL,
- Crear tablas relacionales,
- **Visualizar resultados con gráficas integradas** (QLINE, QBAR, etc.).

#### Paso 1: Diseño relacional (normalización)

Se crean tres tablas para eliminar redundancia:

```sql
CREATE TABLE Clientes (
    ClienteID INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Telefono TEXT UNIQUE NOT NULL,
    Colonia TEXT NOT NULL
);

CREATE TABLE Productos (
    ProductoID INTEGER PRIMARY KEY,
    Nombre TEXT UNIQUE NOT NULL,
    PrecioUnitario REAL NOT NULL
);

CREATE TABLE Ventas (
    VentaID INTEGER PRIMARY KEY,
    ClienteID INTEGER NOT NULL,
    ProductoID INTEGER NOT NULL,
    Fecha DATE NOT NULL,
    Cantidad INTEGER NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
    FOREIGN KEY (ProductoID) REFERENCES Productos(ProductoID)
);
```

> **Clave primaria**: identificador único dentro de la tabla (ej.: ClienteID).  
> **Clave foránea**: enlace a otra tabla (ej.: ClienteID en Ventas apunta a Clientes).


#### Paso 2: Inserción de datos limpios

Ejemplo parcial:

```sql
INSERT INTO Productos (Nombre, PrecioUnitario) VALUES
('Tortilla de maíz', 12.00),
('Tortilla de trigo', 15.00);

INSERT INTO Clientes (Nombre, Telefono, Colonia) VALUES
('Juan Pérez', '5551234567', 'centro'),
('María López', '5559876543', 'roma'),
-- ... otros 4 clientes
;

INSERT INTO Ventas (ClienteID, ProductoID, Fecha, Cantidad) VALUES
(1, 1, '2025-03-01', 5),
(1, 1, '2025-03-01', 3),
(2, 2, '2025-03-02', 4),
-- ... 12 ventas más
;
```

#### Paso 3: Consultas para la toma de decisiones

##### Consulta básica: ingresos por colonia

```sql
SELECT 
    c.Colonia,
    SUM(v.Cantidad * p.PrecioUnitario) AS Ingresos
FROM Ventas v
JOIN Clientes c ON v.ClienteID = c.ClienteID
JOIN Productos p ON v.ProductoID = p.ProductoID
GROUP BY c.Colonia
ORDER BY Ingresos DESC;
```

#### Paso 4: Visualización con SQLite Online (elemento diferenciador)

SQLite Online permite **convertir consultas SQL en gráficas** cambiando `SELECT` por un prefijo especial:

| Tipo de gráfica | Prefijo SQL       | Uso típico en administración |
|------------------|-------------------|-------------------------------|
| Línea            | `QLINE-SELECT`    | Tendencias en el tiempo       |
| Área             | `QAREA-SELECT`    | Acumulados en el tiempo       |
| Barras           | `QBAR-SELECT`     | Comparación por categoría     |
| Pastel           | `QPIE-SELECT`     | Participación por segmento    |
| Burbujas         | `QBUBBLE-SELECT`  | Tres dimensiones (X, Y, tamaño) |

##### Reglas de sintaxis para ejes:

- **Eje X (horizontal)**:
  - `L_Columna` → texto categórico (ej.: colonia, producto)
  - `T_Columna` → fecha en formato Unix timestamp
  - `X_Columna` → número continuo

- **Eje Y (vertical)**:
  - `Y_Columna` → valor numérico (ingresos, cantidad, etc.)
  - Opcional: `Y_cHEX` para color de línea (ej.: `Y_cFF5733`)

- **Opciones adicionales**:
  - `C_HEX` → color del punto
  - `V_Número` → radio del punto (para burbujas)

##### Ejemplo: gráfica de barras de ingresos por colonia

```sql
QBAR-SELECT 
    L_Colonia,
    Y_Ingresos
FROM (
    SELECT 
        c.Colonia,
        SUM(v.Cantidad * p.PrecioUnitario) AS Ingresos
    FROM Ventas v
    JOIN Clientes c ON v.ClienteID = c.ClienteID
    JOIN Productos p ON v.ProductoID = p.ProductoID
    GROUP BY c.Colonia
)
ORDER BY Ingresos DESC;
```

> Esta consulta **se ejecuta en SQLite Online** y produce automáticamente una gráfica de barras. Ideal para reportes ejecutivos.


### CONCEPTOS CLAVE (recapitulación contextualizada)

| Concepto | ¿Por qué importa en Administración? |
|--------|-------------------------------------|
| **Consistencia** | Evita decisiones basadas en datos erróneos (ej.: “maiz” ≠ “maíz”) |
| **Identificador único** | Permite seguir a un cliente aunque cambie de nombre o se escriba mal |
| **Normalización** | Reduce errores y facilita actualizaciones (precio cambia en un solo lugar) |
| **Relaciones (clave foránea)** | Permite cruzar información sin repetirla |
| **Consulta SQL** | Herramienta para formular preguntas de negocio precisas |
| **Visualización integrada** | Transforma cifras en evidencia visual para presentar a equipos o socios |


### PRÓXIMO PASO

Con esta guía de estudio completa, el estudiante ya cuenta con:
- Un **caso realista**,
- Un **dataset educativo**,
- Una **progresión lógica de herramientas**,
- Y los **conceptos técnicos fundamentales**.

Ahora está listo para el **LABORATORIO PASO A PASO**, en el que aprenderá a **usar la IA como tutor** (no como solucionador) para resolver cada etapa con retroalimentación incremental.

