EJERCICIO N° 3

Diseña un flujo de trabajo que procese datos en múltiples etapas utilizando Step Functions y Lambda functions.

1,. Nos dirigimos al servicio de Step Function

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.001.png)

2\.- Clik en empezar

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.002.png)

3\.- Clik en “crear la suya propia”

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.003.png)

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.004.png)

4\.- Creamos nuestra máquina de estado

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.005.png)

{

`  `"Comment": "Flujo de trabajo para procesar datos en múltiples etapas",

`  `"StartAt": "Load Data",

`  `"States": {

`    `"Load Data": {

`      `"Type": "Task",

`      `"Resource": "arn:aws:lambda:REGION:ACCOUNT\_ID:function:load\_data",

`      `"Next": "Process Data 1",

`      `"Catch": [

`        `{

`          `"ErrorEquals": [

`            `"States.ALL"

`          `],

`          `"ResultPath": "$.error",

`          `"Next": "Fail"

`        `}

`      `]

`    `},

`    `"Process Data 1": {

`      `"Type": "Task",

`      `"Resource": "arn:aws:lambda:REGION:ACCOUNT\_ID:function:process\_data1",

`      `"Next": "Process Data 2",

`      `"Catch": [

`        `{

`          `"ErrorEquals": [

`            `"States.ALL"

`          `],

`          `"ResultPath": "$.error",

`          `"Next": "Fail"

`        `}

`      `]

`    `},

`    `"Process Data 2": {

`      `"Type": "Task",

`      `"Resource": "arn:aws:lambda:REGION:ACCOUNT\_ID:function:process\_data2",

`      `"Next": "Store Data",

`      `"Catch": [

`        `{

`          `"ErrorEquals": [

`            `"States.ALL"

`          `],

`          `"ResultPath": "$.error",

`          `"Next": "Fail"

`        `}

`      `]

`    `},

`    `"Store Data": {

`      `"Type": "Task",

`      `"Resource": "arn:aws:lambda:REGION:ACCOUNT\_ID:function:store\_data",

`      `"Catch": [

`        `{

`          `"ErrorEquals": [

`            `"States.ALL"

`          `],

`          `"ResultPath": "$.error",

`          `"Next": "Fail"

`        `}

`      `],

`      `"End": true

`    `},

`    `"Fail": {

`      `"Type": "Fail",

`      `"Cause": "Data processing failed",

`      `"Error": "ProcessingError"

`    `}

`  `}

}

5\.- Clik en crear

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.006.png)

6\.-No tenemos permitido crear una maquina de estado

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.007.png)

7\.-Revisamos el servicio Lambda

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.008.png)

8\.- Clik en “crear una función”

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.009.png)

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.010.png)

9\.- No tenemos el permiso de crear una función

![](Aspose.Words.4925f37a-a0ce-4a8d-affa-c69f35eecb05.011.png)
