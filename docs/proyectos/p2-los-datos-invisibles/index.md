# P2 · Los datos invisibles

**Sesiones 8 a 12 · del 19 de octubre al 4 de noviembre de 2026**
**Cubre:** Unidades 2 y 3 del contenido sintético (Sistemas de información · Manipulación de datos numéricos)
**Destino:** `docs/proyectos/p2-los-datos-invisibles/`

---

## El reto

> Su equipo elige una organización real y pequeña a la que tenga acceso: la cafetería de la unidad, la papelería de la esquina, el negocio familiar de alguno de ustedes, una asociación estudiantil, el taller del tío.
>
> Ahí opera un sistema de información. **Nadie lo llama así, no tiene computadoras, y funciona.** Está hecho de un cuaderno, la memoria de la dueña, un grupo de WhatsApp y una caja de recibos.
>
> Su trabajo es descubrirlo y documentarlo: qué datos se capturan, dónde viven, qué decisiones dependen de ellos, y —lo más importante— **qué información se está perdiendo**.

**Regla de alcance:** el trabajo de campo es **una salida, no cinco**. Un equipo que necesita cinco visitas eligió mal el caso. Delimitar el alcance de un proyecto es en sí una competencia administrativa.

**Casos de respaldo** para equipos sin acceso: la propia coordinación de la licenciatura, la biblioteca de la unidad, un puesto del mercado cercano. El profesor tiene tres casos documentados disponibles en `archivo/estudios-de-caso/` si un equipo se queda sin opciones.

---

## Sesión 8 · Fase activista (lunes 19 de octubre)

### En el aula (0:00–0:50)

Sin teoría previa sobre sistemas de información. Cada equipo diseña, en papel, **la lista de preguntas que le va a hacer a su organización**. El profesor solo pone una restricción: máximo doce preguntas, y ninguna puede contestarse con sí o no.

Puesta en común rápida: los equipos intercambian listas y se marcan preguntas mutuamente inútiles. Esto ya enseña algo sobre levantamiento de requerimientos, sin haberlo nombrado.

### Trabajo de campo (fuera del aula, antes de la sesión 9)

La salida. Cada equipo debe traer:

1. Las doce respuestas.
2. **Fotografía de un artefacto real donde vivan datos**: la página del cuaderno, el pizarrón de pedidos, la libreta de fiados, la pantalla del punto de venta.
3. El registro de **una decisión concreta** que la organización tomó esta semana y de los datos que usó para tomarla.
4. Una lista de cosas que la dueña **sabe pero no está escrito en ninguna parte**.

### Entregable

Evidencia de campo en el cuaderno. **Sin IA.**

---

## Sesión 9 · Fase reflexiva (miércoles 21 de octubre)

### Comparación entre equipos (0:00–0:50)

Cinco organizaciones distintas en el pizarrón, mismas columnas: qué datos capturan, dónde viven, qué decisiones sostienen, qué se pierde.

**El hallazgo que va a emerger solo:** las cinco organizaciones pierden el mismo tipo de información. Casi siempre es histórico —nadie guarda lo que pasó el mes pasado— y casi siempre es lo que haría posible anticipar en vez de reaccionar. Cuando el grupo lo descubre por comparación en lugar de escucharlo del profesor, no se olvida.

### Análisis (0:50–1:40)

Cada equipo responde por escrito:

1. Dibujen el flujo de un dato desde que nace hasta que muere en su organización. ¿Dónde se copia? ¿Dónde se pierde?
2. Identifiquen **una decisión que se toma con información insuficiente** y digan qué dato faltaba.
3. ¿Qué sabe la persona a cargo que, si se fuera mañana, se iría con ella?

### Cierre (1:40–2:00)

Vocabulario mínimo, solo nombres: dato, información, proceso, transacción, y los cuatro tipos de sistema. Sin desarrollo. La teoría es la sesión siguiente.

### Entregable

Diagrama de flujo del dato, a mano, más las tres respuestas. **Sin IA.**

---

## Sesión 10 · Fase teórica (lunes 26 de octubre)

**Lecturas previas:** `06-software-datos-e-instrucciones.md`, `08-pseudocodigo.md`, `09-algoritmos-para-administracion.md`

| Minutos | Fase | Actividad |
|---|---|---|
| 0–20 | Activista | Por parejas: escribir en el pizarrón, en lenguaje natural, los pasos exactos para calcular el cambio de una compra. Descubrir cuántos pasos faltan |
| 20–45 | Reflexivo | Retomar los flujos de la sesión 9 y clasificar cada organización según la tipología: ¿qué tipo de sistema es el cuaderno de la papelería? |
| 45–85 | Teórico | Exposición dialogada: dato/información, tipología TPS-MIS-DSS-ERP, estructura de un algoritmo, pseudocódigo como lenguaje intermedio |
| 85–120 | Pragmático | Cada equipo empieza a escribir en pseudocódigo la decisión que identificó en su organización |

### Bitácora de IA

Tres consultas mínimas sobre la lectura, con verificación. **Caza del error de P2:** dale al chatbot un cálculo administrativo con un caso frontera —un descuento aplicado sobre un total negativo, un inventario que llega a cero, una división entre cero disfrazada— y verifica a mano. Documenta el error y **explica qué tipo de pregunta lo produce**.

---

## Sesión 11 · Fase teórica → pragmática (miércoles 28 de octubre)

### Laboratorio simulado (0:00–1:20)

**El chatbot como computadora que ejecuta el pseudocódigo del equipo.** Orden inviolable:

1. **En papel:** el algoritmo terminado en pseudocódigo.
2. **En papel:** la prueba de escritorio con tres casos, uno de ellos con datos inválidos. Se anotan los valores esperados de cada variable en cada paso.
3. **Simulación:** se le pide al chatbot que ejecute, no que corrija.

   > *Actúa como una computadora que ejecuta este pseudocódigo paso a paso. Muéstrame el valor de cada variable después de cada instrucción. No corrijas el código, no lo mejores y no me expliques nada: solo ejecútalo tal como está con estos datos de entrada.*

4. **Comparación.** Si el resultado difiere de la prueba de escritorio, averiguar quién se equivocó. Casi siempre es el algoritmo, y descubrirlo así es la lección.

**Advertencia para el verificador del equipo:** el chatbot tiende a arreglar el código silenciosamente y ejecutar la versión arreglada. Si el resultado sale perfecto a la primera con un algoritmo que tenía un error obvio, eso ocurrió. Detectarlo es parte del trabajo.

### Construcción del entregable (1:20–2:00)

---

> **Lunes 2 de noviembre: descanso obligatorio, sin clase.** El puente se usa para terminar el entregable y estudiar para el examen 2. Ojo con la deserción posterior al puente: el protocolo de ausencia de 48 horas se activa a la primera falta del miércoles 4.

---

## Sesión 12 · Fase pragmática (miércoles 4 de noviembre)

| Minutos | Qué |
|---|---|
| 0–30 | Entrega del diccionario de datos. Presentación de 5 minutos por equipo |
| 30–110 | **Examen escrito 2**, individual, en papel, sin dispositivos |
| 110–120 | Cierre y arranque de P3 |

---

## El entregable

**Expediente del sistema de información**, con siete componentes:

| # | Componente | Rol que lidera |
|---|---|---|
| 1 | Ficha de la organización y evidencia de campo (fotografías del artefacto de datos) | Explorador |
| 2 | Mapa del proceso administrativo, a mano | Cronista |
| 3 | **Diccionario de datos**: cada dato con nombre, tipo, origen, quién lo usa, con qué frecuencia (**insumo obligatorio de P3**) | Arquitecto |
| 4 | Clasificación del sistema según la tipología, **con justificación basada en evidencia de campo** | Arquitecto |
| 5 | Algoritmo en pseudocódigo de una decisión real del negocio, con diagrama de flujo | Integrador |
| 6 | Prueba de escritorio con tres casos, uno con datos inválidos, y contraste con la simulación | Integrador |
| 7 | Bitácora de IA con la caza del error | Verificador |

Más un **informe individual de 700 a 900 palabras**: qué información pierde esa organización y qué decisión mejoraría si la conservara.

---

## Rúbrica

| Criterio | Insuficiente (0) | Suficiente (1) | Bueno (2) | Excelente (3) |
|---|---|---|---|---|
| **Evidencia de campo** | Sin evidencia o inventada | Respuestas sin artefacto documentado | Evidencia completa y fotografiada | Además captura el conocimiento tácito de la persona a cargo |
| **Diccionario de datos** | Lista de palabras sueltas | Datos con nombre y tipo | Completo, con origen y uso | Además identifica datos redundantes o inconsistentes |
| **Clasificación del sistema** | Etiqueta sin justificar | Justificación genérica | Justificación con evidencia propia | Discute por qué no encaja limpiamente en una sola categoría |
| **Algoritmo** | No ejecutable | Ejecutable, sin manejo de casos inválidos | Correcto, con validación | Correcto y contrastado con la simulación, con las diferencias explicadas |
| **Bitácora de IA** | Ausente o sin verificación | Verificación superficial | Verificación real | Detecta que el chatbot corrigió el código en silencio |
| **Redacción en español** | Ininteligible | Se entiende, con errores | Clara y correcta | Clara, estructurada y con argumento propio |

---

## Examen escrito 2 (23% del curso)

Individual, en papel, 80 minutos. Todas las preguntas sobre la organización que el estudiante estudió.

1. Describe el sistema de información de la organización que estudiaste. Clasifícalo según la tipología vista y **justifica con dos evidencias que recogiste en campo**. *(25 pts)*
2. Señala un dato que esa organización captura pero no usa, y explica qué decisión podría mejorar si lo usara. *(20 pts)*
3. Escribe en pseudocódigo el algoritmo de la decisión que analizó tu equipo. Incluye la validación de un dato inválido. *(30 pts)*
4. Tu equipo hizo una prueba de escritorio y una simulación con IA. ¿Coincidieron? Si no, ¿quién se equivocó y por qué? Si sí, ¿cómo sabes que ambos no estaban mal? *(25 pts)*

La pregunta 4 es la que evalúa directamente el objetivo de este curso respecto a la IA: no si la usó, sino **si tiene criterio para juzgarla**.

---

## Cobertura de estilos

| Estilo | Su terreno | Fuera de zona |
|---|---|---|
| **Activo** | Sesión 8 y el trabajo de campo | Sesión 10 (lectura y formalización) |
| **Reflexivo** | Sesión 9, el análisis del flujo del dato | Sesión 8 (entrevistar sin guion consolidado) |
| **Teórico** | Sesión 10, la clasificación y el diccionario | Sesión 8 (campo desestructurado) |
| **Pragmático** | Sesiones 11 y 12, el algoritmo y la entrega | Sesión 9 (documentar sin producir todavía) |
