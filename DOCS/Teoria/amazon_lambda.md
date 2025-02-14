<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>


#  <p align="center">Amazon Lambda</p>

## ¿Qué es AWS Lambda?
 <p align="justify">AWS Lambda es un servicio de computación sin servidor proporcionado por Amazon Web Services (AWS). Permite ejecutar código de forma automática y escalable en la nube sin la necesidad de aprovisionar ni gestionar servidores. Es ideal para aplicaciones y servicios que requieren una respuesta rápida a eventos y una escalabilidad automática.</p>

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/e51f9fa0-5b42-42f1-8e7f-988c47923485" width=467" height="184">
</p>

## Características Principales

  - ### Computación Sin Servidor
    - AWS Lambda elimina la necesidad de administrar servidores subyacentes, permitiendo a los desarrolladores centrarse en la lógica de negocio.
    - El código se ejecuta en respuesta a eventos específicos, como cargas de archivos en Amazon S3, cambios en bases de datos DynamoDB, o eventos de servicios de AWS como SNS o API Gateway.

  - ### Integraciones y Casos de Uso
    - **Aplicaciones Web y Móviles**: Lambda se utiliza en el backend para procesar solicitudes HTTP a través de Amazon API Gateway.
    - **IoT (Internet de las Cosas)**: Puede integrarse con servicios IoT de AWS para procesar datos y comandos de dispositivos conectados.
    - **Procesamiento de Datos**: Es utilizado para el procesamiento de datos en tiempo real, análisis de logs, y más.

  - ### Escalabilidad Automática
    - Lambda escala automáticamente según la cantidad de eventos recibidos. No hay necesidad de aprovisionar capacidad adicional.
    - Cada ejecución de función Lambda es independiente y se gestiona en paralelo, permitiendo manejar desde unas pocas invocaciones por segundo hasta miles.

  - ### Precios
    - Se factura por el tiempo de ejecución y el número de invocaciones, con una facturación precisa basada en el uso real.
    - No hay costos asociados cuando no hay eventos o demanda, lo que optimiza los costos operativos.

  - ### Integración con Servicios AWS
    - Se integra estrechamente con otros servicios de AWS como Amazon S3, DynamoDB, SNS, API Gateway, y más, facilitando la creación de aplicaciones complejas y escalables.

  - ### Seguridad y Gestión
    - Lambda ofrece configuraciones de seguridad como el acceso basado en roles mediante AWS IAM.
    - Los logs de ejecución y las métricas de desempeño se gestionan automáticamente y están disponibles a través de Amazon CloudWatch.

## Ejemplo de Uso
<p align="justify">Imagina una aplicación que recibe imágenes de usuarios y necesita redimensionarlas automáticamente. Puedes configurar una función Lambda para procesar cada imagen nueva que se cargue en un bucket de Amazon S3, redimensionándola y guardándola de nuevo sin necesidad de provisionar o gestionar servidores dedicados para esta tarea.</p>

## Beneficios
- **Reducción de la Complejidad Operativa**: Elimina la gestión de infraestructura y reduce el tiempo dedicado a operaciones.
- **Escalabilidad Automática**: Maneja automáticamente picos de carga sin intervención manual.
- **Eficiencia y Costo**: Optimiza los costos al facturar solo por el uso real de recursos.


## Referencias
[Amazon](https://aws.amazon.com/es/lambda/)

[Amazon](https://docs.aws.amazon.com/es_es/lambda/latest/dg/lambda-dg.pdf#welcome)


