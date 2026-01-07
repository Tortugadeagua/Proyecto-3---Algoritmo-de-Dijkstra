from Modelos import *

def main():

    # 1. MODELO G(m,n) – MALLA
    print("Generando grafo Malla 20x25...")
    g = grafo_Malla(20, 25)

    # Mostrar nodos y aristas
    g.mostrar_grafo()

    # Nodo inicial (IMPORTANTE: la malla empieza en 1)
    nodo_inicial = 1

    # Ejecutar Dijkstra
    print("Ejecutando Dijkstra...")
    dist, padres = g.dijkstra(nodo_inicial)

    # Exportar árbol de caminos mínimos
    g.exportar_dijkstra_gv("Dijkstra_Malla.gv", padres)

    # 2. MODELO Erdős–Rényi G(n, m)
    print("\nGenerando grafo Erdős–Rényi...")
    g_er = grafo_ErdosRenyi(500, 600)

    g_er.exportar_a_gv("Erdos_500.gv")

    dist_er, padres_er = g_er.dijkstra(0)
    g_er.exportar_dijkstra_gv("Erdos_Dijkstra.gv", padres_er)

    # 3. MODELO Gilbert G(n, p)
    print("\nGenerando grafo Gilbert...")
    g_gil = grafo_Gilbert(50, 5)

    dist_gil, padres_gil = g_gil.dijkstra(0)
    g_gil.exportar_dijkstra_gv("Gilbert_Dijkstra.gv", padres_gil)

    # 4. MODELO Dorogovtsev–Mendes
    print("\nGenerando grafo Dorogovtsev–Mendes...")
    g_dm = grafo_DoroMendes(50)

    dist_dm, padres_dm = g_dm.dijkstra(1)
    g_dm.exportar_dijkstra_gv("DoroMendes_Dijkstra.gv", padres_dm)

    # 5. MODELO Barabási–Albert
    print("\nGenerando grafo Barabási–Albert...")
    g_ba = grafo_BarabasiAlbert(500, 10)

    dist_ba, padres_ba = g_ba.dijkstra(1)
    g_ba.exportar_dijkstra_gv("Barabasi_Dijkstra.gv", padres_ba)

    # 6. MODELO Geográfico simple
    print("\nGenerando grafo Geográfico...")
    g_geo = grafo_Geografico(400, 0.2)

    g_geo.exportar_a_gv("Geografico_400.gv")

    dist_geo, padres_geo = g_geo.dijkstra(1)
    g_geo.exportar_dijkstra_gv("Geografico_Dijkstra.gv", padres_geo)

    print("\nEjecución finalizada correctamente.")


# Punto de entrada
if __name__ == "__main__":
    main()