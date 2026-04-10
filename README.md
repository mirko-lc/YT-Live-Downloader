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
    git clone [https://github.com/TU_USUARIO/stream-sentinel.git](https://github.com/TU_USUARIO/stream-sentinel.git)
    cd stream-sentinel
    ```

2.  **Configuración:**
    En `main.py` edita la sección de configuración con tus datos:
    ```python
    # ================= CONFIGURACIÓN =================
    URL_OBJETIVO = "URL_DEL_DIRECTO"
    HORA_INICIO = "HH:MM" # Formato 24h
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

## Nota personal

Este proyecto fue desarrollado como parte de mis prácticas iniciales en Python, aplicando conceptos de:
* Automatización de procesos.
* Gestión de subprocesos (`subprocess`).
* Manejo de sistemas de archivos y fechas.

Es mi primera contribución por aquí y estaría encantado de recibir feedback.

## Licencia

Este proyecto está bajo la Licencia MIT. Todo el mundo es libre de usarlo, modificarlo y mejorarlo.