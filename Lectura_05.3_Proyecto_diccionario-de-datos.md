# Proyecto Diccionario de Datos
## Metodología de Análisis de Datos: De la Realidad a la Codificación Digital

**Curso:** Informática - Licenciatura en Administración  
**Profesor:** dr. Jesús Zavala Ruiz  
**Basado en:** Lectura 05 - Estudio de Caso del Recibo de Luz CFE
**Fecha:** Octubre de 2025

---

## Introducción

Esta guía presenta una **metodología sistemática** para analizar documentos del mundo real y transformarlos en estructuras de datos digitales. Aprenderás un proceso profesional aplicable a cualquier documento administrativo, comercial o de servicios.

### Principio Fundamental

```
┌─────────────┐      ┌──────────────┐      ┌──────────────┐
│  REALIDAD   │  →   │    DATOS     │  →   │  VALIDACIÓN  │
│             │      │              │      │              │
│ Fenómeno    │      │ Codificación │      │ Documento    │
│ físico o    │      │ digital en   │      │ final que    │
│ proceso     │      │ base de      │      │ cumple el    │
│ real        │      │ datos        │      │ objetivo     │
└─────────────┘      └──────────────┘      └──────────────┘
```

---

## METODOLOGÍA: LAS 7 ETAPAS DEL ANÁLISIS

### ETAPA 1: Comprender el Contexto del Negocio

#### 1.1 Identificar la Realidad

**¿Qué fenómeno vamos a digitalizar?**

Toda digitalización parte de una **realidad física o proceso** que necesita ser medido, registrado y gestionado.

**Ejemplo - Caso CFE:**
- **Realidad física:** Consumo de energía eléctrica en un domicilio
- **Proceso:** El medidor registra continuamente el flujo de electricidad
- **Medición:** En kilovatios-hora (kWh) acumulados

#### 1.2 Identificar la Necesidad de Negocio

**¿Por qué es necesario digitalizar esta realidad?**

**Ejemplo - Caso CFE:**
- **Necesidad operativa:** Cobrar el servicio proporcionado
- **Necesidad administrativa:** Gestionar millones de clientes
- **Necesidad legal:** Documentar el consumo de forma transparente
- **Necesidad financiera:** Generar ingresos para sostener el servicio

#### 1.3 Identificar los Actores Involucrados

**¿Quiénes participan en este proceso?**

**Ejemplo - Caso CFE:**
- **Proveedor:** Comisión Federal de Electricidad (CFE)
- **Cliente:** Usuario doméstico, comercial o industrial
- **Regulador:** Gobierno (subsidios, tarifas)
- **Intermediarios:** Bancos y plataformas de pago

#### 1.4 Identificar el Documento Final

**¿Qué documento valida el proceso completo?**

**Ejemplo - Caso CFE:**
- **Documento:** Recibo de Luz
- **Función:** Informar consumo y solicitar pago
- **Características:** Detallado, transparente, legal

** EJERCICIO PARA TI:**

Selecciona un documento diferente al recibo de luz. Opciones sugeridas:
- Estado de cuenta bancario
- Boleta de calificaciones
- Nómina de empleado
- Factura de servicios médicos
- Ticket de compra en supermercado
- Póliza de seguro
- Contrato de arrendamiento

Completa:
```
MI DOCUMENTO SELECCIONADO: _________________________

1. Realidad a digitalizar:
   _________________________________________________

2. Necesidad de negocio:
   _________________________________________________

3. Actores involucrados:
   - Proveedor: ______________________________________
   - Cliente: ________________________________________
   - Otros: __________________________________________

4. Documento final:
   Nombre: ___________________________________________
   Función: __________________________________________
```

---

### ETAPA 2: Análisis Visual del Documento

#### 2.1 Obtener el Documento Físico o Digital

**Paso crítico:** Conseguir un ejemplar real y completo del documento.

**Ejemplo - Caso CFE:**
- Recibo físico o PDF descargable
- Todas las páginas (frente y reverso si aplica)
- Calidad suficiente para leer todos los datos

#### 2.2 Observación Estructural

**Identifica la arquitectura visual del documento:**

```
┌─────────────────────────────────────────┐
│         ENCABEZADO                      │
│  - Logo institucional                   │
│  - Título del documento                 │
├─────────────────────────────────────────┤
│         SECCIÓN 1: Identificación       │
│  - Datos del cliente                    │
│  - Números de cuenta                    │
├─────────────────────────────────────────┤
│         SECCIÓN 2: Periodo              │
│  - Fechas relevantes                    │
│  - Vigencias                            │
├─────────────────────────────────────────┤
│         SECCIÓN 3: Mediciones           │
│  - Lecturas                             │
│  - Consumos                             │
├─────────────────────────────────────────┤
│         SECCIÓN 4: Costos               │
│  - Desglose detallado                   │
│  - Subtotales e impuestos               │
├─────────────────────────────────────────┤
│         SECCIÓN 5: Total                │
│  - Cantidad a pagar                     │
│  - Métodos de pago                      │
├─────────────────────────────────────────┤
│         PIE DE PÁGINA                   │
│  - Información legal                    │
│  - Contactos                            │
└─────────────────────────────────────────┘
```

**Ejemplo - Caso CFE (Secciones identificadas):**

1. **Información del Cliente y Servicio**
   - Número de servicio, RMU, nombre, dirección

2. **Periodo de Facturación**
   - Fechas de inicio, fin, límite de pago, corte

3. **Datos de Medición**
   - Número de medidor, lecturas, consumo

4. **Desglose de Costos**
   - Consumo por tarifa, impuestos, cargos adicionales

5. **Talón de Pago**
   - Total a pagar, código de barras, instrucciones

#### 2.3 Crear el Mapa Visual

**En tu cuaderno, dibuja:**

```
Técnica: Usa rectángulos para delimitar cada sección
        y anota qué tipo de información contiene

[FOTO/ESCANEO DEL DOCUMENTO]
        ↓
[DIBUJO CON SECCIONES MARCADAS]
        ↓
[LISTA DE SECCIONES IDENTIFICADAS]
```

** EJERCICIO PARA TI:**

Con tu documento seleccionado:

1. **Fotografía o escanea** el documento completo
2. **Imprime o muestra** en pantalla grande
3. **Marca con colores** las diferentes secciones
4. **Lista las secciones:**

```
Secciones identificadas en mi documento:

Sección 1: _______________________________________
   Contenido: ____________________________________

Sección 2: _______________________________________
   Contenido: ____________________________________

Sección 3: _______________________________________
   Contenido: ____________________________________

[Continúa según corresponda...]
```

---

### ETAPA 3: Extracción de Conceptos

#### 3.1 Método de Barrido Sistemático

**Proceso:** Recorre el documento sección por sección, de izquierda a derecha, de arriba hacia abajo.

**Regla de oro:** 
> **NO omitas ningún dato**, por insignificante que parezca. Todo lo que está en el documento tiene una razón de existir.

#### 3.2 Registro Estructurado

Para cada concepto encontrado, registra:

**Formato de registro:**
```
CONCEPTO: [Nombre descriptivo]
UBICACIÓN: [Sección donde aparece]
VALOR EJEMPLO: [Dato real del documento]
OBSERVACIONES: [Notas relevantes]
```

**Ejemplo - Caso CFE (Primeros 10 conceptos):**

```
CONCEPTO: Número de Servicio
UBICACIÓN: Encabezado, esquina superior derecha
VALOR EJEMPLO: 123456789100
OBSERVACIONES: 12 dígitos, identificador único del cliente

CONCEPTO: RMU (Registro Móvil de Usuario)
UBICACIÓN: Debajo del número de servicio
VALOR EJEMPLO: 54168 03 09-09 XAXX-010101 001 CFE
OBSERVACIONES: Código complejo con espacios y guiones

CONCEPTO: Nombre del Titular
UBICACIÓN: Sección de información del cliente
VALOR EJEMPLO: JUAN PEREZ JOLOTE
OBSERVACIONES: En mayúsculas, apellidos completos

CONCEPTO: Dirección de Suministro
UBICACIÓN: Debajo del nombre
VALOR EJEMPLO: Av. Paseo de la Reforma 164 Int 4, C.P. 54168
OBSERVACIONES: Incluye calle, número, interior, código postal

CONCEPTO: Número de Medidor
UBICACIÓN: Sección de medición
VALOR EJEMPLO: G3644V
OBSERVACIONES: Alfanumérico, contiene letras

CONCEPTO: Lectura Anterior
UBICACIÓN: Tabla de medición, columna izquierda
VALOR EJEMPLO: 0
OBSERVACIONES: Valores en kWh, puede ser cero en instalaciones nuevas

CONCEPTO: Lectura Actual
UBICACIÓN: Tabla de medición, columna derecha
VALOR EJEMPLO: 40
OBSERVACIONES: Valores en kWh

CONCEPTO: Consumo Total
UBICACIÓN: Calculado entre lecturas
VALOR EJEMPLO: 40
OBSERVACIONES: Diferencia entre lectura actual y anterior

CONCEPTO: Fecha de Inicio del Periodo
UBICACIÓN: Sección de periodo
VALOR EJEMPLO: 23 JUL 2023
OBSERVACIONES: Formato DD MMM AAAA

CONCEPTO: Límite de Pago
UBICACIÓN: Sección de fechas importantes
VALOR EJEMPLO: 06 OCT 2023
OBSERVACIONES: Fecha límite para pagar sin recargos
```

#### 3.3 Conteo de Conceptos

Al finalizar el barrido, cuenta:
- **Total de conceptos identificados**
- **Conceptos por sección**
- **Conceptos con valores únicos**

**Ejemplo - Caso CFE:**
- Total: 40+ conceptos
- Distribución aproximada:
  - Identificación: 5 conceptos
  - Fechas: 4 conceptos
  - Medición: 6 conceptos
  - Costos: 20+ conceptos
  - Otros: 5+ conceptos

** EJERCICIO PARA TI:**

Realiza el barrido completo de tu documento:

```
LISTA DE CONCEPTOS EXTRAÍDOS
══════════════════════════════

[Usa el formato mostrado para cada concepto]

CONCEPTO #1: _________________________________
UBICACIÓN: ___________________________________
VALOR EJEMPLO: _______________________________
OBSERVACIONES: _______________________________

CONCEPTO #2: _________________________________
UBICACIÓN: ___________________________________
VALOR EJEMPLO: _______________________________
OBSERVACIONES: _______________________________

[Continúa hasta listar TODOS los conceptos...]

RESUMEN:
Total de conceptos identificados: _______
```

---

### ETAPA 4: Clasificación de Datos

#### 4.1 Los 5 Tipos Fundamentales de Datos

Cada concepto debe clasificarse en UNO de estos tipos:

##### **TIPO 1: ALFANUMÉRICO**

**Definición:** Texto que puede contener letras, números y símbolos.

**Características:**
- Longitud variable o fija
- Puede incluir espacios
- No se usan para cálculos matemáticos
- Sensible a mayúsculas/minúsculas

**Cuándo usar:**
- Nombres de personas o empresas
- Direcciones
- Descripciones
- Códigos con letras (placas, RFCs, etc.)

**Ejemplo - Caso CFE:**
```
nombre_usuario = "JUAN PEREZ JOLOTE"
direccion = "Av. Paseo de la Reforma 164 Int 4"
rmu = "54168 03 09-09 XAXX-010101 001 CFE"
num_medidor = "G3644V"  ← ¡Tiene letra G!
tipo_usuario = "Doméstico"
```

**Cuidado con:**
```
INCORRECTO:
   num_servicio = Numérico
   (Aunque solo tiene números, es un ID, no se suma)

CORRECTO:
   num_servicio = Alfanumérico
   (Es un identificador, no un valor para calcular)
```

##### **TIPO 2: NUMÉRICO**

Se divide en dos subtipos:

**A) NUMÉRICO ENTERO**

**Definición:** Números sin parte decimal.

**Características:**
- Valores completos (... -2, -1, 0, 1, 2, ...)
- Para conteos y cantidades discretas
- Ocupan menos espacio en memoria

**Cuándo usar:**
- Cantidades de unidades completas
- Contadores
- Edades en años completos
- kWh (no se miden fracciones)

**Ejemplo - Caso CFE:**
```
lectura_anterior = 0
lectura_actual = 40
consumo_basico = 40
consumo_total = 40
dias_periodo = 62
multiplicador = 1
```

**B) NUMÉRICO REAL (con decimales)**

**Definición:** Números con parte fraccionaria.

**Características:**
- Permite decimales (.25, .50, .99)
- Mayor precisión
- Esencial para dinero

**Cuándo usar:**
- Importes monetarios
- Precios unitarios
- Porcentajes
- Mediciones precisas

**Ejemplo - Caso CFE:**
```
precio_basico = 1.043
subtotal_consumo = 41.72
iva = 8.34
total_pagar = 107.09
costo_suministro = 16.69
```

**Regla de decisión:**
```
¿Tiene o puede tener decimales?
   └─ NO  → ENTERO
   └─ SÍ  → REAL

¿Es dinero?
   └─ Siempre REAL (aunque sea $100.00)
```

##### **TIPO 3: FECHA**

**Definición:** Representa un momento específico en el tiempo.

**Características internas:**
- Se almacena como número (días desde referencia)
- Se muestra con formato legible
- Permite cálculos temporales

**Formatos comunes:**
```
DD/MM/AAAA  →  23/07/2023
DD-MM-AAAA  →  23-07-2023
AAAA-MM-DD  →  2023-07-23 (ISO 8601)
DD MMM AAAA →  23 JUL 2023
```

**Operaciones posibles:**
```
fecha_fin - fecha_inicio = duración (días)

fecha + días = nueva_fecha

fecha_actual > fecha_limite = ¿vencido?
```

**Ejemplo - Caso CFE:**
```
fecha_inicio_periodo = 23/07/2023
fecha_fin_periodo = 23/09/2023
limite_pago = 06/10/2023
fecha_corte = 07/10/2023

// Cálculo automático:
dias_periodo = 23/09/2023 - 23/07/2023 = 62 días
```

**Cuidado con:**
```
INCORRECTO:
   fecha = "23 de julio de 2023"  (Alfanumérico)

CORRECTO:
   fecha = 23/07/2023  (Tipo Fecha)
```

##### **TIPO 4: LÓGICO (BOOLEANO)**

**Definición:** Solo tiene DOS valores posibles.

**Valores permitidos:**
```
Verdadero / Falso
True / False
Sí / No
1 / 0
✓ / ✗
```

**Características:**
- Respuesta binaria
- Ocupa mínimo espacio (1 bit)
- Ideal para condiciones y flags

**Cuándo usar:**
- Estados de activación (activo/inactivo)
- Condiciones (cumple/no cumple)
- Indicadores (tiene/no tiene)
- Permisos (permitido/prohibido)

**Ejemplo - Caso CFE:**
```
es_dac = False              (¿Es tarifa de alto consumo?)
es_lectura_estimada = False (¿La lectura es estimada?)
tiene_adeudos = True        (¿Tiene deudas pendientes?)
medidor_digital = True      (¿El medidor es digital?)
corte_realizado = False     (¿Se realizó corte?)
```

**Uso en lógica:**
```
SI tiene_adeudos = True ENTONCES
   mostrar_advertencia()
   activar_proceso_cobranza()
FIN SI

SI es_dac = True ENTONCES
   aplicar_tarifa_alta()
SINO
   aplicar_tarifa_subsidio()
FIN SI
```

##### **TIPO 5: BLOB (Binary Large Object)**

**Definición:** Datos binarios como imágenes, archivos, multimedia.

**Características:**
- No es texto legible
- Archivos completos almacenados
- Tamaño variable (puede ser muy grande)

**Cuándo usar:**
- Imágenes (logos, fotos, firmas)
- Códigos de barras / QR
- Documentos PDF adjuntos
- Audio o video
- Archivos comprimidos

**Ejemplo - Caso CFE:**
```
codigo_barras = [IMAGEN PNG]     (Para escanear al pagar)
indicador_consumo = [GRÁFICO]    (Semáforo de consumo)
logo_cfe = [IMAGEN]              (Logotipo institucional)
firma_digital = [CERTIFICADO]    (Validación electrónica)
```

**Implementación en base de datos:**
```
┌────────────────┬──────┬─────────┐
│ Campo          │ Tipo │ Tamaño  │
├────────────────┼──────┼─────────┤
│ codigo_barras  │ BLOB │ 50 KB   │
│ recibo_pdf     │ BLOB │ 2.3 MB  │
└────────────────┴──────┴─────────┘
```

#### 4.2 Tabla de Decisión Rápida

```
┌─────────────────────────────┬────────────────┐
│ SI EL DATO...               │ TIPO ES...     │
├─────────────────────────────┼────────────────┤
│ Contiene letras y números   │ Alfanumérico   │
│ Es un nombre o descripción  │ Alfanumérico   │
│ Es un código ID             │ Alfanumérico   │
├─────────────────────────────┼────────────────┤
│ Solo números, sin decimales │ Entero         │
│ Cantidad de unidades        │ Entero         │
│ Resultado de conteo         │ Entero         │
├─────────────────────────────┼────────────────┤
│ Es dinero                   │ Real           │
│ Tiene o puede tener .XX     │ Real           │
│ Es un precio o costo        │ Real           │
│ Es un porcentaje            │ Real           │
├─────────────────────────────┼────────────────┤
│ Representa día/mes/año      │ Fecha          │
│ Se puede calcular duración  │ Fecha          │
│ Marca un momento en tiempo  │ Fecha          │
├─────────────────────────────┼────────────────┤
│ Solo tiene 2 opciones       │ Lógico         │
│ Es Sí o No                  │ Lógico         │
│ Es Verdadero o Falso        │ Lógico         │
│ Indica estado binario       │ Lógico         │
├─────────────────────────────┼────────────────┤
│ Es una imagen               │ BLOB           │
│ Es un código de barras      │ BLOB           │
│ Es un archivo adjunto       │ BLOB           │
└─────────────────────────────┴────────────────┘
```

** EJERCICIO PARA TI:**

Clasifica los conceptos de tu documento:

```
CLASIFICACIÓN DE TIPOS DE DATOS
════════════════════════════════

Concepto 1: _______________________________
Tipo de dato: _____________________________
Justificación: ____________________________

Concepto 2: _______________________________
Tipo de dato: _____________________________
Justificación: ____________________________

[Repite para TODOS tus conceptos...]

RESUMEN DE CLASIFICACIÓN:
Alfanuméricos: _____ conceptos
Enteros: _____ conceptos
Reales: _____ conceptos
Fechas: _____ conceptos
Lógicos: _____ conceptos
BLOBs: _____ conceptos
TOTAL: _____ conceptos
```

---

### ETAPA 5: Construcción del Diccionario de Datos

#### 5.1 ¿Qué es un Diccionario de Datos?

**Definición:**
> Documento estructurado que relaciona cada concepto de la realidad con su representación digital, especificando características técnicas para su almacenamiento en una base de datos.

**Función:**
- Puente entre el análisis conceptual y la implementación técnica
- Guía para desarrolladores de sistemas
- Referencia para mantenimiento futuro

#### 5.2 Estructura del Diccionario

**Columnas obligatorias:**

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| **Concepto** | Nombre descriptivo del dato en lenguaje natural | "Número de Servicio" |
| **Variable** | Nombre técnico para programación (snake_case) | num_servicio |
| **Tipo de Dato** | Clasificación según los 5 tipos | Alfanumérico |
| **Único** | ¿Es único para cada registro? (Sí/No) | Sí |
| **Descripción** | Explicación breve de qué representa | "Identificador único de cada cliente" |
| **Ejemplo** | Valor real tomado del documento | 123456789100 |

#### 5.3 Reglas para Nombres de Variables

**Convenciones de nomenclatura (snake_case):**

**CORRECTO:**
```
num_servicio
fecha_inicio_periodo
total_pagar
consumo_basico
es_cliente_dac
precio_por_kwh
```

**INCORRECTO:**
```
NumServicio        (CamelCase, no usar)
numero servicio    (con espacios, no permitido)
número-de-servicio (con acentos y guiones, evitar)
NS                 (muy corto, no descriptivo)
el_numero_de_servicio_del_cliente (muy largo)
```

**Reglas obligatorias:**
1. Solo letras minúsculas
2. Números permitidos (pero no al inicio)
3. Guión bajo (_) como separador
4. Sin espacios
5. Sin caracteres especiales (ñ, á, é, etc.)
6. Máximo 30 caracteres
7. Nombres descriptivos pero concisos

#### 5.4 Identificar Campos ÚNICOS

**¿Qué significa "Único"?**

Un campo es único cuando:
> Cada registro en la base de datos DEBE tener un valor DIFERENTE en ese campo.

**Pregunta clave:**
> ¿Dos clientes/registros diferentes pueden tener el mismo valor?
> - Si NO → Es ÚNICO
> - Si SÍ → NO es único

**Ejemplo - Caso CFE:**

```
ÚNICOS (Sí):
✓ num_servicio       → Cada cliente tiene uno diferente
✓ num_medidor        → Cada medidor es único
✓ rmu                → Identificador único por usuario

NO ÚNICOS (No):
✗ nombre_usuario     → Pueden existir dos "Juan Perez"
✗ consumo_total      → Varios pueden consumir 40 kWh
✗ total_pagar        → Varios pueden pagar $107.09
✗ direccion          → Varios usuarios en misma dirección
```

**Importancia:**
- Los campos únicos son **Llaves Primarias** en bases de datos
- Permiten identificar sin ambigüedad cada registro
- Evitan duplicados
- Conectan información entre tablas

#### 5.5 Ejemplo Completo de Diccionario de Datos

**Caso CFE - Primeros 20 registros:**

| Concepto | Variable | Tipo | Único | Descripción | Ejemplo |
|----------|----------|------|-------|-------------|---------|
| Número de Servicio | num_servicio | Alfanumérico | Sí | Identificador único del cliente en el sistema CFE | 123456789100 |
| RMU | rmu | Alfanumérico | Sí | Registro Móvil de Usuario para rastreo interno | 54168 03 09-09 XAXX-010101 001 CFE |
| Nombre del Titular | nombre_usuario | Alfanumérico | No | Nombre completo del titular del servicio | JUAN PEREZ JOLOTE |
| Dirección | direccion | Alfanumérico | No | Domicilio donde se suministra la electricidad | Av. Paseo de la Reforma 164 Int 4, C.P. 54168 |
| Tipo de Usuario | tipo_usuario | Alfanumérico | No | Clasificación del servicio (Doméstico/Comercial/Industrial) | Doméstico |
| Número de Medidor | num_medidor | Alfanumérico | Sí | Código único del equipo de medición instalado | G3644V |
| Tipo de Medidor | tipo_medidor | Alfanumérico | No | Tecnología del medidor (Electromecánico/Digital) | Digital |
| Lectura Anterior | lectura_anterior | Numérico (Entero) | No | Valor registrado en el medidor al inicio del periodo (kWh) | 0 |
| Lectura Actual | lectura_actual | Numérico (Entero) | No | Valor registrado en el medidor al final del periodo (kWh) | 40 |
| Multiplicador | multiplicador | Numérico (Entero) | No | Factor de ajuste aplicado a las lecturas del medidor | 1 |
| Fecha Inicio Periodo | fecha_inicio_periodo | Fecha | No | Fecha de inicio de medición del consumo | 23/07/2023 |
| Fecha Fin Periodo | fecha_fin_periodo | Fecha | No | Fecha de finalización de medición del consumo | 23/09/2023 |
| Límite de Pago | limite_pago | Fecha | No | Fecha límite para pagar sin recargos | 06/10/2023 |
| Fecha de Corte | fecha_corte | Fecha | No | Fecha a partir de la cual se suspende el servicio por falta de pago | 07/10/2023 |
| Consumo Básico | consumo_basico | Numérico (Entero) | No | Kilowatts-hora consumidos en el rango de tarifa básica | 40 |
| Consumo Intermedio | consumo_intermedio | Numérico (Entero) | No | Kilowatts-hora consumidos en el rango de tarifa intermedia | 0 |
| Consumo Excedente | consumo_excedente | Numérico (Entero) | No | Kilowatts-hora consumidos en el rango de tarifa excedente | 0 |
| Consumo Total | consumo_total | Numérico (Entero) | No | Suma total de kWh consumidos en el periodo | 40 |
| Precio Básico | precio_basico | Numérico (Real) | No | Costo por kilowatt-hora en tarifa básica (pesos) | 1.043 |
| Precio Intermedio | precio_intermedio | Numérico (Real) | No | Costo por kilowatt-hora en tarifa intermedia (pesos) | 1.260 |

*Continuaría con los 20+ conceptos restantes...*

#### 5.6 Validación del Diccionario

**Checklist de calidad:**

□ Todos los conceptos del documento están incluidos  
□ Cada variable tiene nombre único  
□ Los nombres siguen convención snake_case  
□ Los tipos de datos están correctamente asignados  
□ La columna "Único" está bien determinada  
□ Las descripciones son claras y completas  
□ Los ejemplos son reales y representativos  
□ No hay datos duplicados o redundantes  

** EJERCICIO PARA TI:**

Construye el diccionario completo de tu documento:

```
Usa una tabla con estas columnas:
┌────────────┬──────────┬──────┬───────┬─────────────┬─────────┐
│ Concepto   │ Variable │ Tipo │ Único │ Descripción │ Ejemplo │
└────────────┴──────────┴──────┴───────┴─────────────┴─────────┘

Requisito mínimo: 20 conceptos
Recomendado: Todos los conceptos del documento

Al terminar, responde:
1. Total de conceptos: _______
2. Campos únicos identificados: _______
3. Tipos más frecuentes:
   - Alfanuméricos: _______
   - Numéricos: _______
   - Otros: _______
```

---

### ETAPA 6: Identificación de Estructuras de Datos

#### 6.1 ¿Qué son las Estructuras de Datos?

**Definición:**
> Formas de organizar múltiples datos relacionados para facilitar su manejo, almacenamiento y procesamiento.

**Analogía:**
- **Dato simple** = Una caja con un objeto
- **Estructura** = Un estante organizado con muchas cajas relacionadas

#### 6.2 Las 5 Estructuras Fundamentales

##### **ESTRUCTURA 1: REGISTRO (Record/Struct)**

**Definición:**
Agrupa datos relacionados de UNA MISMA entidad.

**Características:**
- Campos de diferentes tipos
- Describe completamente a un objeto/persona/cosa
- Forma una "fila" en una tabla

**Cuándo usar:**
Cuando necesitas guardar toda la información de:
- Un cliente
- Un producto
- Una transacción
- Un empleado

**Ejemplo - Caso CFE:**
```
REGISTRO: Cliente
├─ num_servicio: "123456789100"
├─ rmu: "54168 03 09-09 XAXX-010101 001 CFE"
├─ nombre_usuario: "JUAN PEREZ JOLOTE"
├─ direccion: "Av. Reforma 164"
└─ tipo_usuario: "Doméstico"

REGISTRO: Medicion_Actual
├─ fecha_inicio: 23/07/2023
├─ fecha_fin: 23/09/2023
├─ lectura_anterior: 0
├─ lectura_actual: 40
└─ consumo_total: 40
```

**Representación visual:**
```
┌─────────────────────────────────┐
│        Cliente #123456789100    │
├─────────────────────────────────┤
│ RMU: 54168 03 09-09...          │
│ Nombre: JUAN PEREZ JOLOTE       │
│ Dirección: Av. Reforma 164      │
│ Tipo: Doméstico                 │
└─────────────────────────────────┘
```

##### **ESTRUCTURA 2: ARREGLO (Array)**

**Definición:**
Colección ordenada de elementos del MISMO TIPO.

**Características:**
- Tamaño fijo o dinámico
- Acceso por índice [0], [1], [2]...
- Todos los elementos son del mismo tipo
- Orden importa

**Cuándo usar:**
- Histórico de 12 meses
- Lista de productos en factura
- Calificaciones de un semestre
- Precios de una tarifa

**Ejemplo - Caso CFE:**
```
Consumo_Mensual[12]:
[0]  Enero:     35 kWh
[1]  Febrero:   38 kWh
[2]  Marzo:     40 kWh
[3]  Abril:     42 kWh
[4]  Mayo:      45 kWh
[5]  Junio:     48 kWh
[6]  Julio:     50 kWh
[7]  Agosto:    47 kWh
[8]  Septiembre: 44 kWh
[9]  Octubre:   41 kWh
[10] Noviembre: 38 kWh
[11] Diciembre: 36 kWh
```

**Representación visual:**
```
┌────┬────┬────┬────┬────┬────┬────┐
│ 35 │ 38 │ 40 │ 42 │ 45 │ 48 │ 50 │
└────┴────┴────┴────┴────┴────┴────┘
  [0]  [1]  [2]  [3]  [4]  [5]  [6]
```

##### **ESTRUCTURA 3: TABLA (Relacional)**

**Definición:**
Conjunto de registros organizados en filas y columnas.

**Características:**
- Filas = Registros completos
- Columnas = Campos/Atributos
- Relaciones mediante llaves
- Base de datos relacional

**Cuándo usar:**
- Almacenar muchos clientes
- Historial de transacciones
- Catálogos de productos
- Registros de empleados

**Ejemplo - Caso CFE:**
```
TABLA: Clientes
┌──────────────┬──────────────────┬─────────────┬──────────┐
│ num_servicio │ nombre_usuario   │ direccion   │ tipo     │
├──────────────┼──────────────────┼─────────────┼──────────┤
│ 12345678910  │ JUAN PEREZ       │ Av. Ref 164 │ Doméstic │
│ 12345678911  │ MARIA LOPEZ      │ Calle 5 #10 │ Comercia │
│ 12345678912  │ CARLOS GARCIA    │ Blvd. 20 #4 │ Industri │
└──────────────┴──────────────────┴─────────────┴──────────┘

TABLA: Consumos
┌────────────┬──────────────┬────────────┬──────────┬───────┐
│ id_consumo │ num_servicio │ fecha_ini  │ consumo  │ monto │
├────────────┼──────────────┼────────────┼──────────┼───────┤
│ 1001       │ 12345678910  │ 23/07/2023 │ 40       │ 107.09│
│ 1002       │ 12345678910  │ 23/09/2023 │ 45       │ 125.50│
│ 1003       │ 12345678911  │ 23/07/2023 │ 120      │ 450.00│
└────────────┴──────────────┴────────────┴──────────┴───────┘
```

**Relación entre tablas:**
```
Clientes.num_servicio ←→ Consumos.num_servicio
        (1)                      (muchos)
   Un cliente puede tener muchos consumos registrados
```

##### **ESTRUCTURA 4: LISTA (List)**

**Definición:**
Colección ordenada de elementos de TIPOS VARIADOS con tamaño variable.

**Características:**
- Tamaño dinámico (crece/decrece)
- Puede contener diferentes tipos
- Fácil agregar/quitar elementos
- Mantiene orden de inserción

**Cuándo usar:**
- Cargos variables en una factura
- Lista de compras con diferentes productos
- Comentarios en un ticket
- Conceptos adicionales

**Ejemplo - Caso CFE:**
```
Lista_Cargos:
[
  {concepto: "Consumo Básico",    monto: 41.72},
  {concepto: "IVA",                monto: 8.34},
  {concepto: "DAP",                monto: 46.00},
  {concepto: "Adeudo Anterior",    monto: 106.60},
  {concepto: "Pago Anterior",      monto: -106.00},
  {concepto: "Ajuste por redondeo", monto: 0.43}
]
```

**Ventaja:**
Puedes agregar o quitar conceptos fácilmente según el caso:
```
Cliente sin adeudos → 4 elementos
Cliente con adeudos → 6 elementos
Cliente con bonificación → 7 elementos
```

##### **ESTRUCTURA 5: DICCIONARIO (Map/Hash)**

**Definición:**
Pares clave-valor donde cada clave es única.

**Características:**
- Búsqueda rápida por clave
- Claves únicas, valores pueden repetirse
- No mantiene orden específico
- Ideal para catálogos

**Cuándo usar:**
- Precios por código
- Configuraciones
- Traducciones
- Tipos de tarifas

**Ejemplo - Caso CFE:**
```
Precios_Por_Tarifa:
{
  "basico":     1.043,
  "intermedio": 1.260,
  "excedente":  3.466
}

Tipos_Usuario:
{
  "D": "Doméstico",
  "C": "Comercial",
  "I": "Industrial",
  "A": "Agrícola"
}

Acceso rápido:
precio = Precios_Por_Tarifa["basico"]  → 1.043
tipo = Tipos_Usuario["D"]               → "Doméstico"
```

#### 6.3 Guía de Selección de Estructura

```
┌─────────────────────────────────────────────────────┐
│          ¿QUÉ ESTRUCTURA USAR?                      │
└─────────────────────────────────────────────────────┘

¿Necesitas guardar datos de UNA entidad completa?
   → REGISTRO

¿Tienes una secuencia de valores del mismo tipo?
   → ARREGLO

¿Necesitas almacenar MUCHAS entidades similares?
   → TABLA

¿La cantidad de elementos varía según el caso?
   → LISTA

¿Necesitas buscar valores por un nombre/código?
   → DICCIONARIO
```

** EJERCICIO PARA TI:**

Identifica estructuras en tu documento:

```
ANÁLISIS DE ESTRUCTURAS
════════════════════════

1. REGISTROS identificados:
   
   Registro 1: ________________________________
   Campos que incluye:
   - _____________________________________________
   - _____________________________________________
   - _____________________________________________

2. ARREGLOS identificados:
   
   Arreglo 1: _________________________________
   Tipo de elementos: __________________________
   Cantidad aproximada: ________________________

3. TABLAS necesarias:
   
   Tabla 1: ___________________________________
   Campos principales:
   - _____________________________________________
   - _____________________________________________

4. LISTAS identificadas:
   
   Lista 1: ___________________________________
   Tipo de elementos: __________________________
   ¿Por qué es lista y no arreglo?: ___________

5. DICCIONARIOS identificados:
   
   Diccionario 1: ______________________________
   Clave: ______________________________________
   Valor: ______________________________________
```

---

### ETAPA 7: Validación y Caso de Uso

#### 7.1 Validar el Análisis con Cálculos

**Objetivo:**
Verificar que los datos identificados son suficientes y correctos para regenerar el documento.

**Método:**
Intentar calcular manualmente los valores finales usando los datos del diccionario.

**Ejemplo - Caso CFE:**

**Datos de entrada (del diccionario):**
```
lectura_anterior = 0
lectura_actual = 40
precio_basico = 1.043
limite_basico = 75
```

**Cálculo manual:**
```
Paso 1: Consumo total
consumo_total = lectura_actual - lectura_anterior
consumo_total = 40 - 0 = 40 kWh

Paso 2: Determinar rango
Si consumo_total <= limite_basico (40 <= 75) → TRUE
Entonces: Todo el consumo está en rango básico

consumo_basico = 40 kWh
consumo_intermedio = 0 kWh
consumo_excedente = 0 kWh

Paso 3: Calcular costo
costo_basico = consumo_basico × precio_basico
costo_basico = 40 × 1.043 = 41.72 pesos

Paso 4: Calcular IVA
iva = subtotal × 0.16
iva = 41.72 × 0.16 = 6.67 pesos

Paso 5: Total preliminar
total = costo_basico + iva + DAP
total = 41.72 + 6.67 + 46.00 = 94.39 pesos
```

**Validación:**
```
¿El total calculado coincide con el del documento?
Documento: $107.09
Calculado: $94.39

No coincide → Hay datos faltantes

Revisión:
Faltó considerar: Adeudo anterior ($106.60) y pago anterior ($106.00)

Cálculo correcto:
total = 41.72 + 8.34 + 46.00 + 106.60 - 106.00 = 96.66

Aún no coincide → Revisar otros conceptos...
```

#### 7.2 Criterios de Validación

**Tu análisis está completo si:**

□ Puedes reconstruir el documento completo con los datos identificados  
□ Los cálculos manuales coinciden con los valores del documento  
□ No faltan datos críticos para generar el documento  
□ Las relaciones entre datos son claras y lógicas  
□ Los tipos de datos permiten las operaciones necesarias  

#### 7.3 Documentar el Proceso Completo

**Crea un informe final que incluya:**

1. **Portada**
   - Título del proyecto
   - Documento analizado
   - Tu nombre
   - Fecha

2. **Introducción**
   - Descripción del documento
   - Objetivo del análisis
   - Contexto del negocio

3. **Metodología**
   - Proceso seguido
   - Herramientas utilizadas
   - Criterios de clasificación

4. **Resultados**
   - Diccionario de datos completo
   - Estructuras identificadas
   - Diagramas visuales

5. **Validación**
   - Cálculos de verificación
   - Casos de prueba
   - Hallazgos

6. **Conclusiones**
   - Aprendizajes
   - Dificultades encontradas
   - Recomendaciones

7. **Anexos**
   - Fotografías del documento original
   - Esquemas de secciones
   - Tablas de apoyo

** EJERCICIO FINAL:**

Realiza la validación completa de tu análisis:

```
VALIDACIÓN DEL ANÁLISIS
════════════════════════

1. Cálculo de verificación:
   
   Dato calculado: _____________________________
   Valor en documento: _________________________
   ¿Coincide?: [ ] Sí  [ ] No
   
   Si no coincide, ¿qué datos faltaron?:
   ___________________________________________

2. Completitud del diccionario:
   
   Total conceptos en documento: ______________
   Total conceptos en diccionario: ____________
   ¿Están todos?: [ ] Sí  [ ] No
   
   Conceptos faltantes identificados:
   ___________________________________________

3. Autoevaluación:
   
   ¿Podría reconstruir el documento con mi análisis?
   [ ] Completamente
   [ ] Con algunas lagunas
   [ ] Falta información crítica
   
   Nivel de confianza: [ ] Alto [ ] Medio [ ] Bajo
```

---

## CASO COMPLETO: RECAPITULACIÓN CFE

### Resumen del Análisis del Recibo de Luz

**ETAPA 1: Contexto**
- Realidad: Consumo eléctrico doméstico
- Necesidad: Facturar y cobrar el servicio
- Actores: CFE (proveedor), Usuario (cliente)
- Documento: Recibo de Luz bimestral

**ETAPA 2: Análisis Visual**
- 5 secciones principales identificadas
- Layout estructurado y estandarizado
- Información organizada jerárquicamente

**ETAPA 3: Extracción**
- 40+ conceptos identificados
- Distribución: ID(5), Fechas(4), Medición(6), Costos(25+)

**ETAPA 4: Clasificación**
- Alfanuméricos: 8 campos (nombres, códigos)
- Enteros: 12 campos (lecturas, consumos)
- Reales: 18 campos (precios, montos)
- Fechas: 4 campos (periodo, límites)
- Lógicos: 3 campos (estados, indicadores)
- BLOBs: 2 campos (código barras, gráficos)

**ETAPA 5: Diccionario**
- 40+ registros documentados
- 3 campos únicos identificados (llaves primarias)
- Convención snake_case aplicada

**ETAPA 6: Estructuras**
- Registros: Cliente, Medición, Facturación
- Arreglos: Historial de 12 meses
- Tablas: Clientes, Consumos, Tarifas
- Listas: Cargos variables
- Diccionarios: Precios por tarifa

**ETAPA 7: Validación**
- Cálculos verificados manualmente
- Documento reconstruible con los datos
- Análisis completo y validado

---

## CHECKLIST DE ENTREGA FINAL

### Documentos Requeridos

□ **Cuaderno de Análisis**
  - Fotografías del documento original
  - Esquema de secciones identificadas
  - Lista completa de conceptos extraídos
  - Clasificación de tipos de datos
  - Notas y observaciones

□ **Diccionario de Datos**
  - Tabla completa (mínimo 20 conceptos)
  - Todas las columnas llenas
  - Nomenclatura correcta
  - Campos únicos identificados

□ **Análisis de Estructuras**
  - Registros diseñados
  - Arreglos especificados
  - Tablas relacionadas
  - Listas documentadas
  - Diccionarios definidos

□ **Validación**
  - Cálculos de verificación
  - Casos de prueba
  - Confirmación de completitud

□ **Informe Final**
  - Formato profesional
  - Todas las secciones incluidas
  - Redacción clara
  - Ortografía revisada

### Criterios de Calidad

**Excelente (9-10):**
- Análisis exhaustivo y completo
- Diccionario impecable
- Estructuras bien justificadas
- Validación rigurosa
- Presentación profesional

**Bueno (7-8):**
- Análisis completo con errores menores
- Diccionario con algunas inconsistencias
- Estructuras identificadas pero mal justificadas
- Validación superficial
- Presentación aceptable

**Suficiente (6):**
- Análisis incompleto
- Diccionario con errores significativos
- Estructuras mal identificadas
- Sin validación
- Presentación descuidada

**Insuficiente (<6):**
- Análisis muy incompleto
- Diccionario inutilizable
- No identifica estructuras
- No hay validación
- Presentación inaceptable

---

## 🎓 REFLEXIÓN FINAL

### ¿Por qué es importante este proceso?

**1. Pensamiento Analítico**
Desarrollas la capacidad de:
- Descomponer problemas complejos
- Identificar patrones
- Abstraer conceptos
- Estructurar información

**2. Competencia Digital**
Entiendes cómo:
- Los sistemas digitales modelan la realidad
- Se diseñan bases de datos
- Se estructura la información
- Se automatizan procesos

**3. Aplicación Profesional**
Preparación para:
- Diseñar sistemas de información
- Analizar procesos empresariales
- Digitalizar organizaciones
- Gestionar datos empresariales

### ¿Dónde se aplica?

- **Bancos:** Estados de cuenta, préstamos
- **Hospitales:** Historias clínicas, recetas
- **Escuelas:** Boletas, control escolar
- **Retail:** Facturas, inventarios
- **Gobierno:** Trámites, servicios
- **Cualquier organización con datos**

### Lecciones Clave

1. **La realidad es compleja, pero estructurable**
   - Todo proceso puede descomponerse
   - Los datos organizados tienen poder

2. **El detalle importa**
   - Cada dato tiene un propósito
   - Omitir información puede invalidar el análisis

3. **La metodología asegura calidad**
   - Seguir un proceso sistemático reduce errores
   - La validación es crítica

4. **La documentación preserva conocimiento**
   - Un buen diccionario es una herramienta permanente
   - Facilita el mantenimiento y evolución

---

## 📚 RECURSOS COMPLEMENTARIOS

### Bibliografía Recomendada

1. **Forouzan, B. A. (2003).** *Introducción a la ciencia de la computación*
   - Capítulos sobre tipos de datos y estructuras

2. **Silberschatz, A. et al. (2000).** *Fundamentos de bases de datos*
   - Modelado de datos
   - Diseño relacional

3. **Date, C. J.** *Introducción a los sistemas de bases de datos*
   - Teoría de bases de datos relacionales

### Herramientas Online

- **Diccionario de Datos:** [DB Designer](https://www.dbdesigner.net/)
- **Modelado ER:** [Lucidchart](https://www.lucidchart.com/)
- **Diagramas:** [Draw.io](https://draw.io/)

---

## PREGUNTAS FRECUENTES

**P: ¿Cuántos conceptos mínimo debo identificar?**
R: Mínimo 20, pero idealmente TODOS los que aparezcan en el documento.

**P: ¿El recibo de luz puede ser mi caso de estudio?**
R: NO. Ya fue usado como ejemplo. Elige otro documento.

**P: ¿Puedo usar facturas electrónicas?**
R: Sí, pero asegúrate de tener acceso a todos los datos.

**P: ¿Qué hago si dos conceptos parecen muy similares?**
R: Si tienen diferente función o aparecen en contextos distintos, son conceptos separados.

**P: ¿Cómo sé si clasifiqué bien un tipo de dato?**
R: Pregúntate: ¿Qué operaciones haré con este dato? Eso determina el tipo.

**P: ¿Un documento muy simple es suficiente?**
R: Debe tener al menos 20 conceptos diferentes y mostrar variedad de tipos de datos.

---

## OBJETIVOS DE APRENDIZAJE ALCANZADOS

Al completar esta metodología, ahora eres capaz de:

✅ Analizar sistemáticamente documentos administrativos  
✅ Identificar y clasificar tipos de datos correctamente  
✅ Crear diccionarios de datos profesionales  
✅ Reconocer estructuras de datos en contextos reales  
✅ Validar la completitud de un análisis  
✅ Documentar tu trabajo técnicamente  
✅ Pensar como un analista de sistemas  

---

**¡ÉXITO EN TU ANÁLISIS!** 🚀

*"La digitalización comienza con entender profundamente la realidad que queremos representar. Un buen análisis de datos es el fundamento de cualquier sistema exitoso."*

**Versión:** 2.0 - Metodología de Análisis  
**Fecha:** 2025
