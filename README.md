# YT Live Downloader

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**YTLD** es un script ligero de Python diseñado para automatizar la grabación de directos de YouTube. Es ideal para capturar clases online, conferencias o eventos en vivo cuando no puedes estar frente al PC.

# Motivación

Hace un tiempo necesitaba grabar una emisión durante la cual yo no podría estar presente porque tenía que asistir a clases. Desarrollé este script usando streamlink para poder hacerlo. 

##  Características

El script detecta si falta `streamlink` y lo instala.
Al definir una hora específica, el script esperará en segundo plano hasta que llegue la hora deseada.


##  Instalación 

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/mirko-lc/YT-Live-Downloader.git](https://github.com/mirko-lc/YT-Live-Downloader.git)
    cd YT-Live-Downloader
    ```

2.  **Configuración:**
    En `main.py` edita la sección de configuración con tus datos:
    ```python
    # ================= CONFIGURACIÓN =================
    URL_OBJETIVO = "URL_DEL_DIRECTO"
    HORA_INICIO = "HH:MM"
    DIRECTORIO = "C:/Ruta/A/Tu/Carpeta/"
    # =================================================
    ```

3.  **Ejecución:**
    Correr el script:
    ```bash
    python main.py
    ```

## Requisitos

* [Python 3.x](https://www.python.org/)
* Conexión a internet estable.

## Licencia

Este proyecto está bajo la Licencia MIT. Todo el mundo es libre de usarlo, modificarlo y mejorarlo.

## Nota personal

Este proyecto es el resultado de mis primeros acercamientos a la programación en Python.
Es mi primera contribución por aquí y estaría encantado de recibir feedback.
Espero que el script sea de ayuda!
Gracias y un abrazo! :D

