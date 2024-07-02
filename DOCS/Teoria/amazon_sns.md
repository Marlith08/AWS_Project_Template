<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>

# <p align="center">AMAZON SNS </p>


## ¿Qué es Amazon SNS?
 <p align="justify">Amazon SNS (Simple Notification Service) es un servicio administrado por AWS que facilita la entrega de mensajes o notificaciones desde los publicadores (fuentes de información) a los suscriptores (destinatarios interesados en recibir dicha información). Es especialmente útil para aplicaciones y sistemas que necesitan enviar actualizaciones en tiempo real a usuarios finales, sistemas internos o servicios externos de manera confiable y escalable.</p>
 
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/6f0d43eb-4ff9-445c-b06a-04f161cb903c" width=467" height="284">
</p>

### Componentes Principales:
  * **Publicadores (Publishers):**
    - Son las entidades que generan mensajes o eventos que deben ser distribuidos a los suscriptores.
    - Pueden ser aplicaciones, sistemas, o cualquier fuente de datos que quiera enviar información a otros.
      
  * **Suscriptores (Subscribers):**
    - Son los destinatarios de los mensajes o notificaciones enviadas por los publicadores.
    - Pueden ser usuarios finales, otras aplicaciones, sistemas, o servicios externos que necesiten estar informados sobre eventos específicos.
      
  * **Tópicos (Topics):**
    - Los mensajes en Amazon SNS se agrupan en "tópicos".
    - Un tópico es como un canal de distribución donde se envían mensajes específicos.
    - Los suscriptores interesados en un tipo particular de mensaje se suscriben a un tópico específico.
      
  * **Entrega de Mensajes:**
    - Cuando un publicador envía un mensaje a un tópico en SNS, el servicio se encarga de entregar el mensaje a todos los suscriptores suscritos a ese tópico.
    -  SNS soporta la entrega de mensajes a través de varios protocolos como HTTP/S, email, mensajes de texto (SMS), y notificaciones móviles (APNs, FCM, etc.).
    -  Los mensajes pueden ser enviados simultáneamente a múltiples suscriptores para asegurar una distribución eficiente y rápida.
       
  * **Flexibilidad:**
    -  SNS ofrece flexibilidad en la forma en que los mensajes son entregados y consumidos.
    -  Permite configurar políticas de filtrado de mensajes y controlar la entrega basada en las preferencias de cada suscriptor.
    -  Soporta integraciones con una amplia gama de plataformas de notificación móvil y servicios de mensajería.

### Casos de Uso Comunes:
  -  *Notificaciones Push:* Envío de notificaciones a dispositivos móviles a través de APNs (Apple Push Notification Service), FCM (Firebase Cloud Messaging), etc.
  -  *Alertas y Monitoreo:* Distribución de alertas y eventos de monitoreo a equipos de operaciones y administradores de sistemas.
  -  *Actualizaciones de Estado:* Informar a usuarios finales sobre cambios en el estado de pedidos, transacciones, o procesos internos.
  -  *Integración de Sistemas:* Comunicación entre diferentes aplicaciones y servicios para mantener sincronizados los datos y eventos.

### Seguridad y Administración:

<p align="justify">Amazon SNS proporciona controles de seguridad robustos, incluyendo la capacidad de gestionar políticas de acceso y autenticación a través de AWS IAM. Además, ofrece funcionalidades avanzadas como el encriptado de mensajes en reposo y en tránsito para asegurar la confidencialidad de los datos.</p>

