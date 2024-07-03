class State:
    def __init__(self, name, state_type, end=False):
        self.name = name #Nombre del estado
        self.state_type = state_type #Tipo de estado
        self.end = end #Indica si un estado  ya esta en la parte final.

class PassState(State): #Se implementa un estado pass
    def __init__(self, name, result, end=False):
        super().__init__(name, "Pass", end)
        self.result = result

class MultiplicaciónState(State): #Se implementa un estado multiplicación
    def __init__(self, name, num1, num2, next_state, end=False):
        super().__init__(name, "Multiplicación", end)
        self.num1 = num1 #Numero la para multiplicación
        self.num2 = num2
        self.next_state = next_state #Damos pase al siguiente estado

    def execute(self):
        return self.num1 * self.num2 #Ejecutar la multiplicación.

class ChoiceState(State): #Implementamos el estado choice
    def __init__(self, name, choices, default_state, end=False):
        super().__init__(name, "Choice", end)
        self.choices = choices #Lista ded condiciones
        self.default_state = default_state #esatdo sin ninguna condición.

    def execute(self, value):
        for condition, next_state in self.choices:
            if condition(value): #Evaluar cada condición con el valor dado
                return next_state #Pasa al siguiente estado si la condición se cumple
        return self.default_state #DEvolver el estadfo por defecto si ninguna condición

class StateMachine: #Implementamos la máquina de estado
    def __init__(self, name):
        self.name = name #Nombre de la maquina de estado
        self.states = {} #Diccionario para almacenar los estados
        self.start_state = None #Estado inicial de la máquina de estados

    def add_state(self, state):
        self.states[state.name] = state #agrega un estado al diccionario
        if not self.start_state:
            self.start_state = state.name #Establece el primero estado como el inicial en caso de que no haya 

    def execute(self):
        current_state_name = self.start_state #estado actual en el estado inicial
        while current_state_name:
            current_state = self.states[current_state_name]#obtenemos el objeto del estado inicial
            print(f"Ejecutando estado: {current_state.name}") #Nombre del estaado actual

            if current_state.state_type == "Pass": #verifica si e4s un estado pass
                print(f"Resultado: {current_state.result}")
                if current_state.end: #verifica si es un estado final
                    print("Fin de la máquina de estados.")
                    break
                current_state_name = None  # Transición al próximo estado (por definir)

            elif current_state.state_type == "Multiplicación":
                result = current_state.execute() #Ejecuta la operación de multiplicación
                print(f"Resultado de la multiplicación: {result}")
                current_state_name = current_state.next_state  # Transición al próximo estado

            elif current_state.state_type == "Choice": #verifica si es un estado choice
                result = current_state.execute(result)  # Usar el resultado del estado anterior
                if current_state_name != result: #si existe una transición de estado
                    print(result) #Mostrará el resultado de la elección dada
                current_state_name = result #Pasa al siguiente estado

            if current_state.end:
                print("Fin de la máquina de estados.")
                break
            
            
def create_state_machine(): #Creamos la maquina de estado
    sm = StateMachine("MultiplicationStateMachine")

    Multiplicación_state = MultiplicaciónState( #DEfinimos los estados y transiciones
        name="Multiplicar Numeros", num1=6, num2=10,    #colocamos los números a ejecutar
        next_state="Verificar Resultado"
    )
    choice_state = ChoiceState(
        name="Verificar Resultado",
        choices=[
            (lambda x: x > 50, "El resultado es > 50"), #condición 1
            (lambda x: x <= 50, "El resultado es <= 50") #condición 2
        ],
        default_state="Desconocido"
    )
    mayor_cincuenta_state = PassState(name="El resultado es > 50", result="¡El número es mayor que 50! ¡Genial!", end=True)
    menor_igual_cincuenta_state = PassState(name="El resultado es <= 50", result="¡Buen intento! ¡Felicitaciones!", end=True)

    #Agregamos los estados a la maquina de estados
    sm.add_state(Multiplicación_state)
    sm.add_state(choice_state)
    sm.add_state(mayor_cincuenta_state)
    sm.add_state(menor_igual_cincuenta_state)

    return sm   #Devolvemos la máquina de estados

def main():
    sm = create_state_machine()
    sm.execute() #Ejecutamos la máquina de estaados

if __name__ == "__main__":
    main()
