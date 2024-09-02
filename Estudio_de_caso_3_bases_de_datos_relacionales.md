# **Estudio de Caso 3: Bases de Datos Relacionales**

## **Introducción**

Una *base de datos relacional* es una forma de organizar y almacenar datos en una base de datos, utilizando *tablas*, *filas* y *columnas*. Estas bases de datos se caracterizan por su capacidad para relacionar datos entre sí, lo que permite la creación de *consultas* complejas y la resolución de problemas de negocio. Las *bases de datos relacionales* tienen varias *ventajas*, como la capacidad para manejar grandes cantidades de datos, la seguridad y la escalabilidad. Sin embargo, también tienen algunas *desventajas*, como la complejidad en su diseño y la necesidad de un buen conocimiento del lenguaje SQL.

Las bases de datos relacionales son ideales para *aplicaciones* o *sistemas de información* que requieren la manipulación y análisis de grandes cantidades de datos, como sistemas de gestión de inventarios, sistemas de información de clientes, sistemas de gestión de recursos humanos, entre otros.

## **Preguntas guía**

1. ¿Cuáles son las características clave de las bases de datos relacionales y cómo se benefician las organizaciones al utilizarlas?
2. ¿Cómo se implementa la integridad referencial en una base de datos relacional y cuál es el papel que juegan las llaves primarias y llaves foráneas?
3. ¿Qué es un lenguaje SQL y cómo se utiliza para interactuar con una base de datos relacional?

## **Diseño de las bases de datos relacionales**

Un *diseño* adecuado es fundamental para la creación efectiva de una base de datos relacional. El diseño debe considerar los requisitos del negocio y los límites técnicos del sistema.

La base de datos *Sakila* es un ejemplo clásico de un *diseño relacional* bien hecho. Contiene varias *tablas* que se relacionan entre sí, como `film`, `film_actor`, `inventory`, `payment`, `rental`, `staff`, `store` y `customer`.

## **Integridad referencial**

La *integridad referencial* es una característica fundamental en las bases de datos relacionales. Permite garantizar que los *datos* sean *coherentes* y *consistentes*.

En Sakila, las *llaves primarias (PK)* se utilizan para identificar único cada registro en una tabla. Las *llaves foráneas* (FK) se utilizan para establecer relaciones entre tablas.

Por ejemplo, en la tabla `film_actor`, la columna `film_id` es una llave foránea que se refiere a la tabla `film`. Esto significa que cada registro en la tabla `film_actor` se refiere a un filme específico en la tabla `film`.

## **Transacciones en una base de datos**

Las *operaciones ACID* (*A*tomicidad, *C*onsistencia, *I*solation (a*I*slamiento), *D*urabilidad) garantizan que las *transacciones* en una base de datos sean seguras y confiables. *Atomicidad*: La transacción se considera como un todo o no se ejecuta. *Consistencia*: La transacción mantiene la consistencia del estado actual. *Isolation* (AIsalamiento): La transacción se ejecuta aislada del resto del sistema. *Durabilidad*: La transacción es permanente y no se pierde en caso de error.

El *commit* es el proceso de *confirmar* una transacción después de que se haya completado con éxito. El *rollback* es el proceso de cancelar una transacción después de que se haya producido un error.

## **Lenguaje SQL**

El *lenguaje SQL* (*S*tructured *Q*uery *L*anguage, Lenguaje de Consulta Estructurado) es utilizado para interactuar con las bases de datos relacionales. Permite *crear*, *modificar* y *consultar* los datos almacenados en la base de datos.

Ejemplo ilustrativo:
```sql
SELECT * FROM film
WHERE title LIKE 'Toy%';
```
Este ejemplo selecciona todos los registros en la tabla `film` donde el título comience con "Toy".

## **Implementación de las bases de datos**

La *implementación* o *implantación* de una base de datos se refiere al proceso de creación y configuración de una base de datos para que pueda ser utilizada en un sistema o aplicación. Esto implica varios pasos, como:

- *Diseño*: Se diseña la estructura y la organización de los datos en la base de datos.
- *Creación*: Se crea la base de datos utilizando un sistema de gestión de bases de datos como MySQL, PostgreSQL, Oracle, etc.
- *Carga de datos*: Se cargan los datos iniciales en la base de datos, ya sean desde un archivo o a través de una interfaz de usuario.
- *Configuración*: Se configura la base de datos para que se ajuste a las necesidades del sistema o aplicación, incluyendo la configuración de los permisos, la indexing, la caching, etc.
- *Pruebas*: Se realizan pruebas para verificar que la base de datos esté funcionando correctamente y que se ajuste a las necesidades del sistema o aplicación.

La implementación de una base de datos es importante porque garantiza que la base de datos esté lista para ser utilizada y que los datos estén organizados y accesibles de manera eficiente.

**Implementación de Sakila en SQLite3 en Windows**

Para implementar Sakila en SQLite3 en Windows 7 x32 bits, sigue los siguientes pasos:

1. Descarga e instala SQLite3 desde el sitio web oficial.
2. Abre el editor SQLite3 (por ejemplo, DB Browser for SQLite).
3. Crea una nueva base de datos llamada "sakila".
4. Carga el script SQL que contiene la definición de las tablas y los datos.
5. Ejecuta el script para crear las tablas.
6. Agrega los datos a las tablas utilizando consultas SQL.

### **Automatización de la implementación de Sakila**

También, puedes utilizar el siguiente script en Python para automatizar la implementación con el **script_implementacion.py**:

```python
import os
import urllib.request
import sqlite3

# Mensaje de bienvenida
print("Bienvenido al script de implementación de Sakila")
print("Este script descarga la base de datos Sakila, la carga en SQLite3 y la pobla con datos")

# Descarga la base de datos Sakila
urllib.request.urlretrieve("https://github.com/mysql/mysql-sqlite-common-tasks/raw/master/sakila.db", "sakila.db")

# Prepara el entorno para crear y cargar la base de datos
conn = sqlite3.connect('sakila.db')
cursor = conn.cursor()

# Ejecuta el script SQL oficial de Sakila para poblar la base de datos
cursor.execute(open("sakila.sql", "r").read())

# Comprometer los cambios
conn.commit()

# Mensaje de finalización
print("La base de datos Sakila ha sido implementada con éxito")
print("Puedes utilizar la base de datos con SQLite3 o un cliente SQL")
```
### **Carga de datos con archivos CSV**

Los *archivos CSV* (Comma Separated Values), también se utilizan para cargar datos en una base de datos relacional de varias maneras:

- *Importación*: Los archivos CSV se importan en la base de datos utilizando herramientas como `mysqlimport`, `pgloader`, `psql`, etc. Estas herramientas leen los archivos CSV y los cargan en la base de datos según la estructura y los esquemas especificados.
- **Cargar datos*: Los archivos CSV se cargan utilizando sentencias SQL como `LOAD DATA` en MySQL o `COPY` en PostgreSQL. Estas sentencias leen los archivos CSV y los cargan en la base de datos.
- *Herramientas de importación*: Los archivos CSV se cargan utilizando herramientas de terceros como Talend, Informatica, Microsoft Power Query, etc. Estas herramientas ofrecen interfaces gráficas y opciones de configuración para cargar los datos en la base de datos.

El proceso general es el siguiente:

1. *Preparar el archivo CSV*: El archivo CSV debe tener la estructura correcta y los datos debidamente formateados.
2. *Conectarse a la base de datos*: Se conecta a la base de datos utilizando un cliente de bases de datos o una herramienta de importación.
3. *Especificar la fuente de datos*: Se especifica el archivo CSV como fuente de datos.
4. *Configurar la importación*: Se configura la importación, incluyendo opciones como la tabla destino, el esquema de columnas, el tipo de dato, etc.
5. *Ejecutar la importación*: Se ejecuta la importación y se cargan los datos en la base de datos.

Es importante tener en cuenta que antes de cargar un archivo CSV, *es importante verificar la estructura y la integridad de los datos* para asegurarse de que sean correctos y compatibles con la base de datos.

### **Operaciones del script **sakila.sql** 

El archivo SQL oficial de Sakila contiene algunas de estas operaciones, como las que se ilustran a continuación:
**Nota:** No se ejecute.

```sql
-- sakila.sql

-- Create table `film`
CREATE TABLE `film` (
  `film_id` smallint(5) unsigned NOT NULL auto_increment,
  `title` varchar(100) NOT NULL,
  `description` text,
  `release_year` year(4) NOT NULL,
  `language_id` smallint(6) NOT NULL,
  PRIMARY KEY  (`film_id`)
);

-- Insert data into tables
INSERT INTO film (title, description, release_year, language_id)
VALUES ('Toy Story', 'Un film sobre juguetes', '1995', '1'),
       ('Toy Story', 'Un film sobre juguetes', '1995', '1'),
       ('Toy Story', 'Un film sobre juguetes', '1995', '1');

```

## **Uso de la base de datos**

A continuación está un script interactivo en Python que permite realizar operaciones básicas sobre la base de datos. Este script interactivo permite mostrar todas las filas de la tabla film, mostrar los actores que han participado en un filme específico y mostrar los clientes que han alquilado un filme específico.

```python
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('sakila.db')
cursor = conn.cursor()

# Mostrar todas las filas de la tabla film
print("Todas las filas de la tabla film:")
cursor.execute("SELECT * FROM film")
films = cursor.fetchall()
for film in films:
    print(film)

# Mostrar los actores que han participado en un filme específico
print("\nActores que han participado en el filme Toy Story:")
cursor.execute("SELECT a.actor_name FROM film_actor fa JOIN actor a ON fa.actor_id = a.actor_id WHERE fa.film_title = 'Toy Story'")
actors = cursor.fetchall()
for actor in actors:
    print(actor)

# Mostrar los clientes que han alquilado un filme específico
print("\nClientes que han alquilado el filme Toy Story:")
cursor.execute("SELECT c.customer_name FROM rental r JOIN customer c ON r.customer_id = c.customer_id WHERE r.inventory_title = 'Toy Story'")
customers = cursor.fetchall()
for customer in customers:
    print(customer)

# Cerrar conexión
conn.close()
```

## **Conclusión**

En este estudio de caso, hemos visto cómo las bases de datos relacionales pueden ser diseñadas y implementadas utilizando el lenguaje SQL. La integridad referencial y las operaciones ACID son fundamentales para garantizar la consistencia y seguridad del sistema. La implantación correcta de una base de datos relacional puede ser un desafío técnico, pero resolverlo se vuelve muy útil para las organizaciones al permitirles almacenar y analizar grandes cantidades de datos.

Este estudio ha proporcionado una visión general sobre las bases de datos relacionales y su potencial en la implantación de **sistemas de información** efectivos.
