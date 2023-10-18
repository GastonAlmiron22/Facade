from EmpanadaFacade import EmpanadaFacade
from NuevoPedido import NuevoPedido
from Empanada import Empanada

facade = EmpanadaFacade()
nuevoPedido = NuevoPedido()
carne = Empanada("Carne", 0)
pollo = Empanada("Pollo", 0)
empanadas = []

def pedir_datos_cliente():
    print("Bienvenido al sistema de pedidos de empanadas, debido a la situacion actual, solo se ofrecen 2 tipos de empanadas: Carne y Pollo.")
    print("Desea empanadas de carne? (S/N)")
    carneResponse = input()
    if carneResponse == "S":
        print("Cuantas empanadas de carne desea?")
        carne.cantidad = input()
        empanadas.append(carne)
    print("Desea empanadas de pollo? (S/N)")
    polloResponse = input()
    if polloResponse == "S":
        print("Cuantas empanadas de pollo desea?")
        pollo.cantidad = input()
        empanadas.append(pollo)
    nuevoPedido.nombre = input("Ingrese su nombre: ")
    nuevoPedido.apellido = input("Ingrese su apellido: ")
    nuevoPedido.email = input("Ingrese su email: ")
    nuevoPedido.documento = input("Ingrese su documento: ")
    nuevoPedido.tipoDocumento = input("Ingrese su tipo de documento: ")
    nuevoPedido.direccion = input("Ingrese su direccion: ")
    nuevoPedido.telefono = input("Ingrese su telefono: ")
    nuevoPedido.empanadas = empanadas

pedir_datos_cliente()
facade.realizarPedido(nuevoPedido)