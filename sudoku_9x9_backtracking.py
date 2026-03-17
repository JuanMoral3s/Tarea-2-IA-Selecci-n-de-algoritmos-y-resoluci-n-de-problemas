import time
import re

#Leer tablero del txt
tablero = []
with open('sudoku_9x9_es.txt', 'r') as f:
    next(f)
    for linea in f:
        fila = list(map(int, linea.split()))
        tablero.append(fila)

#Buscar celdas vacias
def celda_vacia(tablero):
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j
    return None


def valor_valido(tablero,fila,columna,valor):

    #Restriccion filas
    for i in range(9):
        if tablero[fila][i] == valor:
            return False
    #Restriccion columnas   
    for i in range(9):
        if tablero[i][columna] == valor:
            return False
    
    #Restriccion subregion 3x3
    incio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(3):
        for j in range(3):
            if tablero[incio_fila + i][inicio_columna + j] == valor:
                return False
            
    return True


iteraciones = 0
def sudoku_9x9_backtracking(tablero):
    global iteraciones
    celda = celda_vacia(tablero)

    #Se encontro la solucion
    if not celda:
        return True
    
    fila, columna = celda

    for valor in range(1,10):
        iteraciones = iteraciones + 1
        
        if valor_valido(tablero,fila,columna,valor):

            tablero[fila][columna] = valor

            if sudoku_9x9_backtracking(tablero):
                return True

            #Quitar (X - v) Backtracking
            tablero[fila][columna] = 0
        
    return False


inicio_ejecucion = time.time()
resolver_sudoku = sudoku_9x9_backtracking(tablero)
fin_ejecucion = time.time()


if resolver_sudoku:
    print("Estado solución:")
    for fila in tablero:
        print(fila)
    print(f"Tamaño del tablero: {len(tablero)}x{len(tablero[0])}")
    print(f"Tiempo de ejecución: {fin_ejecucion - inicio_ejecucion:.6f}s")
    print(f"Iteraciones totales: {iteraciones}")
else:
    print("No se encontro una solución para el tablero propuesto")