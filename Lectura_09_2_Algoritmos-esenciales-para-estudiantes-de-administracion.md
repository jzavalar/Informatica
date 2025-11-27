# Algoritmos Esenciales para Estudiantes de Administración
# (Explicados como si tuvieras 15 años)

---

## 1. **Algoritmo del Punto de Equilibrio**
**El problema que resuelve:** ¿Cuánto tengo que vender para no perder plata?

**Ejemplo práctico:** Quieres vender polos personalizados. Cada polo te cuesta \$30, lo venderás en \$50 y tus gastos fijos (alquiler, internet) son \$2,000 al mes.

**Pasos (cómo calcularlo):**
1. **Identifica tus costos fijos:** Suma todo lo que pagas igual sin vender nada (\$2,000)
2. **Calcula la ganancia por unidad:** Precio de venta - Costo variable (\$50 - \$30 = \$20)
3. **Aplica la fórmula:** Punto de equilibrio = Costos fijos ÷ Ganancia por unidad
4. **Resultado:** 2,000 ÷ 20 = **100 polos**

**Para que te sirva:** Sabrás exactamente cuándo empiezas a ganar plata real. Si vendes 99 polos, pierdes. Si vendes 101, ganas \$20.

---

## 2. **Método de Evaluación de Proyectos (VAN)**
**El problema que resuelve:** ¿Vale la pena invertir plata en esto o mejor la dejo en el banco?

**Ejemplo práctico:** Un local te pide \$50,000 de inversión y te promete: \$15,000 en año 1, \$20,000 en año 2 y \$25,000 en año 3. El banco te da 10% anual.

**Pasos (cómo calcularlo):**
1. **Dibuja una línea de tiempo:** Año 0 (ahora): -\$50,000. Año 1: +\$15,000. Año 2: +\$20,000. Año 3: +\$25,000
2. **Descuenta cada flujo:** Cada pago futuro se divide por (1+10%) elevado al año que falta
   - Año 1: 15,000 ÷ 1.10 = \$13,636
   - Año 2: 20,000 ÷ 1.21 = \$16,529
   - Año 3: 25,000 ÷ 1.33 = \$18,783
3. **Suma todo:** -50,000 + 13,636 + 16,529 + 18,783 = **-\$1,052**

**Para que te sirva:** Si el VAN es positivo, inviertes. Si es negativo (como aquí), mejor dejas la plata en el banco. Es tu "filtro de tonterías" para inversiones.

---

## 3. **Algoritmo de Asignación Óptima (Método Húngaro)**
**El problema que resuelve:** ¿Cómo asignar tareas a personas para terminar rápido y barato?

**Ejemplo práctico:** Tienes 3 vendedores y 3 zonas. Cada vendedor tarda diferente tiempo en cada zona (horas):

| Vendedor | Zona A | Zona B | Zona C |
|----------|--------|--------|--------|
| Juan     | 5h     | 7h     | 4h     |
| María    | 6h     | 3h     | 5h     |
| Carlos   | 3h     | 4h     | 6h     |

**Pasos (cómo resolverlo):**
1. **Resta el mínimo de cada fila:** A cada fila, réstale su número más pequeño
2. **Resta el mínimo de cada columna:** Ahora haz lo mismo por columnas
3. **Tacha ceros con mínimas líneas:** Si necesitas 3 líneas (igual al número de tareas), ya tienes la solución óptima
4. **Asigna donde estén los ceros:** Juan→Zona C (4h), María→Zona B (3h), Carlos→Zona A (3h)

**Para que te sirva:** Minimizas tiempo, costos o esfuerzo en cualquier asignación: reparto de equipos, rutas de delivery, turnos de trabajo.

---

## 4. **Algoritmo de la Ruta Crítica (CPM)**
**El problema que resuelve:** ¿Qué tareas no puedo retrasar ni un día para no atrasar todo el proyecto?

**Ejemplo práctico:** Lanzarás un producto en 6 meses con estas tareas: Diseño (2 meses), Producción (3 meses), Marketing (2 meses), y Logística (1 mes). Marketing necesita que termine Diseño. Producción también. Logística necesita Producción.

**Pasos (cómo calcularlo):**
1. **Dibuja flechas:** Cada tarea es una flecha entre círculos (inicio y fin)
2. **Calcula el camino más largo:** 
   - Camino 1: Diseño→Marketing = 2+2 = 4 meses
   - Camino 2: Diseño→Producción→Logística = 2+3+1 = **6 meses** ← ¡ESTE ES EL CRÍTICO!
3. **Identifica holgura:** Marketing tiene 2 meses de "holgura" (puede retrasarse sin afectar el final)

**Para que te sirva:** Sabrás exactamente en qué enfocar tu atención. Si se atrasa la Producción, tu proyecto entero se atrasa. Si se atrasa Marketing, no pasa nada (en este caso).

---

## 5. **Algoritmo de Mínimos Cuadrados (Tendencias)**
**El problema que resuelve:** ¿Cómo predecir mis ventas del próximo mes con datos pasados?

**Ejemplo práctico:** Tus ventas de los últimos 4 meses: Enero: 100 unidades, Febrero: 120, Marzo: 140, Abril: 130.

**Pasos (cómo calcularlo):**
1. **Dale número a cada mes:** Enero=1, Febrero=2, Marzo=3, Abril=4
2. **Usa la fórmula de Excel:** `=ESTIMACION.LINEAL(ventas; números de mes)`
3. **O hazlo manual (básico):** Traza una línea que pase "por el centro" de tus puntos
4. **Resultado:** La tendencia es creciente ~+8.5 unidade\$mes. Para mayo (mes 5): **~148 unidades**

**Para que te sirva:** Puedes predecir ventas, gastos, necesidad de empleados. Es tu "bola de cristal" matemática para no tomar decisiones a ciegas.

---

## 6. **Regla de Pareto 80/20 (Algoritmo de Clasificación)**
**El problema que resuelve:** ¿Qué pocos clientes me dan la mayoría de la plata?

**Ejemplo práctico:** Tienes 100 clientes que te generaron \$50,000 este año.

**Pasos (cómo aplicarlo):**
1. **Ordena clientes de mayor a menor venta:** Cliente A: \$8,000, Cliente B: \$6,000, etc.
2. **Calcula el acumulado:** Top 1 cliente: 8,000 (16%). Top 2: 14,000 (28%). Top 3: 18,000 (36%)...
3. **Encuentra el punto 80%:** Te darás cuenta que **~20 clientes** (20% de 100) generan ~\$40,000 (80% de 50,000)

**Para que te sirva:** Enfócate en esos 20 clientes clave. No desperdicies energía igual en todos. Es la regla más poderosa de administración: **20% de las causas dan 80% de los resultados**.

---

## 7. **Algoritmo de Lote Económico (EOQ)**
**El problema que resuelve:** ¿Cuánto comprar de cada producto para no quedarme sin stock ni gastar de más en bodega?

**Ejemplo práctico:** Vendes 1,200 laptop\$año. Cada pedido a fábrica te cuesta \$50 (flete). Guardar una laptop te cuesta \$10/año (seguro, espacio).

**Pasos (cómo calcularlo):**
1. **Identifica:**
   - Demanda (D) = 1,200 unidade\$año
   - Costo de orden (S) = \$50
   - Costo de mantener (H) = \$10 por unidad/año
2. **Aplica la fórmula:** EOQ = √(2 × D × S ÷ H)
3. **Cálculo:** √(2 × 1,200 × 50 ÷ 10) = √12,000 = **110 laptops por pedido**
4. **Frecuencia:** 1,200 ÷ 110 = 11 pedido\$año ≈ cada 33 días

**Para que te sirva:** No compras de más (ahorras bodega) ni de menos (no pierdes ventas). Es el balance perfecto para inventarios.

---

## 8. **Algoritmo de Decisión con Árbol de Decisión**
**El problema que resuelve:** ¿Qué decisión tomar cuando hay probabilidades de que pasen cosas buenas o malas?

**Ejemplo práctico:** ¿Lanzas un producto nuevo? Si el mercado es bueno (40% de probabilidad), ganas \$100,000. Si es malo (60%), pierdes \$30,000.

**Pasos (cómo calcularlo):**
1. **Dibuja el árbol:** Un cuadrado (tu decisión) con líneas a dos círculos (resultados posibles)
2. **Asigna probabilidades y resultados:** Bueno (0.4 × +100,000 = +40,000). Malo (0.6 × -30,000 = -18,000)
3. **Calcula valor esperado:** 40,000 + (-18,000) = **+\$22,000**
4. **Decide:** Si el resultado es positivo, adelante. Si negativo, no lo hagas.

**Para que te sirva:** Toma decisiones con datos, no con miedos. Evalúa inversiones, contrataciones, expansiones con lógica en lugar de intuición.

---

## 9. **Algoritmo de Programación Lineal (Simplex simplificado)**
**El problema que resuelve:** ¿Cómo maximizar ganancias sin pasarme de recursos limitados?

**Ejemplo práctico:** Haces mesas y sillas. Mesas dan \$100 de ganancia, sillas \$60. Una mesa usa 5 horas de madera, una silla 2 horas. Tienes 40 horas de madera disponibles.

**Pasos (cómo calcularlo):**
1. **Define variables:** X = mesas, Y = sillas
2. **Función objetivo:** Maximizar 100X + 60Y
3. **Restricciones:** 5X + 2Y ≤ 40 (madera), X ≥ 0, Y ≥ 0
4. **Encuentra puntos extremos:** 
   - Si haces solo mesas: X=8, ganancia=\$800
   - Si haces solo sillas: Y=20, ganancia=\$1,200
   - Mezcla: X=4, Y=10, ganancia=\$1,000
5. **Solución óptima:** **20 sillas** te dan más ganancia.

**Para que te sirva:** En cualquier problema de "qué tanto producir con recursos limitados" (tiempo, dinero, materiales).

---

## 10. **Algoritmo de Análisis de Sensibilidad**
**El problema que resuelve:** ¿Qué tanto puede cambiar una situación antes de que mi decisión sea mala?

**Ejemplo práctico:** Vas a comprar máquinas que cuestan \$10,000 si vendes más de 500 unidade\$mes, pero \$7,000 si vendes menos. ¿Qué pasa si tus pronósticos fallan?

**Pasos (cómo calcularlo):**
1. **Define escenarios base:** Optimista (700 unidades), Realista (500 unidades), Pesimista (300 unidades)
2. **Calcula para cada escenario:** 
   - Optimista: Mejor máquina cara (más capacidad)
   - Pesimista: Mejor máquina barata (menos pérdida)
3. **Encuentra el "punto de quiebre":** ¿A partir de qué ventas es mejor la máquina cara?
4. **Resultado:** Si vendes >480 unidades, la cara es mejor. Si tu pronóstico es 500 pero puede bajar a 450, **es arriesgado**.

**Para que te sirva:** Prepara plan B, C y D. No te sorprendan los cambios. Es tu "escudo contra la incertidumbre".

---

## **Resumen de Uso Rápido**

| Situación | Algoritmo a usar | Te responde |
|-----------|------------------|-------------|
| ¿Cuánto vender? | Punto de Equilibrio | La cifra mínima |
| ¿Invierto plata? | VAN | Sí/No con números |
| Asignar tareas | Método Húngaro | La mejor combinación |
| Planificar proyecto | Ruta Crítica | Qué no puedes retrasar |
| Predecir futuro | Mínimos Cuadrados | Tendencia clara |
| Priorizar clientes | Regla 80/20 | Dónde enfocarte |
| Comprar inventario | EOQ | Cuándo y cuánto |
| Decisiones inciertas | Árbol de Decisión | Valor esperado |
| Max ganancias | Programación Lineal | Producción óptima |
| Riesgo de fallar | Análisis de Sensibilidad | Qué tan seguro estás |

**Consejo final:** No memorices fórmulas. Usa Excel, Google Sheets o apps. Lo importante es **saber qué algoritmo usar para qué problema**. Esa es la verdadera habilidad de administración.
