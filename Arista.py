from Nodo import Nodo

# Clase que representa una arista entre dos nodos
class Arista:
    def __init__(self, origen, destino, peso=1):
        self.nodo_inicio = Nodo(origen)      # Nodo de inicio
        self.nodo_fin = Nodo(destino)        # Nodo de fin
        self.conexion = (self.nodo_inicio, self.nodo_fin)

        
        self.atributos = {"peso": peso}      # Diccionario para sus atributos
        self.peso = peso                     # Peso de la arista
