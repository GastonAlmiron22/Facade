from Cliente import Cliente
from Empanada import Empanada
import time

class OrdenManager:
    def create_order(self, cliente: Cliente, _empanadas: list):
        print(f"{cliente.nombre} estamos creando tu pedido...\n")
        for empanada in _empanadas:
            print(f"Empanada: {empanada.nombre} Cantidad: {empanada.cantidad}")
        print("#####################\n\n")
        time.sleep(2) 
        return "AAA200"
    def process_order(self, order):
        print(f"Procesando el pedido...\n\n")
        time.sleep(4)
        self.send_order(order)

    def send_order(self, order):
        print(f"Enviando pedido: {order}...\n\n")
        time.sleep(2)
        print(f"Pedido enviado, que lo disfrutes!!")