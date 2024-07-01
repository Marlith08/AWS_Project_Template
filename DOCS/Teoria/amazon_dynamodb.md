# <p align="center">DynamoDB</p>

## ¿Qué es Amazon DynamoDB?
 <p align="justify">Amazon DynamoDB es un servicio de base de datos NoSQL totalmente administrado y escalable ofrecido por Amazon Web Services (AWS). Está diseñado para proporcionar un rendimiento rápido y predecible con baja latencia, siendo ideal para aplicaciones que requieren respuestas rápidas y escalabilidad automática.</p>
 
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


