import threading
import logging
class ParallelState:
    '''
    Modela un estado en una máquina de estados que ejecuta varias tareas en paralelo,
    donde se hace uso de hilos para una mejor gestión.
    '''
    def __init__(self, name, tasks, next_state):
        self.name = name
        self.tasks = tasks # Diccionario de todas las tareas
        self.next_state = next_state # nombre del siguiente estado a ejecutar
        self.completed_tasks = set() # conjutnto para almacenar nombres de las tareas completas

    def execute(self, data):
        logging.info(f"Ejecutando estado paralelo: {self.name}") # Registra el inicio de la ejecución de la tarea
        threads = [] # alamacenar los hilos inciados

        # Iniciar cada tarea en un hilo separado
        for task_name, task_func in self.tasks.items():
            thread = threading.Thread(target=self.run_task, args=(task_name, task_func, data))
            threads.append(thread)
            thread.start()

        # Esperar a que todos los hilos terminen
        for thread in threads:
            thread.join()

        return self.next_state, data

    def run_task(self, task_name, task_func, data):
        '''
        Modela la ejecución las tareas para mantener su
        registro de ejecución
        '''
        logging.info(f"Ejecutando tarea en paralelo: {task_name}")
        result = task_func(data)
        self.completed_tasks.add(task_name)
        logging.info(f"Tarea en paralelo completada: {task_name}")
