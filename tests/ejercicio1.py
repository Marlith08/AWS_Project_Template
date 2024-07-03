from tests.utils.state_machine import StateMachine
class State:
    '''
    Modela un estado de la maquina de estados
    '''
    def __init__(self, execute_func):
        self.execute = execute_func

#Función para el estado de suma
def state_sum(data):
    sum_values = data["num1"] + data["num2"]
    print("Executing state_sum")

    #Retornar el siguiente estado y los datos actualizados
    return "state_check_sum", {"sum_values": sum_values}

#Función para el estado que verifica la suma
def state_check_sum(data):
    sum_values = data["sum_values"]
    if sum_values < 20:
        print("Executing state_check_sum")
        return "state_AddFive", data
    else:
        print("Executing state_check_sum")
        return "state_PrintMessage", data

#Función para el estado que añade cinco a la suma
def state_AddFive(data):
    data["sum_values"] += 5
    print("Executing state_AddFive")
    return "End", data

#Función para el estado que imprime un mensaje
def state_PrintMessage(data):
    sum_values = data["sum_values"]
    print("Executing state_PrintMessage")
    print(f"La suma total es {sum_values} y es ¡Un número muy grande!")
    return "End", data

#Definición de los estados en la máquina de estados
states = {
    "state_sum": State(state_sum),
    "state_check_sum": State(state_check_sum),
    "state_AddFive": State(state_AddFive),
    "state_PrintMessage": State(state_PrintMessage),
    "End": State(lambda data: (None, data))
}

#Definir posiciones fijas para los nodos
positions = {
    "Start": (0, 0),
    "state_sum": (0, -2),
    "state_check_sum": (0, -4),
    "state_AddFive": (-1, -6),
    "state_PrintMessage": (1, -6),
    "End": (0, -8)
}

# Crear la máquina de estados con los estados definidos y la posición inicial
sm = StateMachine(states, "state_sum", positions)

# Añadir transiciones entre estados
sm.add_transition("Start", "state_sum")
sm.add_transition("state_sum", "state_check_sum")
sm.add_transition("state_check_sum", "state_AddFive", "$sum < 20")
sm.add_transition("state_check_sum", "state_PrintMessage", "$sum >= 20")
sm.add_transition("state_AddFive", "End")
sm.add_transition("state_PrintMessage", "End")

# Datos iniciales para la ejecución
data = {"num1": 15, "num2": 10}
print("Executing Start")
sm.execute(data)    #Ejecución de la máquina de estados con los datos iniciales
