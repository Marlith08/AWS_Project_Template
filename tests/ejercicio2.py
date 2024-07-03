import threading
import time
from tests.utils.state_machine import StateMachine
from src.step_functions.state.wait_state import WaitState
class TaskState:
    '''
    Modela la ejecución de una tarea específica dentro de
    una máquina de estados
    '''
    def __init__(self, name, task):
        self.name = name
        self.task = task

    def execute(self, data):
        return self.task(data)

class ParallelState:
    '''
    Modela un estado en una máquina de estados que ejecuta varias tareas en paralelo,
    donde se hace uso de hilos para una mejor gestión.
    '''
    def __init__(self, name, tasks, next_state):
        self.name = name
        self.tasks = tasks  # Diccionario de todas las tareas
        self.next_state = next_state    # nombre del siguiente estado a ejecutar
        self.completed_tasks = set()    # conjutnto para almacenar nombres de las tareas completas

    def execute(self, data):
        print(f"Ejecutando estado paralelo: {self.name}")
        threads = []     # alamacenar los hilos inciados
        results = {}

        #Iniciar cada tarea en un hilo separado
        for task_name, task_func in self.tasks.items():
            thread = threading.Thread(target=self.run_task, args=(task_name, task_func, data, results))
            threads.append(thread)
            thread.start()

        #Esperar a que todos los hilos terminen
        for thread in threads:
            thread.join()

        return self.next_state, data

    def run_task(self, task_name, task_func, data, results):

        results[task_name] = task_func(data)

        # Agregar la tarea completada al conjunto de tareas completadas
        self.completed_tasks.add(task_name)

    def get_completed_tasks(self):
        return list(self.completed_tasks)


class ChoiceState:
    '''
    Modela el tipo de estado dentro de una máquina de estados,
    donde toma deciciones basadas en condiciones específicas
    '''
    def __init__(self, name, choices):
        self.name = name
        self.choices = choices

    def execute(self, data):
        '''
        Evalúa las condiciones definidas y devuelve el próximo estado basado en los datos
        de entrada
        '''
        print(f"Evaluando decisiones en estado: {self.name}")

        # Itera todas las condiciones
        for condition_func, next_state in self.choices:
            if condition_func(data):
                print(f"Condición satisfecha para {next_state}")
                return next_state, data #Retorna el siguiente estado y los datos actualizados

        print("Ninguna condición se cumplió, permaneciendo en el estado actual.")
        return "End", data  #Retorna el siguiente estado y los datos actualizados

# Funciones de tarea específicas para procesamiento paralelo
def proceso_1(data):
    print("\nProcesando datos desde la base de datos... \n")
    time.sleep(1)  # Simulación de proceso de carga
    data["datos_procesados_1"] = True
    return data

def proceso_2(data):
    print("Procesando datos desde la base de datos... \n")
    time.sleep(3)  # Simulación de proceso de limpieza
    data["datos_procesados_2"] = True
    return data

def proceso_3(data):
    print("Procesando datos desde la base de datos... \n")
    time.sleep(5)  # Simulación de proceso de análisis
    data["datos_procesados_3"] = True
    return data

#Funciones de condición para ChoiceState
def verificar_datos_cargados(data):
    return data.get('datos_procesados', False)

def verificar_datos_limpios(data):
    return data.get('datos_procesados', False)

# Función independiente para el final del procesamiento
def end_task(data):
    if all(key in data for key in ['datos_procesados_1', 'datos_procesados_2', 'datos_procesados_3']):
        print(f"Final result: {data.get('resultados_analisis', 'Data processed')}")
    else:
        print("No se han completado todas las tareas necesarias.")

#Definición de los estados en la máquina de estados
states = {
    "espera": WaitState("espera", 2, "decision"),
    "decision": ChoiceState("decision", [
        (verificar_datos_cargados, "procesamiento_datos"),
        (verificar_datos_limpios, "End")
    ]),
    "procesamiento_datos": ParallelState("procesamiento_datos", {
        "proceso_1": proceso_1,
        "proceso_2": proceso_2,
        "proceso_3": proceso_3
    }, "End"),
    "End": TaskState("End", lambda data: (None, data))
}

#Definir posiciones fijas para los nodos
positions = {
    "Start": (0, 0),
    "espera": (0, -2),
    "decision": (0, -4),
    "procesamiento_datos": (0.0055, -5),
    "proceso_1": (0.0035, -7.5),
    "proceso_2": (0.0055, -7.5),
    "proceso_3": (0.0075, -7.5),
    "End": (0, -11)
}
# Crear la máquina de estados con los estados definidos y la posición inicial

sm = StateMachine(states, "espera", positions)

# Añadir transiciones entre estados
sm.add_transition("Start", "espera")
sm.add_transition("espera", "decision")
sm.add_transition("decision", "procesamiento_datos", "$cargados")
sm.add_transition("decision", "End", "$limpios")
sm.add_transition("procesamiento_datos", "cargar_datos")
sm.add_transition("procesamiento_datos", "limpiar_datos")
sm.add_transition("procesamiento_datos", "analizar_datos")
sm.add_transition("proceso_1", "End")
sm.add_transition("proceso_2", "End")
sm.add_transition("proceso_3", "End")

# Datos iniciales para la ejecución
data = {"datos_cargados": True, "datos_limpios": True}
print("Executing Start")
final_state, final_data = sm.execute(data)  #Ejecución de la máquina de estados con los datos iniciales
print(final_data)