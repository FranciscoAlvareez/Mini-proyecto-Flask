# Imagen base con Python
FROM python:3.11  

# Carpeta de trabajo dentro del contenedor
WORKDIR /app  

# Copiamos el contenido de la carpeta app al contenedor
COPY ./app /app  

# Instalamos las dependencias necesarias
RUN pip install flask requests  

# Arranca la aplicación
CMD ["python", "main.py"]
