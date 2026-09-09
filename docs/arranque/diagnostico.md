# Diagnóstico de conocimientos previos

**Destino:** `docs/arranque/diagnostico.md`
**Aplicación:** en línea, del 17 al 20 de septiembre de 2026, junto con el CHAEA
**Duración:** 15 minutos · **No se califica**

---

## 1. Para qué sirve y para qué no

Este instrumento **no evalúa al estudiante**: mide qué tan lejos está el punto de partida real del grupo respecto del que el programa supone. Sirve para tres decisiones concretas del profesor:

1. **Calibrar la sesión 2.** Si el 70% del grupo no distingue archivo de carpeta, el proyecto 1 arranca por ahí y no por la arquitectura de la máquina.
2. **Repartir a los estudiantes en los equipos.** Cruzado con el perfil CHAEA, evita que un equipo concentre a los cinco con más lagunas.
3. **Identificar riesgo de deserción antes de la primera clase.** El cuartil inferior entra al registro de seguimiento desde la sesión 1.

**Se le dice al estudiante, textualmente:** *No es un examen, no vale puntos y nadie va a ver tu resultado más que el profesor. Contesta lo que realmente sabes: si adivinas, el curso se va a diseñar para un grupo que no existe y te va a ir peor.*

Se aplica de nuevo, idéntico, en la última sesión. La diferencia entre ambas aplicaciones es la medida más limpia que vas a tener de lo que el método produjo.

---

## 2. Sección A · Perfil de recursos (5 preguntas, no puntuables)

Determinan qué es viable pedir fuera del aula. Sin esto, el diseño de tareas se hace a ciegas.

1. ¿Tienes computadora propia en casa? (Sí, de uso exclusivo / Sí, compartida / No)
2. ¿Tienes internet en casa? (Sí, estable / Sí, intermitente / Solo datos del celular / No)
3. ¿Qué usas más para trabajos escolares? (Computadora / Celular / Ambos por igual)
4. ¿Has usado alguna vez un chatbot como ChatGPT, Gemini, Copilot o Claude? (Nunca / Una o dos veces / A veces / Casi diario)
5. Si lo has usado, ¿para qué? (Marca todas: buscar información / hacer tareas completas / entender algo que no entendía / redactar / traducir / otra)

> **Lo que va a revelar la pregunta 5:** la mayoría marcará "hacer tareas completas". Ese dato, presentado al grupo de forma anónima y agregada en la sesión 1, es la mejor introducción posible al protocolo de IA. No hace falta sermón: se les muestra su propio dato.

---

## 3. Sección B · Alfabetización digital operativa (8 reactivos, 1 punto cada uno)

Lo que el programa supone que ya traen. Reactivos de opción múltiple, redactados sin jerga.

1. Un archivo se llama `informe_final.docx`. ¿Qué indica la parte que va después del punto?
2. Guardas un archivo y luego no lo encuentras. ¿Cuál de estas acciones tiene más probabilidad de localizarlo? (buscar por nombre en el buscador del sistema / reiniciar / volver a crearlo / preguntar a un compañero)
3. ¿Cuál de estos pesa más? (una foto de tu celular / un documento de dos páginas de texto / un mensaje de WhatsApp de veinte palabras)
4. Copias un archivo de una carpeta a otra. ¿Cuántas copias existen ahora?
5. ¿Qué significa que un documento esté "en la nube"?
6. Recibes un correo de un banco pidiendo tu contraseña por respuesta. ¿Qué haces?
7. En una hoja de cálculo, ¿qué distingue una celda de una columna?
8. Si en una hoja de cálculo escribes `=A1+A2` en la celda A3, ¿qué aparece en A3?

---

## 4. Sección C · Razonamiento con datos (6 reactivos, 1 punto cada uno)

Lo que las unidades 3 y 4 del programa van a exigir. No requiere ningún conocimiento de computación.

9. Una tienda vendió 40 lápices el lunes, 25 el martes y 55 el miércoles. ¿Cuántos vendió en promedio por día?
10. En esa misma tienda, ¿qué dato **falta** para saber si el miércoles fue un buen día? (elige uno y explica en una línea)
11. Una lista tiene los nombres: "Juan Pérez", "juan perez", "J. Pérez". ¿Cuántas personas distintas hay? ¿Qué necesitarías para estar seguro?
12. Un precio sube de $80 a $100. ¿Qué porcentaje subió?
13. Ordena estos pasos para preparar café, del primero al último: [se dan seis pasos desordenados, dos de ellos intercambiables]
14. Escribe, en tus palabras, las instrucciones para que alguien que nunca lo ha hecho saque el dinero de un cajero automático. Debe poder seguirlas sin preguntarte nada.

> El reactivo 14 es el más informativo de todo el instrumento. No mide conocimiento: mide **capacidad de descomponer un procedimiento en pasos explícitos**, que es exactamente la habilidad que el pseudocódigo va a formalizar en P2. Una respuesta que dice "metes la tarjeta y sacas el dinero" y una que enumera ocho pasos con la validación del NIP están a mundos de distancia, y esa distancia predice el desempeño en la unidad 3 mejor que cualquier otra pregunta.

---

## 5. Sección D · Comprensión lectora y expresión (1 reactivo, 3 puntos)

Evalúa directamente el segundo objetivo específico del programa oficial.

15. Se presenta un párrafo de ocho líneas tomado de la lectura *La Computadora 2.0*. Tres preguntas:
    - ¿Cuál es la idea principal? (1 pt)
    - Menciona un dato concreto que el texto usa para sostenerla (1 pt)
    - ¿Estás de acuerdo? Responde en dos o tres líneas justificando. (1 pt)

Se califica claridad y corrección, no la postura.

---

## 6. Puntuación e interpretación

**Máximo: 17 puntos** (8 de la sección B + 6 de la C + 3 de la D).

| Rango | Nivel | Qué implica para el diseño |
|---|---|---|
| 0 – 6 | **Punto de partida elemental** | El curso debe construir los anclajes desde cero. Este estudiante necesita la sesión 2 más que nadie, y necesita seguimiento activo desde la primera semana |
| 7 – 10 | **Punto de partida funcional** | Opera herramientas pero sin modelo mental de qué hacen. Es el perfil modal esperado |
| 11 – 14 | **Punto de partida sólido** | Puede tomar roles de arquitecto o verificador desde P1 |
| 15 – 17 | **Punto de partida avanzado** | Candidato a repartirse entre equipos distintos, no a concentrarse. Riesgo propio: aburrimiento en las fases elementales; se le compensa con el rol de verificador, que es el más exigente |

**Ninguno de estos rangos se le comunica al estudiante como etiqueta.** Lo que recibe es una frase de la forma *"tu punto de partida en X está sólido y en Y hay que trabajar"*, más una recomendación concreta de qué leer antes de la sesión 2.

---

## 7. Uso en la formación de equipos

Cruzando diagnóstico y CHAEA, la regla de reparto en los cinco equipos es:

1. **Ningún equipo con más de un estudiante en el rango 0–6.** Concentrar las lagunas garantiza que ese equipo no despegue.
2. **Al menos un estudiante del rango 11 o superior por equipo**, que naturalmente ocupará arquitecto o verificador en P1.
3. Después de esas dos restricciones, se aplica el reparto por estilo CHAEA descrito en `estilos-chaea.md`.

Cuando ambos criterios entran en conflicto —y van a entrar—, **manda el diagnóstico**. Un equipo desequilibrado en estilos funciona con esfuerzo; un equipo donde nadie entiende el punto de partida no funciona.

---

## 8. Aplicación en línea

El instrumento cabe en un formulario web gratuito de veinte reactivos. Recomendaciones operativas:

- **Un reactivo por pantalla** en la sección B y C: reduce el abandono a la mitad respecto de la lista larga.
- **Los reactivos 14 y 15 en campo de texto abierto**, sin límite de caracteres. Son los que hay que leer uno por uno; los otros trece se autocalifican.
- **Exportación a hoja de cálculo** para volcar los resultados en la hoja `Alumnos` del libro de seguimiento.
- **Correo de recordatorio el sábado 19** a quienes no hayan respondido. La lista de no respondientes es el primer registro de riesgo del trimestre.
