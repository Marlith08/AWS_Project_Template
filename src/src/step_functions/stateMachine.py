class StateMachine:
    '''
    Modela una máquina de estados
    '''
    def __init__(self, states):
        self.states = states    # Almacena todos los estados
        self.current_state = list(states.keys())[0] #Indica que el primer estado como actual

    def execute(self, data):
        '''
        Ejecuta la máquina de estados hasta que termine
        todos los estados
        '''
        while self.current_state is not None:
            state = self.states[self.current_state] #Obtiene el estado actual
            self.current_state, data = state.execute(data)  #Ejecuta el estado y obtiene el siguiente estado con los datos actualizados
        return self.current_state, data #Retorna el último estado y los datos actualizados