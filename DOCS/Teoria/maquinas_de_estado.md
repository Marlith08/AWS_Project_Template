<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>

 
 
 
 # <p align="center">MAQUINA DE ESTADO</p>

## ¿Que es una máquina de estado?

 <p align="justify">Una máquina de estado es un modelo conceptual esencial en la gestión de sistemas complejos, estructurado en una serie de estados o pasos interconectados. Cada estado desempeña una función específica y se organiza de manera lógica para completar procesos más complejos. Esta estructura puede ser representada mediante un diagrama visual o un archivo JSON, que detalla cómo el sistema responde a diferentes eventos. Cada estado puede realizar tareas operativas como invocar funciones Lambda, tomar decisiones basadas en datos, esperar intervalos definidos, manejar excepciones, o ejecutar procesos en paralelo.Pero, estos estados no solo son acciones aisladas, sino que también pueden integrar servicios adicionales de AWS como almacenamiento en S3, bases de datos en DynamoDB, o procesamiento en AWS Glue, entre otros. Esta integración facilita la automatización de flujos de trabajo complejos y garantiza un alto nivel de precisión y control durante la ejecución de tareas. Para optimizar la eficiencia operativa y la respuesta a situaciones adversas en entornos altamente dinámicos y exigentes debemos tener una definición clara de cada estado y cómo va a interactuar.</p>

## Estructura de una maquina de estado:
Una maquina de estado se define utilizando un texto JSON lo cual contiene los siguientes pasos:
  - **Comment (opcional):** Descripción en lenguaje natural de la maquina de estado.
  - **StarAt(Obligatorio):** Cadena que debe de coincidir exactamente mayusculas y minisculas con el nombre de uno de los objetos de estado.
  - **TimeoutSeconds(Opcional):** Numerosos máximo de segundo que puede tarde una ejecución de la maquina de estado.
  - **Versin(Opsional):** Version de Amazon State Lenguaje que se utiliza en la máquina de estado (el valor predeterminado es “1,0”
  - **States(Obligatorio):** Se implementan ls estados.

## Ejemplo de una máquina de estado
   
        { "Comment": "A Hello World example of the Amazon States Language using a Pass state", 
        "StartAt": "HelloWorld", 
        "States": { 
        "HelloWorld": { 
        "Type": "Pass", 
        "Result": "Hello World!", 
        "End": true 
        } 
        }
        }


# <p align="center">ESTADO</p>

## ¿Qué es un estado?

 <p align="justify">Los estados vienen a ser los elementos de una maquina de estado, Los estados pueden ser una cadena, pero teniendo en cuenta que deben de ser únicos dentro de ámbito de toda la maquina de estado.Ls estados individuales tienden a tomar decisiones considerando su entrada, y transferir la salida a tros estados.</p>

  - ### Implementación:
                { "Comment": "A Hello World example of the Amazon States Language using a Pass state", 
                "StartAt": "HelloWorld", 
                **"States":** { 
                "HelloWorld": { 
                "Type": "Pass", 
                "Result": "Hello World!", 
                "End": true 
                } 
                }
                 }

  - ### En la máquina de estado la parte de estates va a contener los estados:
                  {
                  "State1" : { 
                  },
                   "State2" : {
                   }, 
                  ... 
                  }

### Funciones de un estado en una máquina de estado:

  - ### **Task:** 
Puede realiza alguna tarea en la máquina de estado, es decir va ha representar una única unidad de trabajo realizada por la máquina de estado.

    **Ejemplo:**
          "Lambda Invoke": { 
          "Type": "Task", 
          "Resource": "arn:aws:states:::lambda:invoke", 
          "Parameters": { 
          "Payload.$": "$", 
          "FunctionName":"arn:aws:lambda:us-east-2:123456789012:function:HelloFunction: $LATEST" 
          },
           "End": true 
          }

  - ### **Choice:** 
Puede tomar una decisión entre las ramificaciones de una ejecución y cuando encuentra un error, detendrá la ejecución

## Campos de choice:

* **Choices(obligatorio):** Es una matriz de reglas de choice que determina que estado provoca que la máquina de estado adopte el siguiente estado. Debe de definir al menos una regla de estado.
* **Default(opcional,recomendada):** Nombre de estado que se va adoptar si no tiene ninguna de las transiciones de Choices.

### Reglas:
  * Un estado Choice debe tener un campo Choice cuyo valor sea una matriz no vacia. Donde cada elemento de esta matriz es un objeto llamado Choice que contiene lo sigiente: 
  * Una comaración: permite la comparación ente dos variables, teniendo en cuenta el tipo de comparacióny el valor con el que se va a comparar la variable de entrada.
  * Un campo Next: el valor de ese campo debe de coincidir con el nombre del estado que se encuentra en la máquina de estado.

### Ejemplo de implementación:

          {
            "StartAt": "CheckValue",
            "States": {
              "CheckValue": {
                "Type": "Choice",
                "Choices": [
                  {
                    "Variable": "$.value",
                    "NumericGreaterThan": 100,
                    "Next": "GreaterThan100"
                  },
                  {
                    "Variable": "$.value",
                    "NumericEquals": 100,
                    "Next": "Equals100"
                  }
                ],
                "Default": "DefaultState"
              },
              "GreaterThan100": {
                "Type": "Pass",
                "Result": "Mayor que 100",
                "End": true
              },
              "Equals100": {
                "Type": "Pass",
                "Result": "Igual a 100",
                "End": true
              },
              "DefaultState": {
                "Type": "Fail",
                "Error": "InvalidValueError",
                "Cause": "Valor no cumple ninguna condición"
              }
            }
          }

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/c0ae13ca-6e20-49f0-95b1-92b50f2966b0" width="700" height="400">
</p>


  - ### **Fail** o **Succeed:**:
Puede detener una ejecución con errores o con éxito.

### Ejemplo de implementación de Succeed:
        "SuccessState": { 
        "Type": "Succeed" 
        } 

### Campos de Fail:

  * **Cause (Opcional):** Describe la causa del error.
  * **CausePath(Opcional):** Detalla de forma dinámica la causa del error.
  * **Error(opcional):** Un nombre de error que pueda proporcionar para gestionar los errores mediante los campos Retry o Catch.
  * **ErrorPath(opcional):** Proporcionar un nobre al error de forma dinámica 

### Ejemplo de su implementación:

      "FailState": { 
       	"Type": "Fail",
       "CausePath": "$.Cause", 
      "ErrorPath": "$.Error" 
      } 

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/cd5364b0-57b5-43db-8814-9ea10544697d" width="700" height="400">
</p>

  - ### **Pass:**
Puede transferir su entrada a su salida o insertar ciertos datos fijos en el flujo de trabajo, es decir pasa los datos de la entrada  ala salida sin realizar ninguna tarea.

### Campos de estado Pass:

  * **Result(opcional):** Hace referencia al resultado de una tarea virtual que se pasa al siguiente estado.
  * ** ResultPath(opcional):** Especifica donde colocar la salida, teniendo en cuenta la entrada , de la tarea virtual especificada en result.
  * **Parameters(opcional):** Crea una colección de pares de valores de clave que se pasarán como entrada.

### Ejemplo:
        "No-op": { 
        "Type": "Pass", 
        "Result": { 
        "x-datum": 0.381018, 
        "y-datum": 622.2269926397355 
        },
         "ResultPath": "$.coords",
         "End": true 
        }

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/031b8c32-9f90-47ae-9184-aec60dc7c1e1" width="700" height="400">
</p>


  - ### **Wait:**
Puede proporcionar un retraso que dure con tiempo o hasta una fecha u hora determinada

### Campos de Wait:
  * **Seconds:** Tiempo en segundos, tiene que ser un valor entero positivo entre 0 y 99999999
  * **Timestamp:** Tiempo absoluto, va a esperar que comience el estado específic en el campo Next. Esta debe de estar ajustada al perfil RFC3339 de ISO 8601 fecha y hora debe de separarse por T y se usa Z para indicar que no se hace uso de un ajuste numérico, ejemplo: 2024-06-30T03:06:00Z.
  * **SecondsPath:** Tiempo en segundo que se esperará hasta que comience el estado especificado en el camp Next.
  * **TimestampPath:** Tiempo absolut que se va esperar a que comience el estado específico en el campo Next.

### Ejemplo de implementación:

#### Ejemplo 1:
      "wait_ten_seconds": { 
      "Type": "Wait", 
      "Seconds": 10,  
      "Next": "NextState" 
      }

#### Ejemplo2:
      "wait_until" : { 
      "Type": "Wait", 
      "Timestamp": "2024-03-14T01:59:00Z", 
      "Next": "NextState" 
      }

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/3fce69cc-a14e-4917-9da8-fadabd39f073" width="700" height="400">
</p>

  - ### **Parallel:**
Puede iniciar notificaciones en ejecuciones paralelas

### Campos de parallel:
  * **Branches(Obligatorio):** Matriz de objetos que especifíca las máquinas de estado que se ejecutaran en paralelo.
  * **ResultPath(opcional):** Especifica en que lugar de los datos de entrada se va a situal la salida de ramificación.
  * **ResultSelector(opcinal):** Pase a un conjunto de pares clave-valor, donde los valores sean etáticos o se seleccionen del resultado.
  * **Retry(opcional):** Una matriz de objetos, llamados "reintentadores", que definen una política de reintentos en caso de que el estado encuentre errores en tiempo de ejecución.
  * **Catch(opcional):** Una matriz de objetos, denominados "receptores", que definen un estado alternativo que se ejecuta si el estado encuentra errores en tiempo de ejecución y su política de reintentos está agotada o no se ha definido.

### Ejemplo de implementación:
      {
        "Comment": "Parallel Example.",
        "StartAt": "LookupCustomerInfo",
        "States": {
          "LookupCustomerInfo": {
            "Type": "Parallel",
            "End": true,
            "Branches": [
              {
                "StartAt": "LookupAddress",
                "States": {
                  "LookupAddress": {
                    "Type": "Task",
                    "Resource": "arn:aws:lambda:us-east-1:123456789012:function:AddressFinder",
                    "End": true
                  }
                }
              },
              {
                "StartAt": "LookupPhone",
                "States": {
                  "LookupPhone": {
                    "Type": "Task",
                    "Resource": "arn:aws:lambda:us-east-1:123456789012:function:PhoneFinder",
                    "End": true
                  }
                }
              }
            ]
          }
        }
      }


<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/37bb12be-3c3b-4b3c-9627-bb579c1f21d7" width="700" height="400">
</p>


  - ### **Map:**
Puede iterar pasos de forma dinámica

### Modos de procesamiento de estados Map:
  * **En lineal:**
    * Modo de simultaneidad limitada.
    * Acepta una matriz JSON cmo entrada
    * Admite 40 iteraciones simultáneas

  * **Distribuido:**
    *  Modo de alta simultaneidad
    *  Acepta hasta 10000 ejecuciones de flujo de trabajo secundarios en paralelo.
    *  Admite una matriz JSON, o un origen de Amazon S3 como archivo CSV.
    *  Orquestar cargas de trabajo paralelo
    *  Se puede especificar la cantidad de elementos con errores a tolerar

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/271966fb-1184-41be-9f94-50a31b621ffe" width="700" height="400">
</p>


### Reglas para aplicar los estados en una maquina de estado:
  *  Los estamos no cumplen un orden específico ya que no afecta esto al momento de ser ejecutado.
  *  En la máquina de estado solamento puede haber un estad designado cmo start (StarAt).
  *  Los estados que tienen un campo End igual a True se consideran estados end.
  *  Si la máquina  de estado se compone de un solo estado puede ser tanto el estado start o end.

### Campos de estados comunes:
  * **Type(Obligatrio):** Brinda el tipo de estado
  * **Next:** Brinda el nombre del siguiente estado a ejecutar, algunos tipos com choice permite varios estados de transición. Si es el último estado no es necesario colocar next.
  *  **End:** Es un estado terminal si se encuentra establecido como true. Puede existir un número cualquiera de estados terminales por máquina de estado. Solo se puede utilizar nex o end en un estado.



