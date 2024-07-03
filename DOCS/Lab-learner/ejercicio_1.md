<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>


# <p align = "center"> ﻿EJERCICIO N° 1 </p>

#### **Crea una máquina de estado simple en AWS Step Functions utilizando la consola de AWS..**

### 1,. Nos dirigimos al servicio de Step Function
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/18a7cefe-d265-427a-ad4c-896a888b597d" width="700" height="400">
</p>



### 2\.- Clik en crear máquina de estado
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/092c2ed2-73f3-4e94-98ae-9944a591335c" width="700" height="400">
</p>



### 3\.- Clik en hoja en blanco y seleccionamos.
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/4567add5-d8d4-4f83-9151-e749bdb9c320" width="700" height="550">
</p>

- ### Nos dirigimos a la pestaa de código
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/a55be07f-ed58-4ab1-95b7-32c80ac89f89" width="700" height="550">
</p>


### 4\.- Colocamos el código de nuestra máquina de estad en formato JSON
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/1af21c1f-67e2-4be5-951f-debec0566685" width="700" height="400">
</p>

## Código de la máquina de estado

        {
          "Comment": "A Hello World example of the Amazon States Lenguage using a Pass state",
          "StartAt": "HelloWelcome",
          "States": {
            "HelloWelcome": {
              "Type": "Pass",
              "Result":"Hello Welcome",
              "End": true
            }
          }
        }

### 5\.- Clik en cofiguración y realizamos las configuraciones respectivas, como el rol.
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/87d9677c-2fbf-4fa8-8f92-b007b872e8fd" width="700" height="400">
</p>



<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/dd3bfe0a-9dd6-41b9-9ebe-f6c6a857ec8c" width="700" height="400">
</p>

## Creamos...
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/7bee97e2-c6f3-42d1-acc0-6f11490955f4" width="700" height="400">
</p>


### Verificamos que se haya creado correctamente
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/66b25963-ff59-4a7f-923d-44f83ccb83e4" width="700" height="400">
</p>

- ### Iniciamos la ejecución
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/947d61ab-a084-43a9-8058-04e2a210fbf1" width="700" height="400">
</p>


- ### Verificamos la entrada y salida correctamemte. 
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/3cb04029-6626-4b5e-b7e9-83b025f8c9f5" width="700" height="400">
</p>


<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/aaeabd58-9c35-4bf6-babc-738a0f01ce51" width="700" height="400">
</p>


<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/48c285e3-d44b-4300-b6dd-89237e69f9c9" width="700" height="400">
</p>
