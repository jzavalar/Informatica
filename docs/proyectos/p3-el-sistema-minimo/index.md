# P3 · El sistema mínimo

**Sesiones 14 a 18 · del 11 al 25 de noviembre de 2026**
**Cubre:** Unidad 4 del contenido sintético (Manejo de bases de datos) e integración de todo el curso
**Destino:** `docs/proyectos/p3-el-sistema-minimo/`

---

## El reto

> Tomen el diccionario de datos que produjeron en P2 y conviértanlo en una **base de datos relacional que funcione**.
>
> Con ella deben responder **tres preguntas que su organización no puede responder hoy**. No preguntas cualesquiera: preguntas que la dueña querría poder contestar y no puede, porque sus datos viven en un cuaderno.
>
> Al final entregan la propuesta a la organización. De verdad, no como ejercicio.

Este proyecto cierra el arco: de la máquina física (P1) a los datos que existen sin sistema (P2) a la información que produce decisiones (P3).

---

## Sesión 14 · Fase activista (miércoles 11 de noviembre)

**El choque de este proyecto es un fracaso deliberado.**

### Actividad (0:00–1:20)

Cada equipo formula sus tres preguntas de negocio e **intenta responderlas con los datos tal como están hoy**: con la fotografía del cuaderno, con las notas de campo, con lo que la dueña recuerda.

No van a poder. Ese es el punto. Deben documentar **exactamente por qué falla cada intento**:

- El dato existe pero está en tres lugares y no coinciden.
- El dato existe pero no tiene fecha, así que no se puede comparar contra el mes pasado.
- Hay que contar a mano 400 renglones y a la tercera vez ya nadie confía en el conteo.
- El dato de un cliente está escrito con tres nombres distintos y no hay forma de saber si es el mismo.

### Cierre (1:20–2:00)

Cada equipo escribe en el pizarrón **la razón exacta por la que no pudo responder**. Se fotografía. Esa lista es el planteamiento del problema que el modelo relacional resuelve, formulado por ellos.

### Entregable

Registro del intento fallido, con las razones. **Sin IA.**

---

## Sesión 15 · Fase reflexiva (lunes 16 de noviembre)

### Comparación (0:00–0:50)

Las cinco listas del pizarrón se comparan. **Los cinco equipos fracasaron por las mismas cuatro o cinco razones.** Ese descubrimiento —que el problema no era su cuaderno en particular sino la ausencia de estructura— es la sesión completa.

Se agrupan las razones en categorías, que van a resultar ser, sin haberlas nombrado todavía: redundancia, falta de identificador único, ausencia de integridad referencial, y ausencia de estructura temporal.

### Análisis (0:50–1:40)

Cada equipo, en papel:

1. Separen la información de su organización en **grupos de cosas del mismo tipo**. ¿Cuántos grupos les salen?
2. Dentro de cada grupo, ¿qué permitiría distinguir un elemento de otro sin ninguna duda?
3. ¿Qué grupos se relacionan con qué otros grupos, y cómo?

Están construyendo un modelo entidad-relación sin saber que se llama así. En la sesión siguiente se lo nombran, y descubren que ya lo habían hecho.

---

## Sesión 16 · Fase teórica (miércoles 18 de noviembre)

**Lecturas previas:** `12-introduccion-bases-de-datos.md` y `13-de-la-hoja-de-calculo-al-dbms.md`

| Minutos | Fase | Actividad |
|---|---|---|
| 0–20 | Activista | En el pizarrón: dados diez renglones desordenados con datos repetidos, sepáralos en tablas. Contra reloj, por parejas |
| 20–45 | Reflexivo | Se retoman los "grupos" de la sesión 15 y se les pone nombre: entidades. Los identificadores: claves primarias. Las relaciones: claves foráneas |
| 45–85 | Teórico | Exposición dialogada: modelo relacional, redundancia, integridad referencial, y por qué existe un DBMS |
| 85–120 | Pragmático | Cada equipo dibuja a mano su diagrama entidad-relación completo |

### Bitácora de IA

**Caza del error de P3:** pídanle al chatbot bibliografía académica específica sobre un tema estrecho —por ejemplo, estudios sobre sistemas de información en microempresas mexicanas— y **verifiquen que cada referencia exista realmente**. Documenten cuántas eran falsas y expliquen por qué un modelo de lenguaje inventa referencias con formato impecable.

Esta caza es la más importante de las tres, porque es el error que van a encontrar el resto de su carrera al escribir trabajos académicos.

---

## Sesión 17 · Fase teórica → pragmática (lunes 23 de noviembre)

### Laboratorio simulado (0:00–1:20)

**El chatbot como motor de base de datos.** El laboratorio no tiene DBMS instalado; esta es la máquina que no tenemos.

Orden inviolable:

1. **En papel:** el diagrama entidad-relación terminado, con claves primarias y foráneas.
2. **En papel:** las tres tablas llenas con al menos cinco renglones reales de la organización.
3. **En papel:** el resultado esperado de cada una de las tres preguntas de negocio, calculado a mano.
4. **Simulación:**

   > *Actúa como un motor de base de datos relacional. Estas son mis tablas con estos datos: [tablas]. Ejecuta la siguiente consulta y devuélveme únicamente la tabla de resultados, sin explicaciones, sin corregir mi diseño y sin agregar datos que no estén ahí: [consulta en lenguaje natural o en SQL].*

5. **Comparación** con el cálculo manual del paso 3.

**Advertencia obligatoria:** un chatbot simulando un motor relacional se equivoca con frecuencia en agregaciones, con valores nulos y con más de una decena de renglones. **Nunca usen un resultado simulado como si fuera un cálculo verificado.** Que se equivoque no arruina el ejercicio: es el ejercicio. Ustedes son quienes auditan, y esa es exactamente la posición que van a ocupar profesionalmente frente a cualquier sistema que no diseñaron.

### Implementación alternativa (paralela, si hay hoja de cálculo disponible)

Si el laboratorio tiene una hoja de cálculo, aunque sea vieja, implementen ahí las tablas normalizadas y una búsqueda entre ellas. Hacer a mano la integridad referencial que un DBMS haría solo es el mejor argumento posible sobre por qué existe un DBMS.

### Preparación de la presentación (1:20–2:00)

---

## Sesión 18 · Fase pragmática (miércoles 25 de noviembre)

| Minutos | Qué |
|---|---|
| 0–100 | **Presentación de los cinco equipos**, 20 minutos cada uno: el arco completo de P1 a P3 |
| 100–120 | Entrega del expediente final y cierre |

El **Examen escrito 3** se aplica en la semana de evaluaciones globales, del 7 al 11 de diciembre.

---

## El entregable

**El sistema mínimo viable**, con seis componentes:

| # | Componente | Rol |
|---|---|---|
| 1 | Registro del intento fallido de la sesión 14, con las razones documentadas | Cronista |
| 2 | **Diagrama entidad-relación dibujado a mano**, con claves primarias y foráneas justificadas una por una | Arquitecto |
| 3 | Tablas pobladas con datos reales de la organización | Explorador |
| 4 | Las **tres preguntas de negocio respondidas**: resultado calculado a mano, resultado simulado, y explicación de las diferencias | Integrador |
| 5 | **Propuesta de solución tecnológica dirigida a la organización**, en lenguaje que la dueña entienda, con qué ganaría y qué costaría | Integrador |
| 6 | Bitácora de IA con la caza de referencias falsas | Verificador |

Más un **informe individual de 900 a 1,100 palabras** que recorra el arco completo: de la máquina de P1 al sistema de P3, y qué aprendió sobre la relación entre tecnología y decisiones administrativas.

---

## Rúbrica

| Criterio | Insuficiente (0) | Suficiente (1) | Bueno (2) | Excelente (3) |
|---|---|---|---|---|
| **Modelo relacional** | Una sola tabla o entidades mal separadas | Entidades correctas, claves incompletas | Claves primarias y foráneas correctas | Además justifica cada decisión de diseño contra una alternativa |
| **Trazabilidad con P2** | El modelo no proviene del diccionario | Proviene parcialmente | Proviene del diccionario de datos | Además explica qué tuvo que corregir del diccionario y por qué |
| **Respuesta a las preguntas** | No las responde | Responde sin verificar | Responde con verificación manual | Detecta y explica una discrepancia con la simulación |
| **Propuesta a la organización** | Jerga técnica ininteligible para el destinatario | Comprensible pero genérica | Concreta y comprensible | Además dimensiona costo y esfuerzo con realismo |
| **Bitácora de IA** | Ausente | Consultas sin verificar | Verificación real | Documenta referencias falsas y explica el mecanismo del error |
| **Redacción en español** | Ininteligible | Se entiende, con errores | Clara y correcta | Clara, estructurada, con argumento propio sostenido |

---

## Examen escrito 3 · Integrador (24% del curso)

Semana de evaluaciones globales, 7 al 11 de diciembre. Individual, en papel, 100 minutos.

1. Dibuja el diagrama entidad-relación del sistema de tu equipo, con claves primarias y foráneas. Justifica **por qué una de las relaciones es como es y no de otra manera**. *(25 pts)*
2. En la primera sesión de P3 tu equipo no pudo responder sus preguntas de negocio. Explica técnicamente por qué no pudo, usando el vocabulario del modelo relacional. *(20 pts)*
3. Su equipo simuló una consulta con IA. Describe qué pidieron, qué obtuvieron y cómo verificaron el resultado. Si hubo una diferencia, explícala. *(20 pts)*
4. Recorre el arco del trimestre: cómo la máquina que examinaron en octubre, los datos que documentaron en noviembre y el modelo que construyeron se relacionan entre sí. Media cuartilla. *(20 pts)*
5. Tu organización te contrata como administrador. Con lo que sabes ahora, ¿qué le recomendarías hacer primero y por qué? *(15 pts)*

---

## Cobertura de estilos

| Estilo | Su terreno | Fuera de zona |
|---|---|---|
| **Activo** | Sesión 14, el intento fallido; la presentación final | Sesión 16 (formalización del modelo) |
| **Reflexivo** | Sesión 15, la comparación entre fracasos | Sesión 14 (intentar sin método) |
| **Teórico** | Sesiones 16 y 17, el modelo y su justificación | Sesión 14 (actuar sin estructura) |
| **Pragmático** | Sesión 18, la propuesta a la organización | Sesión 15 (analizar sin producir) |

---

## Cierre del curso

En la última sesión de holgura, si está disponible, conviene un ejercicio de diez minutos: pedirle a cada estudiante que compare lo que escribió en la sesión 1 —cuando respondió qué semana le costaría más trabajo y qué haría para no desaparecer— con lo que efectivamente pasó. Es la única evaluación del diseño por estilos que va a existir, y cuesta diez minutos.
