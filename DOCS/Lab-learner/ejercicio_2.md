EJERCICIO N° 2

Desarrolla una máquina de estado que incluya estados de tarea y pasarela. Implementa estos estados utilizando Python y AWS SDK.

Añade estados de espera y elección a la máquina de estado. Utiliza condiciones para decidir el flujo de trabajo.

1,. Nos dirigimos al servicio de Step Function


![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.001.png)

2\.- Clik en empezar

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.002.png)

3\.- Clik en “crear la suya propia”![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.003.png)

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.004.png)

4\.- Creamos nuestra máquina de estado

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.005.png)

5\.- Clik en crear

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.006.png)

{

`  `"Comment": "A description of my state machine",

`  `"StartAt": "Wait",

`  `"States": {

`    `"Wait": {

`      `"Type": "Wait",

`      `"Seconds": 5,

`      `"Next": "Choice"

`    `},

`    `"Choice": {

`      `"Type": "Choice",

`      `"Choices": [

`        `{

`          `"Variable": "$.condition",

`          `"BooleanEquals": true,

`          `"Next": "Pass"

`        `}

`      `],

`      `"Default": "Parallel"

`    `},

`    `"Pass": {

`      `"Type": "Pass",

`      `"End": true

`    `},

`    `"Parallel": {

`      `"Type": "Parallel",

`      `"Branches": [

`        `{

`          `"StartAt": "Cargar datos",

`          `"States": {

`            `"Cargar datos": {

`              `"Type": "Pass",

`              `"End": true

`            `}

`          `}

`        `},

`        `{

`          `"StartAt": "Limpiar datos",

`          `"States": {

`            `"Limpiar datos": {

`              `"Type": "Pass",

`              `"End": true

`            `}

`          `}

`        `},

`        `{

`          `"StartAt": "Analizar datos",

`          `"States": {

`            `"Analizar datos": {

`              `"Type": "Pass",

`              `"End": true

`            `}

`          `}

`        `}

`      `],

`      `"End": true

`    `}

`  `}

}


6\.-Clik en confirmar

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.007.png)

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.008.png)

7\.- Verificamos el servicio IAM

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.009.png)

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.010.png)

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.011.png)

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.012.png)

8\.- No tenemos acceso para crear un rol.

![](Aspose.Words.a6f876ff-b55e-4bc6-a7e7-094989c45c44.013.png)
