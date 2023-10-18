from ClienteManager import ClienteManager
from OrdenManager import OrdenManager
from NuevoPedido import NuevoPedido

class EmpanadaFacade:
    def __init__(self):
        self.clienteManager = ClienteManager()
        self.ordenManager = OrdenManager()

    def realizarPedido(self,nuevoPedido: NuevoPedido):
        cliente = self.clienteManager.get_cliente_by_du(nuevoPedido)
        orden = self.ordenManager.create_order(cliente, nuevoPedido.empanadas)
        self.ordenManager.process_order(orden)