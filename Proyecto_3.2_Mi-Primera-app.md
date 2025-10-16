## **Proyecto 3.2: Mi Primera App Algorítmica**  
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

### **¿Por qué este proyecto es más interesante?**

- **Relevancia personal**: resuelves problemas reales (estudio, finanzas, salud).  
- **Creatividad**: eliges o diseñas tu app.  
- **Conexión con la realidad**: usas herramientas profesionales (PSeInt, R, Posit Cloud, IA).  
- **Pensamiento crítico**: evalúas el papel de la IA sin depender de ella.

---

### **Conclusión**  
Al finalizar este proyecto, no solo habrás creado una aplicación funcional, sino que también habrás desarrollado una comprensión profunda de los fundamentos de la programación y una postura crítica frente al uso de tecnologías emergentes. Estas habilidades son esenciales para navegar con responsabilidad y eficacia en un mundo cada vez más digital.

Este enfoque transforma la programación en una **experiencia significativa**, donde tú como estudiante no solo aprendes sintaxis, sino que **creas soluciones con propósito** y desarrollas una postura crítica frente a las nuevas tecnologías.
