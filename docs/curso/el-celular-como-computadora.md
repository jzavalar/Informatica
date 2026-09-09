# El celular como computadora y como objeto de conocimiento

**Destino:** `docs/curso/el-celular-como-computadora.md`

---

## 1. El giro

Todo el diseño anterior daba vueltas alrededor de una restricción: *no se puede instalar software*. Eso es cierto de las máquinas del laboratorio, y falso del dispositivo que cada estudiante trae en el bolsillo.

**El celular es la única computadora que todos tienen y en la que sí se puede instalar software.** Es más potente que las máquinas del laboratorio, está siempre encendida, es personal, y —esto es lo decisivo— **es completamente opaca para su dueño**.

Ahí está la segunda mitad del giro. El celular no es solo el instrumento del curso: es su **objeto de conocimiento**. Los estudiantes son expertos en manejar aplicaciones y no tienen la menor idea de qué hay debajo. Su funcionamiento sigue siendo un misterio magnificado y oculto tras aplicaciones "sofisticadas". Abrir esa caja negra es, literalmente, el objetivo de la UEA.

Y tiene una consecuencia de equidad que ningún otro recurso ofrece: **el que menos tiene es dueño del laboratorio**. No hay que pedir permiso, no hay que compartir, no hay que llegar temprano al laboratorio, no hay licencia que pagar.

---

## 2. Qué cambia en cada proyecto

### P1 · La máquina desnuda

**Antes:** examinar una máquina vieja del laboratorio.
**Ahora:** examinar **su propio teléfono** y compararlo contra la máquina del laboratorio.

La comparación es el hallazgo. Casi todos van a descubrir que el teléfono de mil pesos que traen en la bolsa tiene más memoria y más núcleos que la computadora de escritorio de la universidad. La pregunta "¿por qué entonces la del laboratorio hace cosas que el teléfono no?" abre sola el tema de arquitectura, sistema operativo y propósito de diseño.

Se agregan al expediente técnico:

- Inventario de hardware del propio teléfono, leído con una app de información de sistema.
- Comparación de especificaciones entre los cinco teléfonos del equipo y la máquina del laboratorio.
- Exploración del sistema de archivos real con un gestor de archivos: **descubrir que su teléfono tiene carpetas** es, para muchos, la primera grieta en la caja negra.
- Medición de cuánto ocupa cada tipo de archivo, ahora en su propio dispositivo.

### P2 · Los datos invisibles

**Antes:** pseudocódigo en papel, ejecutado por simulación con chatbot.
**Ahora:** el pseudocódigo se traduce a Python y **corre en su propio teléfono**.

El algoritmo de punto de reorden que escribieron para la papelería se ejecuta de verdad, con `python` en Termux o en un editor de Python para Android. La secuencia se conserva —papel, prueba de escritorio, ejecución, comparación— pero ahora la ejecución es real y el error es un error de verdad, con su mensaje.

La simulación con chatbot no desaparece: se conserva como **término de comparación**. Ahora tienen tres resultados y no dos.

### P3 · El sistema mínimo

**Este es el cambio grande.** `pkg install sqlite` da un **motor de base de datos relacional completo**, en el teléfono, sin root, sin cuenta, sin conexión permanente y sin permisos de administrador.

Con eso, P3 deja de depender de la simulación *y* del servidor local. Los alumnos:

1. Diseñan el modelo entidad-relación en papel.
2. Calculan a mano el resultado esperado.
3. **Crean las tablas de verdad en su teléfono** con `CREATE TABLE`, con sus claves primarias y foráneas.
4. Descubren que el motor **rechaza** los datos que violan la integridad referencial. Ninguna simulación enseña eso: un chatbot acepta cualquier cosa.
5. Ejecutan sus tres consultas y comparan contra el chatbot.

El servidor local con PostgreSQL sigue siendo valioso —trabajo multiusuario, datos compartidos, una interfaz más cómoda— pero **deja de estar en la ruta crítica del trimestre**. SQLite en el teléfono es suficiente para todo lo que P3 necesita.

---

## 3. El stack de aplicaciones

Todo desde **F-Droid**, que es el repositorio de software libre para Android: sin cuenta, sin publicidad, sin pago, sin rastreadores. Que sea libre no es un detalle ideológico aquí: es lo que hace que un estudiante sin tarjeta y sin cuenta de Google pueda instalarlo.

| Función | Aplicación | Peso | Para qué en el curso |
|---|---|---|---|
| Tienda de apps libres | **F-Droid** | ~10 MB | Punto de entrada de todo lo demás |
| Terminal Linux completa | **Termux** | ~100 MB + paquetes | Núcleo del curso: `sqlite`, `python`. Requiere Android 7 o superior y ~200 MB libres |
| Información del sistema | Una app de tipo *device info* | ~10 MB | Inventario de hardware para P1 |
| Gestor de archivos | **Material Files** u otro libre | ~15 MB | Sistema de archivos, extensiones, tamaños |
| Análisis de almacenamiento | **DiskUsage** | ~2 MB | Ver qué ocupa el espacio: representación de datos hecha visible |
| Notas en texto plano | **Markor** | ~10 MB | Escribir sin formato, para entender qué es texto plano |
| Análisis de red WiFi | **WiFiAnalyzer** | ~5 MB | Diagnosticar el WiFi de la unidad: por qué es malo, con datos |
| Rastreadores en apps | **Exodus Privacy** | ~10 MB | La actividad de privacidad de la sección 5 |

**Comandos que se usan en Termux durante todo el trimestre.** Son ocho, no ochenta:

```
pkg update && pkg upgrade      # actualizar
pkg install sqlite python      # instalar lo del curso
termux-setup-storage           # acceso a sus archivos
ls, cd, pwd                    # moverse por el sistema de archivos
sqlite3 papeleria.db           # abrir su base de datos
python inventario.py           # correr su algoritmo
```

Con eso alcanza. La tentación de enseñar más Linux hay que resistirla: el objetivo no es formar administradores de sistemas, es que el modelo relacional y el algoritmo dejen de ser abstracciones.

---

## 4. Protocolo de instalación y salvaguardas

Se les está pidiendo que modifiquen **el único dispositivo que muchos tienen**. Eso exige reglas explícitas.

| Regla | Razón |
|---|---|
| **La instalación es voluntaria y no se califica** | Nadie debe arriesgar su único teléfono por una calificación. Quien no quiera o no pueda trabaja en el equipo con el dispositivo de otro |
| **Nada requiere root** | Todo lo del stack funciona sin modificar el sistema. Rootear un teléfono lo puede dejar inservible y anula la garantía |
| **Todo es reversible** | Se desinstala como cualquier app. Se les muestra cómo antes de instalar |
| **Se verifica el espacio libre primero** | Termux con Python y SQLite pide unos 300 MB. Un teléfono con 500 MB libres no es candidato, y hay que saberlo antes de empezar |
| **Un dispositivo por equipo es suficiente** | Cinco instalaciones, no veinticinco. Quien tenga el teléfono con más espacio es el anfitrión del equipo |
| **La instalación se hace en clase, con el WiFi de la unidad** | Cero consumo de datos personales. Y si el WiFi falla, se instala desde el servidor local |
| **Siempre hay ruta sin teléfono** | Papel y máquina del laboratorio. Ninguna evaluación depende de tener un dispositivo capaz |

**Sesión de instalación:** los primeros 30 minutos de la sesión 5 (5 de octubre), que es fase teórica y ya tenía IA habilitada. Instalar F-Droid requiere autorizar la instalación desde fuera de la tienda oficial, un paso que hay que acompañar en clase porque el sistema muestra advertencias que asustan.

**iPhone y equipos limitados.** Termux no existe en iOS; el equivalente razonable es **a-Shell**, gratuita y con Python. Para teléfonos Android viejos o sin espacio, la ruta es el equipo compañero, la máquina del laboratorio o el servidor local. Ningún estudiante queda fuera del ejercicio por el teléfono que trae; esa es la línea que no se cruza.

---

## 5. La actividad de la caja negra

Media sesión, en la fase reflexiva de P1, y es la que convierte el teléfono en objeto de conocimiento en lugar de solo en herramienta.

**Paso 1.** Cada estudiante revisa los permisos que ha concedido a sus cinco aplicaciones más usadas. Cuántas tienen acceso al micrófono, a la ubicación, a los contactos. Se anota.

**Paso 2.** Con Exodus Privacy, ven **cuántos rastreadores** trae cada una de esas aplicaciones y a qué empresas pertenecen. El número típico sorprende: aplicaciones triviales con una docena de rastreadores.

**Paso 3.** La pregunta al grupo: *si la aplicación es gratuita y tiene doce rastreadores, ¿cuál es el producto?*

**Paso 4.** Se conecta con la bibliografía que ya está en el curso: la domesticación digital que analiza Lanier, la vigilancia documentada por Snowden, la manipulación algorítmica del caso Cambridge Analytica. Ya no es lectura sobre algo lejano: es la lectura de lo que acaban de encontrar en su propio bolsillo hace diez minutos.

**Por qué importa para administradores y no solo para ciudadanos:** van a decidir qué sistemas adopta una organización y qué datos entrega a un proveedor. Haber visto los rastreadores de su propio teléfono es la vacuna más barata contra firmar un contrato sin leer qué se lleva el proveedor.

---

## 6. Un riesgo con fecha, que además es material del curso

Google implantó un sistema de verificación obligatoria de desarrolladores que condiciona qué aplicaciones pueden instalarse en dispositivos Android certificados, incluso fuera de su tienda. **El despliegue arranca el 30 de septiembre de 2026 en Brasil, Indonesia, Singapur y Tailandia, y se vuelve global durante 2027.** F-Droid advierte que el esquema amenaza la existencia misma de las tiendas alternativas.

**Para 26-O no hay problema:** México no está en la primera oleada y el trimestre termina en diciembre de 2026. **Para 27-I en adelante, sí lo hay.**

Dos coberturas:

1. **Operativa:** espeje los APK del stack en el servidor local ahora, mientras se puede. Es medio giga y resuelve el trimestre siguiente pase lo que pase.
2. **Pedagógica, y es la buena:** esto es exactamente el tema del curso. Un dispositivo que su dueño compró y que, sin embargo, no decide qué software puede correr, es la ilustración más nítida posible de lo que significa el control del proveedor sobre el usuario. Y para un grupo de administración, es el mismo fenómeno que van a enfrentar cuando su organización quede atada a un proveedor de software que decide unilateralmente qué puede y qué no puede hacer con sus propios datos.

Es un caso vivo, en tiempo real, sobre el que se puede pedir seguimiento durante el trimestre.

---

## 7. Reactivo para el examen integrador

> Tu teléfono tiene más memoria y más núcleos que la computadora del laboratorio, y sin embargo hay cosas que la del laboratorio hace y el tuyo no. Explica por qué, usando el vocabulario del curso. *(15 pts)*

Y uno más, que cierra el hilo transdisciplinario y el de la IA:

> Instalaste un motor de base de datos en tu teléfono sin pagar nada y sin pedir permiso a nadie. Al mismo tiempo, hay software que tu teléfono no te deja instalar aunque el aparato sea tuyo. ¿Quién decide, y qué implicaciones tiene eso para una organización que depende de un proveedor de software? *(15 pts)*
