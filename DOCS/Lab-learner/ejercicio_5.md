<p align="right">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/387f6cab-83d1-4de9-ba74-52d8b0841334" width=167" height="84">
</p>

# <p align = "center"> ﻿EJERCICIO N° 5 </p>

#### **Crea un flujo de trabajo que coordine varias funciones Lambda utilizando Step Functions.**

#### **Integra Step Functions con otros servicios de AWS como DynamoDB, S3, y SNS..**

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


### 4\.- Creamos nuestra máquina de estado de acuerdo a las indicaciones
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/d0d29b28-0f27-4478-b418-41fabb4c0196" width="700" height="400">
</p>


### 5\.- Clik en crear
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/150297300/6aa3c9c0-b0ee-4399-8151-0728f12b6202" width="700" height="400">
</p>

## Código de la máquina de estado
        {
          "Comment": "Ejemplo extendido de Step Functions con mÃºltiples servicios y tipos de flujos",
          "StartAt": "ReceiveDataFromS3",
          "States": {
            "ReceiveDataFromS3": {
              "Type": "Task",
              "Resource": "arn:aws:states:::sns:publish",
              "Parameters": {
                "TopicArn": "arn:aws:sns:REGION:ACCOUNT_ID:DataNotificationTopic",
                "Message": {
                  "Input.$": "$",
                  "Bucket.$": "$.Records[0].s3.bucket.name",
                  "Key.$": "$.Records[0].s3.object.key"
                }
              },
              "Next": "ParallelProcessing"
            },
            "ParallelProcessing": {
              "Type": "Parallel",
              "Branches": [
                {
                  "StartAt": "ProcessDataWithLambda",
                  "States": {
                    "ProcessDataWithLambda": {
                      "Type": "Task",
                      "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:ProcessDataLambdaFunction",
                      "Next": "SaveToDynamoDB"
                    },
                    "SaveToDynamoDB": {
                      "Type": "Task",
                      "Resource": "arn:aws:states:::dynamodb:putItem",
                      "Parameters": {
                        "TableName": "MyDynamoDBTable",
                        "Item": {
                          "Data.$": "$.processedData"
                        }
                      },
                      "Next": "NotifyProcessingComplete"
                    },
                    "NotifyProcessingComplete": {
                      "Type": "Task",
                      "Resource": "arn:aws:states:::sns:publish",
                      "Parameters": {
                        "TopicArn": "arn:aws:sns:REGION:ACCOUNT_ID:ProcessingCompleteTopic",
                        "Message": "Procesamiento de datos completo"
                      },
                      "End": true
                    }
                  }
                },
                {
                  "StartAt": "StoreRawDataToS3",
                  "States": {
                    "StoreRawDataToS3": {
                      "Type": "Task",
                      "Resource": "arn:aws:states:::s3:putObject",
                      "Parameters": {
                        "Bucket": "MyRawDataBucket",
                        "Key": "RawData/$.Records[0].s3.object.key",
                        "Body.$": "$"
                      },
                      "Next": "PassState"
                    },
                    "PassState": {
                      "Type": "Pass",
                      "End": true
                    }
                  }
                }
              ],
              "Next": "ChoosePath"
            },
            "ChoosePath": {
              "Type": "Choice",
              "Choices": [
                {
                  "Variable": "$.processingRequired",
                  "BooleanEquals": true,
                  "Next": "InvokeLambdaForAdvancedProcessing"
                },
                {
                  "Variable": "$.processingRequired",
                  "BooleanEquals": false,
                  "Next": "CheckBatchProcessing"
                }
              ],
              "Default": "CheckBatchProcessing"
            },
            "InvokeLambdaForAdvancedProcessing": {
              "Type": "Task",
              "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:AdvancedProcessingLambdaFunction",
              "Next": "SaveAdvancedResultsToS3"
            },
            "SaveAdvancedResultsToS3": {
              "Type": "Task",
              "Resource": "arn:aws:states:::s3:putObject",
              "Parameters": {
                "Bucket": "MyProcessedDataBucket",
                "Key": "ProcessedData/advanced_results.json",
                "Body.$": "$.advancedResults"
              },
              "Next": "NotifyAdvancedProcessingComplete"
            },
            "NotifyAdvancedProcessingComplete": {
              "Type": "Task",
              "Resource": "arn:aws:states:::sns:publish",
              "Parameters": {
                "TopicArn": "arn:aws:sns:REGION:ACCOUNT_ID:AdvancedProcessingCompleteTopic",
                "Message": "Procesamiento avanzado completo"
              },
              "Next": "CheckBatchProcessing"
            },
            "CheckBatchProcessing": {
              "Type": "Task",
              "Resource": "arn:aws:states:::batch:submitJob.sync",
              "Parameters": {
                "JobDefinition": "MyBatchJobDefinition",
                "JobName": "BatchJob-DataProcessing",
                "JobQueue": "MyBatchJobQueue",
                "Parameters": {
                  "input.$": "$"
                }
              },
              "Next": "ReceiveMessagesFromQueue"
            },
            "ReceiveMessagesFromQueue": {
              "Type": "Task",
              "Resource": "arn:aws:states:::sqs:receiveMessage",
              "Parameters": {
                "QueueUrl": "arn:aws:sqs:REGION:ACCOUNT_ID:MyQueue",
                "MaxNumberOfMessages": 1,
                "WaitTimeSeconds": 10
              },
              "End": true
            }
          }
        }


## 6\.-Clik en confirmar la creación
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/1b93c00d-0ac5-4f91-9662-af3771d4b47d" width="700" height="100">
</p>

## Verificamos que no tenemos el permiso para crear una maquina de estado
<p align="center">
  <img src="https://github.com/Marlith08/AWS_Project_Template/assets/136536376/3f9cef4a-cb63-4b03-93d9-749ca393766e" width="700" height="100">
</p>


## 7\.- Procedemos a verificar los roles en el servicio IAM
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
