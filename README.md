# HopitalDataMining 👽👾

# Instalación de django en windows 🐍

cualquiera de estos comandos pueden funcionar:
python -m pip install Django / py -m pip install Django

La creación de nuestras tablas de la BD se encuentran en el siguiente archivo:

pacientes/models.py

# Creacion de la base de datos en el proyecto 💻

ir al archivo Hospital/settings.py y poner los datos de conexion de cada una
de las bases de datos en el objeto "DATABASES = {}"

# Inserción de datos en la base de datos a través de comandos 👨‍💻

parametros:
    cantidad: "Establece la cantidad de registros que se desean agregar a la tabla"
    bd: "Establece la base de datos en donde se agregaran ciertos registros"

👀 Insetar de preferencia en el siguiente orden

Tabla de pacientes:
    ejemplo: 
        python manage.py createPacientes --cantidad=3 --bd=mysql
        python manage.py createPacientes --cantidad=2 --bd=postgres
        python manage.py createPacientes --cantidad=1 --bd=mariadb

Tabla de medicamentos:
    ejemplo: 
        python manage.py createMedicamentos --cantidad=3 --bd=mysql
        python manage.py createMedicamentos --cantidad=2 --bd=postgres
        python manage.py createMedicamentos --cantidad=1 --bd=mariadb

Tabla de Recetas:
    ejemplo:
    python manage.py createRecetas --cantidad=3 --bd=mysql
    python manage.py createRecetas --cantidad=2 --bd=postgres
    python manage.py createRecetas --cantidad=1 --bd=mariadb

# URLS disponibles 🌐

localhost:8000/ --> visualiza a todos los pacientes
localhost:8000/medicamentos 
localhost:8000/recetas
