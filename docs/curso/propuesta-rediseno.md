# Propuesta: Informática 2.0

## Reestructuración del repositorio `jzavalar/Informatica` bajo aprendizaje basado en proyectos

**Autor de la propuesta:** elaborada para el dr. Jesús Zavala Ruiz
**UEA:** Informática, clave 2211088 · Licenciatura en Administración · UAM-Iztapalapa
**Trimestre destino:** 26-Otoño (ajustable)
**Fecha:** septiembre de 2026
**Repositorio base:** `https://github.com/jzavalar/Informatica` (604 commits, HEAD `fdf9a15`)

---

## 1. Diagnóstico del punto de partida

### 1.1 El repositorio

El repositorio contiene cinco trimestres de trabajo docente acumulado. Su problema no es de contenido sino de **arquitectura de la información**: cincuenta archivos en la raíz, sin jerarquía, con bitácoras trimestrales (`22-P.md`, `22-O.md`, `23-I.md`, `24-I.md`, `25-P.md`) que suman más de 330 KB mezcladas con las lecturas del curso, los datasets, los scripts y dos carpetas de imágenes con nombres redundantes (`imagenes/` e `images/`).

Un estudiante de primer trimestre que llega a ese árbol no tiene forma de saber por dónde entrar. La numeración de las lecturas (`Lectura_04_2_1_...`) es un artefacto de la historia de edición, no una guía de estudio. Hay además duplicaciones que reflejan iteraciones sucesivas —`Lectura_03` en versiones v1 y v2, `Lectura_04_1` y `Lectura_04_2_0`, el análisis de datos completo y simplificado— que para el autor son versiones de trabajo y para el lector son ambigüedad.

**Esto no es un defecto del repositorio: es la evidencia material de años de mejora iterativa.** El objetivo de la reestructuración no es borrar esa historia sino separar dos funciones que hoy están fundidas en el mismo espacio: el **taller del profesor** (donde se acumulan versiones, pruebas y bitácoras) y la **superficie de estudio del alumno** (que debe ser mínima, ordenada y sin ambigüedad).

### 1.2 El programa oficial y sus restricciones duras

El programa de estudios vigente (clave 2211088) fija cuatro elementos que **no son negociables** sin pasar por el Consejo Divisional:

| Elemento | Contenido oficial |
|---|---|
| Objetivo general | Conocer los fundamentos actuales de las tecnologías de información |
| Objetivos específicos | (a) Utilizar programas de aplicación general para manejo de datos numéricos y bases de datos; (b) Expresar comprensión de textos y comunicar ideas con uso adecuado de la lengua española |
| Contenido sintético | 1. Fundamentos de computación · 2. Introducción a los sistemas de información · 3. Manipulación de datos numéricos asistido por computadora · 4. Manejo de bases de datos |
| Evaluación global | Al menos **dos evaluaciones periódicas escritas con ponderación del 70%**; el 30% restante mediante ejercicios, laboratorio, tareas, exposiciones y trabajos de investigación |

La bibliografía oficial (Leal *et al.*, 2000; Norton, 2000; Silberschatz *et al.*, 2000) está obsoleta en su capa tecnológica pero es *recomendable*, no obligatoria, lo que deja margen para la bibliografía actualizada que ya usas.

**La tensión central** de esta propuesta es que un paradigma ABP genuino tiende a invertir la proporción 70/30. La solución adoptada (sección 5) cumple la letra del programa sin traicionar el paradigma.

### 1.3 Las condiciones reales de operación

- Grupo de primer trimestre, con **nivel de conocimiento previo deficiente y heterogéneo**.
- Laboratorio institucional con **software preinstalado y desactualizado**, sin permisos de instalación, útil para navegar y ejecutar lo que ya está.
- Estudiantes con **smartphone** universal y laptop en casa de forma desigual.
- Acceso libre a **chatbots gratuitos**, que ya usan, generalmente para delegar en vez de aprender.

Estas condiciones se tratan aquí como **restricciones de diseño productivas**, no como carencias a lamentar. Un laboratorio degradado obliga a entender qué hace la herramienta; una hoja de papel impide que el asistente automático haga el trabajo; un chatbot omnipresente vuelve indispensable enseñar a interrogarlo.

---

## 2. Principios de diseño

### Principio 1 — La teoría llega tarde, a propósito

En la secuencia tradicional se explica el concepto y luego se aplica. Con conocimiento previo deficiente esa secuencia falla: el estudiante no tiene dónde anclar la explicación y la memoriza sin comprenderla. Aquí se invierte: **primero el choque con el problema, después el vocabulario que lo nombra**. El estudiante llega a la lectura teórica habiendo ya tropezado con el fenómeno, y la lectura le da nombres a cosas que ya observó.

Esto atiende directamente la restricción 2 (necesidad de ser elemental): ser elemental no significa simplificar el contenido, significa **no presuponer anclajes que no existen** y construirlos con experiencia directa antes de nombrarlos.

### Principio 2 — El oráculo llega todavía más tarde

El chatbot está **prohibido en la fase activista** de cada proyecto y **obligatorio, con bitácora, en las fases teórica y pragmática**. La razón es mecánica: si la herramienta que puede producir la respuesta está disponible antes de que el estudiante haya formulado la pregunta, no habrá pregunta. Retrasar el acceso no es moralismo, es preservar la condición de posibilidad del aprendizaje.

Cuando el chatbot entra, entra como **tutor interrogado**, no como proveedor. El protocolo de la sección 6 hace verificable esa distinción.

### Principio 3 — Lo analógico como filtro de comprensión

El papel es lento y no autocompleta. Un diagrama entidad-relación dibujado a mano exige decidir cada línea; el mismo diagrama generado por una herramienta puede entregarse sin haberlo entendido. En esta propuesta **todo artefacto conceptual nace en papel** y solo después se digitaliza. La digitalización no es el objetivo: es la prueba de que el diseño en papel era correcto.

### Principio 4 — Cada proyecto recorre el ciclo completo de estilos

El ciclo de Honey y Mumford —activista, reflexivo, teórico, pragmático— se mapea a las cuatro semanas de cada proyecto (sección 4). Cada estudiante encuentra su fase cómoda tres veces en el trimestre y es empujado fuera de ella nueve veces. El equilibrio exigido por tu restricción 5 se cumple **estructuralmente**, no por buena voluntad al planear cada sesión.

### Principio 5 — Encadenamiento acumulativo

P1 produce un inventario; P2 lo convierte en modelo de datos; P3 lo convierte en sistema. Al final del trimestre el estudiante no tiene tres trabajos: tiene **un sistema de información que construyó desde cero**, con la trazabilidad completa de cómo llegó ahí.

---

## 3. Estrategia de migración del repositorio

### 3.1 Decisión: mismo repositorio, reestructurado

Se descarta crear un repositorio nuevo. Razones:

1. **Los enlaces permanentes sobreviven.** Las URL con SHA (`blob/fdf9a15.../archivo.md`) que ya circulan en materiales, correos y el grupo de Telegram siguen resolviendo. En un repositorio nuevo dejan de existir.
2. **`git mv` preserva trazabilidad.** GitHub detecta los renombres y `git log --follow` sigue el rastro de cada archivo a través de la reorganización. No se pierde un solo commit.
3. **La historia es un activo pedagógico.** 604 commits documentan la evolución real de un cuerpo de conocimiento. Es material demostrable en clase sobre control de versiones, y se ve como injerto si se trasplanta a un repositorio nuevo.
4. **Cero riesgo.** No hay reescritura de historia, no hay `filter-repo`, no hay posibilidad de perder objetos.

### 3.2 Marcadores de la transición

```bash
git tag -a v1.0-legado -m "Estado del repositorio al cierre de 25-P, antes de la reestructuración ABP" fdf9a15
git branch legado fdf9a15
git tag -a v2.0-abp -m "Informática 2.0: reestructuración bajo aprendizaje basado en proyectos"
```

El tag `v1.0-legado` deja un punto de entrada permanente y navegable desde la interfaz de GitHub al repositorio "como estaba". La rama `legado` permite hacer checkout del árbol viejo sin salir del estado detached.

### 3.3 Árbol destino

```
Informatica/
├── README.md                      ← portada: qué es el curso, cómo se aprueba, por dónde empezar
├── mkdocs.yml                     ← configuración del sitio
├── LICENSE
├── CONTRIBUTING.md                ← cómo un alumno propone una corrección (pedagógico: PR real)
├── .github/
│   └── workflows/
│       └── pages.yml              ← despliegue automático del sitio
├── docs/
│   ├── index.md                   ← página de inicio del sitio
│   ├── curso/
│   │   ├── programa-oficial.md    ← 00.2_2211088pe_...md (intacto, es el documento normativo)
│   │   ├── programa-analitico.md  ← el programa nuevo, ABP
│   │   ├── calendario.md          ← 12 semanas, 24 sesiones, fechas
│   │   ├── evaluacion.md          ← esquema, rúbricas, criterios
│   │   └── como-estudiar.md       ← guía de uso del propio repositorio
│   ├── arranque/
│   │   ├── diagnostico.md         ← instrumento de conocimientos previos
│   │   ├── estilos-lsq.md         ← protocolo LSQ Honey-Mumford
│   │   └── protocolo-ia.md        ← reglas de uso de chatbots + bitácora
│   ├── proyectos/
│   │   ├── p1-la-maquina-desnuda/
│   │   │   ├── index.md           ← enunciado, entregables, rúbrica
│   │   │   ├── semana-01-activista.md
│   │   │   ├── semana-02-reflexiva.md
│   │   │   ├── semana-03-teorica.md
│   │   │   └── semana-04-pragmatica.md
│   │   ├── p2-los-datos-invisibles/   (misma estructura)
│   │   └── p3-el-sistema-minimo/      (misma estructura)
│   ├── lecturas/                  ← las 20 lecturas, renombradas por tema y no por orden de edición
│   ├── recursos/
│   │   ├── guia-apa-7.md
│   │   ├── glosario.md            ← nuevo: vocabulario mínimo del curso
│   │   ├── scripts/               ← limpiar_bd.py, script.R, suma.psc
│   │   └── datos/                 ← basededatos.csv, analisis_ventas.csv, ...
│   └── assets/                    ← fusión de imagenes/ e images/
├── plantillas/                    ← formatos que el alumno copia para entregar
│   ├── bitacora-de-ia.md
│   ├── entregable-semanal.md
│   └── informe-de-proyecto.md
└── archivo/
    ├── README.md                  ← explica qué es esto y por qué se conserva
    ├── bitacoras/                 ← 22-P.md, 22-O.md, 23-I.md, 24-I.md, 25-P.md
    ├── estudios-de-caso/          ← los cuatro estudios de caso previos
    └── versiones-previas/         ← v0/v1 de lecturas superadas
```

### 3.4 Criterio de asignación de los materiales existentes

| Material actual | Destino | Justificación |
|---|---|---|
| `00.2_2211088pe_Programa...md` | `docs/curso/programa-oficial.md` | Documento normativo, se conserva sin una coma de cambio |
| `00.0_2211088pe.ocr.pdf` | `docs/curso/` | Respaldo del oficial |
| `00.3_Programa-semanal...md` | `archivo/versiones-previas/` | Superado por el programa ABP |
| `Lectura_01`, `Lectura_02` | `docs/lecturas/` | Base conceptual, alimentan P1 |
| `Lectura_03` **v2** | `docs/lecturas/computadora-2-0.md` | **Lectura eje del curso**, alimenta el protocolo de IA |
| `Lectura_03` v1 | `archivo/versiones-previas/` | Conserva las verificaciones de referencias, útil para ti |
| `Lectura_04_*` (sistemas operativos) | `docs/lecturas/` + `archivo/` | v1 al sitio, v0 y prácticas de instalación al archivo (no ejecutables en el laboratorio actual) |
| `Lectura_05_0` (bits y bytes) | `docs/lecturas/` | Alimenta P1 semana teórica |
| `Lectura_06_*`, `07`, `10` | `docs/lecturas/` | Alimentan P2 |
| `Lectura_08_0` (Python) | `archivo/` | Fuera de alcance en laboratorio sin instalación; se conserva |
| `Lectura_09_*` (algoritmos + IA) | `docs/lecturas/` | Núcleo de P2, especialmente `09_3` |
| `Lectura_11.*` (bases de datos) | `docs/lecturas/` | Núcleo de P3; `11.2` alimenta el protocolo de IA |
| `Estudio_de_caso_*` | `archivo/estudios-de-caso/` | Canteras de casos para los proyectos, no material del alumno |
| `22-P`…`25-P.md` | `archivo/bitacoras/` | Memoria docente |
| `Holbeck_2025_beyond-detection.md` | `docs/recursos/` | Sustento del protocolo de IA |
| Scripts y CSV | `docs/recursos/` | Insumos de P3 |

El script `migrar_repo.sh` que acompaña esta propuesta ejecuta la reorganización completa con `git mv`, en un solo commit reversible.

---

## 4. Arquitectura pedagógica: tres proyectos, doce semanas

### 4.1 El módulo de cuatro semanas

Cada proyecto ocupa cuatro semanas (ocho sesiones de dos horas) y recorre el ciclo completo de Honey y Mumford, con una fase dominante por semana:

| Semana | Fase dominante | Qué hace el estudiante | Qué hace el profesor | IA |
|---|---|---|---|---|
| A | **Activista** | Se enfrenta al problema sin teoría previa. Manipula, prueba, se equivoca, produce evidencia bruta | Plantea el reto, no explica. Circula y hace preguntas | **Prohibida** |
| B | **Reflexivo** | Documenta lo que observó, compara con otros equipos, detecta patrones y contradicciones | Orquesta la comparación entre equipos, tabula hallazgos en el pizarrón | **Prohibida** |
| C | **Teórico** | Lee, formaliza, adquiere el vocabulario, corrige su modelo mental | Expone dialogadamente, conecta la lectura con lo que ya observaron | **Obligatoria, con bitácora** |
| D | **Pragmático** | Aplica a un caso real, produce el entregable, presenta y sustenta por escrito | Evalúa, retroalimenta, aplica el examen escrito del proyecto | **Obligatoria, con bitácora** |

Dentro de cada sesión opera además un **microciclo**: los primeros 20 minutos son siempre manipulativos (activista), sigue un momento de puesta en común (reflexivo), un bloque de formalización (teórico) y cierra con una aplicación breve (pragmático). Así ningún perfil pasa dos horas seguidas fuera de su zona.

### 4.2 Los tres proyectos

#### P1 — La máquina desnuda (semanas 1-4)

> *Cubre: Unidad 1 del contenido sintético (Fundamentos de computación).*

**Reto:** el equipo recibe un equipo real del laboratorio —viejo, lento, con software desactualizado— y debe producir el **expediente técnico** de esa máquina: qué la compone, qué hace cada parte, cómo representa la información que procesa, y **por qué es lenta**, con evidencia y no con opinión.

**Producto:** expediente en papel (diagrama de bloques dibujado a mano, tabla de componentes, medición de tiempos de tarea, conversión manual de una muestra de datos a binario y a texto codificado) más un informe escrito de 800 palabras.

**Encadenamiento:** el expediente incluye un **inventario de recursos informáticos** que P2 usará como universo de datos.

**Por qué funciona con nivel previo deficiente:** nadie necesita saber nada para abrir una computadora y observarla. La teoría de representación de datos llega en la semana C, cuando ya vieron que el archivo de texto pesa distinto que la imagen.

---

#### P2 — Los datos que la organización no ve (semanas 5-8)

> *Cubre: Unidades 2 y 3 (Sistemas de información · Manipulación de datos numéricos).*

**Reto:** el equipo elige una organización real y pequeña a la que tenga acceso —la cafetería de la unidad, la papelería de la esquina, el negocio familiar, una asociación estudiantil— y **descubre el sistema de información que ya opera ahí sin que nadie lo llame así**: qué datos se capturan, dónde viven (cuaderno, memoria de la dueña, WhatsApp), qué decisiones dependen de ellos y qué información se pierde.

**Producto:** mapa del proceso administrativo, diccionario de datos en papel, algoritmo en pseudocódigo para una decisión concreta del negocio (cálculo de punto de reorden, de comisión, de precio), diagrama de flujo y **prueba de escritorio con tres casos, uno de ellos con datos inválidos**.

**Encadenamiento:** el diccionario de datos es el insumo directo del modelo relacional de P3.

**Por qué funciona:** conecta el contenido con un mundo que el estudiante conoce. La tipología TPS/MIS/DSS/ERP deja de ser un acrónimo que memorizar y se vuelve una pregunta sobre el negocio que están observando.

---

#### P3 — El sistema mínimo viable (semanas 9-12)

> *Cubre: Unidad 4 (Manejo de bases de datos) e integración.*

**Reto:** convertir el diccionario de datos de P2 en una **base de datos relacional funcional** y usarla para responder tres preguntas que la organización no puede responder hoy.

**Producto:** diagrama entidad-relación dibujado a mano con claves primarias y foráneas justificadas, implementación en el software de hoja de cálculo disponible en el laboratorio (con tablas normalizadas y búsquedas entre ellas), tres consultas resueltas, y una **propuesta de solución tecnológica** entregada como informe formal a la organización estudiada.

**Encadenamiento:** cierra el arco. El estudiante presenta el sistema completo: de la máquina física (P1) a los datos (P2) a la información que produce decisiones (P3).

**Por qué funciona:** la limitación del laboratorio es aquí una ventaja pedagógica. Implementar un modelo relacional en una hoja de cálculo vieja obliga a hacer a mano la integridad referencial que un DBMS haría solo, y a entender por qué existe un DBMS.

---

## 5. Evaluación: cumplir la letra del programa sin traicionar el ABP

### 5.1 El mecanismo

El programa exige al menos dos evaluaciones periódicas **escritas** con ponderación del 70%. La solución adoptada: **tres exámenes escritos individuales, uno al cierre de cada proyecto, cuyas preguntas versan sobre el proyecto que el propio estudiante realizó.**

Un examen del P2 no pregunta "¿qué es un sistema de información?" sino:

> *Describe el sistema de información de la organización que estudiaste. Clasifícalo según la tipología vista y justifica la clasificación con dos evidencias que recogiste en campo. Señala un dato que la organización captura pero no usa, y explica qué decisión podría mejorar si lo usara.*

Esta pregunta es **irrepetible entre equipos, imposible de contestar sin haber hecho el proyecto y no delegable a un chatbot**, porque el chatbot no estuvo en la papelería. Es escrita, es individual, es periódica: cumple el programa al pie de la letra. Y evalúa exactamente lo que el ABP produce.

Cumple además el segundo objetivo específico del programa —expresión escrita en lengua española— de manera no decorativa: la redacción es parte de la calificación en cada examen y en cada informe.

### 5.2 Esquema

| Componente | % | Momento | Naturaleza |
|---|---|---|---|
| Examen escrito 1 (sobre P1) | 23% | Semana 4 | Individual, en papel, preguntas sobre el propio expediente técnico |
| Examen escrito 2 (sobre P2) | 23% | Semana 8 | Individual, en papel, preguntas sobre la organización estudiada |
| Examen escrito 3 (sobre P3) | 24% | Semana 12 | Individual, en papel, integrador de los tres proyectos |
| **Subtotal escrito** | **70%** | | **Cumple el requisito del programa oficial** |
| Entregables de proyecto (3) | 15% | Semanas 4, 8, 12 | Producto de equipo, rúbrica publicada |
| Bitácora de uso de IA | 10% | Continua, revisada en cada cierre | Individual; se califica la calidad de la interrogación, no el uso |
| Participación en fases A y B | 5% | Continua | Presencia activa en las fases donde no hay entregable |
| **Total** | **100%** | | |

**Requisitos de acceso a examen:** 80% de asistencia y entrega del proyecto correspondiente.

### 5.3 Nota sobre el margen institucional

Este esquema es defendible ante cualquier revisión: hay tres evaluaciones periódicas escritas que suman 70%, y el 30% restante corresponde a ejercicios, laboratorio y trabajos, exactamente como dice el programa. La innovación está en el **contenido** de los exámenes, no en su ponderación, y el contenido es facultad del profesor.

---

## 6. Protocolo de uso de chatbots: el tutor universal interrogado

### 6.1 Las tres reglas

**Regla 1 — El oráculo llega tarde.** Prohibido en las fases activista y reflexiva de cada proyecto (semanas A y B). Obligatorio en las fases teórica y pragmática (semanas C y D). La prohibición no se vigila con detectores: las actividades de A y B ocurren en el aula, en papel, con evidencia física de campo que ningún chatbot puede fabricar.

**Regla 2 — Toda consulta se registra.** La bitácora (plantilla en `plantillas/bitacora-de-ia.md`) exige cuatro campos por consulta: qué pregunté, qué respondió, **qué verifiqué y contra qué fuente**, qué corregí o descarté. Se califica la calidad de la interrogación: una bitácora con tres preguntas afiladas y una refutación documentada vale más que una con veinte preguntas y ninguna verificación.

**Regla 3 — Caza del error.** En cada proyecto, una actividad obligatoria consiste en **hacer que el chatbot se equivoque y documentar el error**: pedirle un dato sobre la organización local que no puede saber, un cálculo que hará mal, una referencia bibliográfica que inventará. El estudiante entrega la evidencia y la explicación de por qué falló. Esta es la actividad que convierte la advertencia abstracta ("no confíes ciegamente") en experiencia propia.

### 6.2 Fundamento

La lectura *La Computadora 2.0* ya establece el marco: la IA no es herramienta pasiva sino ecosistema activo que aprende y decide, y la respuesta institucional al fraude académico no es la prohibición ni la detección, sino el **rediseño de la evaluación hacia lo no replicable**. Este protocolo operacionaliza esa tesis. El material `Holbeck_2025_beyond-detection.md` que ya tienes en el repositorio sostiene el mismo argumento y pasa a `docs/recursos/` como lectura de apoyo del protocolo.

Las tres competencias que la lectura propone —creatividad aumentada, gobernanza ética, innovación social— se convierten en los ejes transversales de los tres proyectos: P1 y P2 desarrollan la primera, la bitácora desarrolla la segunda, y la propuesta final a una organización real desarrolla la tercera.

---

## 7. El sitio de estudio

`mkdocs.yml` (incluido) configura MkDocs Material con:

- **Buscador de texto completo** en español, que resuelve el problema de encontrar un concepto entre veinte lecturas.
- **Navegación por proyecto y por semana**, de modo que el estudiante siempre sepa dónde está en el trimestre.
- **Modo oscuro y diseño responsivo**, porque el dispositivo real de lectura es el teléfono.
- **Despliegue automático** vía GitHub Action en cada push a `main`.
- **Botón de edición** en cada página, que enlaza al archivo en GitHub: un estudiante que detecta una errata puede proponer la corrección con un pull request. Es la manera menos artificiosa de enseñar control de versiones.

El repositorio sigue siendo perfectamente legible en GitHub para quien prefiera los archivos crudos. El sitio es una capa de presentación, no un formato propietario.

---

## 8. Secuencia de implementación

| Fase | Cuándo | Acción |
|---|---|---|
| 0 | Antes de iniciar | Ejecutar `migrar_repo.sh`, revisar el árbol resultante, hacer push con los tags |
| 1 | Semana -1 | Aplicar el LSQ y el diagnóstico de conocimientos previos; formar equipos (ver protocolo LSQ) |
| 2 | Semana 1 | Publicar el sitio; sesión de arranque con el protocolo de IA y P1 fase activista |
| 3 | Semanas 1-12 | Operación; una entrega por proyecto, no semanal (reduce carga de revisión de 10 a 3 ciclos) |
| 4 | Semana 13 | Cierre: retroalimentación, y **etiquetado del trimestre** (`git tag 26-O`) para que el repositorio conserve el estado exacto con que operó |

---

## 9. Qué queda abierto

1. **Confirmación de trimestre y tamaño de grupo**, para fijar fechas y número de equipos.
2. **El instrumento LSQ tiene restricción de derechos** (ver documento anexo sobre el protocolo): hay que decidir cómo aplicarlo legalmente.
3. **Selección de casos organizacionales** para P2: conviene tener una lista de respaldo para equipos que no consigan acceso a una organización.
4. **Renombrado fino de las veinte lecturas**: el script propone nombres, pero conviene que los revises uno por uno, porque son tu material.
5. Si quieres alinear el protocolo de IA con el marco conceptual de tu trabajo sobre el uso de IA generativa en la docencia, puedo reescribir la sección 6 sobre esa base en vez de sobre la formulación genérica.
