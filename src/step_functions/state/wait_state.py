import time
import logging
class WaitState:
    '''
    Modela un estado de espera dentro de una máquina
    de estados
    '''
    def __init__(self, name, wait_time, next_state):
        self.name = name
        self.wait_time = wait_time  #Tiempo de espera en segundos
        self.next_state = next_state    #Nombre del siguiente estado a ejecutar

    def execute(self, data):
        '''
        Pausa la ejecución con el tiempo
        de espera especificado
        '''
        logging.info(f"El estado {self.name} fue pausado por {self.wait_time} segundos")    # Registra el inicio de la ejecución de la tarea
        time.sleep(self.wait_time)
        return self.next_state, data    #Retorna el siguiente estado y los mismos datos