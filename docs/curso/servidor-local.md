# Servidor local del curso

**Destino:** `docs/curso/servidor-local.md` (documento técnico, versión docente)

---

## 1. Qué problemas resuelve y en qué orden importan

El servidor no es un accesorio: cada servicio corresponde a una restricción concreta del contexto.

| Restricción real | Qué la resuelve |
|---|---|
| WiFi institucional deficiente | Un punto de acceso propio, **sin salida a internet**. El tráfico es puramente local, así que la latencia es de milisegundos y no compite con la red de la unidad |
| Alumnos sin datos móviles | Todo el contenido se sirve desde la red local: **consumo de datos cero** |
| No se puede instalar software en el laboratorio | Los servicios se usan **desde el navegador**. Nada que instalar, ningún permiso de administrador |
| No hay gestor de bases de datos para P3 | Un PostgreSQL con interfaz web da a los alumnos **un DBMS real**, no simulado |
| Chatbots requieren cuenta, datos y ceden información personal | Un modelo de lenguaje local: **sin cuenta, sin datos móviles, sin que los datos del alumno salgan del salón** |
| Entregas que cuestan datos móviles | Buzón de entregas en la red local |

El cambio más importante es el cuarto. **Con servidor, P3 deja de depender de la simulación**: los alumnos implementan su modelo en un PostgreSQL de verdad, desde el navegador de una máquina donde no se puede instalar nada. La simulación con IA se conserva, pero cambia de función: pasa de ser el sustituto del DBMS a ser el **objeto auditado** —el alumno compara lo que dice el chatbot contra lo que dice el motor real, y ese contraste es pedagógicamente superior a cualquiera de los dos por separado.

---

## 2. Advertencia de calendario

**El trimestre empieza en nueve días.** No ponga el servidor en la ruta crítica de 26-O.

El curso está diseñado para funcionar **sin él**: papel primero, simulación después, degradación elegante ante cualquier falla. El servidor mejora el curso; no lo habilita. Si algo no está listo, la sesión ocurre igual.

Por eso el despliegue va por fases, ordenadas por relación entre beneficio y riesgo:

| Fase | Cuándo | Servicio | Riesgo si falla |
|---|---|---|---|
| **1** | Antes del 21 de septiembre | Sitio y lecturas servidos en local | Ninguno: el sitio también está en GitHub Pages |
| **2** | Durante octubre | Buzón de entregas | Ninguno: la entrega en papel sigue siendo válida |
| **3** | Antes del 11 de noviembre (inicio de P3) | PostgreSQL con interfaz web | Ninguno: P3 corre con simulación, como está diseñado |
| **4** | 27-Invierno, no ahora | Modelo de lenguaje local | Es la fase con más incógnitas de desempeño. No comprometa 26-O con ella |

---

## 3. Arquitectura

```
        ┌──────────────────────────────────────────┐
        │  Servidor (mini PC o equipo de escritorio) │
        │                                          │
        │  Caddy  ──► sitio del curso (MkDocs)      │
        │         ──► lecturas y paquete PDF        │
        │         ──► Filebrowser (buzón)           │
        │         ──► Adminer ──► PostgreSQL        │
        │         ──► Open WebUI ──► Ollama (fase 4)│
        └───────────────┬──────────────────────────┘
                        │ cable Ethernet
                ┌───────┴────────┐
                │ Router en modo │   SSID: informatica-local
                │ punto de acceso│   Sin salida a internet
                └───────┬────────┘
                        │ WiFi local
     ┌──────────────────┼──────────────────┐
  teléfonos        máquinas del         laptop del
  de los alumnos     laboratorio          profesor
```

**Decisión clave: red aislada, sin internet.** Simplifica todo. No hay que pedir permisos de red a la unidad, no hay superficie de ataque desde fuera, no hay que cumplir políticas de la red institucional, y el desempeño es predecible porque nadie más usa esa red. Los alumnos se conectan a un SSID que solo sirve el curso.

---

## 4. Hardware: tres niveles

Los tres funcionan; se diferencian por si soportan o no el modelo de lenguaje local.

### Nivel A · Contenido y entregas

Una computadora de escritorio reciclada (cuatro núcleos, 8 GB de RAM, SSD) o una Raspberry Pi 5 con SSD, más un router de viaje configurado como punto de acceso. Cubre las fases 1 a 3 sin esfuerzo: servir archivos estáticos y un PostgreSQL con veinticinco usuarios ocasionales es una carga trivial.

Si tiene una máquina dada de baja en la unidad, es suficiente. **La fase 3 completa cabe aquí.**

### Nivel B · Mini PC x86 moderno

Un mini PC con procesador de bajo consumo tipo N100, 16 GB de RAM y SSD de 500 GB. Silencioso, consume poco, cabe en una mochila. Corre todo lo del nivel A con holgura y permite experimentar con un modelo de lenguaje pequeño (3 a 4 mil millones de parámetros, cuantizado) en CPU.

Advertencia honesta: en CPU, ese modelo responde a **una** consulta a la vez y despacio. Sirve para que usted experimente, no para cinco equipos simultáneos.

### Nivel C · Equipo con GPU, para la fase 4

Una computadora de escritorio con una GPU de 12 GB de memoria de video (una RTX 3060 usada es el punto dulce de precio y capacidad en el mercado mexicano de equipo usado) y 32 GB de RAM. Con eso, un modelo de 7 a 8 mil millones de parámetros cuantizado atiende a los cinco equipos con tiempos de respuesta aceptables para el uso del curso.

**Verifique precios localmente antes de comprometer presupuesto**; el mercado de GPU usadas se mueve mucho y no tengo datos actuales confiables.

---

## 5. Software

Todo en contenedores, para que reinstalar sea reproducible:

| Servicio | Software | Para qué |
|---|---|---|
| Servidor web | Caddy | Sirve el sitio estático de MkDocs y hace de puerta a los demás servicios |
| Buzón de entregas | Filebrowser | Carga de archivos por navegador, una carpeta por equipo, sin cuentas complicadas |
| Base de datos | PostgreSQL | El DBMS real de P3 |
| Interfaz de base de datos | Adminer | Una sola página, ligera, funciona bien en el navegador de una máquina vieja. Preferible a pgAdmin, que es pesado |
| Modelo de lenguaje (fase 4) | Ollama + Open WebUI | Chatbot local sin cuenta ni datos |
| Sistema | Debian estable o Fedora Server | Lo que usted ya administra |

**Nota sobre Adminer contra pgAdmin:** en las máquinas del laboratorio, que son viejas y con navegadores desactualizados, pgAdmin va a ir mal o no cargar. Adminer es un solo archivo y funciona en casi cualquier cosa. Esta decisión importa más de lo que parece.

---

## 6. Cómo cambia P3 con el servidor

Sin servidor, la secuencia de P3 es: papel → cálculo manual → simulación con chatbot → comparación.

**Con servidor son cuatro instancias en lugar de tres**, y la comparación se vuelve mucho más rica:

1. **En papel:** el diagrama entidad-relación y las tablas.
2. **A mano:** el resultado esperado de las tres preguntas de negocio.
3. **En PostgreSQL:** implementan las tablas de verdad y ejecutan la consulta real. Aquí descubren que un modelo mal diseñado **no deja** insertar los datos: el motor rechaza lo que viola la integridad referencial. Ninguna simulación enseña eso, porque un chatbot acepta cualquier cosa.
4. **Con el chatbot:** la misma consulta, simulada. Y ahora tienen **tres resultados que comparar**: el suyo, el del motor real y el del modelo de lenguaje.

Cuando el chatbot difiere del motor real, tienen la evidencia más contundente posible de por qué no se le puede creer. Es exactamente la lección del curso, demostrada con un experimento controlado en lugar de con una advertencia.

---

## 7. Operación y riesgos

| Riesgo | Mitigación |
|---|---|
| El servidor no arranca el día de la sesión | La sesión funciona sin él. Siempre. Esa es la regla |
| Custodia física del equipo | Se lleva y se trae, o queda bajo llave. No se deja conectado a la red institucional sin resolver antes las políticas de la unidad |
| Datos personales de alumnos en el servidor | **No se almacenan.** El buzón guarda entregas académicas; las calificaciones viven en el libro de seguimiento, fuera del servidor |
| Respaldo | Copia del volumen de datos a un disco externo al terminar cada semana. Son megabytes |
| Que se convierta en el proyecto en lugar del curso | Fases 1 a 3 este trimestre como máximo. La fase 4 es un proyecto de investigación propio, no un requisito de docencia |

---

## 8. Lo que esto abre más allá del curso

El servidor con modelo local resuelve un problema que va mucho más allá de esta UEA: **da acceso a IA generativa a estudiantes que no pueden pagar una suscripción ni tienen datos**, sin que sus consultas salgan de la institución.

En una universidad pública con población en condiciones de marginación, esa brecha —quien paga la versión de paga tiene mejor tutor que quien no— es una desigualdad nueva que se está instalando ahora mismo, en silencio, y sobre la que casi no hay literatura empírica en México. Documentar la implementación, el costo real y el uso durante un trimestre es material publicable, y encaja directamente con el argumento de la lectura *La Computadora 2.0* sobre democratización y sobre el uso ético de estas herramientas en educación.

Pero para 27-Invierno. Este trimestre, fases 1 a 3.
