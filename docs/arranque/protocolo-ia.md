# Protocolo de uso de IA y el laboratorio simulado

**Destino:** `docs/arranque/protocolo-ia.md`
**Se presenta en:** sesión 2 (miércoles 23 de septiembre de 2026)

---

## 1. El problema que este protocolo resuelve

Tú ya usas chatbots. Todos los usan. La pregunta de este curso no es si los vas a usar, sino **si vas a salir sabiendo más o sabiendo menos por haberlos usado**.

Un chatbot puede escribir tu tarea. Si lo hace, la tarea queda hecha y tú quedas igual que antes. El problema no es ético en primera instancia: es que estás pagando una carrera para adquirir una capacidad, y delegar el ejercicio que la construye equivale a pagar un gimnasio para que alguien más levante las pesas.

Al mismo tiempo, prohibirlos sería una tontería. En tu vida profesional vas a trabajar con estas herramientas todos los días, y **saber interrogarlas es una competencia administrativa real**. Este curso te va a enseñar a hacerlo bien, que es lo contrario de usarlas para no pensar.

---

## 2. Las tres reglas

### Regla 1 — El oráculo llega tarde

| Sesión del proyecto | Fase | IA |
|---|---|---|
| 1 | Activista | 🚫 **Prohibida** |
| 2 | Reflexiva | 🚫 **Prohibida** |
| 3 | Teórica | ✅ Obligatoria, con bitácora |
| 4 | Teórica→Pragmática | ✅ Obligatoria, con bitácora |
| 5 | Pragmática (entrega y examen) | 🚫 **Prohibida** |

**Por qué.** Si la herramienta que produce la respuesta está disponible antes de que formules la pregunta, no habrá pregunta. Retrasar el acceso no es moralismo: es preservar la condición que hace posible aprender algo.

**Cómo se sostiene sin vigilancia.** No hay detectores ni software de plagio. No hacen falta: las sesiones 1 y 2 ocurren en el aula, en papel, sobre evidencia física que recogiste tú. Ningún chatbot estuvo en el laboratorio contigo ni entrevistó a la dueña de la papelería. La entrega de esas sesiones es tu cuaderno fotografiado, y un cuaderno con observaciones genéricas se distingue de uno con observaciones reales sin necesidad de ninguna herramienta.

### Regla 2 — Toda consulta se registra

Cada consulta a un chatbot en las sesiones 3 y 4 se anota en la **bitácora de IA**, con cuatro campos:

| Campo | Qué va aquí |
|---|---|
| **Qué pregunté** | La pregunta textual, no un resumen |
| **Qué respondió** | Lo esencial de la respuesta, en tus palabras |
| **Qué verifiqué y contra qué** | La lectura, el dato de campo, el cálculo manual que usaste para comprobar |
| **Qué corregí, descarté o añadí** | Lo que la respuesta no traía y tú pusiste |

**Se califica la calidad de la interrogación, no la cantidad de uso.** Una bitácora con tres preguntas afiladas y una refutación documentada vale más que una con veinte preguntas y ninguna verificación. Una bitácora donde el tercer campo dice siempre "nada" es una bitácora reprobada, porque documenta que delegaste.

Vale 10% de la calificación final.

### Regla 3 — Caza del error

En cada proyecto, una actividad obligatoria consiste en **hacer que el chatbot se equivoque y documentar el error**. No es un juego: es la única forma de que la advertencia deje de ser abstracta.

Tres tipos de error que puedes provocar, uno por proyecto:

| Proyecto | Tipo de error a cazar | Cómo |
|---|---|---|
| **P1** | Error factual sobre algo local | Pregúntale por las características del modelo exacto de la máquina que tienes enfrente, o por el precio actual de un componente en el mercado mexicano |
| **P2** | Error de cálculo o de lógica | Dale un cálculo administrativo con un caso frontera —un descuento sobre un total negativo, un inventario en cero— y verifica a mano |
| **P3** | Referencia inventada | Pídele bibliografía académica específica sobre un tema estrecho y verifica que cada referencia exista realmente |

Entregas la evidencia (captura o transcripción) y **la explicación de por qué falló**. Esa explicación es lo que se califica: no basta con mostrar el error, hay que entender qué tipo de pregunta lo produce.

---

## 3. El laboratorio simulado

Este curso tiene un problema material: **no podemos instalar software** en las máquinas del laboratorio. No hay gestor de bases de datos, no hay entorno de programación, no hay permisos de administrador.

En lugar de lamentarlo, lo convertimos en el mecanismo central del curso. **El chatbot va a hacer de máquina que no tenemos.**

### 3.1 Cómo funciona

Le pides al chatbot que se comporte como un sistema, no como un asesor. La diferencia es fundamental:

| Uso pobre | Uso de laboratorio simulado |
|---|---|
| "Explícame qué es una consulta SQL" | "Actúa como un motor de base de datos. Estas son mis tres tablas con estos datos. Ejecuta esta consulta y devuélveme **solo** el resultado, sin explicaciones" |
| "¿Cómo calculo el punto de reorden?" | "Actúa como una computadora ejecutando este pseudocódigo paso a paso. Muéstrame el valor de cada variable después de cada instrucción, sin corregir mi código" |
| "Hazme un diagrama entidad-relación" | "Estas son mis entidades y relaciones. Actúa como validador: dime qué anomalías de integridad referencial tendría este diseño, sin proponerme uno nuevo" |

La instrucción crítica en los tres casos es **"sin explicaciones", "sin corregir", "sin proponer"**. Le estás pidiendo que ejecute, no que enseñe. Un simulador que además te da la respuesta correcta no simula nada.

### 3.2 La regla que hace que esto funcione

> **Nada se simula antes de haberse resuelto en papel.**

El orden es siempre el mismo, y es inviolable:

1. **Diseñas en papel** el modelo, el algoritmo, la consulta.
2. **Calculas a mano** el resultado esperado, al menos para un caso.
3. **Simulas con el chatbot** y obtienes su resultado.
4. **Comparas.** Si coinciden, tu diseño probablemente está bien. Si no coinciden, uno de los dos se equivocó —y averiguar cuál es el ejercicio.

El paso 4 es donde ocurre el aprendizaje. Un estudiante que solo hace el paso 3 no aprendió nada y no puede detectar cuando la simulación está mal, que ocurre con frecuencia. Un estudiante que hizo los cuatro pasos **tiene criterio**, que es exactamente lo que un administrador necesita frente a cualquier sistema informático que no diseñó.

### 3.3 Por qué esto es mejor que tener el software instalado

Cuando ejecutas una consulta en un gestor real, el resultado es correcto y no aprendes nada del proceso. Cuando la ejecutas en un simulador falible **estás obligado a saber cuál debería ser el resultado**, porque eres tú quien lo audita.

La limitación del laboratorio te fuerza a la posición que vas a ocupar profesionalmente: la de quien tiene que juzgar si lo que el sistema le devuelve tiene sentido, sin poder abrir el sistema.

### 3.4 Advertencia obligatoria

Un chatbot simulando un motor de base de datos **se equivoca**, especialmente con tablas grandes, con valores nulos y con casos frontera. Esto no es un defecto del ejercicio: es el ejercicio. La simulación es una herramienta de aprendizaje, no una fuente de resultados confiables. Nunca uses una simulación como si fuera un cálculo verificado.

---

## 4. Qué está prohibido, sin ambigüedad

| Prohibido | Por qué |
|---|---|
| Usar IA en las sesiones 1, 2 y 5 de cualquier proyecto | Destruye el propósito de esas fases |
| Entregar texto generado y presentarlo como propio | Es fraude académico y está sujeto al reglamento de la UAM |
| Usar IA durante los exámenes | Son individuales, en papel, sin dispositivos |
| Omitir consultas en la bitácora | La bitácora incompleta se califica como no entregada |
| Usar la simulación sin haber resuelto en papel primero | Invalida el ejercicio completo |

**Y algo que no está prohibido y conviene decir en voz alta:** pedirle al chatbot que te explique diez veces lo mismo hasta entenderlo, que te ponga ejercicios, que te corrija la redacción de un párrafo tuyo, que te haga preguntas para ver si entendiste. Eso es usarlo como tutor, y es exactamente lo que este curso quiere que aprendas a hacer. Un tutor universal, disponible a las tres de la mañana, que no se cansa de repetir, es un recurso extraordinario para un estudiante con lagunas. **Lo que no puede hacer es aprender en tu lugar.**

---

## 5. Lectura obligatoria de apoyo

- Zavala Ruiz, J. (2025). *La Computadora 2.0: la revolución de la inteligencia artificial*. → `docs/lecturas/03-la-computadora-2-0.md`
- Holbeck (2025). Más allá de la detección. → `docs/recursos/holbeck-2025-mas-alla-de-la-deteccion.md`
