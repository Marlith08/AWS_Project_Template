<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>

# <p align= "center"> AWS Step Functions: </p>


## ¿Qué es Step functions?

<p align="justify">Es una herramienta avanzada que nos facilita la coordinación de diversos servicios de AWS a través de flujos de trabajo visuales, permitiendo una gestión detallada de cada etapa del proceso, conocido como estado. Con esta herramienta, es posible diseñar y ejecutar flujos de trabajo que integran servicios como AWS Lambda, Amazon ECS, y AWS Batch, entre otros, de manera eficiente y coherente. Uno de los elementos clave de esta herramienta es su consola visual, la cual permite la monitorización y depuración detallada de la ejecución de los flujos de trabajo. Esta consola ofrece una vista clara del estado actual, los errores y reintentos, así como las salidas de cada estado, facilitando el seguimiento y la resolución de problemas en tiempo real. Asimismo, AWS Step Functions nos permite la creación y modificación de flujos de trabajo mediante la definición de máquinas de estados en JSON. Su capacidad para integrarse con otros servicios AWS y la flexibilidad de sus estados la convierten en una herramienta ideal para manejar flujos de trabajo complejos y automatizar tareas, asegurando un alto nivel de precisión y control en la orquestación de procesos. Por lo tanto, AWS Step Functions no solo optimiza la eficiencia operativa, sino que también mejora significativamente la gestión de tareas en entornos dinámicos y exigentes.</p>



<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/74c9fe2c-08ad-4a90-912c-0a36451ce4d9" height="304">
</p>




## Flujos de trabajo de Step Functions:

- ### Flujos de trabajo estándar:
  <p align="justify">Son adecuados para los flujos de trabajo auditables, duraderos y de ejecución prolongadas, también se puede recuperar su historial completo de ejecución a través de la API step functions, se le puede hacer hasta los 90 días después de que la función se haya ejecutado. Sigue un patrón de que en que las tareas y los estados nunca se ejecuten más de una vez. Este es fundamental para orquestar acciones que no sean idempotentes, como el inicio de cúster de Amazon EMR o el procesamiento de pagos. Pues estes se facturan de acuerdo al número de transiciones de estado que se han procesado.</p>


- ### Flujos de trabajo express:
  <p align="justify">Son adecuados para cargas de trabajo de procesamiento de eventos de volumen elevados, el streaming de transformación y el procesamiento de datos y los bakents de aplicaciones móviles . En este caso existe la posibilidad de que su ejecución se realice más de una vez, lo cual los hace importantes para osquertar acciones indepotentes como la transformación de los dats de entrada y el almacenamiento a traves de PUT  en Amazon DynamonDB. Asimismo, estos se facturan de acuerdo al número de ejecución, la duración de la ejecución y la memoria consiumida durante la ejecución.p>

  - ### Flujos de trabajo express asíncronos.
    * Confirman cuando el flujo de trabajo se ha iniciado, sin que se haya completado.
    * Es necesario verificar el cloudwatch para obtener el resultado.
    * Es ideal cuando no se necesita una salida de respuesta inmediata.

  - ### Flujo de trabajo express sícronos:
    * Espera a que se complete el flujo de trabajo para brindar el resultado deseado.
    * Son ideales para orquestar microservicios.
    * Se puede desarrollar aplicaciones sin la necesidad de desarrollar código adicional.



|                       | Flujos de Trabajo Estándar                                 | Flujos de Trabajo Rápidos                                 |
|-----------------------|------------------------------------------------------------|------------------------------------------------------------|
| **Duración Máxima**   | Un año                                                     | Cinco minutos                                               |
| **Velocidad de Inicio de Ejecución Admitida** | Consultar cuotas relacionadas con la limitación controlada de las acciones de la API | Consultar cuotas relacionadas con la limitación controlada de las acciones de la API |
| **Velocidad de Transición de Estado Admitida** | Consultar cuotas relacionadas con la limitación controlada de estados | Sin límite |
| **Precios**           | Basado en el número de transiciones de estado               | Varía según el número de ejecuciones, duración y consumo de memoria |
| **Historial de Ejecuciones** | Enumeración y descripción con API de Step Functions, depuración visual en la consola, análisis en CloudWatch Logs con registro en la máquina de estado | Enumeración y descripción con API de Step Functions, inspección en CloudWatch Logs con registro en la consola de Step Functions |
| **Semántica de Ejecuciones** | Ejecución del flujo de trabajo exactamente una vez.        | Flujos rápidos asíncronos: ejecución del flujo de trabajo al menos una vez. Flujos rápidos síncronos: ejecución del flujo de trabajo como máximo una vez. |



### Definiciones:
  - **Flujo de trabajo:** Secuencias de pasos.
  - **Estados:** Pasos que se realizan de manera individual en la máquina de estados, que toman decisiones y realizan acciones  de acuerdo a las entradas y pasan a una salida a otros estados.

### Configuración de entrada y salida:
<p align="justify">Puesto que en el caso de step function recibe un archivo JSON como entrada, pues esto lo transfiere dicha entrada al primer estado en el flujo de trabaja, Asi como los estados individuales recieben un archivo JSON como entrada, pues lo pasan de la misma forma como salida para el siguiente estado, por lo cual step function brinda filtros que nos permiten controlar el flujo de datos de entrada y salida entre estados, los cuales son:</p>

  - **InputPath:** Selecciona qué parte de toda la carga de entrada se utilizará como entrada de una tarea.
  - **Parámetros:** Especifica cómo debe de mostrarse la entrada antes de invocar la tarea.
  - **ResultSelector:** Determina que elegir del resultado de una tarea
  - **ResultPath:** Determina dónde colocar el resultado de una tarea
  - **OutputPath:** Determina que enviar al siguiente estado.


### Casos de uso:
<p align="justify">Ya que step functios se centra más en crear y actualizar aplicaciones rápidamente ya que brinda un mayor gestionamiento de las componentes y la lógica de las aplicaciones para que de esa manera pueda escribir menos código. Por lo cual se tienen los cason en los que son más usados step functions:</p>

  - ### Caso de uso n°1: Orquestación de funciones:
    <p align="justify">Esto se basa en crear un flujo de trabajo donde se ejecuta un grupo de funciones lambda es decir pasos que siguen un orden específico. Es decir se recorre de manera secuencial donde al salir de la ejecución de una función lambda se dirige a la entra de la siguiente función y asi sucesivamente y donde el último paso del flujo de trabajo va a arrojar el resultado. Y recuerde que con estep function se puede ver la interacción de cada paso del flujo de trabajo y esto nos permite verificar y asegurarse que se cumplan todos los pasos.</p>
    
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/c047cddf-0a8c-454a-a9b7-2056e87e01c9" width=467" height="284">
</p>

  - ### Caso de uso n°2: Ramificación:
    <p align="justify">Esto se da cuando el cliente requiere un aumento del límite de crédito. Por ejemplo cuando se usa un estado Choice, puede realizar que step functions tome decisiones teniendo en cuenta las aportaciones del estado Choice. Es decir que tengamos un determinado crédito que ya a sido aprobado por el cliente y si la solicitud requerida supera dicho límite step functions envia la solicitud de su cliente para que sea aprobado. En cambio si la solicitud viene a ser menor, pues step functions va a aprobar la solicitud automaticamnete</p>

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/8a35fcb2-4e96-4cf0-98ff-87cf98ae56cd" width=467" height="284">
</p>

  - ### Caso de uso n°3: Gestión de errores:
    * <p align="justify">Retry: puede ser usado en el caso de que un cliente solicita un nombre de usuario, donde la primera vez la solicitud no es válida. Por lo cual mediante Retry puede hacer que Step functions vuelva a intentar la solicitud de su cliente. La primera vez.la solicitud de su cliente es válida.</p>

     * <p align="justify">Catch: tiene un uso similar a retry, donde un cliente solicita un nombre de usuario no disponible, pues haciendo uso de catch step functions va a sugerir un nombre de usuario disponible. hora si el cliente utiliza el nombre de usuario disponible va ha permitir que  step functions pase al siguiente flujo de trabajo que consiste en enviar un coreo de confirmación, en caso contrario step functions se redirigirá a otro paso de flujo de trabajo que tendrá que volver a iniciar el proceso de registro.</p>
     
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/06325052-96f7-4417-bbe4-87ee8ceac490)" width=467" height="284">
</p>

  - ### Caso de uso n°4: Humano en el bucle:
     <p align="justify">Continuando con el ejemplo de se cuenta con una aplicación bancaria , donde un cliente envia dinero a uno de sus amigo. El cliente espera un correo de confirmación. Por lo cual con una llamada o un tokend, step funcions le dice a lambda que envié el dinero a su cliente e informe cuando el amigo de su cliente lo reciba. Es así que, cuando lambda informa que el amigo del cliente ha recibido el respectivo dinero hace uso de step functions pase al siguiente paso de flujo de trabajo que consiste enviar un correo electrónico de confirmación.</p>


<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/d24b9903-b2db-49d5-a28c-c94d62d23ecc" width=467" height="284">
</p>

  - ### Caso de uso n°5: Procesamiento paralelo:
     <p align="justify">En este caso se hace uso de el estado Parallel, por ejemplo se cuenta con un video y un cliente le convierte en cuatro resoluciones de pantallas diferentes para que los espectadores puedan ver el video en varios dispositivos. Por lo cual en step functions introduce el archivo del video para que de esa manera lambda pueda procesarlo en 4 resoluciones de pantalla al mismo tiempo.</p>

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/86fdc5c0-2894-4ef2-ac66-896372f3b636" width=467" height="284">
</p>

  - ### Caso de uso n°6: Paralelismo dinámico:
     <p align="justify">En este caso se hace uso del estado Map, el ejemplo es que un cliente realiza un pedido de tres artículos y deben de realizar la preparación de cada uno de ellos para su respectiva entrega. Por lo cual se comprueba la disponibilidad de cada artículo, reúne cada artículo y a continuación empaqueta cada artículo para su entrega y mediante dicho estado step functions hace que lambda procese en paralelo cada uno de los artículos del cliente, una vez que todos esten empaquetados, step functions pasa al siguiente flujo de trabajo que consiste en enviar un correo de confirmación al cliente y ademas con la respectiva información de seguimiento.</p>

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/55675b5c-91c1-45c4-8d71-0cef4f3193b2" width=467" height="284">
</p>

