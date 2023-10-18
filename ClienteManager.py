from NuevoPedido import NuevoPedido
from Cliente import Cliente
import sys
import time

cliente1 = Cliente("Juan", "Perez", "12345678", "Calle 123", "12345678", "email@mail.com")
cliente2 = Cliente("Pedro", "Gomez", "87654321", "Calle 321", "87654321", "email@mail.com")

class Empanada:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

class ClienteManager:
    clientList = [
        cliente1,
        cliente2
    ]
    def get_cliente_by_du(self, nuevoPedido: NuevoPedido):
        print(f"\nObteniendo información del cliente...")
        time.sleep(2)
        clientDoc = nuevoPedido.documento
        cliente = None
        for client in self.clientList:
            if client.documento == clientDoc:
                cliente = client
                break
        if cliente is None:
            cliente = self.createClient(nuevoPedido)
        return cliente
    
    def createClient(self, nuevoPedido: NuevoPedido):
        print(f"Creando nuevo cliente...\n\n")
        client = Cliente(
            nuevoPedido.nombre,
            nuevoPedido.apellido,
            nuevoPedido.documento,
            nuevoPedido.direccion,
            nuevoPedido.telefono,
            nuevoPedido.email
        )
        self.clientList.append(client)
        return client

