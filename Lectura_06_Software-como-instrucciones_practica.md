## ⚡ Práctica Express. El Software como instrucciones: Las 4 Operaciones ESAP en 30 Minutos

### 🎯 Objetivo
Experimentar de primera mano la diferencia entre **compilación** e **interpretación** creando una **Calculadora de Descuentos** en C y Python.

**⏱️ Duración:** 30 minutos  
**🌐 Plataforma:** RStudio.cloud  
**👥 Nivel:** Principiante absoluto  

---

### 🚀 Preparación Rápida (5 minutos)

#### Paso 1: Acceso a RStudio.cloud
1. Ve a [https://rstudio.cloud](https://posit.cloud/plans/free) en una nueva pestaña de tu navegador
2. Inicia sesión o crea cuenta con tu cuenta de Gmail. Accede a tu cuenta de Gmail, confirma y accede.
3. Crea nuevo proyecto `New Project --> New RStudio Project`con el nombre **"ESAP-Express"** (Cambia `Untitled Project` por `ESAP-Express`)  

#### Paso 2: Configurar Terminal
En la **Terminal** de RStudio.cloud copia o escribe cada línea, una a la vez:

```bash
## Crear directorio del proyecto
mkdir esap-express
cd esap-express

## Verificar compilador C
gcc --version
```
Observa la salida y comprueba la existencia del programa compilador `gcc`.

### 💼 El Proyecto: Calculadora de Descuentos

**Escenario real:** Eres gerente de una tienda y necesitas calcular rápidamente el precio final de productos con descuento.

**Las 4 operaciones ESAP:**
- 📥 **E**NTRADA: Precio original y porcentaje de descuento
- ⚙️ **P**ROCESAMIENTO: Calcular precio final
- 💾 **A**LMACENAMIENTO: Guardar cálculo en archivo
- 📊 **S**ALIDA: Mostrar resultado al usuario

### 🔧 Parte 1: Programa en C - Compilado (10 minutos)

#### Paso 3: Crear calculadora.c
Ve al panel inferior derecho y escoge `Files --> Blanck File --> Text File` escribe `calculadora.c` como nombre del archivo. Copia el siguiente texto en el archivo y pega el texto con `Ctrl + v`.
```c
#include <stdio.h>

int main() {
    // ========================================
    // 📥 ENTRADA: Recibir datos
    // ========================================
    printf("🛒 CALCULADORA DE DESCUENTOS\n");
    printf("============================\n");
    
    float precio_original, descuento_porcentaje;
    
    printf("💰 Precio original: $");
    scanf("%f", &precio_original);
    
    printf("🏷️  Descuento (%%): ");
    scanf("%f", &descuento_porcentaje);
    
    // ========================================
    // ⚙️ PROCESAMIENTO: Calcular descuento
    // ========================================
    float descuento_dinero = precio_original * (descuento_porcentaje / 100);
    float precio_final = precio_original - descuento_dinero;
    
    // ========================================
    // 💾 ALMACENAMIENTO: Guardar en archivo
    // ========================================
    FILE *archivo = fopen("calculo_c.txt", "w");
    fprintf(archivo, "CÁLCULO DE DESCUENTO - PROGRAMA C\n");
    fprintf(archivo, "Precio original: $%.2f\n", precio_original);
    fprintf(archivo, "Descuento: %.1f%% ($%.2f)\n", descuento_porcentaje, descuento_dinero);
    fprintf(archivo, "Precio final: $%.2f\n", precio_final);
    fclose(archivo);
    
    // ========================================
    // 📊 SALIDA: Mostrar resultado
    // ========================================
    printf("\n📊 RESULTADO:\n");
    printf("💵 Precio original: $%.2f\n", precio_original);
    printf("🏷️  Descuento: %.1f%% ($%.2f)\n", descuento_porcentaje, descuento_dinero);
    printf("✅ Precio final: $%.2f\n", precio_final);
    printf("💾 Guardado en: calculo_c.txt\n");
    
    return 0;
}
```

#### Paso 4: Compilar y ejecutar
Copia o escribe cada línea en la Terminal a la derecha de `$`: 
```bash
## 🔨 COMPILACIÓN (crear ejecutable)
echo "🔨 Compilando programa C..."
gcc -o calculadora calculadora.c
```

```bash
## Verificar que se creó el ejecutable
ls -la calculadora
```

```bash
## 🚀 EJECUCIÓN del programa compilado
echo "🚀 Ejecutando programa compilado..."
./calculadora
```

**📝 Datos de prueba:**
- Precio: `100`
- Descuento: `15`

---

### 🐍 Parte 2: Programa en Python - Interpretado (10 minutos)

#### Paso 5: Crear calculadora.py

```python
#!/usr/bin/env python3

def main():
    ## ========================================
    ## 📥 ENTRADA: Recibir datos
    ## ========================================
    print("🛒 CALCULADORA DE DESCUENTOS")
    print("🐍 Versión Python (Interpretado)")
    print("============================")
    
    try:
        precio_original = float(input("💰 Precio original: $"))
        descuento_porcentaje = float(input("🏷️  Descuento (%): "))
        
        ## ========================================
        ## ⚙️ PROCESAMIENTO: Calcular descuento
        ## ========================================
        descuento_dinero = precio_original * (descuento_porcentaje / 100)
        precio_final = precio_original - descuento_dinero
        ahorro_texto = f"¡Ahorras ${descuento_dinero:.2f}!"
        
        ## ========================================
        ## 💾 ALMACENAMIENTO: Guardar en archivo
        ## ========================================
        with open("calculo_python.txt", "w") as archivo:
            archivo.write("CÁLCULO DE DESCUENTO - PROGRAMA PYTHON\n")
            archivo.write(f"Precio original: ${precio_original:.2f}\n")
            archivo.write(f"Descuento: {descuento_porcentaje:.1f}% (${descuento_dinero:.2f})\n")
            archivo.write(f"Precio final: ${precio_final:.2f}\n")
            archivo.write(f"Ahorro: ${descuento_dinero:.2f}\n")
        
        ## ========================================
        ## 📊 SALIDA: Mostrar resultado
        ## ========================================
        print(f"\n📊 RESULTADO:")
        print(f"💵 Precio original: ${precio_original:.2f}")
        print(f"🏷️  Descuento: {descuento_porcentaje:.1f}% (${descuento_dinero:.2f})")
        print(f"✅ Precio final: ${precio_final:.2f}")
        print(f"🎉 {ahorro_texto}")
        print(f"💾 Guardado en: calculo_python.txt")
        
        ## Bonus: Recomendación automática
        if descuento_porcentaje >= 20:
            print("🔥 ¡Excelente descuento! Aprovecha la oferta.")
        elif descuento_porcentaje >= 10:
            print("👍 Buen descuento para considerar.")
        else:
            print("💡 Descuento moderado.")
            
    except ValueError:
        print("❌ Error: Ingresa solo números válidos")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
```

#### Paso 6: Ejecutar Python

```bash
## 🐍 INTERPRETACIÓN (sin compilar, directo)
echo "🐍 Ejecutando Python (sin compilar)..."
python3 calculadora.py
```

**📝 Usa los mismos datos para comparar.**

---

### 🔍 Parte 3: Comparación Inmediata (5 minutos)

#### Paso 7: Analizar diferencias

```bash
## Ver archivos generados
echo "📄 Archivos generados:"
ls -la *.txt

## Comparar contenido
echo -e "\n📊 RESULTADO C:"
cat calculo_c.txt

echo -e "\n📊 RESULTADO PYTHON:"
cat calculo_python.txt

## Mostrar diferencias clave
echo -e "\n🔍 DIFERENCIAS OBSERVADAS:"
echo "✅ C: Compilación requerida, ejecución inmediata después"
echo "✅ Python: Sin compilación, interpretación línea por línea"
echo "✅ Ambos: Misma funcionalidad, diferente proceso"
```

#### Paso 8: Experimento de velocidad

```bash
## Mostrar tiempo de preparación vs ejecución
echo -e "\n⏱️ EXPERIMENTO DE TIEMPO:"

echo "🔨 C - Tiempo de compilación:"
time gcc -o calculadora_test calculadora.c

echo -e "\n🚀 C - Tiempo de ejecución (ya compilado):"
echo "100\n15" | time ./calculadora_test

echo -e "\n🐍 Python - Tiempo total (interpretación + ejecución):"
echo "100\n15" | time python3 calculadora.py
```

---

### 📋 Reflexión Express (5 minutos)

#### Paso 9: Completar tabla comparativa

```bash
## Crear reporte final
cat > reporte_comparativo.txt << 'EOF'
🔍 COMPARACIÓN: COMPILADO vs INTERPRETADO
==========================================

PROGRAMA EN C (COMPILADO):
✅ Ventajas:
   - Ejecución muy rápida
   - Un solo archivo ejecutable
   - No requiere software adicional para ejecutar

❌ Desventajas:
   - Requiere compilación antes de ejecutar
   - Cambios requieren recompilar
   - Sintaxis más compleja

PROGRAMA EN PYTHON (INTERPRETADO):
✅ Ventajas:
   - Ejecución inmediata (sin compilar)
   - Fácil modificación y prueba
   - Sintaxis más simple y legible
   - Mejor manejo de errores

❌ Desventajas:
   - Ejecución más lenta
   - Requiere Python instalado
   - Errores aparecen durante ejecución

CONCLUSIÓN:
- C: Ideal para software de producción que requiere velocidad
- Python: Ideal para desarrollo rápido, automatización, análisis

APLICACIÓN EN ADMINISTRACIÓN:
- C: Sistemas de punto de venta, software empresarial crítico
- Python: Análisis de datos, reportes automáticos, herramientas de gestión
EOF

echo "📄 Reporte creado: reporte_comparativo.txt"
cat reporte_comparativo.txt
```

---

### 🎯 Verificación de Aprendizaje

#### ✅ Checklist de 30 segundos:

**Responde mentalmente:**

1. **¿Cuáles son las 4 operaciones ESAP?**
   - Entrada, Procesamiento, Almacenamiento, Salida

2. **¿Cuál es la diferencia principal entre C y Python?**
   - C se compila antes de ejecutar, Python se interpreta línea por línea

3. **¿Cuándo usarías cada uno?**
   - C: Para velocidad máxima
   - Python: Para desarrollo rápido y flexibilidad

4. **¿Identificaste las 4 operaciones en ambos programas?**
   - ✅ Entrada: scanf() / input()
   - ✅ Procesamiento: cálculos matemáticos
   - ✅ Almacenamiento: archivos .txt
   - ✅ Salida: printf() / print()

---

### 🏆 Desafío Bonus (Opcional)

**Si tienes 5 minutos extra:**

Modifica el programa Python para calcular descuentos de múltiples productos:

```python
## Agregar al final de calculadora.py:
print("\n🔄 ¿Calcular otro producto? (s/n):")
if input().lower() == 's':
    main()  ## Ejecutar de nuevo
```

---

### 🎉 ¡Felicidades!

**En solo 30 minutos has:**

✅ Experimentado la **compilación** (C) vs **interpretación** (Python)  
✅ Identificado las **4 operaciones ESAP** en programas reales  
✅ Creado una herramienta útil para administración  
✅ Comparado ventajas y desventajas de cada enfoque  
✅ Generado archivos de resultado comparables  

**🔑 Concepto clave aprendido:** 
> El software son instrucciones que transforman datos de entrada en información útil de salida, pasando por procesamiento y almacenamiento.

**🚀 Próximo paso:** 
Aplica estos conceptos creando herramientas similares para tu área de interés (finanzas, marketing, recursos humanos).

---

### 📱 Para llevar

**Guarda estos comandos básicos:**

```bash
## Compilar C:
gcc -o programa programa.c

## Ejecutar C:
./programa

## Ejecutar Python:
python3 programa.py

## Ver archivos generados:
ls -la *.txt
```

**¡Ya eres oficialmente capaz de distinguir entre código compilado e interpretado! 🎓**
