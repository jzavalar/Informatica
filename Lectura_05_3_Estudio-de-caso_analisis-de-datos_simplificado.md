# **Lectura 5.3. Estudio de Caso: Análisis de Datos** (Versión simplificada)

prof. dr. Jesús Zavala Ruiz[^1]

---

## **Introducción**

Este estudio de caso examina el servicio de electricidad de la Comisión Federal de Electricidad (CFE) en México, centrándonos en cómo la realidad del consumo eléctrico se transforma en datos codificados y estructurados que dan origen al recibo de luz ([Figura 1](https://github.com/jzavalar/Informatica/blob/main/images/123456789100_Page_1.png)). 

El caso ilustra tres aspectos fundamentales para la administración de información:
1. La realidad que se va a digitalizar (el servicio de luz)
2. La codificación de esa realidad en datos estructurados
3. La validación a través del documento final (el recibo de luz)

## **1. La Realidad: El Consumo Eléctrico**

La electricidad es un servicio esencial que debe ser medido y cobrado. La CFE necesita registrar:
- Quién consume (cliente)
- Cuánto consume (kilovatios-hora)
- Cuándo consume (periodo de facturación)
- Dónde consume (ubicación)
- Qué tipo de consumidor es (doméstico, comercial, industrial)

Esta información existe en la realidad física, pero para ser administrada eficientemente debe convertirse en datos digitales.

## **2. Los Datos: Codificación de Conceptos**

### **2.1. Tipos de Datos y sus Operaciones**

La codificación de la realidad requiere definir tipos específicos de datos:

#### **Alfanumérico**
**Descripción**: Datos que contienen letras, números y/o símbolos.
**Ejemplos**: Nombres, direcciones, códigos.
**Operaciones válidas**:
- Concatenación: "Juan" + "Pérez" = "Juan Pérez"
- Comparación: "ABC123" = "ABC123" (verdadero)
- Búsqueda: ¿"CFE" está en "Recibo CFE"? (verdadero)
- Extracción: Primeros 3 caracteres de "123456789" = "123"

#### **Numérico**
**Descripción**: Valores que representan cantidades.
- **Entero**: Números sin decimales
- **Real**: Números que pueden incluir decimales

**Ejemplos**: Consumo de energía (40 kWh), importes ($107.09)
**Operaciones válidas**:
- Aritméticas: Suma, resta, multiplicación, división
- Comparación: Mayor que, menor que, igual a
- Estadísticas: Promedio, máximo, mínimo, totales
- Financieras: Porcentajes, redondeo, truncamiento

#### **Fecha**
**Descripción**: Representación de un punto en el tiempo.
**Ejemplos**: Fecha de inicio (23/07/2023), fecha límite (06/10/2023)
**Operaciones válidas**:
- Cálculo de intervalos: días entre fechas
- Comparación: fecha actual > fecha límite
- Adición/sustracción: fecha + 30 días
- Extracción: mes, año, día de la semana

#### **BLOB** (Binary Large Object)
**Descripción**: Datos binarios que no son texto ni números.
**Ejemplos**: Código de barras, imágenes, archivos
**Operaciones válidas**:
- Almacenamiento y recuperación
- Visualización (mostrar imagen)
- Codificación/decodificación

#### **Lógico (Booleano)**
**Descripción**: Valores que solo pueden ser verdadero o falso.
**Ejemplos**: ¿Es cliente de alto consumo? (sí/no)
**Operaciones válidas**:
- Operaciones lógicas: AND, OR, NOT
- Condicionales: Si es verdadero entonces X, sino Y
- Verificación: ¿Es verdadero?

### **2.2. Codificación de los Datos**

Para que el sistema de facturación funcione correctamente, cada concepto de la realidad debe traducirse a un dato en la computadora. Este proceso crea un **diccionario de datos**, que es como un traductor entre la realidad y el sistema digital.

La siguiente tabla muestra una selección de los conceptos más importantes del recibo de luz con sus respectivos tipos de datos y ejemplos:

| **Concepto** | **Variable** | **Tipo de Dato** | **Ejemplo** | **¿Único?** |
|--------------|--------------|------------------|-------------|-------------|
| **Número de Servicio** | num_servicio | Alfanumérico | 123456789100 | Sí |
| **Nombre de Usuario** | nombre_usuario | Alfanumérico | JUAN PÉREZ JOLOTE | No |
| **Dirección** | direccion | Alfanumérico | Av. Reforma 164 Int 4 | No |
| **Fecha Inicio** | fecha_inicio | Fecha | 23/07/2023 | No |
| **Fecha Fin** | fecha_fin | Fecha | 23/09/2023 | No |
| **Lectura Anterior** | lectura_anterior | Numérico (Entero) | 0 | No |
| **Lectura Actual** | lectura_actual | Numérico (Entero) | 40 | No |
| **Consumo Total** | consumo_total | Numérico (Entero) | 40 | No |
| **Precio por kWh** | precio_basico | Numérico (Real) | 1.043 | No |
| **Subtotal** | subtotal | Numérico (Real) | 41.72 | No |
| **IVA** | iva | Numérico (Real) | 8.34 | No |
| **Total a Pagar** | total_pagar | Numérico (Real) | 107.09 | No |
| **Código de Barras** | codigo_barras | BLOB | [Imagen] | No |
| **Es Cliente DAC** | es_dac | Lógico | False | No |

Los campos marcados como "Único" no pueden repetirse en la base de datos, garantizando que cada cliente tenga su propio identificador exclusivo.

### **2.3. Estructuras de Datos Básicas**

Además de definir tipos de datos individuales, necesitamos organizarlos en estructuras coherentes:

1. **Registros**: Agrupan datos relacionados sobre una entidad (cliente)
   ```
   Cliente = {
       num_servicio: "123456789100",
       nombre: "JUAN PÉREZ JOLOTE",
       direccion: "Av. Reforma 164"
   }
   ```

2. **Tablas**: Colecciones de registros del mismo tipo
   ```
   Tabla_Clientes = [
       {num_servicio: "123456789100", nombre: "JUAN PÉREZ"},
       {num_servicio: "123456789101", nombre: "MARÍA LÓPEZ"}
   ]
   ```

3. **Listas**: Secuencias ordenadas de elementos
   ```
   Conceptos_Cobro = ["Consumo Básico", "IVA", "DAP"]
   ```

## **3. El Recibo de Luz: Validación de los Datos**

El recibo de luz (Figura 1) es la materialización final del proceso de codificación. En él podemos identificar claramente cómo los datos se han estructurado en áreas funcionales:

1. **Área de Identificación**: Contiene datos del cliente y su servicio
2. **Área de Consumo**: Muestra lecturas y kilovatios consumidos
3. **Área de Cobro**: Detalla importes, tarifas e impuestos
4. **Área de Fechas**: Especifica periodos y plazos de pago
5. **Área de Pago**: Proporciona medios para realizar el pago

Estas áreas funcionan como "plantillas" que organizan los datos de manera coherente y comprensible para el usuario.

### **3.1. Casos Especiales de Datos**

Algunos datos requieren tratamiento especial:

1. **Fechas**: Se almacenan como números internamente, pero se muestran en formato legible (23/07/2023). Esto permite calcular automáticamente:
   - Duración del periodo de facturación
   - Días restantes para el pago
   - Si una factura está vencida

2. **Identificadores Únicos**: Números y códigos que garantizan que cada registro sea único:
   - Número de Servicio: 123456789100
   - RMU: 54168 03 09-09 XAXX-010101 001 CFE

3. **Datos Calculados**: Valores que se obtienen mediante operaciones matemáticas:
   - Consumo = Lectura Actual - Lectura Anterior
   - Subtotal = Consumo × Precio por kWh
   - Total = Subtotal + IVA + DAP

### **3.2. Aplicación Administrativa**

La codificación de datos tiene aplicaciones directas en la administración:

1. **Facturación Masiva**: Permite generar millones de recibos automáticamente
2. **Análisis de Consumo**: Posibilita la segmentación de clientes según patrones
3. **Proyecciones Financieras**: Facilita estimaciones de ingresos futuros
4. **Detección de Anomalías**: Identifica consumos inusuales o errores de lectura
5. **Transparencia**: Proporciona desglose detallado de cobros

**Ejemplo empresarial**: Una tienda departamental podría aplicar principios similares para analizar compras de clientes con tarjeta de fidelidad:

| **Concepto** | **Variable** | **Tipo de Dato** | **Ejemplo** |
|--------------|--------------|------------------|-------------|
| **ID Cliente** | id_cliente | Alfanumérico | TDC-78529463 |
| **Compra Mensual** | compra_mensual | Numérico (Real) | 3,478.50 |
| **Puntos Acumulados** | puntos | Numérico (Entero) | 2,340 |
| **Es Cliente VIP** | es_vip | Lógico | True |

## **4. Conclusiones**

1. La **codificación de datos** transforma la realidad en información estructurada que puede ser procesada eficientemente. En nuestro caso, convierte el consumo físico de electricidad en datos digitales.

2. Los **tipos de datos** definen la naturaleza de la información y determinan las operaciones válidas que pueden realizarse con ella. La elección correcta del tipo de dato es crucial para la integridad y utilidad del sistema.

3. Las **estructuras de datos** organizan la información de manera lógica y coherente, facilitando su procesamiento, presentación y análisis.

4. La **validación** a través de documentos como el recibo de luz demuestra que el sistema refleja correctamente la realidad que busca representar.

Este proceso de digitalización es fundamental en la administración moderna, donde la toma de decisiones depende cada vez más de la capacidad para transformar realidades complejas en datos estructurados y analizables.

## **5. Ejercicio Práctico**

Identifique en un recibo o factura de cualquier servicio (teléfono, agua, etc.):

1. Cinco datos diferentes y clasifíquelos según el tipo de dato correspondiente
2. Las operaciones que podrían realizarse con cada uno de esos datos
3. Tres ejemplos de datos únicos que sirvan como identificadores
4. Un ejemplo de dato calculado a partir de otros valores

[^1]: Profesor-investigador del Departamento de Economía de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Contacto: [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx), [Telegram](https://t.me/jzavalar).

Última actualización: 17 de junio de 2025
