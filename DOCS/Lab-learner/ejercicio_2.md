<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>

# <p align = "center"> ﻿EJERCICIO N° 2 </p>

#### **Desarrolla una máquina de estado que incluya estados de tarea y pasarela. Implementa estos estados utilizando Python y AWS SDK.**

#### **Añade estados de espera y elección a la máquina de estado. Utiliza condiciones para decidir el flujo de trabajo.**

### 1,. Nos dirigimos al servicio de Step Function
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/ba0ecaab-e8e0-4e8b-a9fa-fe21a9fb0932" width="700" height="400">
</p>



### 2\.- Clik en empezar
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/373175f3-c786-41a5-bf1e-54e03eb0fefb" width="700" height="400">
</p>



### 3\.- Clik en “crear la suya propia”
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/4a61578b-7f8e-4002-acc0-0950afe40ab0" width="700" height="550">
</p>

<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/35d867bb-f6d7-41d4-b757-b27f67b47801" width="700" height="550">
</p>


### 4\.- Creamos nuestra máquina de estado
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/9e24618c-82eb-4ad6-9bc3-5b0684b7b0c7" width="700" height="400">
</p>


### 5\.- Clik en crear
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/c916d586-2c11-4aee-824f-bbf787a0df95" width="700" height="400">
</p>

## Código de la máquina de estado


      {
        "Comment": "A description of my state machine",
        "StartAt": "Wait",
        "States": {
          "Wait": {
            "Type": "Wait",
            "Seconds": 5,
            "Next": "Choice"
          },
          "Choice": {
            "Type": "Choice",
            "Choices": [
              {
                "Next": "Pass"
              }
            ],
            "Default": "Parallel"
          },
          "Pass": {
            "Type": "Pass",
            "End": true
          },
          "Parallel": {
            "Type": "Parallel",
            "End": true,
            "Branches": [
              {
                "StartAt": "Pass (1)",
                "States": {
                  "Pass (1)": {
                    "Type": "Pass",
                    "End": true
                  }
                }
              },
              {
                "StartAt": "Pass (2)",
                "States": {
                  "Pass (2)": {
                    "Type": "Pass",
                    "End": true
                  }
                }
              },
              {
                "StartAt": "Pass (3)",
                "States": {
                  "Pass (3)": {
                    "Type": "Pass",
                    "End": true
                  }
                }
              }
            ]
          }
        }
      }

## 6\.-Clik en confirmar
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/1b93c00d-0ac5-4f91-9662-af3771d4b47d" width="700" height="100">
</p>

## Verificamos que no tenemos el permiso para crear una maquina de estado
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/3f9cef4a-cb63-4b03-93d9-749ca393766e" width="700" height="100">
</p>


## 7\.- Verificamos el servicio IAM
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/6452f385-8ef3-4785-ba96-73c1d0816528" width="700" height="400">
</p>


<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/1bea4f82-ecdd-42af-894b-6b855c68a994" width="700" height="400">
</p>



<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/62ad8e7b-c814-4c24-a5cc-93060e45c35a" width="700" height="400">
</p>


<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/648a2cce-6682-49ec-b0b1-b31c8e44d87f" width="700" height="400">
</p>


## 8\.- No tenemos acceso para crear un rol.
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/1fb6d103-4581-47bd-928b-f9cdea4eea16" width="700" height="100">
</p>

