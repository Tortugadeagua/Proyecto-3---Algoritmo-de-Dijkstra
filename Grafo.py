from Nodo import Nodo
from Arista import Arista
import random
import heapq


# Clase Grafo (no dirigido, ponderado)
class Grafo:
    def __init__(self):
        self.nodos = dict()       # id -> Nodo
        self.aristas = []         # lista de objetos Arista
        self.atributos = dict()
        self.adyacencias = dict()

    # =========================
    # MÉTODOS BÁSICOS
    # =========================
    def agregar_nodo(self, identificador):
        if identificador not in self.nodos:
            self.nodos[identificador] = Nodo(identificador)

    # Alias por compatibilidad
    def agregar_Nodo(self, identificador):
        self.agregar_nodo(identificador)

    def agregar_arista(self, origen, destino, peso=None):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)

        if peso is None:
            peso = random.randint(1, 100)

        arista = Arista(origen, destino, peso)
        self.aristas.append(arista)

    # Alias por compatibilidad
    def agregar_Arista(self, origen, destino):
        self.agregar_arista(origen, destino)

    def mostrar_grafo(self):
        print("Nodos:")
        for nodo in self.nodos.values():
            print(f"  Nodo {nodo.id}")

        print("\nAristas:")
        for arista in self.aristas:
            print(
                f"  {arista.nodo_inicio.id} "
                f"-> {arista.nodo_fin.id} "
                f"(peso: {arista.peso})"
            )

    # =========================
    # EXPORTACIÓN GRAPHVIZ
    # =========================
    def exportar_a_gv(self, nombre_archivo):
        with open(nombre_archivo, "w") as f:
            f.write("graph G {\n")

            usadas = set()
            nodos_con_arista = set()

            for arista in self.aristas:
                a = arista.nodo_inicio.id
                b = arista.nodo_fin.id
                peso = arista.peso

                if (b, a) not in usadas:
                    f.write(f'    {a} -- {b} [label="{peso}"];\n')
                    usadas.add((a, b))

                nodos_con_arista.update((a, b))

            for nodo_id in self.nodos:
                if nodo_id not in nodos_con_arista:
                    f.write(f"    {nodo_id};\n")

            f.write("}\n")

    def exportar_dijkstra_gv(self, archivo, padres):
        with open(archivo, "w") as f:
            f.write("graph G {\n")

            for nodo in self.nodos:
                f.write(f'    {nodo};\n')

            usadas = set()
            for arista in self.aristas:
                u = arista.nodo_inicio.id
                v = arista.nodo_fin.id
                peso = arista.peso

                if (v, u) in usadas:
                    continue
                usadas.add((u, v))

                color = "red" if padres.get(v) == u or padres.get(u) == v else "black"
                f.write(f'    {u} -- {v} [label="{peso}", color={color}];\n')

            f.write("}\n")

    # =========================
    # ADYACENCIAS + DIJKSTRA
    # =========================
    def construir_adyacencias(self):
        self.adyacencias = {n: [] for n in self.nodos}
        for arista in self.aristas:
            u = arista.nodo_inicio.id
            v = arista.nodo_fin.id
            w = arista.peso
            self.adyacencias[u].append((v, w))
            self.adyacencias[v].append((u, w))

    def dijkstra(self, inicio):
        self.construir_adyacencias()

        dist = {n: float("inf") for n in self.nodos}
        dist[inicio] = 0
        padres = {}
        visitados = set()
        heap = [(0, inicio)]

        while heap:
            d, u = heapq.heappop(heap)
            if u in visitados:
                continue
            visitados.add(u)

            for v, w in self.adyacencias[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    padres[v] = u
                    heapq.heappush(heap, (dist[v], v))

        return dist, padres

    # =========================
    # BFS
    # =========================
    def BFS(self, s):
        if s not in self.nodos:
            print("Nodo no existe")
            return False

        capas = [[s]]
        visitados = [s]
        padres = {}

        nivel = 0
        while capas[nivel]:
            nueva = []

            for u in capas[nivel]:
                for arista in self.aristas:
                    a = arista.nodo_inicio.id
                    b = arista.nodo_fin.id

                    if a == u and b not in visitados:
                        visitados.append(b)
                        nueva.append(b)
                        padres[b] = u
                    elif b == u and a not in visitados:
                        visitados.append(a)
                        nueva.append(a)
                        padres[a] = u

            capas.append(nueva)
            nivel += 1

        if not capas[-1]:
            capas.pop()

        self.bfs_resultado = {
            "capas": capas,
            "padres": padres,
            "visitados": visitados
        }

        return self.bfs_resultado

    # =========================
    # DFS
    # =========================
    def DFS_recursiva(self, s, visitados=None, arbol=None):
        if s not in self.nodos:
            return False

        if visitados is None:
            visitados = set()
        if arbol is None:
            arbol = []

        visitados.add(s)

        for arista in self.aristas:
            a = arista.nodo_inicio.id
            b = arista.nodo_fin.id

            if a == s and b not in visitados:
                arbol.append((s, b))
                self.DFS_recursiva(b, visitados, arbol)
            elif b == s and a not in visitados:
                arbol.append((s, a))
                self.DFS_recursiva(a, visitados, arbol)

        return arbol

    def DFS_iterativa(self, s):
        if s not in self.nodos:
            return False

        visitados = set()
        arbol = []
        stack = [(s, None)]

        while stack:
            u, padre = stack.pop()
            if u not in visitados:
                visitados.add(u)

                if padre is not None:
                    arbol.append((padre, u))

                vecinos = []
                for arista in self.aristas:
                    a = arista.nodo_inicio.id
                    b = arista.nodo_fin.id
                    if a == u and b not in visitados:
                        vecinos.append(b)
                    elif b == u and a not in visitados:
                        vecinos.append(a)

                for v in reversed(vecinos):
                    stack.append((v, u))

        return arbol