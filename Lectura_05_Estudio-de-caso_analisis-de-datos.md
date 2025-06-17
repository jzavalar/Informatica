# **Lectura 5. Estudio de Caso: Análisis de Datos**

prof. dr. Jesús Zavala Ruiz[^1]

---

## **Introducción**

Para construir el estudio de caso del **servicio de luz** y su digitalización, nos enfocaremos en cómo la **Comisión Federal de Electricidad (CFE)** en México maneja un sistema que parte de la realidad del consumo eléctrico en cada hogar y empresa, y cómo esta realidad se codifica y estructura en datos para crear un recibo de luz, como el mostrado en la Figura 1: 
(Código HTML para desplegar la imagen: 
```text
![Recibo de luz de la CFE](https://github.com/jzavalar/Informatica/blob/main/images/123456789100_Page_1.png)
```
Figura 1. Recibo de Luz de la CFE
![Recibo de luz de la CFE](https://github.com/jzavalar/Informatica/blob/main/images/123456789100_Page_1.png)
Figura 1. Recibo de Luz de la CFE

(Código HTML para desplegar la imagen: 
```text
<img src="https://github.com/jzavalar/Informatica/blob/main/images/123456789100_Page_1.png" alt="Recibo de Luz de la CFE" style="width: 90%; height: auto; margin: 20px auto; display: block;">
```
<img src="https://github.com/jzavalar/Informatica/blob/main/images/123456789100_Page_1.png" alt="Recibo de Luz de la CFE" style="width: 90%; height: auto; margin: 20px auto; display: block;">

Este recibo es el resultado de un proceso en el que se miden, interpretan y almacenan datos de consumo para informar al usuario y realizar el cobro correspondiente. La narrativa se desarrolla en tres partes: (1) la realidad (el servicio de luz), (2) los datos (la recolección, creación y organización de datos) y (3) validación de los datos (el recibo de luz digitalizado).

## **1. La Realidad: El Consumo Eléctrico y el Servicio de Luz**

### **1.1. Contexto**

La **electricidad** es un recurso esencial en la vida moderna, indispensable para actividades domésticas, comerciales e industriales. En México, la Comisión Federal de Electricidad (CFE) es responsable de suministrar este servicio a millones de hogares y empresas a nivel nacional. La electricidad permite el funcionamiento de electrodomésticos, sistemas de climatización, iluminación y tecnologías de comunicación y entretenimiento. Sin embargo, la provisión de electricidad no es gratuita; implica costos de generación, distribución y mantenimiento de la infraestructura.

Para administrar este servicio, la CFE debe rastrear el **consumo de electricidad** de cada usuario, lo que varía significativamente según factores como el tipo de cliente (doméstico o industrial), las condiciones climáticas y los hábitos de consumo. Este seguimiento permite a la CFE aplicar tarifas ajustadas a los niveles de consumo y ofrecer subsidios en algunos casos, promoviendo el uso eficiente de la energía.

### **1.2. La Necesidad: Cobrar el Servicio de Luz**

El **recibo de luz** es el documento final que permite al usuario visualizar y comprender su consumo eléctrico, al mismo tiempo que actúa como el medio formal de la CFE para realizar el cobro. La creación de este recibo es posible gracias a la **codificación de datos** que transforma las lecturas de consumo y los detalles del usuario en un formato estandarizado. A partir de la información digitalizada, el sistema de la CFE genera automáticamente un recibo que incluye:

   - **Datos del usuario**: Nombre, dirección y número de servicio.
   - **Periodo de facturación**: Inicio y fin del periodo de consumo medido.
   - **Detalles de consumo**: Cantidad de kWh consumidos en cada rango tarifario (básico, intermedio y excedente).
   - **Desglose de costos**: Subtotal del consumo en cada rango tarifario, sumas de impuestos (IVA), y cargos adicionales (como el Derecho de Alumbrado Público - DAP).
   - **Total a pagar**: La suma final que el usuario debe cubrir para saldar su consumo del periodo.

Cada recibo es una **representación digital de la realidad del consumo eléctrico** del usuario. Este documento no solo facilita la recaudación de ingresos para la CFE, sino que también ofrece al usuario una herramienta para monitorear su uso de energía y tomar decisiones informadas sobre su consumo. 

### **1.3. La Necesidad de Digitalización**

El **consumo eléctrico**, aunque es una realidad física, debe traducirse en datos cuantificables para poder ser medido y cobrado. Esta traducción se realiza mediante **medidores eléctricos** instalados en cada punto de servicio (domicilio o empresa). Estos medidores registran el flujo de energía en unidades de kilovatios-hora (kWh), que representan la cantidad de energía consumida durante un periodo específico.

Los datos capturados por el medidor incluyen:
   - **Lectura actual**: El número total de kWh al final del periodo.
   - **Lectura anterior**: El número total de kWh al inicio del periodo.
   - **Consumo del periodo**: La diferencia entre la lectura actual y la anterior.

Además de estos datos, otros factores deben ser codificados:
   - **Tarifa aplicada**: Determinada por el tipo de cliente y nivel de consumo.
   - **Ubicación y tipo de usuario**: Definidos para aplicar tarifas específicas (residencial, comercial, industrial).
   - **Rangos tarifarios**: Segmentos de consumo (básico, intermedio, excedente) que permiten ajustar el cobro según los subsidios y los niveles de uso.

Cada uno de estos elementos es capturado, digitalizado y almacenado en una **base de datos central**. Este proceso de digitalización permite que los datos de millones de usuarios se estructuren en un formato uniforme y se mantengan accesibles para el cálculo de facturas, la generación de estadísticas de consumo y la administración del servicio a nivel nacional.

### **1.4. Ventajas de la Digitalización del Servicio de Luz**

La codificación y digitalización del servicio de luz ofrecen múltiples ventajas:
   - **Eficiencia**: Los datos de consumo de millones de usuarios pueden procesarse y facturarse automáticamente.
   - **Transparencia**: Cada recibo proporciona un desglose claro de cómo se calcula el total a pagar, permitiendo a los usuarios entender sus costos.
   - **Flexibilidad y Personalización**: La CFE puede aplicar diferentes tarifas y subsidios y ajustar el recibo a las características individuales de consumo de cada usuario.
   - **Monitoreo y Análisis**: La base de datos de consumo permite a la CFE monitorear patrones de consumo a nivel regional y temporal, ayudando a planificar la demanda y ajustar la oferta de energía.

## **2. Los Datos: Codificación de los Conceptos**

### **2.1. Contexto**

A continuación se expone un resumen estructurado de los **conceptos de la realidad** que deben ser consignados en la **base de datos central** de la CFE, tal como lo haría un analista de sistemas. Este primer entregable describe los **datos clave** que *representan la realidad* del consumo y los detalles del usuario, y que serán fundamentales para generar el recibo de luz. La lista se basa en el contexto desarrollado en el caso de uso.

### **2.2. Conceptos de la Realidad por Digitalizar**

1. **Información del Cliente y Punto de Servicio**
   - **Número de Servicio**: Identificación única asignada a cada cliente para su facturación.
   - **RMU (Registro Móvil de Usuario)**: Código único que permite rastrear la ubicación y el historial del usuario en el sistema.
   - **Nombre o Razón Social**: Nombre del titular del servicio (persona o entidad).
   - **Dirección de Suministro**: Incluye la calle, número, colonia, ciudad, código postal y entidad federativa.
   - **Tipo de Usuario**: Clasificación del cliente (doméstico, comercial, industrial).
   
2. **Datos de Medición**
   - **Número de Medidor**: Código que identifica el equipo instalado en el domicilio o empresa para medir el consumo eléctrico.
   - **Tipo de Medidor**: Especifica si el medidor es electromecánico o digital.
   - **Lectura Anterior**: Registro de kWh al inicio del periodo de facturación.
   - **Lectura Actual**: Registro de kWh al final del periodo de facturación.
   - **Multiplicador**: Factor aplicado a la lectura para ajustar el cálculo de consumo según el tipo de medidor.

3. **Periodo de Facturación**
   - **Fecha de Inicio del Periodo**: Fecha en que comienza la medición del consumo.
   - **Fecha de Fin del Periodo**: Fecha en que termina la medición del consumo.
   - **Límite de Pago**: Fecha límite para que el usuario realice el pago sin recargos.
   - **Fecha de Corte**: Fecha a partir de la cual se procederá al corte del servicio en caso de impago.

4. **Datos de Consumo**
   - **Consumo por Nivel Tarifario**:
     - **Consumo Básico (kWh)**: kWh consumidos en el rango básico de la tarifa.
     - **Consumo Intermedio (kWh)**: kWh consumidos en el rango intermedio de la tarifa.
     - **Consumo Excedente (kWh)**: kWh consumidos en el rango excedente de la tarifa.
   - **Consumo Total (kWh)**: Suma de los kWh en todos los niveles tarifarios.

5. **Detalle de Costos**
   - **Precio por Nivel Tarifario**:
     - **Precio Básico ($/kWh)**: Costo por kWh en el rango básico.
     - **Precio Intermedio ($/kWh)**: Costo por kWh en el rango intermedio.
     - **Precio Excedente ($/kWh)**: Costo por kWh en el rango excedente.
   - **Subtotal de Consumo**: Total del costo de consumo antes de impuestos y cargos adicionales.
   
6. **Costos de la Energía en el Mercado Mayorista**
   - **Suministro**: Costo por el suministro de electricidad al usuario.
   - **Distribución**: Costo de distribución de electricidad en media y baja tensión.
   - **Transmisión**: Costo por la transmisión de electricidad.
   - **CENACE**: Costo asociado al Centro Nacional de Control de Energía.
   - **Generación**: Costo de generación de electricidad en los diferentes periodos (base, intermedio, punta).
   - **Capacidad**: Costo de capacidad de carga según demanda.
   - **ScnMEM**: Cargos de servicio relacionados con el mercado eléctrico mayorista.
   - **Aportación Gubernamental**: Subsidio del gobierno que reduce el costo total en ciertos casos.

7. **Desglose de Importe a Pagar**
   - **IVA**: Impuesto al Valor Agregado aplicado al subtotal de consumo.
   - **Derecho de Alumbrado Público (DAP)**: Cargo adicional por el uso de alumbrado público.
   - **Cargos y Créditos**: Cualquier otro cargo o crédito adicional aplicado al recibo (e.g., ajustes por redondeo, cargos pendientes de otros periodos).
   - **Adeudo Anterior**: Cantidad pendiente de pagos anteriores.
   - **Pago Anterior**: Pago realizado en el periodo anterior.
   - **Total a Pagar**: Monto final que el usuario debe pagar para el periodo actual.

8. **Información Adicional del Recibo**
   - **Talón de Caja**:
     - **Código de Barras**: Código para realizar el pago en ventanillas de la CFE o bancos.
     - **Canales de Contacto**: Información para que el cliente reporte problemas o levante aclaraciones.
   
   - **Indicador de Consumo**: Gráfico que muestra el nivel de consumo y recomienda medidas de ahorro energético para evitar el paso a la tarifa de alto consumo (DAC).

9. **Catálogo de Cargos y Créditos Adicionales**
   - **Diagnóstico Energético**: Cargo por asesoría para mejorar el consumo energético.
   - **Financiamiento**: Cargo por financiamiento de mejoras en el consumo.
   - **Reconexión**: Cargo por reconexión del servicio después de un corte.
   - **Revisión del Medidor**: Costo de inspección y revisión del funcionamiento del medidor.
   - **Bonificación por Interrupción**: Bonificación por interrupciones en el suministro.
   - **Otros Cargos**: Cualquier otro cargo aplicable (e.g., ajustes de convenios, actualizaciones de demanda).
   
### **2.3. Codificación de los Datos**

La tabla resumen que se muestra a continuación es la lista de conceptos de la realidad que se consignarían en la base de datos central de la CFE, es decir, es el producto de la **codificación de los datos**. Está organizada como un **diccionario de datos**, que relaciona los conceptos de la realidad con su representación simbólica como dato. Por eso, a cada concepto se le ha asignado un nombre corto, llamado "campo" o "Variable", el "Tipo de Dato" y si el valor es "Único" (para aquellos campos que deben ser exclusivos para cada cliente o registro).

| **Concepto**                       | **Variable**            | **Tipo de Dato** | **Único** | **Descripción** |
|------------------------------------|---------------------------------|------------------|-----------|-----------------|
| **Número de Servicio**             | num_servicio                    | Alfanumérico     | Sí        | Identificación única asignada a cada cliente. |
| **RMU (Registro Móvil de Usuario)**| rmu                             | Alfanumérico     | Sí        | Código único para rastrear ubicación e historial del usuario. |
| **Nombre o Razón Social**          | nombre_usuario                  | Texto            | No        | Nombre del titular del servicio (persona o entidad). |
| **Dirección de Suministro**        | direccion                       | Texto            | No        | Dirección completa del suministro eléctrico. |
| **Tipo de Usuario**                | tipo_usuario                    | Texto            | No        | Clasificación del cliente (doméstico, comercial, industrial). |
| **Número de Medidor**              | num_medidor                     | Alfanumérico     | Sí        | Código que identifica el equipo de medición en el domicilio o empresa. |
| **Tipo de Medidor**                | tipo_medidor                    | Texto            | No        | Tipo de medidor (electromecánico o digital). |
| **Lectura Anterior (kWh)**         | lectura_anterior                | Numérico         | No        | Valor del medidor al inicio del periodo de facturación. |
| **Lectura Actual (kWh)**           | lectura_actual                  | Numérico         | No        | Valor del medidor al final del periodo de facturación. |
| **Multiplicador**                  | multiplicador                   | Numérico         | No        | Factor aplicado a la lectura del medidor. |
| **Fecha de Inicio del Periodo**    | fecha_inicio_periodo            | Fecha            | No        | Fecha en que comienza el periodo de facturación. |
| **Fecha de Fin del Periodo**       | fecha_fin_periodo               | Fecha            | No        | Fecha en que termina el periodo de facturación. |
| **Límite de Pago**                 | limite_pago                     | Fecha            | No        | Fecha límite para realizar el pago sin recargos. |
| **Fecha de Corte**                 | fecha_corte                     | Fecha            | No        | Fecha a partir de la cual se procederá al corte del servicio. |
| **Consumo Básico (kWh)**           | consumo_basico                  | Numérico         | No        | kWh consumidos en el rango básico de la tarifa. |
| **Consumo Intermedio (kWh)**       | consumo_intermedio              | Numérico         | No        | kWh consumidos en el rango intermedio de la tarifa. |
| **Consumo Excedente (kWh)**        | consumo_excedente               | Numérico         | No        | kWh consumidos en el rango excedente de la tarifa. |
| **Consumo Total (kWh)**            | consumo_total                   | Numérico         | No        | Suma de los kWh en todos los niveles tarifarios. |
| **Precio Básico ($/kWh)**          | precio_basico                   | Numérico         | No        | Costo por kWh en el rango básico. |
| **Precio Intermedio ($/kWh)**      | precio_intermedio               | Numérico         | No        | Costo por kWh en el rango intermedio. |
| **Precio Excedente ($/kWh)**       | precio_excedente                | Numérico         | No        | Costo por kWh en el rango excedente. |
| **Subtotal de Consumo**            | subtotal_consumo                | Numérico (Moneda)| No        | Total del costo de consumo antes de impuestos. |
| **Suministro**                     | costo_suministro                | Numérico (Moneda)| No        | Costo por el suministro de electricidad. |
| **Distribución**                   | costo_distribucion              | Numérico (Moneda)| No        | Costo de distribución en media y baja tensión. |
| **Transmisión**                    | costo_transmision               | Numérico (Moneda)| No        | Costo por transmisión de electricidad. |
| **CENACE**                         | costo_cenace                    | Numérico (Moneda)| No        | Costo asociado al Centro Nacional de Control de Energía. |
| **Generación**                     | costo_generacion                | Numérico (Moneda)| No        | Costo de generación de electricidad por periodo. |
| **Capacidad**                      | costo_capacidad                 | Numérico (Moneda)| No        | Costo de capacidad según la demanda. |
| **ScnMEM**                         | costo_scnmem                    | Numérico (Moneda)| No        | Cargos de servicio relacionados con el mercado eléctrico mayorista. |
| **Aportación Gubernamental**       | aportacion_gubernamental        | Numérico (Moneda)| No        | Subsidio del gobierno para reducir el costo. |
| **IVA**                            | iva                             | Numérico (Moneda)| No        | Impuesto al Valor Agregado sobre el subtotal. |
| **Derecho de Alumbrado Público**   | dap                             | Numérico (Moneda)| No        | Cargo adicional para el alumbrado público. |
| **Cargos y Créditos Adicionales**  | cargos_creditos                 | Numérico (Moneda)| No        | Cargos o créditos adicionales aplicados al recibo. |
| **Adeudo Anterior**                | adeudo_anterior                 | Numérico (Moneda)| No        | Cantidad pendiente de pagos anteriores. |
| **Pago Anterior**                  | pago_anterior                   | Numérico (Moneda)| No        | Pago realizado en el periodo anterior. |
| **Total a Pagar**                  | total_pagar                     | Numérico (Moneda)| No        | Monto final que el usuario debe cubrir en el periodo actual. |
| **Código de Barras**               | codigo_barras                   | Binario (Imagen) | No        | Código para realizar el pago en ventanillas de la CFE o bancos. |
| **Indicador de Consumo**           | indicador_consumo               | Binario (Imagen) | No        | Gráfico que muestra el nivel de consumo en colores. |
| **Conceptos Adicionales**          | concepto_adicional              | Texto            | No        | Texto descriptivo de otros cargos y créditos adicionales. |

Esta tabla es el primer entregable del **análisis de datos** que se convierte en un **diccionario de datos** para la base de datos central de la CFE, donde se almacenarán los datos de cada cliente y su consumo de electricidad. La estructura permite que el sistema administre de manera eficiente el registro de consumo, la generación de recibos detallados y la aplicación de políticas tarifarias de forma consistente.

Cada campo o Variable representa un aspecto de la realidad del servicio eléctrico, traducido en un dato digital que facilita el seguimiento del consumo, la transparencia en el cobro y el análisis para la optimización de la distribución de energía. 

Con esta base de datos central organizada, la CFE puede gestionar el suministro de electricidad para millones de usuarios, ofreciendo una experiencia de facturación transparente y estructurada que refleja fielmente el consumo real de cada cliente. 

## **3. El Recibo de Luz: Aplicación y Validación**

### **3.1. Contexto**

El recibo de luz se convierte en el documento que permite cobrar el consumo de luz, logrando el **objetivo de negocio** y validando la precisión del análisis de datos realizado. Este análisis considera las áreas de datos identificadas, los tipos especiales de datos y el tratamiento adecuado de datos alfanuméricos y numéricos para su correcta codificación en la base de datos de la CFE.

### **3.2. Áreas de Datos en el Recibo de Luz**

A partir del recibo mostrado en la [Figura 1](https://github.com/jzavalar/Informatica/blob/main/images/123456789100_Page_1.png), se identificaron las siguientes áreas clave, donde cada una organiza y presenta información específica:

1. **Información del Cliente y Servicio**:
   - **Nombre**: JUAN PEREZ JOLOTE  
     - **Descripción**: Nombre completo del usuario.  
     - **Tipo de Dato**: Texto  
   - **Dirección**: Av. Paseo de la Reforma 164 Int 4, Vicente Guerrero y Morelos, San Juan Ixtacala amp Norte, C.P. 54168, Tlalnepantla de Baz, Estado de México.  
     - **Descripción**: Dirección completa del suministro eléctrico.  
     - **Tipo de Dato**: Texto  
   - **Número de Servicio**: `123456789100`  
     - **Descripción**: Identificador único del cliente.  
     - **Tipo de Dato**: Alfanumérico  
   - **RMU**: `54168 03 09-09 XAXX-010101 001 CFE`  
     - **Descripción**: Registro Móvil de Usuario (identificación interna).  
     - **Tipo de Dato**: Alfanumérico  
   - **Número de Cuenta**: `29DF07D012345678`  
     - **Descripción**: Código de cuenta asignado al cliente.  
     - **Tipo de Dato**: Alfanumérico  

2. **Periodo de Facturación y Fechas Clave**:
   - **Periodo de Facturación**: 23 JUL 2023 - 23 SEP 2023  
     - **Descripción**: Periodo en el que se mide el consumo de electricidad.  
     - **Tipo de Dato**: Fecha  
   - **Límite de Pago**: 06 OCT 2023  
     - **Descripción**: Fecha límite para realizar el pago sin recargos.  
     - **Tipo de Dato**: Fecha  
   - **Fecha de Corte**: 07 OCT 2023  
     - **Descripción**: Fecha en la cual se realiza el corte del servicio en caso de impago.  
     - **Tipo de Dato**: Fecha  

3. **Datos de Consumo**:
   - **Lectura Anterior**: 0 kWh (Estimada)  
     - **Descripción**: Valor del medidor al inicio del periodo de facturación.  
     - **Tipo de Dato**: Numérico  
   - **Lectura Actual**: 40 kWh (Medida)  
     - **Descripción**: Valor del medidor al final del periodo de facturación.  
     - **Tipo de Dato**: Numérico  
   - **Multiplicador**: 1  
     - **Descripción**: Factor aplicado para ajustar el cálculo de consumo.  
     - **Tipo de Dato**: Numérico  
   - **Consumo en kWh**:
     - **Consumo Básico**: 40 kWh  
       - **Descripción**: kWh consumidos en el rango básico de la tarifa.  
       - **Tipo de Dato**: Numérico  
     - **Total Consumo**: 40 kWh  
       - **Descripción**: Consumo total registrado en el periodo.  
       - **Tipo de Dato**: Numérico  

4. **Costos de la Energía y Desglose de Importe a Pagar**:
   - **Subtotal de Consumo Básico**: $41.72 MXN  
     - **Descripción**: Costo de consumo en el rango básico de la tarifa.  
     - **Tipo de Dato**: Numérico (Moneda)  
   - **IVA (16%)**: $8.34 MXN  
     - **Descripción**: Impuesto al Valor Agregado aplicado al subtotal.  
     - **Tipo de Dato**: Numérico (Moneda)  
   - **Derecho de Alumbrado Público (DAP)**: $46.00 MXN  
     - **Descripción**: Cargo adicional por el uso de alumbrado público.  
     - **Tipo de Dato**: Numérico (Moneda)  
   - **Adeudo Anterior**: $106.60 MXN  
     - **Descripción**: Cantidad pendiente de pagos anteriores.  
     - **Tipo de Dato**: Numérico (Moneda)  
   - **Pago Anterior**: $106.00 MXN  
     - **Descripción**: Pago realizado en el periodo anterior.  
     - **Tipo de Dato**: Numérico (Moneda)  
   - **Total a Pagar**: $107.09 MXN  
     - **Descripción**: Monto final que el usuario debe cubrir para el periodo actual.  
     - **Tipo de Dato**: Numérico (Moneda)  

5. **Talón de Caja**:
   - **Total a Pagar**: $107.09 MXN  
     - **Descripción**: Monto total a pagar indicado en el talón.  
     - **Tipo de Dato**: Numérico (Moneda)  
   - **Código de Barras**: (Visual en el recibo para facilitar el pago)  
     - **Descripción**: Código utilizado para el pago en ventanillas o bancos.  
     - **Tipo de Dato**: Binario (Imagen)  
   - **Número de Cuenta y Servicio**: `29DF07D012345678` y `123456789100`  
     - **Descripción**: Identificadores adicionales del cliente y su servicio.  
     - **Tipo de Dato**: Alfanumérico  

Estas áreas de datos se distribuyen en el recibo de forma que el usuario pueda acceder fácilmente a información relevante, como su consumo, el costo, las fechas de pago y el desglose de los importes.

### **3.3. Tipos de Datos en el Recibo de Luz**

Los diferentes tipos de datos utilizados en el recibo de luz se clasifican en:

1. **Texto**:
   - Datos que contienen caracteres alfabéticos, numéricos y especiales. Utilizado para información descriptiva o identificadores alfanuméricos. Ejemplos: Nombre, Dirección.

2. **Alfanumérico**:
   - Combinación de letras, números y caracteres especiales que funcionan como identificadores únicos en el sistema. Ejemplos: Número de Servicio, RMU, Número de Cuenta.

3. **Numérico**:
   - Representa valores exclusivamente numéricos utilizados para cálculos. Incluye el consumo de electricidad, lecturas del medidor. Ejemplos: Consumo en kWh, Lectura Anterior, Lectura Actual.

4. **Fecha**:
   - Tipo de dato que almacena fechas en formato estandarizado para facilitar el cálculo de periodos y validaciones temporales. Ejemplos: Periodo de Facturación, Límite de Pago, Fecha de Corte.

5. **Numérico (Moneda)**:
   - Valores numéricos que representan montos en una moneda específica (MXN en este caso), utilizados en cálculos monetarios y presentados con precisión decimal. Ejemplos: Subtotal de Consumo Básico, IVA, Total a Pagar.

6. **Binario (Imagen)**:
   - Tipo de dato que contiene información visual o gráfica, como un código de barras o un indicador gráfico, que no se interpreta como texto o números sino como un recurso visual. Ejemplo: Código de Barras.

### **3.4. Tipos Especiales de Datos**

Dentro de estas áreas, se identificaron varios tipos especiales de datos que deben manejarse de manera específica en la base de datos:

#### **Fechas**
   - **Campos**: 
     - Fecha de Inicio del Periodo: `23 JUL 2023`
     - Fecha de Fin del Periodo: `23 SEP 2023`
     - Límite de Pago: `06 OCT 2023`
     - Fecha de Corte: `07 OCT 2023`
   - **Tratamiento**: Las fechas deben almacenarse en un formato estándar (ej., AAAAMMDD) para asegurar consistencia en su uso y permitir el cálculo de periodos y plazos de pago.

#### **Listas de Datos o Dataframes**
   - **Consumo por Nivel Tarifario**:
     - **Campos y Valores**: Consumo Básico: `40 kWh`, Precio Básico: `$1.043/kWh`, Subtotal Básico: `$41.72 MXN`
     - **Propósito**: Estos datos reflejan el consumo en distintos niveles tarifarios y permiten el cálculo preciso del costo total.
   
   - **Costos de la Energía y Desglose de Importe**:
     - **Campos y Valores**:
       - Subtotal de Consumo Básico: `$41.72 MXN`
       - IVA (16%): `$8.34 MXN`
       - Derecho de Alumbrado Público (DAP): `$46.00 MXN`
       - Adeudo Anterior: `$106.60 MXN`
       - Pago Anterior: `$106.00 MXN`
       - Total a Pagar: `$107.09 MXN`
     - **Propósito**: Esta lista permite desglosar cada costo y calcular el monto final, proporcionando transparencia al usuario.

Almacenarlos como **dataframes** en la base de datos permite que cada uno de estos elementos se procese y sume adecuadamente para obtener el total, manteniendo una estructura que facilita su consulta y análisis.

### **3.5. Identificadores Únicos y Datos Complejos**

En el recibo, algunos campos tienen apariencia alfanumérica pero representan valores únicos y constantes, esenciales para identificar de manera inequívoca al usuario o al equipo de medición:

1. **Número de Servicio**:
   - **Valor**: `123456789100`
   - **Descripción**: Funciona como el identificador único del cliente en la base de datos.
   
2. **Número de Medidor**:
   - **Valor**: `G3644V`
   - **Descripción**: Aunque contiene letras y números, es un identificador único para el equipo de medición del cliente.
   
3. **RMU (Registro Móvil de Usuario)**:
   - **Valor**: `54168 03 09-09 XAXX-010101 001 CFE`
   - **Descripción**: Sirve como identificador constante en el sistema para el usuario.

Estos campos deben definirse como únicos en la base de datos para evitar duplicados y asegurar que cada usuario esté correctamente identificado.

### **3.6. Aplicaciones en Administración Empresarial**

Los conceptos de codificación de datos y estructuración de información vistos en este caso de estudio tienen aplicaciones directas en la administración:

1. **Gestión de clientes y facturación**: Similar al caso de la CFE, las empresas necesitan sistemas robustos para codificar datos de clientes, productos y servicios para generar facturas precisas. La metodología aplicada en este caso puede adaptarse a cualquier empresa que preste servicios recurrentes a sus clientes.

2. **Análisis de consumo y segmentación**: Los datos recopilados permiten análisis de patrones de consumo para:
   - Segmentar clientes según nivel de uso
   - Identificar oportunidades de venta cruzada
   - Optimizar precios y ofertas

3. **Toma de decisiones basada en datos**: La estructuración correcta de datos permite:
   - Proyectar ingresos futuros
   - Planificar recursos según demanda histórica
   - Identificar anomalías y oportunidades de mejora

**Ejemplo práctico**: Una cadena de tiendas departamentales podría aplicar principios similares para analizar las compras de sus clientes con tarjeta de fidelidad:

| **Concepto** | **Variable** | **Tipo de Dato** | **Único** | **Descripción** |
|--------------|--------------|------------------|-----------|-----------------|
| **ID Cliente** | id_cliente | Alfanumérico | Sí | Identificador único del cliente en el programa de fidelidad |
| **Nombre Cliente** | nombre_cliente | Texto | No | Nombre completo del cliente |
| **Compra Total Mensual** | compra_mensual | Numérico (Moneda) | No | Monto total de compras en el mes |
| **Segmento Cliente** | segmento | Texto | No | Clasificación del cliente (oro, plata, bronce) |
| **Puntos Acumulados** | puntos | Numérico | No | Puntos de fidelidad acumulados |
| **Fecha Última Compra** | fecha_ultima_compra | Fecha | No | Fecha de la última transacción |

## **4. Conclusiones**

1. La **codificación de datos** transforma la realidad en información accesible y utilizable. El proceso de codificación de datos en un sistema digital convierte el consumo de electricidad, un fenómeno físico continuo, en información estructurada y accesible para el usuario final. Cada dato, desde el número de servicio hasta el consumo en kWh y las fechas de pago, es un reflejo directo de la realidad del uso de energía por parte del cliente. Esta transformación permite a la CFE, administrar grandes volúmenes de datos de manera eficiente y proporcionar a los usuarios una representación detallada y comprensible de su consumo. La digitalización, por tanto, hace que un recurso tan esencial como la electricidad sea monitoreable y gestionable a través de los datos, beneficiando tanto a la administración como a los consumidores.

2. La **organización en áreas de datos** facilita la comprensión y transparencia. Dividir el recibo en áreas de datos (información del cliente, fechas clave, consumo, desglose de costos y talón de caja) permite un diseño de interfaz claro y organizado que facilita la comprensión de la información. Esta organización en áreas bien definidas es una práctica fundamental en el análisis de datos, ya que agrupa elementos similares y los presenta de manera lógica. La transparencia en el desglose de costos y la claridad en la presentación de fechas y detalles de consumo son el resultado directo de esta organización. En el ensayo académico, esta conclusión resalta la importancia de estructurar los datos de forma que sean comprensibles para el usuario, reforzando la confianza en el sistema de facturación y en la empresa que ofrece el servicio.

3. La necesidad de un **tratamiento específico para tipos especiales de datos**. La precisión en el manejo de tipos especiales de datos, como las **fechas** y las **listas de consumos tarifarios** o **costos**, es esencial para el correcto funcionamiento del sistema de información. Las fechas, al estar estandarizadas, permiten cálculos automáticos y ajustes en caso de pagos tardíos o cortes, mientras que las listas de consumo y costos permiten que el sistema desglose el total de manera transparente. El tratamiento adecuado de tipos especiales de datos es un paso crítico en la codificación de la realidad. La digitalización de estos elementos convierte la información en datos manejables y confiables, haciendo que sistemas complejos sean más eficientes y accesibles.

4. Los identificadores únicos como **garantía de integridad y seguimiento**. Los identificadores únicos, como el número de servicio, el RMU y el número de medidor, son fundamentales para la integridad de los datos en la base de datos de la CFE. Estos identificadores aseguran que cada registro esté vinculado de manera precisa al cliente correspondiente, evitando duplicados y errores en el consumo o los cargos. Los identificadores únicos subrayan la importancia de diseñar sistemas de datos que aseguren la integridad y precisión de la información. Esto permite un seguimiento individualizado y confiable, lo cual es esencial en sistemas de datos a gran escala y refuerza la confianza del usuario en la exactitud de la información proporcionada.

5. **La estructura de datos que permite un desglose detallado y estandarizado de datos**, como los costos (como el IVA, el DAP y los costos por nivel de consumo) asegura que el usuario comprenda el origen de cada cargo y confíe en la exactitud del recibo. Esta transparencia es posible gracias a una codificación de datos que integra cada elemento de costo de forma organizada y detallada. Nótese la necesidad de que cualquier sistema de digitalización de la realidad no solo represente fielmente la información, sino que también lo haga de manera transparente y comprensible. La estandarización de cálculos y desgloses permite una experiencia de usuario clara y refuerza la percepción de justicia y precisión en los cargos.

El análisis del recibo de luz como estudio de caso demuestra cómo el proceso de digitalización de la realidad facilita la administración de servicios esenciales mediante sistemas de información. La estructuración adecuada, el tratamiento específico de datos especiales, la transparencia en el desglose de datos vitales como los costos y el uso de identificadores únicos son prácticas clave en la creación de sistemas de datos efectivos. Estas conclusiones subrayan la importancia de la codificación de datos como medio para transformar fenómenos reales en información accesible y precisa, fomentando una relación de confianza entre los usuarios y los sistemas que gestionan estos datos.

## **5. Ejercicios de Aplicación**

### **5.1. Análisis Comparativo**

**Instrucciones**: Examine su propio recibo de luz o cualquier otro recibo de servicios (agua, gas, teléfono) e identifique:
   - ¿Qué campos adicionales o diferentes encuentra respecto al ejemplo estudiado?
   - ¿Cómo clasificaría estos campos según los tipos de datos estudiados?
   - ¿Qué ventajas o desventajas encuentra en la organización de los datos en ese recibo comparado con el caso analizado?

**Entregable**: Elabore una tabla comparativa que incluya al menos 5 campos diferentes, su clasificación por tipo de datos y una breve justificación de su importancia en el contexto del servicio.

### **5.2. Diseño de Base de Datos**

**Instrucciones**: Proponga un esquema simplificado de base de datos para una empresa minorista que necesita facturar productos a clientes, aplicando los principios de codificación vistos.

**Entregable**: Diseñe un diccionario de datos con al menos 15 campos que incluya:
   - Identificadores únicos para clientes y productos
   - Campos para el registro de ventas (fechas, cantidades, precios)
   - Campos para el cálculo de impuestos y descuentos
   - Campos para el seguimiento de pagos

Indique para cada campo: nombre de variable, tipo de dato, si es único o no, y descripción.

### **5.3. Caso Empresarial**

**Instrucciones**: Una empresa de servicios de streaming necesita estructurar datos de consumo de contenido por usuario para implementar un sistema de recomendaciones y facturación personalizada.

**Entregable**: Elabore un informe breve (máximo 2 páginas) que incluya:
   - Identificación de los datos clave que la empresa debe recopilar
   - Propuesta de estructura para almacenar estos datos
   - Explicación de cómo estos datos podrían utilizarse para generar recomendaciones personalizadas y optimizar planes de suscripción
   - Consideraciones éticas y de privacidad en la recopilación y uso de estos datos

**Nota**: Aplique los conceptos de codificación de datos, tipos de datos y organización de información estudiados en este caso.

---

[^1]: Profesor-investigador del Departamento de Economía de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Contacto: [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx), [Telegram](https://t.me/jzavalar).

Última actualización: 16 de junio de 2025
