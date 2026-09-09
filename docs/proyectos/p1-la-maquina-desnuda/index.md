# P1 · La máquina desnuda

**Sesiones 3 a 7 · del 28 de septiembre al 14 de octubre de 2026**
**Cubre:** Unidad 1 del contenido sintético oficial (Fundamentos de computación)
**Destino:** `docs/proyectos/p1-la-maquina-desnuda/`

---

## El reto

> Su equipo recibe una computadora del laboratorio. Es vieja, es lenta y nadie sabe exactamente qué tiene adentro.
>
> Al final de tres semanas van a entregar el **expediente técnico** de esa máquina: de qué está hecha, qué hace cada parte, cómo representa la información que procesa y **por qué es lenta** —con evidencia medida, no con opiniones.
>
> Ese expediente incluye un inventario de recursos informáticos que van a necesitar en el proyecto siguiente. No lo pierdan.

**Por qué este reto y no otro:** no requiere ningún conocimiento previo. Cualquiera puede mirar una computadora, abrirla si se puede, medir cuánto tarda en algo y anotarlo. La puerta de entrada no exige nada que no traigan. La teoría llega en la sesión 3, cuando ya vieron el fenómeno.

---

## Sesión 3 · Fase activista (lunes 28 de septiembre)

**No hay exposición previa. El profesor no explica qué es una computadora.**

### Actividad (0:00–1:20)

Cada equipo recibe una máquina y esta lista de preguntas, sin ninguna pista sobre cómo responderlas:

1. ¿Cuántas partes distintas pueden identificar, por fuera y por dentro? Dibújenlas.
2. ¿Cuál de esas partes creen que guarda la información cuando la máquina está apagada? ¿Cómo lo comprobarían?
3. Abran el archivo más grande que encuentren y **midan con el cronómetro del teléfono** cuánto tarda. Repítanlo tres veces. ¿Da lo mismo?
4. Creen un archivo de texto con una sola letra. Anoten cuánto pesa. Ahora uno con mil letras. ¿Cuánto pesa? ¿La relación es la que esperaban?
5. Encuentren tres números que la computadora reporte sobre sí misma y anótenlos, aunque no entiendan qué significan.

### Cierre (1:20–2:00)

Cada equipo escribe en el pizarrón **una cosa que le sorprendió y una pregunta que no supo responder**. El profesor no responde ninguna. Las preguntas se quedan escritas y se fotografían: se van a responder en la sesión 5, y ese momento —ver respondida la propia pregunta— es parte del diseño.

### Entregable de la sesión

Fotografía de las hojas del cuaderno con los cinco puntos. **Sin IA.**

### Nota sobre estilos

Esta sesión es cómoda para los **activos** e incómoda para **teóricos** y **reflexivos**, que van a pedir que se les explique primero. La respuesta es: todavía no, y es a propósito. El microciclo de la sesión les da su espacio en el cierre, cuando toca formular la pregunta precisa, que es terreno del teórico.

---

## Sesión 4 · Fase reflexiva (miércoles 30 de septiembre)

### Actividad (0:00–0:40) — Comparación entre equipos

Los cinco equipos vacían sus datos en una tabla común en el pizarrón: tiempos medidos, pesos de archivo, números encontrados. **Las diferencias son el material de la sesión.** ¿Por qué el equipo 2 midió 4 segundos y el equipo 5 midió 11 en la misma operación? ¿Por qué el mismo archivo pesa distinto en dos máquinas?

### Actividad (0:40–1:30) — Del dato al patrón

Cada equipo responde por escrito:

1. ¿Qué mediciones coincidieron entre equipos y cuáles no? ¿Qué explicaría la diferencia?
2. Ordenen las cinco máquinas de más rápida a más lenta con la evidencia disponible. **Justifiquen el criterio que usaron para ordenar.**
3. De los números que anotaron sin entender, ¿cuáles parecen medir lo mismo en unidades distintas?

### Cierre (1:30–2:00)

El profesor presenta el vocabulario mínimo —**solo los nombres**, sin teoría todavía— de las cosas que los equipos ya observaron. Es el puente hacia la sesión teórica: *eso que midieron tiene un nombre y la próxima sesión vamos a entender por qué funciona así*.

### Entregable

Hoja de comparación con las tres respuestas. **Sin IA.**

---

## Sesión 5 · Fase teórica (lunes 5 de octubre)

**Lecturas previas obligatorias:** `02-que-es-la-computadora.md` y `04-bits-bytes-y-mas-alla.md`

### Microciclo

| Minutos | Qué |
|---|---|
| 0–20 | **Activista:** ejercicio de conversión a binario en el pizarrón, por parejas, contra reloj |
| 20–45 | **Reflexivo:** se retoman las preguntas que quedaron escritas en la sesión 3 y se van respondiendo una por una con lo que traen de la lectura |
| 45–85 | **Teórico:** exposición dialogada. Arquitectura de la máquina, jerarquía de memoria, representación de datos. Por qué mil letras pesan mil veces más pero no exactamente |
| 85–120 | **Pragmático:** cada equipo reinterpreta sus propias mediciones con el vocabulario nuevo y corrige lo que había supuesto mal |

### Uso de IA — primera bitácora

En los últimos 20 minutos, cada estudiante hace **al menos tres consultas** a un chatbot sobre algo que sigue sin entender de la lectura, y las registra en la bitácora con los cuatro campos.

**Caza del error de P1:** pregúntenle al chatbot por las especificaciones exactas del modelo de máquina que tienen enfrente, o por el precio actual de un componente en el mercado mexicano. Documenten qué respondió y verifiquen contra lo que ustedes midieron. **Escriban por qué falló.**

---

## Sesión 6 · Fase teórica → pragmática (miércoles 7 de octubre)

> **Entre esta sesión y la siguiente cae el lunes 12 de octubre, descanso obligatorio.** Los equipos lo usan para conseguir acceso a la organización que van a estudiar en P2. El expediente de P1 se termina en ese puente.

### Laboratorio simulado (0:00–1:10)

Aquí entra el mecanismo central del curso. **Cada paso en papel antes de la simulación.**

1. **En papel:** conviertan a binario el número de serie de su máquina. A mano, con el método visto.
2. **En papel:** calculen cuántos bytes ocuparía un archivo de texto con los nombres de los cinco integrantes del equipo, contando cada carácter.
3. **Simulación:** pidan al chatbot que actúe como conversor, sin explicaciones, y comparen con su resultado manual.
4. **Si no coinciden:** averigüen quién se equivocó y por qué. Esa averiguación es la parte que se califica.

Instrucción sugerida para la simulación, que se pega en la bitácora:

> *Actúa como un conversor de sistemas numéricos. Convierte el siguiente número decimal a binario y devuélveme solo el resultado, sin explicaciones ni pasos intermedios: [número]*

### Construcción del entregable (1:10–2:00)

El equipo arma el expediente. Reparto por rol: el explorador aporta las mediciones, el cronista la documentación, el arquitecto el diagrama y el vocabulario, el integrador la redacción, el verificador la bitácora consolidada.

---

## Sesión 7 · Fase pragmática (miércoles 14 de octubre)

| Minutos | Qué |
|---|---|
| 0–30 | Entrega del expediente. Cada equipo lo presenta en 5 minutos |
| 30–110 | **Examen escrito 1**, individual, en papel, sin dispositivos |
| 110–120 | Cierre y asignación formal de P2: cada equipo declara qué organización consiguió |

---

## El entregable

**Expediente técnico de la máquina**, en papel o digital, con seis componentes:

| # | Componente | Quién lo lidera |
|---|---|---|
| 1 | Diagrama de bloques de la máquina, **dibujado a mano**, con los componentes identificados y nombrados correctamente | Arquitecto |
| 2 | Tabla de mediciones: tiempos, pesos de archivo, números del sistema, con las tres repeticiones de cada medición | Explorador |
| 3 | Ejercicio de representación de datos: una conversión a binario resuelta a mano y su verificación por simulación | Arquitecto |
| 4 | **Diagnóstico argumentado de por qué la máquina es lenta**, con la evidencia que lo sostiene | Integrador |
| 5 | **Inventario de recursos informáticos** de la máquina (insumo obligatorio para P2) | Cronista |
| 6 | Bitácora de IA del equipo, incluida la caza del error | Verificador |

Más un **informe escrito individual de 600 a 800 palabras** con el diagnóstico y su justificación. Este texto es donde se evalúa el objetivo específico de expresión escrita en español.

---

## Rúbrica del entregable (15% del curso, repartido entre los tres proyectos)

| Criterio | Insuficiente (0) | Suficiente (1) | Bueno (2) | Excelente (3) |
|---|---|---|---|---|
| **Evidencia** | Datos ausentes o inventados | Mediciones presentes pero sin repeticiones | Mediciones completas y repetidas | Además, identifican y explican mediciones anómalas |
| **Vocabulario técnico** | Usa términos coloquiales | Usa términos correctos con errores | Usa el vocabulario correctamente | Usa el vocabulario y distingue matices (memoria vs. almacenamiento) |
| **Argumentación del diagnóstico** | Opinión sin evidencia | Conclusión con evidencia parcial | Conclusión sostenida en sus datos | Considera y descarta explicaciones alternativas |
| **Bitácora de IA** | Ausente o con el campo de verificación vacío | Consultas registradas, verificación superficial | Verificación real contra fuente | Documenta una refutación al chatbot y explica el tipo de error |
| **Redacción en español** | Ininteligible o con errores graves | Se entiende, con errores | Clara y correcta | Clara, correcta y bien estructurada |
| **Trabajo por roles** | Uno o dos hicieron todo | Reparto desigual | Cada rol aportó lo suyo | Se nota la integración de las cinco aportaciones |

---

## Examen escrito 1 (23% del curso)

Individual, en papel, 80 minutos, sin dispositivos. **Cuatro preguntas, todas sobre la máquina que el estudiante trabajó.** Ejemplo del banco:

1. Dibuja de memoria el diagrama de bloques de la máquina de tu equipo e identifica dónde reside la información cuando está apagada. Explica cómo lo comprobaron ustedes. *(20 pts)*
2. Su equipo midió tres veces la misma operación y obtuvo tiempos distintos. Da dos explicaciones posibles de esa variación y di cuál te parece más probable y por qué. *(25 pts)*
3. Convierte a binario el número [dato tomado del expediente de su equipo] y explica el procedimiento. *(20 pts)*
4. Argumenta en un texto de media cuartilla por qué la máquina de tu equipo es lenta. Debes citar al menos dos mediciones propias. *(35 pts)*

**Por qué este examen cumple el programa oficial y es a prueba de chatbot:** es una evaluación periódica escrita, individual, exactamente como exige el programa. Y ningún modelo de lenguaje puede responderla, porque no estuvo frente a esa máquina ni tomó esas mediciones. La única forma de aprobarlo es haber hecho el proyecto.

---

## Cobertura de estilos en el proyecto

| Estilo | Dónde tiene su terreno | Dónde trabaja fuera de zona |
|---|---|---|
| **Activo** | Sesión 3 completa; primeros 20 min de cada sesión | Sesión 5 (lectura y formalización) |
| **Reflexivo** | Sesión 4 completa; puestas en común | Sesión 3 (acción sin preparación) |
| **Teórico** | Sesión 5; construcción del diagrama y el vocabulario | Sesión 3 (actuar sin marco) |
| **Pragmático** | Sesiones 6 y 7; el diagnóstico y el entregable | Sesión 5 (teoría sin aplicación inmediata) |
