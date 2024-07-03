import logging
class TaskState:
    '''
    Modela la ejecución de una tarea específica dentro de
    una máquina de estados
    '''
    def __init__(self, name, task, next_state=None):
        self.name = name
        self.task = task    # tarea a ejecutar
        self.next_state = next_state    #Nombre del siguiente estado a ejecutar

    def execute(self, data):
        '''
        Ejecuta la tarea asociada y devuelve el siguiente estado
        con los datos actualizados
        '''
        logging.info(f"Ejecutando tarea: {self.name}")  # Registra el inicio de la ejecución de la tarea
        data = self.task(data)

        return self.next_state, data    #Retorna el siguiente estado y los datos actualizados