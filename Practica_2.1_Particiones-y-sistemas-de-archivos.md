## **Guía paso a paso – Práctica 2.1: Particiones y sistemas de archivos**

### **Objetivo general**  
Aprender a identificar, gestionar y recuperar particiones y sistemas de archivos en dispositivos de almacenamiento.

---

### **Parte 1: Investigación y análisis del sistema propio**

#### **Paso 1. Estudie los conceptos clave**  
Consulte los videos y fuentes indicadas para comprender:
- Partición (primaria, extendida, lógica, de arranque)
- Esquemas de particionado: **MBR** y **GPT**
- Qué es un **sistema de archivos** (NTFS, FAT32, exFAT, ext4, etc.)
- Qué es un **archivo** y sus tipos: texto, binario, ejecutable
- Cómo se almacena un archivo en disco
- Operaciones básicas: crear, copiar, mover, renombrar, eliminar

Anote definiciones claras en su **cuaderno físico o digital**, con ejemplos y citas de las fuentes.

#### **Paso 2. Analice su computadora**
1. **Identifique las unidades de almacenamiento**:
   - Abra **Administración de discos** (`diskmgmt.msc`) o use **PowerShell**:
     ```powershell
     Get-Disk
     ```
2. **Determine el esquema de particionado** (MBR o GPT):
   - En **Administración de discos**, haga clic derecho en el disco → **Propiedades** → pestaña **Volúmenes**.
   - O en PowerShell:
     ```powershell
     Get-Disk | Select-Object Number, PartitionStyle
     ```
3. **Liste las particiones y sus sistemas de archivos**:
   - En **Explorador de archivos**, observe las unidades (C:, D:, etc.).
   - En PowerShell:
     ```powershell
     Get-Volume | Select-Object DriveLetter, FileSystem, Size, FileSystemLabel
     ```

#### **Paso 3. Explore tipos de archivos en carpetas clave**
Navegue en:
- `Documentos`
- `Descargas`
- `Música`
- `Videos`
- `C:\Windows\System32`

Para cada carpeta, anote en su cuaderno:
- Extensiones comunes (`.txt`, `.pdf`, `.exe`, `.dll`, `.mp3`, `.mp4`, etc.)
- Tipo de archivo (texto, binario, programa)
- Tamaño aproximado y propósito

> En `System32`, encontrará principalmente archivos **binarios** y **ejecutables del sistema** (`.exe`, `.dll`, `.sys`).

#### **Entregable 1**
- **Video tutorial** (3–5 min): muestre en pantalla las herramientas usadas (`diskmgmt.msc`, PowerShell, Explorador) y explique lo que hace.
- **Fotografías del cuaderno** con sus apuntes.
- Suba ambos al **grupo de Telegram**.
- Asegúrese de usar **español claro y técnico**.

---

### **Parte 2: Gestión de particiones en una USB**

#### **Materiales necesarios**
- **USB de al menos 8 GiB**, sin datos importantes (se borrará todo).

#### **Paso 4. Practique con Administración de discos**
1. Conecte la USB.
2. Abra **Administración de discos** (`diskmgmt.msc`).
3. **Elimine todas las particiones** existentes en la USB (haga clic derecho → *Eliminar volumen*).
4. **Cree una nueva partición**:
   - Haga clic derecho en el espacio sin asignar → *Nuevo volumen simple*.
   - Asigne todo el espacio.
   - Formatee con **FAT32** → nombre: “FAT32”.
5. **Repita el proceso tres veces más**, creando particiones (una a la vez) con:
   - **FAT**
   - **exFAT**
   - **NTFS** (nombre: “NTFS”)

> Nota: Windows no permite crear particiones FAT en discos grandes desde la GUI. Si no aparece la opción, omita FAT y use solo FAT32, exFAT y NTFS.

6. **En la partición NTFS**:
   - Copie dos archivos (por ejemplo, un `.txt` y un `.jpg`).
   - Luego, **elimine la partición NTFS** (haga clic derecho → *Eliminar volumen*).

7. **Reflexione en su cuaderno**:
   - ¿Qué diferencias observó entre los sistemas de archivos?
   - ¿Qué límites tiene cada uno? (ej. FAT32 no permite archivos >4 GB)
   - ¿Qué sistema es más adecuado para qué uso?

#### **Entregable 2**
- **Video tutorial**: muestre todo el proceso en pantalla, explicando cada acción.
- **Fotos del cuaderno** con sus conclusiones.
- Suba al **grupo de Telegram** con transcripción en español.

---

### **Parte 3: Recuperación de partición y archivos con TestDisk**

#### **Paso 5. Instale y use TestDisk**
1. Descargue **TestDisk** desde: [https://www.cgsecurity.org/wiki/TestDisk_ES](https://www.cgsecurity.org/wiki/TestDisk_ES)
2. Extraiga el archivo ZIP y ejecute **testdisk_win.exe** como administrador.
3. Siga estos pasos:
   - Seleccione su **USB** (¡no el disco duro!).
   - Elija **Intel** (para MBR) o **EFI GPT** si aplica.
   - Seleccione **Analyse** → **Quick Search**.
   - TestDisk mostrará particiones borradas. Si encuentra la NTFS, selecciónela y presione **P** para ver archivos.
   - Para recuperar la partición: seleccione **Write**.
   - Para recuperar solo archivos: use **PhotoRec** (incluido en la misma carpeta).

> Si la partición no aparece, intente **Deep Search**.

4. Verifique que los archivos copiados en la Parte 2 se pueden recuperar.

#### **Entregable 3**
- **Video tutorial**: muestre el uso de TestDisk, la detección de la partición perdida y la recuperación.
- **Fotos del cuaderno** con observaciones (¿se recuperó todo? ¿qué falló?).
- Suba al **grupo de Telegram** con transcripción en español.

