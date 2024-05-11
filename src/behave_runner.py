import random
import subprocess
import os
import queue
import threading
import sys


def run_reporter():
    port = str(random.randint(1024, 49151))
    # Generar y abrir el reporte de Allure después de que terminen todos los procesos de Behave
    if sys.platform == 'win32':
        subprocess.run('allure generate ' + basedir + '/allure-results --output ' + basedir + '/allure-report --clean',
                       shell=True)
        command = ['allure', 'open', '--port', port, basedir + '/allure-report']
        subprocess.run(command, shell=True)
    elif sys.platform == "darwin":
        subprocess.run(['allure', 'generate', '../allure-results', '--output', '../allure-report', '--clean'])
        subprocess.run(['allure', 'open', '--port', port, basedir + '/allure-report'])


def run_behave(script):
    subprocess.run(
        ['behave', '-f', 'allure_behave.formatter:AllureFormatter', '-o', '../allure-results', '-f', 'pretty', script])


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        run_behave(item)
        q.task_done()


if __name__ == "__main__":
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    # Lista de rutas de archivos de características
    feature_files = [
        basedir + '/src/features/consultar_registros.feature',
        basedir + '/src/features/iniciar_sesion.feature'
    ]

    num_threads = 1  # El número de hilos para ejecutar los procesos Behave simultáneamente
    q = queue.Queue()

    # Agregar características a la cola
    for file_path in feature_files:
        q.put(file_path)

    # Crear e iniciar hilos trabajadores
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # Esperar a que todos los elementos de la cola se procesen
    q.join()

    # Detener los hilos trabajadores
    for _ in range(num_threads):
        q.put(None)
    for t in threads:
        t.join()

    print("Ejecución paralela de Behave completada")
    run_reporter()
