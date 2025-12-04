# **Documento técnico: Script de limpieza y normalización de datos**  
**Proyecto:** Sistema de información para “Tortillería El Boleo”  
**Versión:** 1.0  
**Fecha:** 4 de diciembre de 2025  
**Autor:** dr. Jesús Zavala Ruiz
**Ayudante:** [deepai.org](deepai.org)

---

## 1. Objetivo

El script [`limpiar_bd.py`](limpiar_bd.py)` automatiza la **limpieza, estandarización y validación** de un conjunto de datos operativos provenientes de fuentes no estructuradas (por ejemplo, registros manuales en hojas de cálculo). Su propósito es preparar los datos para su carga en un **sistema gestor de bases de datos relacional (DBMS)**, garantizando consistencia, unicidad y calidad mínima para la generación de informes gerenciales.

---

## 2. Contexto del dataset

El archivo de entrada (`basededatos.csv`) contiene registros de ventas diarias con los siguientes campos:

- `Fecha`: fecha de la transacción  
- `Cliente`: nombre del cliente (con inconsistencias en mayúsculas, acentos y espacios)  
- `Telefono`: número telefónico (con o sin guiones, espacios o paréntesis)  
- `Colonia`: ubicación del cliente  
- `Producto`: tipo de producto vendido  
- `Cantidad`: número de unidades  
- `PrecioUnitario`: precio por unidad  

Los datos presentan **inconsistencias típicas en entornos administrativos no automatizados**, tales como:
- Variantes ortográficas (“maiz” vs. “maíz”)
- Mayúsculas/minúsculas arbitrarias (“CENTRO”, “centro”, “Centro”)
- Teléfonos con formato no estándar (“55 1234-5678”)
- Fechas en formatos no homogéneos

---

## 3. Metodología de limpieza

El proceso sigue los principios de **calidad de datos**:
- **Validez**: los datos cumplen con reglas de formato esperado  
- **Consistencia**: el mismo concepto se representa de forma uniforme  
- **Completitud**: se eliminan registros con campos críticos faltantes  
- **Unicidad**: se eliminan duplicados lógicos

### 3.1. Normalización textual

Se aplica una función genérica `limpiar_texto()` que:

1. Convierte el texto a minúsculas  
2. Elimina acentos mediante normalización Unicode (NFD + filtrado de marcas diacríticas)  
3. Crea nombres propios con mayúscula en la primera letra de cada palabra (formato “Nombre Propio”)  
4. Elimina espacios al inicio y al final

Esta función es reutilizada en los campos: `Cliente`, `Colonia` y `Producto`.

### 3.2. Normalización específica por campo

| Campo | Transformación adicional |
|------|--------------------------|
| **Producto** | Reemplazo de “maiz” → “maíz” mediante expresión regular |
| **Teléfono** | Eliminación de todos los caracteres no numéricos (`\D`) |
| **Fecha** | Conversión a formato ISO (`YYYY-MM-DD`) con manejo de errores |
| **Cantidad / PrecioUnitario** | Conversión a tipo numérico; valores inválidos → `NaN` |

### 3.3. Validación y deduplicación

- Se eliminan filas con valores nulos en **cualquier campo crítico**  
- Se eliminan **duplicados exactos** considerando todas las columnas, lo que evita registros redundantes tras la normalización

---

## 4. Dependencias

El script requiere las siguientes bibliotecas de Python:

- `pandas` ≥ 1.3  
- `numpy`  
- `re` (módulo estándar)  
- `unicodedata` (módulo estándar)

Ejecución recomendada en entornos como **Google Colab**, **Jupyter Notebook** o cualquier intérprete de Python 3.8+, como RStudio.

---

## 5. Resultado esperado

El script genera un archivo de salida:  
**`basededatos_limpia.csv`**

Características del archivo limpio:

- Todo texto en formato **Nombre Propio** (ej.: “María López”, “Tortilla De Maíz”)  
- Teléfonos como cadenas numéricas de 10 dígitos (ej.: “5551234567”)  
- Fechas en formato **ISO 8601** (`2025-03-01`)  
- Productos estandarizados (“maiz” corregido a “maíz”)  
- Sin filas duplicadas ni con datos faltantes en campos esenciales

Este archivo está listo para:
- Carga en un DBMS relacional (ej.: SQLite, MySQL)  
- Análisis descriptivo  
- Generación de indicadores gerenciales

---

## 6. Uso del script (instrucciones)

1. Guardar el script como `limpiar_datos.py`  
2. Colocar el archivo `basededatos.csv` en el mismo directorio  
3. Ejecutar en terminal o notebook:  
   ```bash
   python limpiar_datos.py
   ```
4. Verificar la creación de `basededatos_limpia.csv`

> **Nota**: En Google Colab, reemplazar `pd.read_csv('basededatos.csv')` por la carga desde el explorador de archivos o desde una URL.

---

## 7. Consideraciones para producción

- Para datasets grandes (>100k filas), considerar particionamiento o procesamiento en lotes.  
- Si el precio unitario varía en el tiempo, se recomienda registrar el precio **en el momento de la venta** (actualmente se asume fijo por producto).  
- Para entornos multilingües, se debe revisar la estrategia de eliminación de acentos.

---

## 8. Licencia

Este script se distribuye con fines educativos y de demostración. Puede adaptarse libremente bajo los principios de **transparencia y reproducibilidad en la gestión de datos**.

--- 

**Fin del documento**.
