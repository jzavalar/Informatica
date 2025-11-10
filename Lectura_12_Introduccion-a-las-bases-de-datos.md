## **Lectura 12: Introducción a las Bases de Datos**[^1]

prof. dr. Jesús Zavala Ruiz[^2]

---

### **1. Introducción**

El concepto de **bases de datos** tiene sus raíces en los esfuerzos por organizar y estructurar información de manera eficiente. En las primeras civilizaciones, los **registros manuales** en tablas y documentos fueron fundamentales para gestionar el comercio, la administración y la contabilidad. Ejemplos de esto son las tablillas de arcilla de los sumerios, utilizadas para registrar transacciones comerciales hace más de 5000 años.

Con el avance de la tecnología, surgió la necesidad de **automatizar** estos procesos. Un hito importante fue el trabajo de Herman Hollerith, quien en 1890 desarrolló una **máquina de tabulación** que utilizaba tarjetas perforadas para almacenar y procesar datos. Esta innovación permitió analizar los datos del censo de los Estados Unidos con una eficiencia sin precedentes. La empresa de Hollerith se convertiría en **IBM**, una de las pioneras en tecnologías de cómputo y en de bases de datos, en especial.

En las décadas de 1960 y 1970, el auge de las computadoras dio lugar al desarrollo de **modelos estructurados para gestionar datos**. Los primeros enfoques incluyeron el modelo jerárquico y el modelo de red, los cuales ofrecían formas organizadas de almacenar y acceder a datos.

El **modelo jerárquico**  organiza los datos en una estructura tipo árbol, donde cada nodo padre puede tener varios nodos hijos, pero cada hijo tiene un único padre. Este enfoque era eficiente para aplicaciones con relaciones predecibles, como directorios telefónicos y registros de empleados. Sin embargo, su rigidez dificultaba la gestión de relaciones complejas. El **modelo de red** está basado en grafos y permitía que un nodo tuviera varios padres, ofreciendo mayor flexibilidad que el modelo jerárquico. Fue implementado por sistemas como el *Integrated Data Store* (IDS) de Charles Bachman, quien recibió el Premio Turing en 1973 por su contribución a las bases de datos.

El cambio paradigmático llegó en 1970 con el **modelo relacional**, propuesto por **Edgar F. Codd** en su artículo clásico *A Relational Model of Data for Large Shared Data Banks*. Este modelo representó un avance significativo al organizar los datos en *tablas bidimensionales* (matemáticamente llamadas *relaciones*), donde cada fila representaba una *tupla* (o **registro**) y cada columna un **atributo**. Las bases de datos relacionales ofrecen las siguientes dos ventajas fundamentales: (1) una *independencia de los datos*, que permitió que los usuarios trabajaran con datos sin preocuparse por su almacenamiento físico y, (2) el uso de *lenguajes de consulta declarativos* al introducir el **SQL** (*Structured Query Language*), que se convertiría en el estándar de facto para interactuar con bases de datos relacionales.

Durante las décadas de 1980 y 1990, las bases de datos relacionales dominaron el mercado. Empresas como Oracle, IBM y Microsoft desarrollaron **sistemas de bases de datos** (**DBMS**) comerciales que popularizaron el uso del SQL. Estos sistemas fueron esenciales para aplicaciones empresariales, desde la gestión de inventarios hasta sistemas financieros, lo que dio origen a los modernos sistemas empresariales ERP. También en esta década surgieron los DBMS de escritorio como   

En paralelo, surgieron bases de datos orientadas a objetos, que integraban los principios de la programación orientada a objetos con bases de datos. Aunque este enfoque tuvo menos adopción que el modelo relacional, fue precursor de sistemas más flexibles que combinarán estructuras complejas.

Con el advenimiento de internet y el auge de las redes sociales en la década de 2000, surgieron nuevas demandas de escalabilidad y gestión de **datos no estructurados**. Esto dio origen a las bases de datos NoSQL, que incluyen (1) **bases de datos clave-valor** (como Redis), (2) **bases de datos de documentos** (como MongoDB) y (3) **bases de datos en grafo** (por ejemplo, Neo4j).

Las **bases de datos distribuidas** también cobraron relevancia para manejar grandes volúmenes de **datos distribuidos geográficamente**. Sistemas como Apache Cassandra y Google Bigtable respondieron a estas necesidades, siendo esenciales para aplicaciones de Big Data.

Las **tendencias actuales** de las bases de datos han evolucionado hacia entornos más accesibles y escalables gracias a la **computación en la nube**. Servicios como Amazon RDS, Google BigQuery y Microsoft Azure SQL Database ofrecen soluciones que eliminan la necesidad de infraestructura física, permitiendo a las organizaciones centrarse en el análisis de datos y la toma de decisiones. La integración de **inteligencia artificial** y **aprendizaje automático** está transformando la manera en que se analizan y gestionan los datos. Bases de datos como Google Vertex AI combinan almacenamiento con herramientas de análisis predictivo y modelos de aprendizaje automático. Finalmente, la **tecnología blockchain** ha introducido una nueva forma de almacenar datos de manera descentralizada y segura. Aunque inicialmente asociada con criptomonedas, esta tecnología tiene aplicaciones en sectores como la gestión de la cadena de suministro y la verificación de identidades.

En **conclusión**, la historia de las bases de datos es un viaje desde registros manuales hasta sistemas altamente sofisticados y distribuidos. A través de cada etapa, estas herramientas han evolucionado para responder a las necesidades de organización y procesamiento de datos de las sociedades modernas. Desde las tablillas de arcilla hasta las bases de datos en la nube, el objetivo principal ha sido el mismo: *convertir datos en información útil*. 

Los **DBMS de escritorio** han evolucionado desde los sistemas monolíticos como **dBase** hasta herramientas modernas como **SQLite** y **DBeaver**. Al mismo tiempo, los sistemas gestores de bases de datos libres y abiertos, liderado por **PostgreSQL** y **MariaDB**, han transformado la forma en que las organizaciones gestionan los datos, proporcionando alternativas confiables y accesibles para sistemas de escritorio, servidores y aplicaciones en la nube. Hoy, es, hasta cierto punto irracional, en términos económicos, que se use software privativo, si existe software libre y abierto de clase empresarial gratuito para crear toda una plataforma completa como LAMP (**L**inux - **A**pache - **M**ySQL (o **M**ariaDB) - **P**HP (**P**ython o **P**erl)). Los avances tecnológicos recientes y las tendencias actuales apuntan a un futuro donde las bases de datos serán cada vez más inteligentes, seguras y esenciales para la toma de decisiones informada. 

### **2. Conceptos Fundamentales**

Ya hemos revisado el concepto de basede datos como un sistema tecnológico de gestión de datos. Sin embargo, una **base de datos** es mucho más que un simple repositorio de información; es un sistema organizado que permite almacenar, gestionar y recuperar datos de manera eficiente. Este sistema se construye en torno a una serie de **conceptos fundamentales** y **principios clave** que aseguran su funcionalidad y utilidad.

El funcionamiento de una base de datos se basa en la transformación progresiva de datos en información y, finalmente, en conocimiento. No hay que olvidar que los **datos** son hechos o cifras brutas que carecen de contexto, como "45" o "azul"; que, aunque por sí mismos no tienen significado, constituyen la base para generar información. Los datos se transforman en **información** al organizar y contextualizarlos; por ejemplo, "45" significa "45 estudiantes inscritos en un curso", lo que convierte al número en un mensaje significativo. Y, finalmente, la información se transforma en **conocimiento** cuando la interpretación y aplicación de la información se utiliza para la *toma de decisiones*, que es el corazón de la administración; por ejemplo, "decidir dividir esos 45 estudiantes en tres grupos para optimizar el aprendizaje". Este proceso convierte los datos dispersos en conocimiento útil, permitiendo una toma de decisiones informada y eficiente. Eso es lo que apoyan las bases de datos cuando se generan reportes. 

Por lo anterior es importante conocer los **componentes esenciales** de un **sistema de información** que trabajan juntos para proporcionar un sistema funcional y eficiente:

1. **Base de Datos**: Representan el contenido que se almacena. Los datos pueden ser estructurados (como nombres o fechas) o no estructurados (como documentos, audios, imágenes o videos).
2. **Usuarios**: Incluyen diferentes tipos de actores:
   - **Administradores de bases de datos (DBA)**: Personal técnico quienes diseñan, gestionan y mantienen la base de datos.
   - **Desarrolladores**: Quienes crean aplicaciones que interactúan con la base de datos.
   - **Usuarios finales**: Quienes utilizan estas aplicaciones para acceder y analizar la información, que es el rol de la mayoría de los usuarios.
3. **Sistema de Gestión de Bases de Datos (DBMS)**: Es el software que actúa como intermediario entre los usuarios y los datos y que administra el almacenamiento, la consulta y la actualización de datos, garantizando su integridad y seguridad; se le conoce, coloquialmente como "base de datos".
4. **Hardware:** Consiste en los dispositivos físicos que soportan el sistema, como servidores locales o servicios en la nube.

Las bases de datos tienen aplicaciones en una amplia gama, como los **gestores de contactos** que almacenan información como nombres, direcciones y teléfonos, las **aplicaciones bancarias** que registran transacciones, saldos y estados de cuenta, los **sistemas de salud** que organizan historiales médicos y tratamientos y las aplicaciones de **comercio electrónico** que gestionan catálogos de productos y pedidos, por ejemplo. Estas aplicaciones permiten a las organizaciones gestionar grandes volúmenes de información de manera eficiente y confiable, mediante operaciones llamadas transacciones.

Las **transacciones** son la unidad básica de trabajo en una base de datos, compuestas por una o varias operaciones que *deben ejecutarse como un todo*. Por ejemplo, en una transferencia bancaria, una transacción podría implicar debitar una cuenta y acreditar otra. La principal cualidad de una transacción es su **confiabilidad**, que se refiere a la capacidad del sistema para asegurar que los datos almacenados y procesados sean precisos, consistentes y seguros frente a fallos. Esto incluye *proteger la información* contra *errores humanos*, *fallas técnicas* o *accesos no autorizados*. Para alcanzar este nivel de confiabilidad, las bases de datos implementan transacciones con propiedades definidas por el **modelo ACID**, que debe cumplir las siguientes cuatro reglas:

1. **A***tomicidad*,es decir, que todas las operaciones de una transacción *se completan o ninguna lo hace*. Si se completan se confirma con un **commit** y, si ocurre un error, se ejecuta un **rollback** para revertir los cambios.
2. **C***onsistencia* de las transacciones que llevan la base de datos de un estado válido (o consistente) a otro también válido, respetando todas las reglas definidas.
3. *a***I***slamiento* que garantiza que las **transacciones concurrentes** (que ocurren al mismo tiempo) *no interfieran entre sí*.
4. **D***urabilidad*, que garantiza que, una vez completada, la transacción es permanente, incluso ante fallos del sistema. 

El término coloquial "**base de datos chocolateada**" hace referencia a una base de datos que ha sido manipulada, modificada o corrompida, de manera poco estructurada, sin seguir los principios básicos de diseño, normalización o buenas prácticas. Una *base de datos chocolateada* generalmente es resultado de cambios improvisados, soluciones rápidas o falta de planificación inicial. Estas bases de datos suelen presentar problemas como **duplicación de datos** que dificultan su gestión y actualización, **falta de normalización** de datos estructurados por estructuras mal diseñadas que generan inconsistencias y **dificultad para escalar** que tiene complicaciones al aumentar el volumen de datos o implementar nuevas funcionalidades. En otras palabras, una base de datos chocolateada es un ejemplo claro de cómo la ausencia de principios como ACID y buenas prácticas puede afectar el desempeño de un sistema.

Como ha quedado claro, la confiabilidad es el aspecto esencial de cualquier base de datos moderna, garantizando que los datos permanezcan precisos, seguros y consistentes incluso ante fallas técnicas. Los conceptos fundamentales y el modelo ACID forman el cimiento de su funcionalidad. Al comprender las propiedades de las transacciones y el modelo ACID, es posible apreciar cómo las bases de datos transforman los datos dispersos en conocimiento para la toma de decisiones, en cualquier organización moderna. Enseguida, abordaremos cómo crear una base de datos.

### **3. Diseño de Bases de Datos Relacionales**

El **diseño de una base de datos** es un proceso crucial para garantizar que cumpla con los requisitos funcionales de una organización, manteniendo la integridad, escalabilidad y eficiencia. Este proceso se divide en varias etapas, desde la *conceptualización* hasta la *implementación física*. En este apartado, se exploran los conceptos fundamentales y las herramientas necesarias para diseñar bases de datos relacionales.

El **diseño de una base de datos relacional** incluye dos etapas principales: el diseño lógico y el diseño físico. Estas etapas se complementan para garantizar que los datos se almacenen y gestionen de manera óptima. El **diseño lógico** se enfoca en la *representación abstracta de la base de datos*, sin considerar los detalles técnicos de su implementación. Esta etapa define las **entidades** o conceptos y sus atributos (o propiedades), las relaciones entre entidades y las restricciones de integridad, durante la inserción (INSERT), actualización (UPDATE) o eliminación (DELETE) de datos. Las herramientas comunes en esta etapa incluyen **diagramas de entidad-relación** (E-R) o diagramas en UML (Unified Modeling Language o Lenguaje de Modelado Unificado). 

Una vez concluido, el diseño lógico, se procede al **diseño físico** que implica la implementación práctica del modelo lógico en un sistema de gestión de bases de datos (DBMS) específico. En este proceso, las *entidades* se convierten en **tablas**, los atributos en campos de un tipo de dato específico, las relaciones entre entidades se implementan con el uso de **llaves primarias** (*PK*, de **Primary Key**) y **llaves foráneas** (*FK*, de **Foreign Key**) y las restricciones de integridad se implementan con CONSTRAINTS y **triggers**. También se implementan detalles como **índices** (para acelerar la búsqueda), **particiones** (para mejorar el desempeño) y su almacenamiento en disco. A su vez, se optimizan aspectos como el rendimiento, la escalabilidad, el acceso concurrente y la replicación.

El **diseño lógico** comienza con la recopilación y el análisis de requisitos, seguido de la modelación de los datos mediante herramientas conceptuales. El **análisis de los requisitos** se puede realizar con la técnica "**Sujeto-Verbo-Complemento**", que permite identificar las entidades, atributos y relaciones mediante la descomposición de requisitos funcionales en frases simples de la forma sujeto-verbo-complemento. Por ejemplo, el requisito "Los **cliente**s **alquila**n **película**s" se descompone en **Sujeto**: Cliente (entidad) - **Verbo**: Alquilar (relación) - **Complemento**: Película (entidad). Este análisis garantiza que los requisitos o requerimentos se traduzcan directamente en elementos del modelo conceptual.

El producto de este análisis conceptual es la relación de entidades, atributos y relaciones. las **entidades** representan objetos o conceptos importantes, como clientes, películas o pedidos; los **atributos** son las propiedades que describen a las entidades, como el nombre del cliente o el título de una película y las **relaciones** definen las **asociaciones entre entidades**, como "un cliente *puede* alquilar *varias* películas". Posteriormente, esos elementos se organizan en representaciones gráficas o modelos, como el Modelo Entidad-Relación (E-R) o el Diagrama de Clases en el Lenguaje Unificado de Modelado (UML). 

El **modelo E-R** es una herramienta gráfica para representar las entidades, atributos y relaciones identificadas durante el análisis de requisitos. Los elementos clave incluyen entidades que se representan como **rectángulos**, atributos que se grafican como **óvalos** y relaciones que se representan como **rombos**, como se muestra en la siguiente figura: 
![](https://es.wikipedia.org/wiki/Archivo:Ejemplo_Diagrama_E-R_extendido.PNG)

Aunque también se representan de otras maneras, dependiendo del autor, como se muestra en la siguiente figura:
![](http://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/ERD_Representation.svg/320px-ERD_Representation.svg.png)

En la actualidad, está ganando popularidad el uso de un **diagrama de clases en UML**. El **UML** (Unified Modeling Language) es una herramienta integral que se usa para el modelado de sistemas y uno de sus diagramas centrales es el *diagrama de clases*. Mientras que el modelo E-R se centra en la estructura de los datos, el UML permite modelar la estructura y el comportamiento de los objetos en un sistema. En el contexto de bases de datos, las **clases** representan entidades, los *atributos** detallan las propiedades de las clases y las **asociaciones** definen las relaciones entre las clases. Por ejemplo, un diagrama de clases podría mostrar a la clase "Cliente" con atributos como "ID", "Nombre" y "Dirección" y la relación "Alquila" con la clase "Película".

Pero, ya sea que se use un antiguo diagrama E-R o un moderno diagrama de clases UML, representarán un modelo llamado esquema de la dase de datos. Existen múltiples herramientas de software libre que facilitan el diseño conceptual y lógico de bases de datos, como [MySQL Workbench](https://www.mysql.com/products/workbench/design/), [DbSchema](https://dbschema.com/index_es.html), [DBeaver](https://dbeaver.com/docs/dbeaver/ER-Diagrams/) o [Draw.io](https://app.diagrams.net/). 

### **4. Ejemplo de diseño e implementación de una base de datos**

La base de datos **Sakila**, desarrollada por MySQL, es un esquema relacional que modela una hipotética **tienda de alquiler de videos**, que permite comprender cómo traducir un diseño conceptual a un esquema práctico. La base de datos **Sakila**, disponible en [GitHub](https://github.com/jOOQ/sakila/), incluye tablas como `Actor`, `Film`, `Customer`, y `Rental`, lo que la convierte en un recurso ideal para aprender SQL.

El diagrama E-R de la base de datos Sakila, se muestra enseguida: 

![Sakila Database Schema](https://www.jooq.org/img/sakila.png)

Obsérvese en la figura un ejemplo típico en el contexto de la hipotética tienda de alquiler de películas, que incluiría entidades como "Cliente" (CLIENT), "Película" (FILM) e "Inventario" (INVENTORY), con relaciones como "Alquila".

El proceso que ha llevado a ese esquema se ejemplifica con los siguientes tres requerimeintos:

**1. Análisis de Requisitos** con la técnica **Sujeto-Verbo-Complemento:**
  - "Los clientes alquilan películas."
  - "Las películas están en inventario."
  - "Los pagos registran el costo de los alquileres."

**2. Modelo E-R:**
El modelo E-R de Sakila incluye:

   1. **Entidades:**
      - Cliente (CUSTOMER).
      - Película (FILM).
      - Inventario (INVENTORY).
      - Pago (PAYMENT).

   2. **Relaciones:**
      - Un cliente realiza múltiples pagos.
      - Una película está en múltiples inventarios.
      - Un inventario puede ser alquilado por varios clientes.

**3. Esquema de la base de datos:**

El **esquema de una base de datos** es la representación estructural que define cómo se organizan y relacionan los datos dentro de un sistema de gestión de bases de datos (DBMS). Actúa como el diseño lógico de la base de datos, especificando elementos como tablas, columnas, relaciones, claves primarias y foráneas y restricciones de integridad. Este esquema es esencial para garantizar la coherencia, la integridad y la eficiencia en el almacenamiento y recuperación de datos. Diseñado a partir de modelos conceptuales, como el modelo entidad-relación, *el esquema es implementado físicamente mediante lenguajes como SQL*, convirtiéndose en la base para todas las operaciones que se realizan sobre los datos.

El **SQL** (*Structured Query Language*) es el estándar universal para definir, manipular y gestionar datos en bases de datos relacionales. Una de sus funciones esenciales es la implementación del **esquema de una base de datos**, que establece la estructura lógica de los datos. A través de su sublenguaje **DDL (Data Definition Language)**, SQL permite crear tablas, definir relaciones entre ellas, establecer restricciones de integridad y configurar índices que optimizan el acceso a la información. Este proceso traduce los modelos conceptuales y lógicos, como el modelo entidad-relación, en estructuras físicas listas para ser gestionadas por un sistema de gestión de bases de datos (DBMS). SQL no solo es la base para estructurar datos, sino también una herramienta poderosa para garantizar la integridad y eficiencia en su manejo.

La base de datos **Sakila** está diseñada para gestionar una tienda de alquiler de películas y su esquema permite modelar diversos requerimientos operativos. Los tres requerimientos a analizar son:

1. "Los clientes alquilan películas."
2. "Las películas están en inventario."
3. "Los pagos registran el costo de los alquileres."

La relación entre estos tres requerimientos puede representarse de forma lógica utilizando las conexiones entre las tablas del esquema:

1. Un cliente (tabla `customer`) realiza un alquiler (tabla `rental`) de copias específicas (tabla `inventory`) de películas (tabla `film`).
2. El inventario (tabla `inventory`) vincula las películas disponibles con las transacciones de alquiler.
3. Los pagos (tabla `payment`) registran el costo asociado a cada alquiler, permitiendo realizar un seguimiento financiero.

A continuación, analizo cómo se implementan estos requerimientos en el esquema de la base de datos, en el archivo del esquema de la base de datos con SQLite: [sqlite-sakila-schema.sql](https://github.com/jOOQ/sakila/blob/main/sqlite-sakila-db/sqlite-sakila-schema.sql). Después, doy ejemplos prácticos en SQL de cómo se comprueba la validez del requerimiento. 

**Requerimiento 1: Los clientes alquilan películas**

   Este requerimiento está modelado mediante las siguientes tablas, campos y relaciones:
   - **`customer` (clientes)**: Identifica unívocamente a los clientes (con el campo llave primaria (PK) `customer_id`) que pueden realizar alquileres.
   - **`rental` (alquileres)**: Registra las transacciones de alquiler, asociando un cliente (`customer_id`) con un ejemplar específico de películas del inventario (`inventory_id`) y la fecha del alquiler.
   - **`inventory` (inventario):** Representa cada copia física (`inventory_id`) disponible para alquiler y está relacionada con la tabla `film` (películas) mediante su llave foránera `film_id`.
   - **`film` (películas):** Contiene los detalles de las películas (`film_id` (llave primaria), título, duración, etc.).

   A continuación se cita la definición de la tabla `customer`, tal como se implementa con las instrucciones DDL `CREATE <tabla>`, `CREATE <index>` y `CREATE <trigger>`, en el archivo `.sql`, líneas 174 a 211:
  
   ```sql
   --
   -- Table structure for table customer
   --
  
   CREATE TABLE customer (
     customer_id INTEGER NOT NULL,
     store_id INT NOT NULL,
     first_name VARCHAR(45) NOT NULL,
     last_name VARCHAR(45) NOT NULL,
     email VARCHAR(50) DEFAULT NULL,
     address_id INT NOT NULL,
     active CHAR(1) DEFAULT 'Y' NOT NULL,
     create_date TIMESTAMP NOT NULL,
     last_update TIMESTAMP NOT NULL,
     PRIMARY KEY  (customer_id),
     CONSTRAINT fk_customer_store FOREIGN KEY (store_id) REFERENCES store (store_id) ON DELETE NO ACTION ON UPDATE CASCADE,
     CONSTRAINT fk_customer_address FOREIGN KEY (address_id) REFERENCES address (address_id) ON DELETE NO ACTION ON UPDATE CASCADE
   )
   ;

   CREATE  INDEX idx_customer_fk_store_id ON customer(store_id)
   ;
   CREATE  INDEX idx_customer_fk_address_id ON customer(address_id)
   ;
   CREATE  INDEX idx_customer_last_name ON customer(last_name)
   ;

   CREATE TRIGGER customer_trigger_ai AFTER INSERT ON customer
    BEGIN
     UPDATE customer SET last_update = DATETIME('NOW')  WHERE rowid = new.rowid;
    END
   ;
   
   CREATE TRIGGER customer_trigger_au AFTER UPDATE ON customer
    BEGIN
     UPDATE customer SET last_update = DATETIME('NOW')  WHERE rowid = new.rowid;
    END
   ;
   ``` 

   Las demás tablas se definen de manera semejante. Se deja al lector que verifique cómo se lleva a acabo.
  
   A continuación se cita la instrucción SQL que valida la implementación del requerimiento bajo análisis: 
  
   Consulta la base de datos y *muestra las películas alquiladas por todos los clientes*.

   ```sql
   SELECT c.customer_id, c.first_name, c.last_name, f.title, r.rental_date
   FROM customer c
   JOIN rental r ON c.customer_id = r.customer_id
   JOIN inventory i ON r.inventory_id = i.inventory_id
   JOIN film f ON i.film_id = f.film_id
   ORDER BY c.customer_id, r.rental_date;
   ```

   Explicación: 
   - Se combinan las tablas `customer`, `rental`, `inventory` y `film` para obtener el historial de alquileres de cada cliente.
   - Incluye los nombres de los clientes, títulos de las películas y las fechas de alquiler.

   De manera similar se cumplimentan los otros dos requerimientos. Se deja el lector que confirme la creación de las tablas, los índices y los triggers correspondientes. A continuación sólo se valida el cumplimiento de los requerimientos. 
  
**Requerimiento 2: Las películas están en inventario**

   Este requerimiento está modelado mediante las siguientes tablas:
   - **`rental` (alquileres)**: Registra las transacciones de alquiler, asociando un cliente (`customer_id`) con un ejemplar específico de películas del inventario (`inventory_id`) y la fecha del alquiler.
   - **`inventory` (inventario):** Representa cada copia física (`inventory_id`) disponible para alquiler y está relacionada con la tabla `film` (películas) mediante su llave foránera `film_id`.
   - **`film` (películas):** Contiene los detalles de las películas (`film_id` (llave primaria), título, duración, etc.).

   Consulta que valida el requerimiento: *Mostrar todas las películas y su disponibilidad en inventario*.

   ```sql
   SELECT f.title, COUNT(i.inventory_id) AS total_copies,
          COUNT(r.rental_id) AS rented_copies,
          COUNT(i.inventory_id) - COUNT(r.rental_id) AS available_copies
   FROM film f
   LEFT JOIN inventory i ON f.film_id = i.film_id
   LEFT JOIN rental r ON i.inventory_id = r.inventory_id AND r.return_date IS NULL
   GROUP BY f.film_id, f.title
   ORDER BY available_copies DESC;
   ```

   Explicación:
   - Cuenta el número total de copias (`total_copies`), las alquiladas actualmente (`rented_copies`) y las disponibles (`available_copies`) para cada película.
   - Utiliza una combinación izquierda (`LEFT JOIN`) para incluir todas las películas, incluso si no tienen copias disponibles.

**Requerimiento 3: Los pagos registran el costo de los alquileres**

   Este requerimiento está modelado mediante las siguientes tablas:
   - **`customer` (clientes)**: Identifica unívocamente a los clientes (con el campo llave primaria (PK) `customer_id`) que pueden realizar alquileres.
   - **`rental` (alquileres)**: Registra las transacciones de alquiler, asociando un cliente (`customer_id`) con un ejemplar específico de películas del inventario (`inventory_id`) y la fecha del alquiler.
   - **`inventory` (inventario):** Representa cada copia física (`inventory_id`) disponible para alquiler y está relacionada con la tabla `film` (películas) mediante su llave foránera `film_id`.
   - **`film` (películas):** Contiene los detalles de las películas (`film_id` (llave primaria), título, duración, etc.).
   - **`payment` (pagos):** Registra los pagos realizados por los clientes, asociando un alquiler (`rental_id`) con un cliente (`customer_id`), la cantidad pagada (`amount`) y la fecha del pago (`payment_date`).

   Consulta a la base de datos que valida el requerimiento: **Mostrar el historial de pagos de cada cliente.**

   ```sql
   SELECT c.customer_id, c.first_name, c.last_name, r.rental_date, p.amount, p.payment_date
   FROM payment p
   JOIN rental r ON p.rental_id = r.rental_id
   JOIN customer c ON p.customer_id = c.customer_id
   ORDER BY c.customer_id, p.payment_date;
   ```

   Explicación:
   - Combina las tablas `payment`, `rental` y `customer` para obtener los detalles de pagos realizados por los clientes.
  - Incluye información sobre el cliente, la fecha del alquiler, la cantidad pagada y la fecha del pago.

  Como puede verse con este pequeño ejemplo, el esquema de la base de datos Sakila implementa los tres requerimientos con un diseño eficiente que utiliza claves primarias y foráneas para garantizar la integridad referencial. La combinación de las tablas `customer`, `film`, `inventory`, `rental` y `payment` permite modelar completamente la lógica del negocio de una tienda de alquiler de películas, desde la disponibilidad de las películas hasta el registro de pagos por los clientes. 
  
Este diseño relacional facilita consultas complejas para análisis de datos y gestión operativa. Esto hace que el diseño de bases de datos relacionales sea un conocimiento fundamental para garantizar que los datos se gestionen de manera estructurada y eficiente. Desde el análisis de requisitos hasta la generación del esquema y su implementación, el uso de herramientas adecuadas y un diseño meticuloso aseguran que las bases de datos cumplan con sus objetivos funcionales y operativos.

A continuación haré un breve repaso sobre el lenguaje de las bases de datos: SQL.

### **4. Lenguajes de Bases de Datos**

Los lenguajes de bases de datos son fundamentales para interactuar con sistemas de gestión de bases de datos (DBMS). A través de ellos, los usuarios pueden definir estructuras, manipular datos y controlar el acceso. En este apartado, exploraremos el lenguaje más utilizado y las operaciones esenciales en SQL, acompañadas de ejemplos prácticos basados en la base de datos **Sakila** que se expuso en el apartado previo.

El **lenguaje SQL** (*Structured Query Language*) es el estándar para trabajar con bases de datos relacionales. SQL se divide en tres sublenguajes, cada uno con un propósito específico: el DDL (Data Definition Language, Lenguaje de Definición de Datos), el DML (Data Manipulation Language, Lenguaje de Manipulación de Datos) y el DCL (Data Control Language, Lenguaje de Control de Datos).

El **DDL (Data Definition Language)** se utiliza para definir y modificar la estructura de las bases de datos. Las entencias comunes son:
   - `CREATE`: Crea tablas, bases de datos u otros objetos.
   - `ALTER`: Modifica estructuras existentes, como agregar columnas.
   - `DROP`: Elimina tablas u otros objetos.

El **DML (Data Manipulation Language)** permite manipular los datos almacenados en las bases de datos. las sentencias comunes:
   - `SELECT`: Recupera datos de las tablas.
   - `INSERT`: Agrega nuevos datos.
   - `UPDATE`: Modifica datos existentes.
   - `DELETE`: Elimina registros específicos.

El **DCL (Data Control Language)** gestiona los permisos y la seguridad de la base de datos. Las entencias comunes:
   - `GRANT`: Otorga permisos a usuarios.
   - `REVOKE`: Revoca permisos otorgados.

A continuación, exploraremos algunas de las sentencias más importantes de SQL y cómo se aplican en el contexto de la base de datos **Sakila**.

**1. CREATE: Crear Tablas y Esquemas**
La sentencia `CREATE` se utiliza para definir nuevas tablas y esquemas en una base de datos.

Ejemplo: Crear una tabla `Actor` para almacenar información sobre actores en la base de datos Sakila:
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

**2. SELECT: Consultar Datos**
La sentencia `SELECT` es fundamental para recuperar datos de una base de datos. Permite filtrar, ordenar y combinar datos de múltiples tablas.

Ejemplo: Consultar los nombres de todos los actores en la tabla `Actor`:
```sql
SELECT first_name, last_name
FROM Actor;
```
Ejemplo avanzado: Obtener los actores que participaron en películas específicas, combinando las tablas `Actor`, `Film_Actor` y `Film`:
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

**3. INSERT: Insertar Datos**
La sentencia `INSERT` agrega nuevos registros a una tabla.

Ejemplo: Insertar un nuevo actor en la tabla `Actor`:
```sql
INSERT INTO Actor (first_name, last_name)
VALUES ('John', 'Doe');
```
En este caso, se crea un registro para un actor llamado "John Doe".

**4. UPDATE: Actualizar Datos**
La sentencia `UPDATE` permite modificar registros existentes en una tabla.

Ejemplo: Actualizar el apellido de un actor específico:
```sql
UPDATE Actor
SET last_name = 'Smith'
WHERE actor_id = 1;
```
En este ejemplo:
- El apellido del actor con `actor_id = 1` se cambia a "Smith".

**5. DELETE: Eliminar Datos**
La sentencia `DELETE` elimina registros de una tabla, basándose en una condición específica.

Ejemplo: Eliminar a un actor de la tabla `Actor`:
```sql
DELETE FROM Actor
WHERE actor_id = 1;
```
En este caso, se elimina el actor con `actor_id = 1`.

**Ejemplo Completo con la Base de Datos Sakila**

**1. Crear y Consultar Tablas**
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

**2. Relaciones entre Tablas**
Sakila utiliza relaciones para conectar tablas como `Film` y `Actor`. Por ejemplo, la tabla `Film_Actor` almacena las asociaciones entre películas y actores.

Consultar películas protagonizadas por un actor específico:
```sql
SELECT f.title
FROM Film f
JOIN Film_Actor fa ON f.film_id = fa.film_id
JOIN Actor a ON fa.actor_id = a.actor_id
WHERE a.first_name = 'John' AND a.last_name = 'Doe';
```

**3. Actualizar y Eliminar Registros**
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

Las principales **buenas prácticas** en el uso de SQL son:

1. **Utilizar Claves Primarias y Foráneas:** Garantizan la integridad referencial entre tablas relacionadas.
2. **Indexar Columnas:** Mejora el rendimiento de las consultas frecuentes.
3. **Evitar Consultas Sin Filtro:** Siempre incluir condiciones (`WHERE`) para evitar modificaciones o eliminaciones masivas accidentales.
4. **Probar Consultas en Entornos de Prueba:** Asegura que los cambios no afecten datos críticos en producción.

El lenguaje SQL es esencial para interactuar con bases de datos relacionales. Desde la creación de estructuras con DDL hasta la manipulación de datos con DML, SQL ofrece una gama de herramientas que permiten satisfacer las necesidades de almacenamiento y análisis de datos. La base de datos Sakila proporciona un entorno práctico para aprender y aplicar estas herramientas, haciendo que los conceptos se vuelvan tangibles y relevantes para situaciones del mundo real.

Conviene recordar que todas las tecnologías alrededor de las bases de datos han posibilitado la creación de los sistemas empresariales ERP, muy lejos del primer ERP del mundo: El Proyecto LEO. El **Proyecto LEO** (Lyons Electronic Office) desarrolló entre 1949 y 1951, en Gran Bretaña, la primer computadora y **el primer ERP del mundo** para uso civil, que manejó tareas administrativas, como la gestión de inventarios, el procesamiento de pedidos y la nómina de J. Lyons y, de otras compañías, bajo contrato. Ese proyecto marcó el inicio de los sistemas automatizados para la gestión de grandes volúmenes de datos, sentando las bases para los sistemas de bases de datos computarizadas.  El Proyecto LEO se convitió en el *primer servicio de outsourcing* de procesamiento de datos, en el mundo.  

### **5. Conclusiones**

Esta lectura proporciona una visión integral del diseño y manejo de las bases de datos en contextos históricos, conceptuales y prácticos. A lo largo de esta lectura, se ha explorado cómo las bases de datos han evolucionado desde registros manuales y tecnologías pioneras como las tarjetas perforadas de Hollerith, hasta los sofisticados sistemas actuales basados en la nube, inteligencia artificial y blockchain.

Los fundamentos conceptuales, como la jerarquía entre datos, información y conocimiento, y los componentes esenciales de las bases de datos, sientan las bases para comprender cómo estas herramientas transforman datos en conocimiento accionable. Además, se detalla el diseño lógico y físico de bases de datos relacionales, enfatizando la importancia de estructuras organizadas y herramientas prácticas como el modelo entidad-relación (E-R) y los diagramas UML.

El lenguaje SQL, descrito de manera introductoria, destaca por su versatilidad y su capacidad de interactuar con bases de datos mediante sublenguajes como DDL, DML y DCL. Ejemplos prácticos basados en la base de datos Sakila demuestran cómo aplicar sentencias esenciales como `CREATE`, `SELECT`, `INSERT`, `UPDATE` y `DELETE` para gestionar y manipular datos de manera eficiente.

En síntesis, esta lectura subraya que las bases de datos son fundamentales para el manejo de grandes volúmenes de información en la era digital. Al combinar principios de diseño sólido, buenas prácticas y herramientas avanzadas, se pueden crear sistemas de bases de datos confiables y escalables que soporten las necesidades actuales y futuras de las organizaciones.

### **6. Bibliografía básica**

1. Codd, E. F. (1970). A relational model of data for large shared data banks. *Communications of the ACM*, *13*(6), 377-387. [url](https://dl.acm.org/doi/10.1145/362384.362685) 
   - Este artículo seminal introduce el modelo relacional, un pilar fundamental en la teoría y práctica de las bases de datos.

2. DBeaver. *DBeaver Community. Universal Database Tool*. Retrieved December 11, 2024, from [https://sqliteonline.com/](https://sqliteonline.com/).
   - Herramienta gratuita y multiplataforma diseñada para desarrolladores, administradores de bases de datos, analistas y cualquier persona que trabaje con datos. Compatible con bases de datos SQL populares como MySQL, MariaDB, PostgreSQL, SQLite y Apache Family, entre otras, ofrece una solución versátil para la gestión y análisis de datos en diferentes entornos.

3. GitHub. (n.d.). *Sakila database*. Retrieved December 11, 2024, from [https://github.com/jOOQ/sakila/](https://github.com/jOOQ/sakila/) 

4. Mata-Toledo, R., & Cushman, P. (2000). *Schaum's outline of fundamentals of relational databases*. McGraw-Hill.
   - Un texto completo y un recurso excelente para aquellos que buscan una guía accesible y estructurada para dominar los fundamentos de las bases de datos relacionales.

5. Video2Brain, (s.f.). *Fundamentos de la programacion: Bases de datos* (Español). [Curso en video]. [torrent](https://thepiratebay.org/description.php?id=11887748).
   - Curso básico en video.

6. **SQL Tutorial**. SQL cheat sheet. Retrieved December 11, 2024, from [https://www.sqltutorial.org/sql-cheat-sheet/](https://www.sqltutorial.org/sql-cheat-sheet/).
   - Tutorial y tips.

7. **SQLite online**. Retrieved December 11, 2024, from [https://sqliteonline.com/](https://sqliteonline.com/).
   - Base de datos en línea para practicar.
  
--- 

[^1]: Profesor-investigador del Departamento de Economía de la Universidad Autónoma Metropolitana, Unidad Iztapalapa. Contacto: [jzr@xanum.uam.mx](mailto:jzr@xanum.uam.mx), [Telegram](https://t.me/jzavalar).
[^2]: Lectura leída el 11 de diciembre de 2024.

Ultima actualización: 19 de diciembre de 2024.
