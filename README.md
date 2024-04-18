# Data_challenge
Proyecto de Integración de Coordenadas y Códigos Postales
Descripción del Proyecto
Este proyecto tiene como objetivo integrar coordenadas geográficas con códigos postales utilizando el servicio web de postcodes.io. La solución propuesta consta de dos microservicios escritos en Python con el framework Django: uno para recibir y procesar el archivo de coordenadas y otro para consumir el API de postcodes.io y completar la información de los códigos postales.

Arquitectura del Proyecto
El proyecto sigue una arquitectura hexagonal para separar claramente las capas de dominio, aplicación e infraestructura. Se compone de los siguientes componentes principales:

application: Contiene los casos de uso de la aplicación.
infrastructure: Contiene los adaptadores para interactuar con servicios externos como el API de postcodes.io y los repositorios para la persistencia de datos.
domain: Define las entidades y objetos de valor del dominio.
A continuación, se presenta un diagrama de la arquitectura propuesta:

  +---------------------+
  |      Application    |
  |       (Use Cases)   |
  +---------------------+
            |
            v
  +---------------------+
  |       Domain        |
  +---------------------+
            |
            v
  +---------------------+
  |   Infrastructure    |
  |   (Adapters, Repositories) |
  +---------------------+
            |
            v
     External Services
  (postcodes.io API, Database)


Pasos para Hacer Funcionar el Proyecto
Clona el repositorio desde GitHub:
git clone https://github.com/Sard0z/Data_challenge.git

Instala las dependencias del proyecto:
cd DATA_CHALLENGE
pip install -r requirements.txt
Configura las variables de entorno necesarias, como la URL del API de postcodes.io.

Levanta los microservicios utilizando Docker Compose:
docker compose up
docker-compose up --build
Accede a la interfaz del microservicio de carga de archivos de coordenadas en tu navegador web:
python manage.py runserver
http://localhost:8000/upload-coordinates/
Sube el archivo de coordenadas y verifica que se procese correctamente.
