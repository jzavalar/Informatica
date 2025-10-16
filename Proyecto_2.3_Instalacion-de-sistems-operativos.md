## **Proyecto 2.3: Instalación de sistemas operativos**  
**Prof. Dr. Jesús Zavala Ruiz**  
**Octubre de 2025**

- **Entrega parcial (Partes 1–3):** Semana 3  
- **Entrega final (Partes 1–4):** Semana 4  

---

### **Parte 1: Conceptos – Sistemas operativos**

#### **Objetivo**  
Comprender qué es un sistema operativo y comparar cuatro ejemplos comunes: **Windows, Linux, macOS y Android**, analizando sus características técnicas y de uso.

#### **Actividades**  
1. Investigue los siguientes conceptos:
   - ¿Qué es un sistema operativo?
   - ¿Cuáles son sus funciones principales?
   - Tipos de sistemas operativos (por ejemplo: monousuario/multiusuario, monoproceso/multiproceso, en tiempo real, etc.).

2. Compare los cuatro sistemas operativos en los siguientes aspectos:
   - Ventajas y desventajas
   - Nivel de seguridad
   - Facilidad de uso (interfaz, curva de aprendizaje)
   - Robustez (estabilidad y tolerancia a fallos)

3. Use fuentes confiables, como:
   - La **playlist de la UNAM Sepacomputo** en YouTube (3 videos cortos).
   - Wikipedia (en español o inglés).
   - Sitios oficiales: Microsoft, Apple, Fedora, etc.
   - Libros o artículos académicos, si están disponibles.

4. Registre sus notas en su **cuaderno físico o digital**, incluyendo:
   - Un resumen claro de los conceptos.
   - Una **tabla comparativa** (puede ser dibujada a mano o creada en Word/Google Docs).
   - **Citas completas** con autor, fecha, título y enlace (si aplica).

#### **Entregable 1: Video tutorial**  
- **Duración:** 3 a 5 minutos.  
- **Contenido:** Explique con sus propias palabras lo que investigó. **No lea** su cuaderno. Use ejemplos, señale en una pizarra, muestre imágenes o esquemas si le ayudan a explicar.  
- **Idioma:** Español claro, con pronunciación comprensible y vocabulario técnico apropiado.  
- **Entrega:** Suba el video al **grupo de Telegram** asignado.

> **Consejo:** Practique antes de grabar. Use un fondo limpio, buena iluminación y evite ruidos de fondo.

---

### **Parte 2: Crear una Live USB con Balena Etcher**

#### **Objetivo**  
Crear una **Live USB** (unidad USB de arranque) usando **Balena Etcher** en Windows, para probar sistemas operativos sin instalarlos en la computadora.

#### **Materiales necesarios**  
- Una **memoria USB de al menos 8 GiB**, sin archivos importantes (se borrará su contenido).
- Una computadora con **Windows 10 o 11**.
- Archivos **ISO** de al menos **dos** de los siguientes sistemas operativos:
  - **Fedora Workstation 43**
  - **Zorin OS 18** (edición Core, gratuita)
  - **Windows 11** (versión de evaluación oficial de Microsoft)  
    *(Nota: Windows 7 ya no se distribuye oficialmente. Si se usa, debe ser con fines educativos y en entornos aislados, por ejemplo desde Archive.org).*

#### **Pasos a seguir**  

1. **Investigue los conceptos básicos**:
   - ¿Qué es una **Live USB**? ([Wikipedia: Live USB](https://es.wikipedia.org/wiki/Live_USB))
   - ¿Qué es una **imagen ISO**? ([Wikipedia: Imagen ISO](https://es.wikipedia.org/wiki/Imagen_ISO))

2. **Descargue e instale Balena Etcher**:
   - Sitio oficial: [https://www.balena.io/etcher/](https://www.balena.io/etcher/)
   - Ejecute el instalador y siga las instrucciones.

3. **Obtenga las imágenes ISO**:
   - **Fedora 43**: [https://getfedora.org/es/workstation/](https://getfedora.org/es/workstation/)  
     *(Si Fedora 43 aún no está disponible, use la versión más reciente y anótelo en su video).*
   - **Zorin OS 18**: [https://zorin.com/os/](https://zorin.com/os/) → Descargue la edición **Core** (gratuita).
   - **Windows 11 (evaluación)**: [https://www.microsoft.com/software-download/windows11](https://www.microsoft.com/software-download/windows11)

4. **Cree la Live USB**:
   - **Importante**: Balena Etcher **solo permite grabar una ISO por USB**.  
     → Si quiere probar dos sistemas, necesitará **dos memorias USB distintas** o regrabar la misma dos veces.
   - Procedimiento:
     1. Conecte la USB.
     2. Abra Balena Etcher.
     3. Haga clic en **“Flash from file”** y seleccione su archivo ISO.
     4. Haga clic en **“Select target”** y elija la USB.
     5. Haga clic en **“Flash!”** y espere a que termine (la USB se formateará).

#### **Entregable 2: Video tutorial**  
- Muestre claramente:
  - Cómo instaló Balena Etcher.
  - Cómo descargó al menos una ISO (Fedora 43 o Zorin OS 18 preferentemente).
  - El proceso completo de grabado en la USB.
  - Una breve explicación de por qué Etcher es seguro y fácil de usar.
- Suba el video al **grupo de Telegram**.

---

### **Parte 3: Arranque desde la Live USB**

#### **Objetivo**  
Arrancar su computadora desde la Live USB y probar al menos **un sistema operativo en modo Live** (sin instalarlo).

#### **Actividades**  

1. **Investigue los siguientes conceptos**:
   - ¿Qué significa **“arrancar” o “bootear”** una computadora?
   - Diferencias entre **BIOS y UEFI**.
   - ¿Qué son los esquemas de particionado **MBR y GPT**?
   - Cómo acceder al menú de arranque según la marca de su computadora (por ejemplo, **F12 en Lenovo**, **ESC en HP**, **F2 en Dell**, etc.).

2. **Identifique el tipo de firmware de su computadora**:
   - En Windows, abra **Ejecutar** (`Win + R`), escriba `msinfo32` y busque la línea **“Modo BIOS”**:
     - Si dice **“Legacy”**, su sistema usa **BIOS + MBR**.
     - Si dice **“UEFI”**, usa **UEFI + GPT**.

3. **Arranque desde la USB**:
   - Reinicie la computadora.
   - Presione la tecla de arranque (F2, F12, ESC, DEL, etc.) **inmediatamente al encender**.
   - En el menú de arranque, seleccione su **USB**.
   - En el sistema operativo (Fedora o Zorin OS), elija la opción **“Probar sin instalar”**.
   - Verifique que el escritorio se carga correctamente.

> **Nota**: Windows 7 **no tiene modo Live**; solo muestra el instalador. Por eso se recomienda usar Fedora o Zorin OS para esta parte.

#### **Entregable 3: Video tutorial**  
- Grabe el proceso completo:
  - Cómo accede al menú de arranque.
  - Cómo selecciona la USB.
  - Cómo se carga el escritorio de **Fedora 43** o **Zorin OS 18** en modo Live.
  - Una breve explicación de los conceptos de BIOS/UEFI y MBR/GPT.
- Suba el video al **grupo de Telegram**.

---

### **Parte 4: Virtualización con VirtualBox**

#### **Objetivo**  
Instalar y ejecutar sistemas operativos en **máquinas virtuales** usando **VirtualBox**, como alternativa segura al arranque físico.

#### **Pasos a seguir**  

1. **Instale VirtualBox**:
   - Descargue desde: [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
   - Instale el programa principal **y** el **Extension Pack** (mismo enlace).

2. **Cree dos máquinas virtuales**:
   - **Máquina 1: Fedora 43 o Zorin OS 18**
     - RAM: 2–4 GB  
     - Disco duro: 20–25 GB  
     - En “Almacenamiento”, monte la ISO descargada.  
     - Inicie en **modo Live** (no es necesario instalar).
   - **Máquina 2: Windows 11 (evaluación) o Windows 7**
     - RAM: 2 GB  
     - Disco duro: 25 GB  
     - Monte la ISO y muestre la pantalla del instalador.

3. **Verifique que ambas máquinas inicien correctamente**.

#### **Entregable 4: Video tutorial**  
- Muestre:
  - La instalación de VirtualBox y el Extension Pack.
  - La creación y configuración de las dos máquinas virtuales.
  - El arranque exitoso de ambos sistemas operativos.
  - Una breve comparación entre **Live USB** y **máquina virtual** (ventajas y desventajas).
- Suba el video al **grupo de Telegram**.

---

### **Notas importantes para los estudiantes**

- **Balena Etcher no permite multiarranque**. Cada USB solo puede contener **una ISO**.
- **Zorin OS 18** es una distribución de Linux basada en Ubuntu, con interfaz similar a Windows, ideal para principiantes.
- **Windows 7 no tiene modo Live**. Solo se puede mostrar el instalador. Por eso, para las pruebas de escritorio funcional, use **Fedora** o **Zorin OS**.
- Si **Fedora 43** no está disponible al momento de realizar la práctica, use **Fedora 42** o **Zorin OS 18**, y **menciónelo claramente en su video**.
- Todos los videos deben ser **explicativos**, no lecturas. Use sus propias palabras, ejemplos y demostraciones visuales.

---

Este formato mejora la **legibilidad**, elimina ambigüedades, organiza la información por bloques lógicos y refuerza las instrucciones clave para evitar errores comunes.
