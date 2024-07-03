<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>


# <p align="center">DynamoDB</p>

## ¿Qué es Amazon DynamoDB?
 <p align="justify">Amazon DynamoDB es un servicio de base de datos NoSQL totalmente administrado y escalable ofrecido por Amazon Web Services (AWS). Está diseñado para proporcionar un rendimiento rápido y predecible con baja latencia, siendo ideal para aplicaciones que requieren respuestas rápidas y escalabilidad automática.</p>

 <p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/ea718dc0-b207-42f2-b564-af1cf247e7bd" width=267" height="484">
</p>

### Características Principales:
  * **Escalabilidad Automática:** DynamoDB puede manejar automáticamente aumentos en el tráfico de solicitudes ajustando la capacidad de las tablas según la demanda. Esto asegura que las aplicaciones funcionen sin interrupciones, desde unas pocas solicitudes por segundo hasta millones.
    
  *  **Alta Disponibilidad y Durabilidad:** Los datos en DynamoDB se replican automáticamente en múltiples centros de datos dentro de una región de AWS, garantizando disponibilidad continua y protección contra fallos de hardware.
Modelo de Datos y Consistencia: Soporta modelos de datos flexibles y esquemas dinámicos, permitiendo almacenar y recuperar cualquier cantidad de datos. Ofrece consistencia eventual y fuerte para adaptarse a diferentes necesidades de las aplicaciones.
  * **Transacciones ACID:** Permite ejecutar operaciones atómicas, consistentes, aisladas y duraderas en múltiples ítems dentro de una tabla, garantizando la integridad de los datos.
    
  *  **Integración con Servicios AWS:** Se integra fácilmente con otros servicios de AWS como Lambda, API Gateway, S3 y Redshift, facilitando la construcción de aplicaciones complejas y escalables.
    
  * **Cifrado y Seguridad:** Proporciona cifrado en reposo para proteger los datos sensibles almacenados en la base de datos.
  
  * **Modelo de Precios Basado en el Consumo:** Ofrece opciones de capacidad provisionada y modo de capacidad bajo demanda, permitiendo pagar solo por la capacidad de lectura y escritura utilizada.

### Tipos de Tablas en DynamoDB:
  - **Tablas Estándar:** Son las tablas básicas que almacenan y recuperan cualquier cantidad de datos, con un modelo de tarifas basado en la capacidad.
    
  -  **Índices Globales y Locales:** Permiten crear índices para mejorar el rendimiento de las consultas. Los índices globales pueden abarcar toda la tabla, mientras que los índices locales están limitados a rangos de partición.

### Ventajas:
  - Escalabilidad Automática: Capacidad para manejar picos de tráfico sin intervención manual.
  - Rendimiento Predecible: Baja latencia y alta velocidad de respuesta para consultas.
  - Integración con AWS: Facilita la construcción de arquitecturas de aplicaciones complejas.
  - Seguridad y Cumplimiento: Ofrece cifrado en reposo y cumplimiento de normativas de seguridad.

### Desventajas:
  - Costo: Puede resultar costoso en comparación con soluciones NoSQL autohospedadas en ciertos escenarios.
  - Complejidad de Modelado: La gestión de esquemas dinámicos puede requerir una planificación cuidadosa.


## Estructura de Amazon DynamoDB

- **Tablas:** Son similares a las tablas en bases de datos relacionales. Cada tabla está compuesta por ítems.

- **Ítems:** Son instancias individuales de datos en una tabla. Cada ítem es una colección de atributos, donde cada atributo tiene un nombre único.

- **Atributos:** Son los datos individuales dentro de un ítem. Cada atributo tiene un nombre y un valor.

- **Claves:** DynamoDB utiliza dos tipos de claves principales para identificar ítems de manera única:
  - **Clave de partición:** Un único atributo simple que sirve como clave de partición. DynamoDB utiliza el valor de este atributo como entrada en una función hash para determinar la partición donde se almacenará el ítem.
  - **Clave de ordenación (opcional):** Un segundo atributo opcional que ordena los ítems con la misma clave de partición. DynamoDB almacena todos los ítems con la misma clave de partición juntos y en orden ordenado por el valor de la clave de ordenación.

- **Índices:** DynamoDB admite índices locales y globales para permitir diferentes patrones de acceso a los datos:
  - Los **índices locales** están limitados a una única partición de tabla y mejoran la eficiencia de las consultas dentro de esa partición.
  - Los **índices globales** permiten búsquedas eficientes en toda la tabla, abarcando múltiples particiones.

- **Capacidades:** Permite configurar la capacidad de lectura y escritura para cada tabla, determinando cuántas operaciones de lectura y escritura por segundo puede manejar la tabla.

- **Consistencia:** DynamoDB ofrece dos modelos de consistencia:
  - **Consistencia eventual:** Permite lecturas rápidas y consistentes, donde los datos pueden tardar un tiempo en propagarse.
  - **Consistencia fuerte:** Garantiza que todas las lecturas reflejen las escrituras más recientes, ofreciendo consistencia inmediata.

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/9caa1fd3-71ee-4e45-b29a-a9e396c36536" width=650" height="384">
</p>

##  Referencia:

[Amazon.com](https://aws.amazon.com/es/blogs/aws/fine-grained-access-control-for-amazon-dynamodb/)

[Sopin, S. (2021, marzo 23). Potential pitfalls with DynamoDB. SERGII SOPIN.]( https://sopin.dev/2021/03/22/Should-Amazon-DynamoDB-be-your-default-database-choice-when-architecting-on-AWS/)

[Amazon.com](https://docs.aws.amazon.com/es_es/amazondynamodb/latest/developerguide/Introduction.html)

[Amazon.com](https://docs.aws.amazon.com/es_es/amazondynamodb/latest/developerguide/dynamodb-dg.pdf#Introduction)

