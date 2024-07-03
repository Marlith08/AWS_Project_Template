# Utilizamos  una imagen base de Python oficial
FROM python:3.9-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instalamos las dependencias de la aplicación
RUN pip install -r requirements.txt


# Especificamos el comando para ejecutar la aplicación
CMD ["python", "app.py"]
