## **Lectura 11: Introducción a las Bases de Datos**[^1]

prof. dr. Jesús Zavala Ruiz[^2]

---

### **1. Introducción**

El concepto de **bases de datos** tiene sus raíces en los esfuerzos por organizar y estructurar información de manera eficiente. En las primeras civilizaciones, los **registros manuales** en tablas y documentos fueron fundamentales para gestionar el comercio, la administración y la contabilidad. Ejemplos de esto son las tablillas de arcilla de los sumerios, utilizadas para registrar transacciones comerciales hace más de 5000 años.

Con el avance de la tecnología, surgió la necesidad de automatizar estos procesos. Un hito importante fue el trabajo de Herman Hollerith, quien en 1890 desarrolló una **máquina de tabulación** que utilizaba tarjetas perforadas para almacenar y procesar datos. Esta innovación permitió analizar los datos del censo de los Estados Unidos con una eficiencia sin precedentes. Hollerith fundó posteriormente la empresa que se convertiría en **IBM**, una de las pioneras en tecnologías de bases de datos.

En las décadas de 1960 y 1970, el auge de las computadoras dio lugar al desarrollo de **modelos estructurados para gestionar datos**. Los primeros enfoques incluyeron el modelo jerárquico y el modelo de red, los cuales ofrecían formas organizadas de almacenar y acceder a datos.

El **modelo jerárquico**  organiza los datos en una estructura tipo árbol, donde cada nodo padre puede tener varios nodos hijos, pero cada hijo tiene un único padre. Este enfoque era eficiente para aplicaciones con relaciones predecibles, como directorios telefónicos y registros de empleados. Sin embargo, su rigidez dificultaba la gestión de relaciones complejas. El **modelo de red** está basado en grafos y permitía que un nodo tuviera varios padres, ofreciendo mayor flexibilidad que el modelo jerárquico. Fue implementado por sistemas como el *Integrated Data Store* (IDS) de Charles Bachman, quien recibió el Premio Turing en 1973 por su contribución a las bases de datos.

El cambio paradigmático llegó en 1970 con el **modelo relacional**, propuesto por **Edgar F. Codd** en su artículo clásico *A Relational Model of Data for Large Shared Data Banks*. Este modelo representó un avance significativo al organizar los datos en *tablas bidimensionales* (matemáticamente llamadas *relaciones*), donde cada fila representaba una *tupla* (o **registro**) y cada columna un **atributo**. Las bases de datos relacionales ofrecen las siguientes dos ventajas fundamentales: (1) una *independencia de los datos*, que permitió que los usuarios trabajaran con datos sin preocuparse por su almacenamiento físico y, (2) el uso de *lenguajes de consulta declarativos* al introducir el **SQL** (*Structured Query Language*), que se convertiría en el estándar de facto para interactuar con bases de datos relacionales.

Durante las décadas de 1980 y 1990, las bases de datos relacionales dominaron el mercado. Empresas como Oracle, IBM y Microsoft desarrollaron **sistemas de bases de datos** (**DBMS**) comerciales que popularizaron el uso del SQL. Estos sistemas fueron esenciales para aplicaciones empresariales, desde la gestión de inventarios hasta sistemas financieros, lo que dio origen a los modernos sistemas empresariales ERP.  

Conviene recordar que el **invento del DBMS** materializó el deseo del **Proyecto LEO** (Lyons Electronic Office), que desarrolló entre 1949 y 1951, en Gran Bretaña, la primer computadora y **el primer ERP del mundo** para uso civil, que manejó tareas administrativas, como la gestión de inventarios, el procesamiento de pedidos y la nómina de J. Lyons y, de otras compañías, bajo contrato. Ese proyecto marcó el inicio de los sistemas automatizados para la gestión de grandes volúmenes de datos, sentando las bases para los sistemas de bases de datos computarizadas.  El Proyecto LEO se convitió en el *primer servicio de outsourcing* de procesamiento de datos, en el mundo.  

En paralelo, surgieron bases de datos orientadas a objetos, que integraban los principios de la programación orientada a objetos con bases de datos. Aunque este enfoque tuvo menos adopción que el modelo relacional, fue precursor de sistemas más flexibles que combinarán estructuras complejas.

Con el advenimiento de internet y el auge de las redes sociales en la década de 2000, surgieron nuevas demandas de escalabilidad y gestión de **datos no estructurados**. Esto dio origen a las bases de datos NoSQL, que incluyen (1) **bases de datos clave-valor** (como Redis), (2) **bases de datos de documentos** (como MongoDB) y (3) **bases de datos en grafo** (por ejemplo, Neo4j).

Las **bases de datos distribuidas** también cobraron relevancia para manejar grandes volúmenes de **datos distribuidos geográficamente**. Sistemas como Apache Cassandra y Google Bigtable respondieron a estas necesidades, siendo esenciales para aplicaciones de Big Data.

Las **tendencias actuales** de las bases de datos han evolucionado hacia entornos más accesibles y escalables gracias a la **computación en la nube**. Servicios como Amazon RDS, Google BigQuery y Microsoft Azure SQL Database ofrecen soluciones que eliminan la necesidad de infraestructura física, permitiendo a las organizaciones centrarse en el análisis de datos y la toma de decisiones. La integración de **inteligencia artificial** y **aprendizaje automático** está transformando la manera en que se analizan y gestionan los datos. Bases de datos como Google Vertex AI combinan almacenamiento con herramientas de análisis predictivo y modelos de aprendizaje automático. Finalmente, la **tecnología blockchain** ha introducido una nueva forma de almacenar datos de manera descentralizada y segura. Aunque inicialmente asociada con criptomonedas, esta tecnología tiene aplicaciones en sectores como la gestión de la cadena de suministro y la verificación de identidades.

En **conclusión**, la historia de las bases de datos es un viaje desde registros manuales hasta sistemas altamente sofisticados y distribuidos. A través de cada etapa, estas herramientas han evolucionado para responder a las necesidades de organización y procesamiento de datos de las sociedades modernas. Desde las tablillas de arcilla hasta las bases de datos en la nube, el objetivo principal ha sido el mismo: *convertir datos en información útil*. Los avances tecnológicos recientes y las tendencias actuales apuntan a un futuro donde las bases de datos serán cada vez más inteligentes, seguras y esenciales para la toma de decisiones informada.

### **2. Conceptos Fundamentales**

Ya hemos revisado el concepto de basede datos como un sistema tecnológico de gestión de datos. Sin embargo, una **base de datos** es mucho más que un simple repositorio de información; es un sistema organizado que permite almacenar, gestionar y recuperar datos de manera eficiente. Este sistema se construye en torno a una serie de conceptos fundamentales y principios clave que aseguran su funcionalidad y utilidad.

El funcionamiento de una base de datos se basa en la transformación progresiva de datos en información y, finalmente, en conocimiento:

- **Datos:** Son hechos o cifras brutas que carecen de contexto, como "45" o "azul". Aunque por sí mismos no tienen significado, constituyen la base para generar información.
- **Información:** Surge al organizar y contextualizar los datos. Por ejemplo, "45 estudiantes inscritos en un curso" convierte un número en un mensaje significativo.
- **Conocimiento:** Representa la interpretación y aplicación de la información para la toma de decisiones. Por ejemplo, "dividir los 45 estudiantes en dos grupos optimizará el aprendizaje".

Este proceso convierte los datos dispersos en conocimiento útil, permitiendo una toma de decisiones informada y eficiente.

#### **Componentes Principales de una Base de Datos**

Las bases de datos modernas incluyen varios componentes esenciales que trabajan juntos para proporcionar un sistema funcional y eficiente:

1. **Datos:** Representan el contenido que se almacena. Pueden ser estructurados (como nombres o fechas) o no estructurados (como documentos, imágenes o videos).
2. **Usuarios:** Incluyen diferentes tipos de actores:
   - **Administradores de bases de datos (DBA):** Diseñan, gestionan y mantienen la base de datos.
   - **Desarrolladores:** Crean aplicaciones que interactúan con la base de datos.
   - **Usuarios finales:** Utilizan estas aplicaciones para acceder y analizar la información.
3. **Sistema de Gestión de Bases de Datos (DBMS):** Es el software que actúa como intermediario entre los usuarios y los datos. Administra el almacenamiento, la consulta y la actualización de datos, garantizando su integridad y seguridad.
4. **Hardware:** Consiste en los dispositivos físicos que soportan el sistema, como servidores locales o servicios en la nube.

#### **Aplicaciones Prácticas de las Bases de Datos**

Las bases de datos tienen aplicaciones en una amplia gama de sectores:

- **Gestores de contactos:** Almacenan información como nombres, direcciones y teléfonos.
- **Banca:** Registran transacciones, saldos y estados de cuenta.
- **Salud:** Organizan historiales médicos y tratamientos.
- **Comercio electrónico:** Gestionan catálogos de productos y pedidos.

Estas aplicaciones permiten a las organizaciones gestionar grandes volúmenes de información de manera eficiente y confiable, mediante operaciones llamadas transacciones.

#### **Transacciones en una base de datos**

Las **transacciones** son la unidad básica de trabajo en una base de datos, compuestas por una o varias operaciones que *deben ejecutarse como un todo*. Por ejemplo, en una transferencia bancaria, una transacción podría implicar debitar una cuenta y acreditar otra.

La **confiabilidad** en una base de datos se refiere a la capacidad del sistema para asegurar que los datos almacenados y procesados sean precisos, consistentes y seguros frente a fallos. Esto incluye *proteger la información contra errores humanos, fallos técnicos o accesos no autorizados*. Para alcanzar este nivel de confiabilidad, las bases de datos implementan transacciones con propiedades definidas por el modelo **ACID**:

1. **A***tomicidad*: Todas las operaciones de una transacción se completan o ninguna lo hace. Si ocurre un error, se ejecuta un **rollback** para revertir los cambios.
2. **C***onsistencia:* Las transacciones llevan la base de datos de un estado válido a otro, respetando todas las reglas definidas.
3. *a***I***slamiento:* Garantiza que las transacciones concurrentes no interfieran entre sí.
4. **D***urabilidad:* Una vez completada, la transacción es permanente, incluso ante fallos del sistema.

El **rollback** es una herramienta crucial para garantizar la atomicidad. Por ejemplo, si una transferencia bancaria falla después de debitar una cuenta pero antes de acreditar otra, el rollback restaura el saldo original.

El término coloquial "**base de datos chocolateada**" hace referencia a una base de datos que ha sido manipulada o modificada de manera poco estructurada, sin seguir los principios básicos de diseño, normalización o buenas prácticas. Estas bases de datos suelen presentar problemas como:

1. **Duplicación de Datos:** Datos redundantes que dificultan su gestión y actualización.
2. **Falta de Normalización:** Estructuras mal diseñadas que generan inconsistencias.
3. **Dificultad para Escalar:** Complicaciones al aumentar el volumen de datos o implementar nuevas funcionalidades.

Una base de datos "chocolateada" generalmente es resultado de cambios improvisados, soluciones rápidas o falta de planificación inicial. Esto puede ocasionar problemas de confiabilidad, rendimiento y mantenibilidad a largo plazo. Es un ejemplo claro de cómo la ausencia de principios como ACID y buenas prácticas puede afectar el desempeño de un sistema.

#### **Conclusión**

La confiabilidad es un aspecto esencial de las bases de datos modernas, garantizando que los datos permanezcan precisos, seguros y consistentes incluso ante fallos. Junto con los conceptos fundamentales y el modelo ACID, esto forma el cimiento de su funcionalidad. Al comprender las propiedades de las transacciones y el modelo ACID, es posible apreciar cómo las bases de datos transforman los datos dispersos en conocimiento accionable, desempeñando un papel vital en la sociedad moderna.

### **3. Diseño de Bases de Datos Relacionales**

El **diseño de una base de datos** es un proceso crucial para garantizar que cumpla con los requisitos funcionales de una organización, manteniendo la integridad, escalabilidad y eficiencia. Este proceso se divide en varias etapas, desde la conceptualización hasta la implementación física. En este apartado, se exploran los conceptos fundamentales y las herramientas necesarias para diseñar bases de datos relacionales.

El diseño de una base de datos relacional incluye dos etapas principales: el diseño lógico y el diseño físico. Estas etapas se complementan para garantizar que los datos se almacenen y gestionen de manera óptima.

1. **Diseño Lógico:** Se enfoca en la representación abstracta de la base de datos, sin considerar los detalles técnicos de su implementación. Esta etapa define:
   - Entidades y atributos.
   - Relaciones entre entidades.
   - Restricciones de integridad.

   Las herramientas comunes en esta etapa incluyen diagramas de entidad-relación (E-R) y UML (Unified Modeling Language).

2. **Diseño Físico:** Implica la implementación práctica del modelo lógico en un sistema de gestión de bases de datos (DBMS).
   - Define detalles como índices, particiones y su almacenamiento en disco.
   - Se optimizan aspectos como el rendimiento, la escalabilidad y el acceso concurrente.

#### **Diseño Lógico Básico**

El **diseño lógico** comienza con la recopilación y el análisis de requisitos, seguido de la modelación de los datos mediante herramientas conceptuales. 

El análisis de los requisitos se puede realizar con la técnica "**Sujeto-Verbo-Complemento**", que permite identificar las entidades, atributos y relaciones mediante la descomposición de requisitos funcionales en frases simples de la forma sujeto-verbo-complemento. Por ejemplo:

- Requisito: "Los **cliente**s **alquila**n **película**s."
  - **Sujeto:** Cliente (entidad).
  - **Verbo:** Alquilar (relación).
  - **Complemento:** Película (entidad).

Este análisis garantiza que los requisitos se traduzcan directamente en elementos del modelo conceptual.

El producto de este análisis conceptual es la relación de entidades, atributos y relaciones:

- **Entidades:** Representan objetos o conceptos importantes, como clientes, películas o pedidos.
- **Atributos:** Son las propiedades que describen a las entidades, como el nombre del cliente o el título de una película.
- **Relaciones:** Definen las asociaciones entre entidades, como "un cliente puede alquilar varias películas".

Posteriormente, esos elementos se organizan en representaciones gráficas o modelos, como el Modelo Entidad-Relación (E-R) o el Diagrama de Clases en el Lenguaje Unificado de Modelado (UML). 

El **modelo E-R** es una herramienta gráfica para representar las entidades, atributos y relaciones identificadas durante el análisis de requisitos. Los elementos clave incluyen:

- **Rectángulos:** Representan entidades.
- **Óvalos:** Representan atributos.
- **Rombos:** Representan relaciones.

Un ejemplo típico en el contexto de una tienda de alquiler de películas incluiría entidades como "Cliente", "Película" e "Inventario", con relaciones como "Alquila".

Ver diagrama: [https://www.jooq.org/img/sakila.png](https://www.jooq.org/img/sakila.png)

**Diagrama de Clases en UML**

El **UML** (Unified Modeling Language) es una herramienta complementaria al modelo E-R. Mientras que el modelo E-R se centra en la estructura de los datos, el UML permite modelar la estructura y el comportamiento de los objetos en un sistema. En el contexto de bases de datos:

- **Clases:** Representan entidades.
- **Atributos:** Detallan las propiedades de las clases.
- **Asociaciones:** Definen las relaciones entre clases.

Por ejemplo, un diagrama de clases podría mostrar "Cliente" con atributos como "ID", "Nombre" y "Dirección", y relaciones con "Alquiler" y "Película".

#### **Esquema de la Base de Datos**

El resultado del diseño lógico es el **esquema de la base de datos**, que incluye la especificación correspondiente a:

1. **Tablas:** Corresponden a las entidades y relaciones identificadas.
2. **Columnas:** Representan los atributos de las tablas.
3. **Claves Primarias y Foráneas:** Garantizan la integridad referencial entre las tablas.

#### **Herramientas para el Diseño de Bases de Datos**

Existen múltiples herramientas de software libre que facilitan el diseño conceptual y lógico de bases de datos:

1. **MySQL Workbench:**
   - Herramienta integral para diseño E-R y administración de bases de datos.
   - Permite generar diagramas E-R y exportar esquemas directamente a SQL.

2. **DbSchema:**
   - Herramienta visual para diseño de esquemas y simulación de consultas SQL.
   - Compatible con varios DBMS, incluidos MySQL, PostgreSQL y SQLite.

3. **DBeaver:**
   - Ideal para administración y modelado básico de bases de datos.
   - Compatible con múltiples DBMS.

4. **Draw.io:**
   - Útil para crear diagramas E-R y UML de forma sencilla.
   - Integración con herramientas como Google Drive.

#### **Ejemplo: Diseño Conceptual de la Base de Datos Sakila**

La base de datos **Sakila**, desarrollada por MySQL, es un esquema relacional que modela una hipotética **tienda de alquiler de videos**. Este ejemplo permite comprender cómo traducir un diseño conceptual a un esquema práctico.

**1. Análisis de Requisitos** con la técnica **Sujeto-Verbo-Complemento:**
  - "Los clientes alquilan películas."
  - "Las películas están en inventario."
  - "Los pagos registran el costo de los alquileres."

**2. Modelo E-R:**
El modelo E-R de Sakila incluye:

  1. **Entidades:**
     - Cliente (Customer).
     - Película (Film).
     - Inventario (Inventory).
     - Pago (Payment).

  2. **Relaciones:**
     - Un cliente realiza múltiples pagos.
     - Una película está en múltiples inventarios.
     - Un inventario puede ser alquilado por varios clientes.

**3. Esquema Generado**
A partir del modelo E-R, se crean tablas como:

- **Customer:**
  - ID, Nombre, Dirección.
- **Film:**
  - ID, Título, Descripción, Duración.
- **Inventory:**
  - ID, PelículaID, Fecha de Adquisición.
- **Payment:**
  - ID, ClienteID, Monto, Fecha de Pago.

**4. Diagrama UML**
En el diagrama UML, estas entidades se convierten en clases, con atributos detallados y relaciones representadas por asociaciones entre clases.

#### Conclusión

El diseño de bases de datos relacionales es una disciplina fundamental para garantizar que los datos se gestionen de manera estructurada y eficiente. Desde el análisis de requisitos hasta la generación del esquema, el uso de herramientas adecuadas y un diseño meticuloso aseguran que las bases de datos cumplan con sus objetivos funcionales y operativos.

### **4. Lenguajes de Bases de Datos**

Los lenguajes de bases de datos son fundamentales para interactuar con sistemas de gestión de bases de datos (DBMS). A través de ellos, los usuarios pueden definir estructuras, manipular datos y controlar el acceso. En este apartado, exploraremos los lenguajes más utilizados y las operaciones esenciales en SQL, acompañadas de ejemplos prácticos basados en la base de datos **Sakila**.

#### **Introducción a DDL, DML y SQL**

El lenguaje SQL (Structured Query Language) es el estándar para trabajar con bases de datos relacionales. SQL se divide en varios sublenguajes, cada uno con un propósito específico:

1. **DDL (Data Definition Language):**
   - Se utiliza para definir y modificar la estructura de las bases de datos.
   - Sentencias comunes:
     - `CREATE`: Crea tablas, bases de datos u otros objetos.
     - `ALTER`: Modifica estructuras existentes, como agregar columnas.
     - `DROP`: Elimina tablas u otros objetos.

2. **DML (Data Manipulation Language):**
   - Permite manipular los datos almacenados en las bases de datos.
   - Sentencias comunes:
     - `SELECT`: Recupera datos de las tablas.
     - `INSERT`: Agrega nuevos datos.
     - `UPDATE`: Modifica datos existentes.
     - `DELETE`: Elimina registros específicos.

3. **DCL (Data Control Language):**
   - Gestiona los permisos y la seguridad de la base de datos.
   - Sentencias comunes:
     - `GRANT`: Otorga permisos a usuarios.
     - `REVOKE`: Revoca permisos otorgados.

#### **Sentencias Esenciales de SQL**

A continuación, exploraremos algunas de las sentencias más importantes de SQL y cómo se aplican en el contexto de la base de datos **Sakila**.

##### **1. CREATE: Crear Tablas y Esquemas**
La sentencia `CREATE` se utiliza para definir nuevas tablas y esquemas en una base de datos.

**Ejemplo:** Crear una tabla `Actor` para almacenar información sobre actores en la base de datos Sakila:
```sql
CREATE TABLE Actor (
    actor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
En este ejemplo:
- `actor_id` es la clave primaria que identifica de manera única a cada actor.
- `first_name` y `last_name` son atributos obligatorios.
- `last_update` almacena la última vez que se actualizó el registro.

##### **2. SELECT: Consultar Datos**
La sentencia `SELECT` es fundamental para recuperar datos de una base de datos. Permite filtrar, ordenar y combinar datos de múltiples tablas.

**Ejemplo:** Consultar los nombres de todos los actores en la tabla `Actor`:
```sql
SELECT first_name, last_name
FROM Actor;
```
**Ejemplo avanzado:** Obtener los actores que participaron en películas específicas, combinando las tablas `Actor`, `Film_Actor` y `Film`:
```sql
SELECT a.first_name, a.last_name, f.title
FROM Actor a
JOIN Film_Actor fa ON a.actor_id = fa.actor_id
JOIN Film f ON fa.film_id = f.film_id
WHERE f.title LIKE 'A%';
```
En este ejemplo:
- Se recuperan los nombres de actores y títulos de películas que comienzan con la letra "A".
- Se utilizan combinaciones (`JOIN`) para conectar las tablas relacionadas.

##### **3. INSERT: Insertar Datos**
La sentencia `INSERT` agrega nuevos registros a una tabla.

**Ejemplo:** Insertar un nuevo actor en la tabla `Actor`:
```sql
INSERT INTO Actor (first_name, last_name)
VALUES ('John', 'Doe');
```
En este caso, se crea un registro para un actor llamado "John Doe".

##### **4. UPDATE: Actualizar Datos**
La sentencia `UPDATE` permite modificar registros existentes en una tabla.

**Ejemplo:** Actualizar el apellido de un actor específico:
```sql
UPDATE Actor
SET last_name = 'Smith'
WHERE actor_id = 1;
```
En este ejemplo:
- El apellido del actor con `actor_id = 1` se cambia a "Smith".

##### **5. DELETE: Eliminar Datos**
La sentencia `DELETE` elimina registros de una tabla, basándose en una condición específica.

**Ejemplo:** Eliminar a un actor de la tabla `Actor`:
```sql
DELETE FROM Actor
WHERE actor_id = 1;
```
En este caso, se elimina el actor con `actor_id = 1`.

#### **Ejemplo Completo con la Base de Datos Sakila**

La base de datos **Sakila**, disponible en [GitHub](https://github.com/jOOQ/sakila/tree/main/sqlite-sakila-db), es un esquema diseñado para simular la gestión de una tienda de alquiler de videos. Incluye tablas como `Actor`, `Film`, `Customer`, y `Rental`, lo que la convierte en un recurso ideal para aprender SQL.

##### **1. Crear y Consultar Tablas**
Crear una nueva tabla para registrar géneros de películas:
```sql
CREATE TABLE Genre (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);
```
Insertar datos en la tabla `Genre`:
```sql
INSERT INTO Genre (name) VALUES ('Comedy'), ('Action'), ('Drama');
```
Consultar todos los géneros:
```sql
SELECT * FROM Genre;
```

##### **2. Relaciones entre Tablas**
Sakila utiliza relaciones para conectar tablas como `Film` y `Actor`. Por ejemplo, la tabla `Film_Actor` almacena las asociaciones entre películas y actores.

Consultar películas protagonizadas por un actor específico:
```sql
SELECT f.title
FROM Film f
JOIN Film_Actor fa ON f.film_id = fa.film_id
JOIN Actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'John' AND a.last_name = 'Doe';
```

##### **3. Actualizar y Eliminar Registros**
Actualizar la categoría de una película específica:
```sql
UPDATE Film
SET category_id = 3
WHERE title = 'Academy Dinosaur';
```
Eliminar un cliente de la tabla `Customer`:
```sql
DELETE FROM Customer
WHERE customer_id = 10;
```

#### **Buenas Prácticas en el Uso de SQL**

1. **Utilizar Claves Primarias y Foráneas:** Garantizan la integridad referencial entre tablas relacionadas.
2. **Indexar Columnas:** Mejora el rendimiento de las consultas frecuentes.
3. **Evitar Consultas Sin Filtro:** Siempre incluir condiciones (`WHERE`) para evitar modificaciones o eliminaciones masivas accidentales.
4. **Probar Consultas en Entornos de Prueba:** Asegura que los cambios no afecten datos críticos en producción.

#### **Conclusión**

El lenguaje SQL es esencial para interactuar con bases de datos relacionales. Desde la creación de estructuras con DDL hasta la manipulación de datos con DML, SQL ofrece una gama de herramientas que permiten satisfacer las necesidades de almacenamiento y análisis de datos. La base de datos Sakila proporciona un entorno práctico para aprender y aplicar estas herramientas, haciendo que los conceptos se vuelvan tangibles y relevantes para situaciones del mundo real.

### Conclusiones

### **Conclusión General**

La **Lectura 11: Introducción a las Bases de Datos** proporciona una visión integral del desarrollo, diseño y manejo de las bases de datos en contextos históricos, conceptuales y prácticos. A lo largo de esta lectura, se ha explorado cómo las bases de datos han evolucionado desde registros manuales y tecnologías pioneras como las tarjetas perforadas de Hollerith y el Proyecto LEO, hasta los sofisticados sistemas actuales basados en la nube, inteligencia artificial y blockchain.

Los fundamentos conceptuales, como la jerarquía entre datos, información y conocimiento, y los componentes esenciales de las bases de datos, sientan las bases para comprender cómo estas herramientas transforman datos en conocimiento accionable. Además, se detalla el diseño lógico y físico de bases de datos relacionales, enfatizando la importancia de estructuras organizadas y herramientas prácticas como el modelo entidad-relación (E-R) y los diagramas UML.

El lenguaje SQL, descrito en detalle, destaca por su versatilidad y su capacidad de interactuar con bases de datos mediante sublenguajes como DDL, DML y DCL. Ejemplos prácticos basados en la base de datos Sakila demuestran cómo aplicar sentencias esenciales como `CREATE`, `SELECT`, `INSERT`, `UPDATE` y `DELETE` para gestionar y manipular datos de manera eficiente.

En síntesis, esta lectura subraya que las bases de datos son fundamentales para el manejo de grandes volúmenes de información en la era digital. Al combinar principios de diseño sólido, buenas prácticas y herramientas avanzadas, se pueden crear sistemas de bases de datos confiables y escalables que soporten las necesidades actuales y futuras de las organizaciones.

### Bibliografía básica

1. Codd, E. F. (1970). A Relational Model of Data for Large Shared Data Banks. *Communications of the ACM*, *13*(6), 377-387.  
   - Este artículo seminal introduce el modelo relacional, un pilar fundamental en la teoría y práctica de las bases de datos.

2. Silberschatz, A., Korth, H. F., & Sudarshan, S. (2020). *Database System Concepts*. McGraw-Hill Education.  
   - Un texto completo y ampliamente utilizado que cubre todos los aspectos fundamentales de los sistemas de bases de datos, incluidos diseño, lenguajes y aplicaciones avanzadas.

3. Elmasri, R., & Navathe, S. B. (2016). *Fundamentals of Database Systems*. Pearson.  
   - Este libro proporciona una introducción detallada al diseño conceptual, lógico y físico de bases de datos, así como al uso de SQL y otras tecnologías modernas.

--- 

[^1]: Profesor-investigador del Departamento de Economía de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Contacto: [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx), [Telegram](https://t.me/jzavalar).
[^2]: Lectura leída el 11 de diciembre de 2024.

Ultima actualización: 11 de diciembre de 2024.
