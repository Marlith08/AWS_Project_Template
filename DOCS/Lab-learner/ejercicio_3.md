<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>
 
 
 # <p align="center"> EJERCICIO N° 3 </p>

#### Diseña un flujo de trabajo que procese datos en múltiples etapas utilizando Step Functions y Lambda functions.

### 1,. Nos dirigimos al servicio de Step Function
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/97ff8727-1f3f-4405-836e-59239ad8273a" width="700" height="400">
</p>

### 2\.- Clik en empezar

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/1607a829-1e12-4240-abe6-b07ae2b83248" width="700" height="400">
</p>

### 3\.- Clik en “crear la suya propia”
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/46d55d72-b293-42e1-97a9-28a4c08dc003" width="700" height="400">
</p>

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/4ca72332-5f99-4ccc-ad72-26a2b101ae99" width="700" height="400">
</p>


### 4\.- Creamos nuestra máquina de estado
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/47312e25-207c-4d4b-b0ed-059cdb0b714d" width="700" height="400">
</p>



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

### 5\.- Clik en crear
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/4017cbfd-9bb7-475c-9e89-4eb3fd64ae77" width="700" height="400">
</p>

### 6\.-No tenemos permitido crear una maquina de estado
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/aeafa511-71cd-429b-aeaf-406a952ddd43" width="500" height="100">
</p>


### 7\.-Revisamos el servicio Lambda
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/aad1c77f-e495-4ce5-b01c-98c11eb56f00" width="700" height="300">
</p>


### 8\.- Clik en “crear una función”
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/992b3434-6f95-4ba8-8ac5-1508325363e4" width="500" height="200">
</p>

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/7385531f-a6c6-4fdf-bf26-f78e1c21eced" width="700" height="200">
</p>


### 9\.- No tenemos el permiso de crear una función
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/59e74c36-ac1a-4223-9168-ef7e9f9603ad" width="500" height="100">
</p>

