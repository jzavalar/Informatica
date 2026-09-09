# La laptop del profesor como infraestructura del curso

**Destino:** `docs/curso/laptop-del-profesor.md` (documento docente)
**Contexto:** Fedora Linux con máquina virtual de Windows, llevada al salón en todas las sesiones

---

## 1. El servidor ya existe

El documento sobre el [servidor local](servidor-local.md) planteaba comprar o reciclar hardware. Con una laptop de Fedora que ya va a clase todas las sesiones, **las fases 1 a 3 no requieren hardware adicional**:

| Fase | Servicio | Dónde corre |
|---|---|---|
| 1 | Sitio del curso y lecturas sin conexión | Contenedor en la laptop |
| 2 | Buzón de entregas | Contenedor en la laptop |
| 3 | PostgreSQL con interfaz web | Contenedor en la laptop |
| 4 | Modelo de lenguaje local | **Aquí sí hace falta hardware dedicado.** Sigue siendo proyecto para 27-I |

La compra de equipo se pospone a la fase 4, que es la única que la justifica. Y con SQLite corriendo en los teléfonos, ni siquiera P3 depende ya de esto: el servidor mejora el curso, no lo habilita.

---

## 2. Montaje con Podman

En Fedora, Podman es lo natural: viene en la distribución, corre sin root y se integra con systemd. Todo el stack son cuatro contenedores.

### Preparación

```bash
sudo dnf install -y podman podman-compose qrencode
mkdir -p ~/curso/{sitio,entregas,pgdata,apks}
```

### `~/curso/compose.yml`

```yaml
services:
  sitio:
    image: docker.io/library/nginx:alpine
    ports: ["8080:80"]
    volumes:
      - ./sitio:/usr/share/nginx/html:ro,Z
      - ./apks:/usr/share/nginx/html/apks:ro,Z

  entregas:
    image: docker.io/filebrowser/filebrowser:latest
    ports: ["8081:80"]
    volumes:
      - ./entregas:/srv:Z

  db:
    image: docker.io/library/postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: informatica
      POSTGRES_DB: curso
    volumes:
      - ./pgdata:/var/lib/postgresql/data:Z

  adminer:
    image: docker.io/library/adminer:latest
    ports: ["8082:8080"]
```

### Las dos trampas de Fedora

**SELinux.** Los `:Z` al final de cada volumen no son opcionales. Sin ellos, el contenedor arranca y no puede leer nada, con un permiso denegado que no dice por qué. Es el error que más tiempo cuesta en Fedora.

**firewalld.** Bloquea los puertos por omisión, así que los contenedores funcionan en la laptop y son invisibles desde los teléfonos. Hay que abrirlos, y conviene hacerlo solo en una zona dedicada:

```bash
sudo firewall-cmd --permanent --new-zone=clase
sudo firewall-cmd --permanent --zone=clase --add-port=8080/tcp
sudo firewall-cmd --permanent --zone=clase --add-port=8081/tcp
sudo firewall-cmd --permanent --zone=clase --add-port=8082/tcp
sudo firewall-cmd --reload
```

Asignar la interfaz del hotspot a la zona `clase` y no a `public` evita exponer estos servicios cuando la laptop está en cualquier otra red.

### Publicar el sitio en local

```bash
cd ~/Informatica && mkdocs build -d ~/curso/sitio
```

El mismo sitio que está en GitHub Pages, servido desde la laptop. Sin internet, sin consumir datos de nadie.

---

## 3. La red del salón

```bash
nmcli device wifi hotspot ifname wlan0 ssid informatica password claseUAM2026
```

Un comando. La laptop se vuelve punto de acceso y los teléfonos se conectan a ella, no al WiFi de la unidad. **El tráfico nunca sale del salón**: latencia mínima, consumo de datos cero, y el WiFi institucional deja de ser un factor.

**Antes de contar con esto, verifique que su tarjeta lo soporta:**

```bash
iw list | grep -A 10 "Supported interface modes"
```

Debe aparecer `AP` en la lista. Si no aparece, o si necesita estar conectado a internet y servir el hotspot al mismo tiempo con una sola antena, la solución es un adaptador WiFi USB de veinte dólares o un router de viaje conectado por Ethernet.

**Advertencia con Android:** una red sin salida a internet a veces se descarta sola y el teléfono se pasa a datos móviles. Si pasa, en los ajustes de esa red hay que marcar la opción de mantener la conexión aunque no tenga internet. Conviene resolverlo con un equipo de prueba antes de la sesión 5, no con veinticinco alumnos esperando.

---

## 4. El repositorio de APK: lo más urgente

Esto es lo que hay que tener listo para **la sesión 5, el 5 de octubre**, que es la de instalación en dispositivos.

Descargue desde su laptop, con anticipación, los APK de F-Droid, Termux y las demás aplicaciones del stack, y déjelos en `~/curso/apks`. En clase, los alumnos los instalan desde el hotspot: **sin consumir un solo megabyte de sus datos** y sin depender del WiFi de la unidad.

Para que no tengan que teclear una dirección:

```bash
qrencode -o ~/curso/sitio/qr.png "http://10.42.0.1:8080/apks/"
```

`10.42.0.1` es la dirección que NetworkManager asigna por omisión al hotspot; confírmela con `ip addr show wlan0`. Proyecte el código QR y los veinticinco lo escanean en diez segundos.

Y una razón adicional para hacerlo ahora: el esquema de verificación obligatoria de desarrolladores de Google empieza a desplegarse el 30 de septiembre de 2026 y se vuelve global en 2027. **Los APK espejados en su laptop son la cobertura para 27-I.** Descárguelos mientras se puede.

---

## 5. La máquina de Fedora como objeto de enseñanza

Su laptop no es solo infraestructura: es el mejor material didáctico del curso, y está desaprovechado.

**Una computadora, dos sistemas operativos corriendo a la vez.** Eso es una demostración en vivo de qué es un sistema operativo, algo que ninguna lectura transmite igual. Cuatro momentos donde encaja:

| Cuándo | Demostración | Qué revela |
|---|---|---|
| P1, sesión teórica | Arrancar la VM de Windows dentro de Fedora, en pantalla | Que el sistema operativo es un programa, no la máquina. Que se le asignan RAM y disco. Que se puede apagar sin apagar la computadora |
| P1, sesión teórica | `lsblk`, `df -h`, `free -h` proyectados | Los mismos números que ellos leyeron en su teléfono con una app, ahora en texto crudo. Misma arquitectura, otra presentación |
| P2, laboratorio | Ejecutar el pseudocódigo de un equipo en la terminal | El algoritmo corriendo fuera del teléfono, con el mismo resultado. La lógica es independiente de la máquina |
| P3, laboratorio | Comparar SQLite del teléfono contra PostgreSQL del servidor | La misma consulta, dos motores, el mismo resultado. Y el chatbot, que da otro |

**El argumento de fondo, que es el del curso:** el profesor usa software libre, sin licencia, en una máquina que administra él. No es una postura ideológica que se enuncia: es una máquina funcionando frente a ellos, que además está corriendo Windows adentro cuando hace falta. Eso vale más que cualquier discurso sobre alternativas al software propietario.

El material de particiones y sistemas de archivos que quedó en `archivo/versiones-previas/` recupera aquí su utilidad: no como práctica que los alumnos ejecutan —no pueden— sino como **demostración que ellos observan y documentan**.

---

## 6. Riesgos de convertir su equipo de trabajo en infraestructura

| Riesgo | Mitigación |
|---|---|
| La laptop falla o no llega, y la sesión depende de ella | **Ninguna sesión depende de ella.** Es la regla que ya rige todo el diseño. Si no hay servidor, la sesión ocurre igual |
| Los contenedores no arrancan tras suspender la laptop | `podman-compose down && up -d` al llegar al salón, como parte de la rutina. Dos minutos |
| Batería agotada a mitad de clase | Servir WiFi y contenedores consume bastante. Localice el contacto del salón en la sesión 1 y lleve extensión |
| Servicios expuestos en otras redes | La zona `clase` de firewalld, aplicada solo a la interfaz del hotspot |
| Datos personales de alumnos en su equipo | El buzón guarda entregas académicas. Las calificaciones viven en el libro de seguimiento, que no se sirve por red |
| Proyectar y servir a la vez | Funciona, pero pruebe la combinación de proyector y hotspot antes de la sesión 1: algunos adaptadores de video interfieren con el WiFi en 2.4 GHz |

---

## 7. Rutina de sesión

**Antes de salir de casa**

```bash
cd ~/curso && podman-compose up -d && podman ps
```

**Al llegar al salón**

```bash
nmcli device wifi hotspot ifname wlan0 ssid informatica password claseUAM2026
ip addr show wlan0 | grep inet          # confirmar la dirección
```

Proyectar el QR. Verificar con un teléfono propio que el sitio carga.

**Al terminar**

```bash
nmcli connection down Hotspot
cd ~/curso && podman-compose down
```

Y una copia del buzón de entregas al disco de respaldo, semanalmente. Son megabytes.
