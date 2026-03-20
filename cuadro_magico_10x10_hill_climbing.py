import random
import time
import re
import math

with open("cuadro_magico_10_especificacion.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    N = int(re.search(r"Orden n = (\d+)", contenido).group(1))
    CONSTANTE_MAGICA = int(re.search(r"Constante mágica = (\d+)", contenido).group(1))

MAX_ITER = 100000000 

def calcular_costo(cuadro, n, magica):
    costo = 0
    # Filas
    for fila in cuadro: costo += abs(sum(fila) - magica)
    # Columnas
    for j in range(n):
        suma_col = sum(cuadro[i][j] for i in range(n))
        costo += abs(suma_col - magica)
    # Diagonales
    d1 = sum(cuadro[i][i] for i in range(n))
    d2 = sum(cuadro[i][n-1-i] for i in range(n))
    return costo + abs(d1 - magica) + abs(d2 - magica)

def generar_vecino(cuadro, n):
    nuevo = [fila[:] for fila in cuadro]
    r1, c1 = random.randint(0, n-1), random.randint(0, n-1)
    r2, c2 = random.randint(0, n-1), random.randint(0, n-1)
    nuevo[r1][c1], nuevo[r2][c2] = nuevo[r2][c2], nuevo[r1][c1]
    return nuevo

def hill_climbing_con_reinicio(n, magica, iter_max):
   
    def inicializar():
        nums = list(range(1, n**2 + 1))
        random.shuffle(nums)
        s = [nums[i*n : (i+1)*n] for i in range(n)]
        return s, calcular_costo(s, n, magica)

    s, costo_s = inicializar()
    mejor_s, mejor_costo = s, costo_s
    
    paciencia = 0
    LIMITE_PACIENCIA = 5000 
    
    for t in range(1, iter_max + 1):
        s_prima = generar_vecino(s, n)
        costo_s_prima = calcular_costo(s_prima, n, magica)
        
        if costo_s_prima <= costo_s:
            if costo_s_prima < costo_s:
                paciencia = 0 
            else:
                paciencia += 1
                
            s = s_prima
            costo_s = costo_s_prima
            
            if costo_s < mejor_costo:
                mejor_costo = costo_s
                mejor_s = s
        else:
            paciencia += 1

        if costo_s == 0:
            return s, costo_s, t

      
        if paciencia >= LIMITE_PACIENCIA:
            s, costo_s = inicializar()
            paciencia = 0
          

        if t % 100000 == 0:
            print(f"Iteracion {t} | Costo Actual: {costo_s} | Mejor Global: {mejor_costo}")

    return mejor_s, mejor_costo, iter_max

def imprimir_reporte_detallado(cuadro, n, magica, costo, iters, tiempo):

    print(f"Costo Total de Error: {costo}")
    print(f"Iteraciones: {iters} | Tiempo: {tiempo:.2f}s")
    
    print("Solucion")
    print("-" * 51)
    for fila in cuadro:
        print("|" + "".join(f"{num:4}" for num in fila) + " |")
    print("-" * 51)
    
    print("\nVERIFICACION DE FILAS:")
    for i, f in enumerate(cuadro):
        sf = sum(f)
        print(f"Fila {i+1:2}: {sf:4} {'[ OK ]' if sf == magica else '[ DIFF: '+str(sf-magica)+' ]'}")

    print("\nVERIFICACION DE COLUMNAS:")
    for j in range(n):
        sc = sum(cuadro[i][j] for i in range(n))
        print(f"Col  {j+1:2}: {sc:4} {'[ OK ]' if sc == magica else '[ DIFF: '+str(sc-magica)+' ]'}")

    d1 = sum(cuadro[i][i] for i in range(n))
    d2 = sum(cuadro[i][n-1-i] for i in range(n))
    print(f"\nDiagonal P: {d1:4} | Diagonal S: {d2:4}")
    print("="*60)

inicio = time.time()
solucion, c_final, iters_f = hill_climbing_con_reinicio(N, CONSTANTE_MAGICA, MAX_ITER)
fin = time.time()

imprimir_reporte_detallado(solucion, N, CONSTANTE_MAGICA, c_final, iters_f, fin - inicio)