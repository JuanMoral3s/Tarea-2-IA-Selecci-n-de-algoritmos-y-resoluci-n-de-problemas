import random
import time

def calcular_ataques(s):
    n = len(s)
    ataques = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j] or abs(s[i] - s[j]) == abs(i - j):
                ataques += 1
    return ataques

def obtener_vecinos(s):
    vecinos = []
    n = len(s)
    for col in range(n):
        fila_actual = s[col]
        for fila_nueva in range(n):
            if fila_nueva != fila_actual:
                s_vecino = list(s)
                s_vecino[col] = fila_nueva
                movimiento = (col, fila_actual)
                vecinos.append((s_vecino, movimiento))
    return vecinos

def busqueda_tabu_reinas(n, k, iter_max):
    
    s = [random.randint(0, n-1) for _ in range(n)]
    best = list(s)
    lista_tabu = [] 
    iter_realizadas = 0 # Inicialización necesaria

    for t in range(1, iter_max + 1):
        iter_realizadas = t # Guardamos el progreso
        
        # Encontramos una solucion
        if calcular_ataques(s) == 0: 
            break
            
        vecinos = obtener_vecinos(s)
        
        candidatos = []
        for v, mov in vecinos:
            costo_v = calcular_ataques(v)
            if mov not in lista_tabu or costo_v < calcular_ataques(best):
                candidatos.append((v, mov, costo_v))
        
       
        # Buscar el vecino mas optimo
        s_star, mov_star, costo_star = min(candidatos, key=lambda x: x[2])
        
        #Actualizar lista tabu
        lista_tabu.append(mov_star)
        if len(lista_tabu) > k:
            lista_tabu.pop(0) # pop_old
            
        s = s_star
        
        # if c(s) < c(best)
        if calcular_ataques(s) < calcular_ataques(best):
            best = list(s)
            
    return best, iter_realizadas

#Parametros tabu
n = 8          
tenure = 5     
maximas_iteraciones = 200

inicio_ejecucion = time.time()
mejor_solucion, iter_final = busqueda_tabu_reinas(n, tenure, maximas_iteraciones)
fin_ejecucion = time.time()

print(f"Conflictos finales (Costo): {calcular_ataques(mejor_solucion)}") 
print(f"Estado solución (Filas): {mejor_solucion}")                       
print(f"Tamaño del tablero (N): {n}")                                 
print(f"Limite de lista tabu (k): {tenure}")                                        
print(f"Iteraciones realizadas: {iter_final}")                                 
print(f"Tiempo de ejecución: {fin_ejecucion - inicio_ejecucion:.6f}s")