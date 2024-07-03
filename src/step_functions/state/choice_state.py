import logging
class ChoiceState:

    '''
    Modela el tipo de estado dentro de una máquina de estados,
    donde toma deciciones basadas en condiciones específicas
    '''
    def __init__(self, name, choices, default_state):
        self.name = name
        self.choices = choices #
        self.default_state = default_state

    def execute(self, data):
        '''
        Evalúa las condiciones definidas y devuelve el próximo estado basado en los datos
        de entrada
        '''
        logging.info(f"Evaluando decisiones en estado: {self.name}") # Registra el inicio de la ejecución de la tarea

        # Itera todas las condiciones
        for condition, value, next_state in self.choices:
            if data.get(condition) == value:
                logging.info(f"Condición '{condition}': {value} cumple, pasando a estado: {next_state}")
                return next_state, data #Retorna el siguiente estado y los datos actualizados

        # En caso de que ninguna condición se cumpla pasa al estado por defecto
        logging.info(f"Ninguna condición cumple, pasando al estado por defecto: {self.default_state}")
        return self.default_state, data #Retorna el siguiente estado y los datos actualizados