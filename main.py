import subprocess
import time
import os
import sys
import importlib.util
from datetime import datetime

# ================= CONFIGURACIÓN DE USUARIO =================

URL = "https://youtube.com/live/ejemplo" # CHANGE THIS
START = "11:59" # CHANGE THIS
DIRECTORY = "./ytld_videos"  # CHANGE THIS IF NEEDED
TODAY = datetime.now().strftime("%d-%m")
FILE_NAME = os.path.join(
    DIRECTORIO, f"video{FECHA_HOY}.mp4")  
# =================================================


def dependencias():  # Instalar dependencias de ser necesario
    if importlib.util.find_spec("streamlink") is None:
        print("--- Streamlink no detectado. Instalando... ---")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "streamlink"])
        print("--- Instalación completada. ---\n")


dependencias()


def esperar_hora():  # El script espera a la hora indicada para empezar a grabar
    print(f"--- INICIANDO LA GRABACIÓN ---")
    print(f"Objetivo: {URL}")
    print(f"Hora programada: {START}")
    print(f"Archivo: {FILE_NAME}")
    print(f"Directorio actual: {os.getcwd()}")
    print("-" * 45)

    while True:
        ahora = datetime.now().strftime("%H:%M")

        if ahora >= START:
            print(
                f"\n[{datetime.now().strftime('%H:%M:%S')}] ¡HORA ALCANZADA! Lanzando Streamlink...")
            lanzar_grabacion()
            break
        else:

            print(
                f"Estado: Esperando... Hora PC: {datetime.now().strftime('%H:%M:%S')}", end="\r")
            time.sleep(5)

# Ejecución


def lanzar_grabacion():

    import sys

    comando = [
        sys.executable, "-m", "streamlink",
        URL,
        "best",
        "-o", FILE_NAME,
        "--force",
        "--retry-streams", "30",
        "--retry-max", "20"
    ]

    try:

        print(f"Grabando en: {os.path.abspath(FILE_NAME)}")
        subprocess.run(comando, check=True)
        print(
            f"\n[{datetime.now().strftime('%H:%M:%S')}] Transmisión terminada y guardada.")
    except KeyboardInterrupt:
        print("\nGrabación detenida manualmente.")
    except Exception as e:
        print(f"\nERROR CRÍTICO: {e}")
        print("Asegúrate de que 'streamlink' esté instalado correctamente.")


if __name__ == "__main__":
    try:
        esperar_hora()
    except KeyboardInterrupt:
        print("\nScript cerrado por el usuario.")
