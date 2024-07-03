class DevOpsStateMachine:
    def __init__(self):
        self.state = 'Start' #se inicializa com star la máquina de estado
        self.data = None  # Variable para almacenar datos

    def process_event(self, event):
        if self.state == 'Start':  # Inicialización de datos (simulación)
            self.data = {"app_name": "MiAplicacion", "version": "1.0"} #se establece los datos de la aplicación
            print(f"Estado: Iniciando proceso para {self.data['app_name']} (v{self.data['version']})")
            self.state = 'Build' #se pasa al siguiente estado
        
        elif self.state == 'Build': # Simulación de la compilación del estado
            print(f"Estado: Compilando {self.data['app_name']} (v{self.data['version']})...")   # Aquí podrías llamar a funciones o métodos para compilar la aplicación
            self.state = 'Test'
        
        elif self.state == 'Test': # Simulación de las pruebas automáticas
            print(f"Estado: Ejecutando pruebas automáticas para {self.data['app_name']} (v{self.data['version']})...")  # Aquí podrías llamar a funciones o métodos para ejecutar pruebas
            self.state = 'Deploy'
        
        elif self.state == 'Deploy': # Simulación del despliegue
            print(f"Estado: Desplegando {self.data['app_name']} (v{self.data['version']}) en producción...")     # Aquí podrías llamar a funciones o métodos para desplegar la aplicación
            print("¡Despliegue exitoso!")
            self.state = 'End' #se pasa el estado a end
        
        elif self.state == 'End':
            print("Proceso finalizado.") #el proceso a finalizado
        
        else:
            print("Estado no reconocido.") #para manejar estados n reconcidos

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la máquina de estados
    devops_workflow = DevOpsStateMachine()

    # Simular el flujo de eventos
    devops_workflow.process_event('start')
    devops_workflow.process_event('build')
    devops_workflow.process_event('test')
    devops_workflow.process_event('deploy')
