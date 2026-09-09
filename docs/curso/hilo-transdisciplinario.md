# El hilo transdisciplinario

**Destino:** `docs/curso/hilo-transdisciplinario.md`

---

## 1. La tesis del curso

Las ciencias de la computación no son una disciplina más entre otras: se volvieron una **transdisciplina**, porque sus conceptos, enfoques y métodos fueron adoptados por campos que no se hablan entre sí. Las matemáticas y la estadística, las ciencias naturales, todas las ingenierías, y también la administración, la psicología, la sociología, las artes y las humanidades.

Para un estudiante de administración esto tiene una consecuencia práctica: **lo que aprende aquí no es una herramienta auxiliar de su carrera, es parte del vocabulario común con el que hoy se argumenta en casi cualquier campo.** Y esa es la razón de que la UEA esté en el primer trimestre y no en el último.

La computadora es el instrumento; la computación es la forma de pensar; y la IA —la Computadora 2.0— es la fase actual, donde el instrumento dejó de ser pasivo y empezó a decidir. Los tres son recursos transdisciplinarios, no temas de un curso técnico.

---

## 2. Dónde vive el hilo dentro del curso

No se enseña como una unidad aparte, porque se volvería un discurso. Vive en tres lugares:

| Lugar | Duración | Qué ocurre |
|---|---|---|
| **Panorama inicial**, sesión 1 | 15 min | Se plantea la tesis con ejemplos, no con argumentos |
| **Puente**, al cierre de cada proyecto | 10 min | El concepto que acaban de aprender se muestra operando en otras disciplinas |
| **Un reactivo por examen** | — | Se evalúa, para que no se perciba como adorno |

Los tres puentes caben en las sesiones 7, 12 y 18, en los últimos diez minutos, después de la entrega y antes o después del examen. No cuestan sesiones adicionales.

---

## 3. Panorama de la sesión 1 (15 minutos)

La estructura que funciona es **un concepto, cuatro campos**, en ronda rápida. No se explica cada caso: se enuncia y se pasa al siguiente. La acumulación es el argumento.

**Concepto: representar la realidad como datos.**

- En **biología**, el genoma es una secuencia de cuatro símbolos, y compararlos entre especies es un problema de alineamiento de cadenas, el mismo que resuelve un corrector ortográfico.
- En **agronomía**, una imagen satelital de una parcela es una matriz de números por banda espectral, y decidir si un cultivo tiene estrés hídrico es clasificar esa matriz.
- En **música**, una partitura es un formato de datos que codifica altura, duración y dinámica, y existió cuatro siglos antes que la computadora.
- En **administración**, el balance general es una representación de una organización entera en un conjunto acotado de datos.

**Concepto: el procedimiento explícito.**

- Un **protocolo clínico** es un algoritmo con condiciones y ramificaciones. Un **método experimental** también. Una **receta de cocina** es el mismo objeto. Un **procedimiento administrativo** documentado es exactamente lo mismo, y la mayoría de las organizaciones no lo tiene escrito.

**Cierre (2 min).** *No estoy diciendo que la computación se metió en todas partes. Estoy diciendo que la computación puso nombre a cosas que ya estaban en todas partes y no lo tenían. Por eso el vocabulario sirve fuera de aquí.*

---

## 4. Puente de P1 · Representación (sesión 7, 10 min)

**Lo que acaban de aprender:** que toda información se representa como una secuencia de símbolos discretos, y que la elección de la representación determina qué se puede hacer con ella.

**Dónde más vive:**

| Campo | El mismo concepto |
|---|---|
| Genética | Cuatro bases codifican la información hereditaria de todo lo vivo |
| Cartografía | Un mapa es una representación con pérdida, y decidir qué se pierde es la decisión de diseño |
| Contabilidad | La partida doble es un formato de representación que hace detectables ciertos errores por construcción |
| Lenguas | Un alfabeto es un conjunto discreto de símbolos para un fenómeno continuo, el sonido |

**Pregunta para el grupo:** *¿Qué se pierde en cada una de estas representaciones? Porque todas pierden algo.*

**Reactivo del examen 1 (5 pts):** menciona una representación de datos que uses en tu vida cotidiana y que no sea informática. Explica qué información conserva y cuál pierde.

---

## 5. Puente de P2 · El procedimiento explícito (sesión 12, 10 min)

**Lo que acaban de aprender:** que un proceso puede escribirse como una secuencia de pasos sin ambigüedad, con condiciones y validaciones, y que escribirlo revela los huecos que la práctica informal encubre.

**Dónde más vive:**

| Campo | El mismo concepto |
|---|---|
| Medicina | Los protocolos de triage y las listas de verificación quirúrgica redujeron la mortalidad al volver explícito lo que se suponía sabido |
| Aviación | La lista de verificación previa al despegue es un algoritmo cuya omisión mata |
| Derecho | El procedimiento administrativo es un algoritmo con condiciones, plazos y excepciones |
| Investigación | La sección de método de un artículo existe para que el procedimiento sea reproducible por otro |

**La observación que importa para administradores:** en las cuatro, escribir el procedimiento **no describe el trabajo, lo cambia**. Los huecos que aparecen al escribirlo estaban ahí antes y nadie los veía. Eso es exactamente lo que su equipo encontró en la papelería.

**Reactivo del examen 2 (5 pts):** describe un procedimiento de tu vida —académico, laboral o doméstico— que nadie ha escrito nunca. ¿Qué crees que se descubriría si se escribiera?

---

## 6. Puente de P3 · Estructura y relación (sesión 18, 10 min)

**Lo que acaban de aprender:** que organizar información en entidades relacionadas, con identificadores únicos, es lo que permite hacer preguntas que antes no se podían hacer.

**Dónde más vive:**

| Campo | El mismo concepto |
|---|---|
| Biología | La taxonomía de Linneo es una jerarquía de entidades con identificador único, tres siglos anterior al modelo relacional |
| Bibliotecología | La ficha catalográfica y el ISBN son clave primaria e integridad referencial con otro nombre |
| Demografía | Un padrón electoral es una base de datos, y sus problemas de duplicados son los mismos que los del cuaderno de fiados |
| Química | La tabla periódica es una estructura relacional donde la posición predice propiedades |

**La observación de cierre del curso:** en los cuatro casos, **la estructura permitió preguntas que antes no existían**. Linneo no descubrió especies nuevas: hizo posible preguntar cuáles se parecen entre sí. Su base de datos hizo lo mismo con la papelería.

**Reactivo del examen 3 (5 pts):** identifica una estructura de información fuera de la computación que organice entidades con identificadores únicos. ¿Qué pregunta permite hacer que sin esa estructura sería imposible?

---

## 7. Y la IA en todo esto

El hilo se cierra con la tesis de la lectura *La Computadora 2.0*: la inteligencia artificial no es una herramienta más, sino un cambio de naturaleza del instrumento. La computadora dejó de ser pasiva —como una calculadora o un procesador de texto— y se volvió un ecosistema que aprende, evoluciona y toma decisiones con consecuencias reales.

Su carácter transdisciplinario es aún más marcado que el de la computación clásica, porque el mismo modelo que redacta un correo predice estructuras de proteínas, y eso no le había pasado a ninguna tecnología antes.

**Y por eso el protocolo de este curso.** Una herramienta que atraviesa todas las disciplinas es también una herramienta que puede atrofiar la capacidad de pensar en todas ellas. Que sea transdisciplinaria es exactamente la razón por la que hay que aprender a interrogarla en lugar de obedecerla.
