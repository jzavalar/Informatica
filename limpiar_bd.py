# ==============================================================================
# limpiar_bd.py
# Versión 1.0
# Script de limpieza y normalización de datos para carga en base de datos relacional
# Caso de estudio: "Tortillería El Boleo"
# Autor: dr. Jesús Zavala Ruiz 
# Fecha: 3 de diciembre de 2025
# Propósito: Ilustra una técnica de transformación de datos crudos en un conjunto 
#            estandarizado, consistente y libre de errores, listo para su 
#            migración a un DBMS (ej. SQLite).
# ==============================================================================

import pandas as pd
import numpy as np
import re

# ------------------------------------------------------------------------------
# CARGA DE DATOS CRUDOS
# ------------------------------------------------------------------------------
# Se carga el archivo CSV original que contiene registros operativos con errores
# típicos de entrada manual: inconsistencias ortográficas, formatos variables,
# datos faltantes y duplicados lógicos.
# ------------------------------------------------------------------------------
df = pd.read_csv('basededatos.csv')


# ------------------------------------------------------------------------------
# FUNCIONES DE NORMALIZACIÓN
# Cada función aplica reglas de negocio específicas para garantizar consistencia
# y calidad en un campo determinado. Están diseñadas para ser reutilizables,
# atómicas y con manejo explícito de valores nulos.
# ------------------------------------------------------------------------------

def limpiar_texto(texto):
    """
    Normaliza texto genérico aplicando:
    1. Eliminación de espacios al inicio y final (strip)
    2. Conversión a minúsculas
    3. Eliminación de acentos mediante normalización Unicode (NFD + filtrado de marcas)
    4. Capitalización estilo título (cada palabra inicia en mayúscula)

    Esto garantiza que "juan pérez", "JUAN PÉREZ" y "Juan   PéRez" se conviertan
    en "Juan Pérez", facilitando la comparación y deduplicación.
    """
    if pd.isnull(texto):
        return ''
    texto = texto.strip().lower()
    
    # Eliminación de acentos usando el estándar Unicode
    import unicodedata
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'  # 'Mn' = Nonspacing_Mark (acentos)
    )
    
    # Capitalización por palabra (formato "Nombre Propio")
    texto = ' '.join(word.capitalize() for word in texto.split())
    return texto


def normalizar_nombre(nombre):
    """
    Normaliza nombres de clientes usando la función genérica de limpieza textual.
    No se aplica lógica adicional, ya que el estándar de "Nombre Propio" es suficiente.
    """
    return limpiar_texto(nombre)


def normalizar_colonia(colonia):
    """
    Normaliza nombres de colonias para permitir agrupaciones consistentes
    (ej.: "CENTRO", "centro", "Centro" → "Centro").
    """
    return limpiar_texto(colonia)


def normalizar_producto(producto):
    """
    Normaliza nombres de productos con reglas específicas de negocio:
    - Aplica limpieza textual genérica
    - Corrige variantes ortográficas comunes (ej.: "maiz" → "maíz")
    
    La corrección usa expresión regular con límites de palabra (\b) para evitar
    reemplazos parciales no deseados (ej.: en "panmaiz" no se aplicaría).
    """
    producto = limpiar_texto(producto)
    producto = re.sub(r'\bmaiz\b', 'maíz', producto)
    return producto


def limpiar_telefono(telefono):
    """
    Estandariza números telefónicos eliminando cualquier carácter no numérico.
    Convierte entradas como "(55) 1234-5678" o "55 1234 5678" en "5512345678".
    
    Esto permite usar el teléfono como identificador lógico único en contextos pequeños.
    """
    telefono = str(telefono)
    return re.sub(r'\D', '', telefono)  # \D = cualquier carácter no dígito


def asegurar_fecha(fecha):
    """
    Convierte cualquier formato de fecha reconocible por pandas en formato ISO:
    AAAA-MM-DD (estándar para bases de datos relacionales).
    
    Si la conversión falla (por datos inválidos), devuelve np.nan para su posterior
    eliminación en la etapa de validación.
    """
    try:
        return pd.to_datetime(fecha).strftime('%Y-%m-%d')
    except Exception:
        return np.nan


# ------------------------------------------------------------------------------
# APLICACIÓN DE REGLAS DE NORMALIZACIÓN
# Se transforman los campos uno por uno, aplicando la función adecuada según
# la semántica del dato y las reglas de negocio.
# ------------------------------------------------------------------------------

df['Cliente'] = df['Cliente'].apply(normalizar_nombre)
df['Telefono'] = df['Telefono'].apply(limpiar_telefono)
df['Colonia'] = df['Colonia'].apply(normalizar_colonia)
df['Producto'] = df['Producto'].apply(normalizar_producto)
df['Fecha'] = df['Fecha'].apply(asegurar_fecha)

# Conversión forzada a tipo numérico; errores se convierten en NaN
df['Cantidad'] = pd.to_numeric(df['Cantidad'], errors='coerce')
df['PrecioUnitario'] = pd.to_numeric(df['PrecioUnitario'], errors='coerce')


# ------------------------------------------------------------------------------
# VALIDACIÓN Y LIMPIEZA FINAL
# ------------------------------------------------------------------------------

# Elimina registros con campos críticos faltantes (calidad mínima requerida)
# Un registro sin fecha, cliente o producto no aporta valor analítico.
df.dropna(
    subset=[
        'Fecha', 'Cliente', 'Telefono', 'Colonia',
        'Producto', 'Cantidad', 'PrecioUnitario'
    ],
    inplace=True
)

# Elimina duplicados lógicos: si todos los campos coinciden tras la normalización,
# se considera el mismo registro.
df.drop_duplicates(
    subset=[
        'Fecha', 'Cliente', 'Telefono', 'Colonia',
        'Producto', 'Cantidad', 'PrecioUnitario'
    ],
    inplace=True
)


# ------------------------------------------------------------------------------
# EXPORTACIÓN DEL CONJUNTO DE DATOS LIMPIO
# ------------------------------------------------------------------------------
# El archivo resultante está listo para:
# - Carga en un DBMS relacional (SQLite, MySQL, etc.)
# - Análisis descriptivo
# - Generación de indicadores gerenciales
# ------------------------------------------------------------------------------
df.to_csv('basededatos_limpia.csv', index=False)

print("Limpieza y normalización completadas. Archivo guardado como 'basededatos_limpia.csv'.")
