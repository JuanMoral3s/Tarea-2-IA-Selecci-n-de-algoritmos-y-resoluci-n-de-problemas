import math
import random
import time

adj = {}

with open('mapa_5_paises_adyacencias.txt', 'r') as f:
    next(f)
    for linea in f:
        if ':' not in linea: continue
        pais, vecinos = linea.split(':')
        adj[pais.strip()] = [v.strip() for v in vecinos.split(',') if v.strip()]




def calcular_costo(estado, adj):
    conflictos = 0
    for pais, vecinos in adj.items():
        for vecino in vecinos:
        
            if estado[pais] == estado[vecino]:
                conflictos += 1
    return conflictos // 2

def vecino_aleatorio(estado, colores):
    nuevo_estado = estado.copy()
    
    pais = random.choice(list(nuevo_estado.keys()))

    color_actual = nuevo_estado[pais]
    opciones = [c for c in colores if c != color_actual]
    nuevo_estado[pais] = random.choice(opciones)
    return nuevo_estado

def schedule(T0, t, alpha=0.99):
    # Enfriamiento 
    return T0 * (alpha ** t)

def simulated_annealing(adj, k, T0, iterMax):
    paises = list(adj.keys())
    colores = list(range(1, k + 1))
    
   # Estado aleatorio
    s = {pais: random.choice(colores) for pais in paises}
    costo_s = calcular_costo(s, adj)
    
    for t in range(1, iterMax + 1):
 
        T = schedule(T0, t)
        
        if T <= 1e-10: 
            return s, costo_s, t
            
        
        s_prima = vecino_aleatorio(s, colores)
        costo_s_prima = calcular_costo(s_prima, adj)
        
  
        dE = costo_s_prima - costo_s
        

        if dE <= 0:
            s = s_prima
            costo_s = costo_s_prima
        else:
       
            probabilidad = math.exp(-dE / T)
            if random.random() < probabilidad:
                s = s_prima
                costo_s = costo_s_prima
        
        # Encontro solucion
        if costo_s == 0:
            return s, costo_s, t
            
    return s, costo_s, iterMax


K_COLORES = 3      
T0 = 100.0           
ITER_MAX = 50000        

inicio = time.time()
solucion, costo_final, iters = simulated_annealing(adj, K_COLORES, T0, ITER_MAX)
fin = time.time()


print(f"Estado solución: {solucion}")
print(f"Dominio (k): {K_COLORES}")
print(f"Iteraciones realizadas: {iters}")
print(f"Tiempo de ejecución: {fin - inicio:.6f}s")

