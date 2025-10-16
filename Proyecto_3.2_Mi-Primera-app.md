## **Proyecto 3.2: Mi Primera App**  
**Entrega:**  
- Partes 1 y 2: Semana 6  
- Parte 3 (IA): Semana 6  

### **Introducción**  
Programar no es solo escribir código: es resolver problemas reales con lógica, creatividad y herramientas adecuadas. Este proyecto te guiará desde el pseudocódigo hasta la implementación en R, y te invitará a reflexionar críticamente sobre el uso de la inteligencia artificial en el aprendizaje algorítmico.

---

### **Parte 1: Diseña tu idea (en pseudocódigo con PSeInt)**

**¿Qué harás?**  
Crearás un algoritmo útil en **PSeInt** que resuelva un problema real. Puedes usar uno de los ejercicios asignados por tu número de lista **o** proponer tu propio algoritmo (siempre que incluya estructuras secuenciales, condicionales e iterativas).

#### ✅ **Ejemplo concreto: “Calculadora de promedio ponderado”**

**Problema:**  
Un estudiante necesita calcular su promedio final considerando los créditos de cada materia (no todas valen lo mismo).

**Algoritmo en pseudocódigo (perfil UNAM FCA):**
```pseudocode
Algoritmo PromedioPonderado
    Definir n, i, creditos, totalCreditos, calif, suma Como Entero
    Definir promedio Como Real

    Escribir "¿Cuántas materias tienes?"
    Leer n

    totalCreditos = 0
    suma = 0

    Para i = 1 Hasta n Hacer
        Escribir "Materia ", i
        Escribir "Ingresa créditos:"
        Leer creditos
        Escribir "Ingresa calificación (0-100):"
        Leer calif

        // Validación básica
        Si calif < 0 O calif > 100 Entonces
            Escribir "Calificación inválida. Se usará 0."
            calif = 0
        FinSi

        suma = suma + (calif * creditos)
        totalCreditos = totalCreditos + creditos
    FinPara

    Si totalCreditos > 0 Entonces
        promedio = suma / totalCreditos
        Escribir "Tu promedio ponderado es: ", promedio
    Sino
        Escribir "No se ingresaron créditos válidos."
    FinSi
FinAlgoritmo
```

**Características del ejemplo:**
- Usa ciclo `Para`.
- Incluye validación de entrada.
- Calcula un valor real con sentido práctico.
- Termina de forma controlada.

**Entregable:**  
- Archivo: `15. PromedioPonderado.psc`  
- Diagrama de flujo (imagen PNG/JPG)  
- **Video tutorial** explicando el algoritmo como si lo presentaras en una feria escolar.

---

### **Parte 2: Dale vida en R**

**Pasos:**  
1. Crea una cuenta en **[Posit Cloud](https://posit.cloud)** y un proyecto llamado `MiAppAlgoritmica`.  
2. Traduce tu algoritmo a R.  
3. Documenta en un archivo **RMarkdown** (`MiAppAlgoritmica.Rmd`):  
   - Descripción del problema  
   - Pseudocódigo  
   - Código en R con explicación de equivalencias  
   - Captura de ejecución

#### ✅ **Ejemplo en R (equivalente al pseudocódigo anterior):**
```r
# Algoritmo_15.R
cat("¿Cuántas materias tienes?\n")
n <- as.integer(readline())

suma <- 0
total_creditos <- 0

for (i in 1:n) {
  cat("Materia", i, "\n")
  creditos <- as.integer(readline("Ingresa créditos: "))
  calif <- as.numeric(readline("Ingresa calificación (0-100): "))

  if (calif < 0 | calif > 100) {
    cat("Calificación inválida. Se usará 0.\n")
    calif <- 0
  }

  suma <- suma + (calif * creditos)
  total_creditos <- total_creditos + creditos
}

if (total_creditos > 0) {
  promedio <- suma / total_creditos
  cat("Tu promedio ponderado es:", round(promedio, 2), "\n")
} else {
  cat("No se ingresaron créditos válidos.\n")
}
```

**Entregable:**  
- Script: `Algoritmo_15.R`  
- Archivo: `MiAppAlgoritmica.Rmd`  
- **Video tutorial** mostrando la ejecución en Posit Cloud.

---

### **Parte 3: Programar con IA – ¿Aliado o atajo?**

**Actividad:**  
1. Pide a una IA (ChatGPT, Copilot, etc.):  
   > “Escribe un algoritmo en pseudocódigo estilo UNAM FCA que calcule el promedio ponderado considerando créditos y calificaciones.”  
2. Compara su propuesta con la tuya.  
3. Reflexiona en tu cuaderno:  
   - ¿La IA validó las entradas?  
   - ¿Usó buenas prácticas?  
   - ¿Entiendes todo lo que generó?  

**Entregable:**  
- **Video corto** (1–2 min) con tu análisis.  
- **Foto de tu reflexión escrita**.

---

### **Lista de problemas para principiantes**

A continuación, se presenta una **lista de problemas prácticos y accesibles para principiantes**, diseñados específicamente para el enfoque de este proyecto, que combina pseudocódigo, programación en R y reflexión crítica con IA. Estos problemas son:

- **Reales y cotidianos** (fáciles de entender y motivadores).  
- **Técnicamente adecuados** para estudiantes sin experiencia previa en programación.  
- **Escalables**: permiten incluir estructuras secuenciales, condicionales e iterativas.  
- **Compatibles** con los ejercicios del documento de Rodríguez (s.f.) y con el perfil “UNAM FCA” de PSeInt.

La lista de problemas es la siguiente:

1. **Calculadora de promedio simple o ponderado**  
   *Ingresar calificaciones y créditos, validar rangos, calcular promedio.*

2. **Conversor de unidades básicas**  
   *Ej.: Celsius ↔ Fahrenheit, kilómetros ↔ millas, pesos ↔ dólares (con tipo de cambio fijo).*

3. **Planificador de gastos semanales**  
   *Registrar ingresos y gastos diarios, mostrar saldo y alertar si se excede el presupuesto.*

4. **Generador de contraseñas seguras**  
   *Pedir longitud, incluir letras, números y símbolos; mostrar una contraseña aleatoria.*

5. **Juego de adivinación de números**  
   *La computadora elige un número entre 1 y 100; el usuario intenta adivinarlo con pistas (“muy alto”, “muy bajo”).*

6. **Calculadora de IMC (Índice de Masa Corporal)**  
   *Pedir peso y estatura, calcular IMC, mostrar categoría (bajo peso, normal, sobrepeso, etc.).*

7. **Contador de palabras o caracteres en un texto**  
   *El usuario escribe una frase; el programa cuenta palabras, letras o vocales.*

8. **Simulador de ahorro para una meta**  
   *Pedir meta (ej. $5000), ahorro mensual, mostrar cuántos meses se necesitan.*

9. **Menú interactivo de opciones**  
   *Mostrar un menú con 3–4 funciones (ej. calculadora, conversor, juego) y permitir elegir una.*

10. **Validador de correos electrónicos simples**  
    *Verificar si la entrada contiene “@” y “.”; dar retroalimentación básica (no requiere expresiones regulares).*

11. **Calculadora de descuento en compras**  
    *Ingresar precio y porcentaje de descuento; mostrar precio final.*

12. **Registro de hábitos diarios**  
    *Preguntar si realizó una actividad (ej. “¿Hiciste ejercicio hoy?”), contar días seguidos.*

13. **Conversor de tiempo (segundos ↔ horas:minutos:segundos)**  
    *Entrada en segundos → salida legible; o viceversa.*

14. **Calculadora de propina**  
    *Ingresar monto de la cuenta y porcentaje de propina; mostrar total a pagar.*

15. **Clasificador de triángulos**  
    *Ingresar tres lados; determinar si es equilátero, isósceles o escaleno (y si es válido).*

### **Recomendaciones para el estudiante:**

- Elige un problema que te interese o que resuelva algo de tu vida diaria.  
- Si ya tienes asignados ejercicios por número de lista, puedes usar uno de ellos **o** proponer uno de esta lista (previa validación con tu profesor).  
- Asegúrate de incluir:  
  - **Entrada de datos**  
  - **Validación básica** (evitar valores negativos, fuera de rango, etc.)  
  - **Al menos un ciclo** (`Mientras`, `Repetir` o `Para`)  
  - **Al menos una condición** (`Si...Entonces...Sino`)  
  - **Salida clara y amigable**

Estos problemas preparan al estudiante no solo para dominar la lógica algorítmica, sino también para pensar como creador de soluciones digitales reales.

---

### **¿Por qué este proyecto es más interesante?**

- **Relevancia personal**: resuelves problemas reales (estudio, finanzas, salud).  
- **Creatividad**: eliges o diseñas tu app.  
- **Conexión con la realidad**: usas herramientas profesionales (PSeInt, R, Posit Cloud, IA).  
- **Pensamiento crítico**: evalúas el papel de la IA sin depender de ella.

---

### **Conclusión**  
Al finalizar este proyecto, no solo habrás creado una aplicación funcional, sino que también habrás desarrollado una comprensión profunda de los fundamentos de la programación y una postura crítica frente al uso de tecnologías emergentes. Estas habilidades son esenciales para navegar con responsabilidad y eficacia en un mundo cada vez más digital.

Este enfoque transforma la programación en una **experiencia significativa**, donde tú como estudiante no solo aprendes sintaxis, sino que **creas soluciones con propósito** y desarrollas una postura crítica frente a las nuevas tecnologías.
