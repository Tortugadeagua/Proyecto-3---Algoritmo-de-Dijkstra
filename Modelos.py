from Grafo import Grafo
import random
import math


# ======================================
# Erdős–Rényi G(n, m)
# ======================================
def grafo_ErdosRenyi(n, m, dirigido=False):
    grafo = Grafo()

    for i in range(n):
        grafo.agregar_nodo(i)

    posibles = [(i, j) for i in range(n) for j in range(i + 1, n)]
    seleccionadas = random.sample(posibles, m)

    for i, j in seleccionadas:
        grafo.agregar_arista(i, j)

    return grafo


# ======================================
# Gilbert G(n, p)
# ======================================
def grafo_Gilbert(n, p, dirigido=False):
    grafo = Grafo()

    for i in range(n):
        grafo.agregar_nodo(i)

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() <= p / 100:
                grafo.agregar_arista(i, j)

    return grafo


# ======================================
# Geográfico simple G(n, r)
# ======================================
def grafo_Geografico(n, r, dirigido=False):
    grafo = Grafo()
    posiciones = {}

    for i in range(1, n + 1):
        grafo.agregar_nodo(i)
        posiciones[i] = (random.random(), random.random())

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            x1, y1 = posiciones[i]
            x2, y2 = posiciones[j]

            if math.hypot(x2 - x1, y2 - y1) <= r:
                grafo.agregar_arista(i, j)

    return grafo


# ======================================
# Barabási–Albert G(n, d)
# ======================================
def grafo_BarabasiAlbert(n, d, dirigido=False):
    grafo = Grafo()
    grados = {i: 0 for i in range(1, n + 1)}

    for i in range(1, n + 1):
        grafo.agregar_nodo(i)

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if grados[i] < d and grados[j] < d:
                p = min(1 - grados[i] / d, 1 - grados[j] / d)
                if random.random() < p:
                    grafo.agregar_arista(i, j)
                    grados[i] += 1
                    grados[j] += 1

    return grafo


# ======================================
# Dorogovtsev–Mendes
# ======================================
def grafo_DoroMendes(n, dirigido=False):
    grafo = Grafo()

    # Triángulo inicial
    for i in range(1, 4):
        grafo.agregar_nodo(i)

    aristas = [(1, 2), (2, 3), (3, 1)]
    for a, b in aristas:
        grafo.agregar_arista(a, b)

    for nuevo in range(4, n + 1):
        grafo.agregar_nodo(nuevo)
        a, b = random.choice(aristas)

        grafo.agregar_arista(nuevo, a)
        grafo.agregar_arista(nuevo, b)

        aristas.append((nuevo, a))
        aristas.append((nuevo, b))

    return grafo


# ======================================
# Malla G(m, n)
# ======================================
def grafo_Malla(m, n):
    grafo = Grafo()
    nodos = {}
    contador = 1

    for i in range(m):
        for j in range(n):
            nodos[(i, j)] = contador
            grafo.agregar_nodo(contador)
            contador += 1

    for i in range(m):
        for j in range(n):
            actual = nodos[(i, j)]

            if j + 1 < n:
                grafo.agregar_arista(actual, nodos[(i, j + 1)])

            if i + 1 < m:
                grafo.agregar_arista(actual, nodos[(i + 1, j)])

    return grafo
