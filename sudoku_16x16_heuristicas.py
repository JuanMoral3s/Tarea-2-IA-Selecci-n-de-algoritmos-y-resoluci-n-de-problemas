import time

SIMBOLOS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

tablero = []

with open('sudoku_16x16_es.txt', 'r') as f:
    next(f)
    next(f)
    next(f)
    lineas = [l.split() for l in f if len(l.split()) == 16]
    for l in lineas:
        tablero.append(l)
   


def valor_valido(tablero,fila,columna,valor):

    #Restriccion filas
    for i in range(16):
        if tablero[fila][i] == valor:
            return False
    #Restriccion columnas   
    for i in range(16):
        if tablero[i][columna] == valor:
            return False
    
    #Restriccion subregion 4x4
    incio_fila, inicio_columna = 4 * (fila // 4), 4 * (columna // 4)
    for i in range(4):
        for j in range(4):
            if tablero[incio_fila + i][inicio_columna + j] == valor:
                return False
            
    return True


def obtener_mrv(tablero):
    mejor_celda = None
    min_opciones = 17

    for r in range(16):
        for c in range(16):
            if tablero[r][c] == '.':
                opciones = sum(1 for v in SIMBOLOS if valor_valido(tablero, r, c, v))
                if opciones < min_opciones:
                    min_opciones = opciones
                    mejor_celda = (r, c)
                if min_opciones == 1: 
                    return mejor_celda
    return mejor_celda

def preproceso_ac3(tablero):
    cambio = True
    while cambio:
        cambio = False
        for r in range(16):
            for c in range(16):
                if tablero[r][c] == '.':
                    opciones = [v for v in SIMBOLOS if valor_valido(tablero, r, c, v)]
                    if len(opciones) == 1:
                        tablero[r][c] = opciones[0]
                        cambio = True


def resolver_sudoku_16x16(tablero):
    
    global iteraciones
    if iteraciones % 10000 == 0:
        print(f"Iteración: {iteraciones} | Celdas asignadas: {sum(row.count('.') == 0 for row in tablero)}")

    celda = obtener_mrv(tablero)
    if not celda: return True
    
    fila, col = celda

    for valor in SIMBOLOS: 
        if valor_valido(tablero, fila, col, valor):
            tablero[fila][col] = valor
            
           
            if potencial(tablero):
                iteraciones += 1
                if resolver_sudoku_16x16(tablero):
                    return True
            
           
            tablero[fila][col] = '.'
    return False

def potencial(tablero):
   
    for r in range(16):
        for c in range(16):
            if tablero[r][c] == '.':
                tiene_opcion = False
                for v in SIMBOLOS:
                    if valor_valido(tablero, r, c, v):
                        tiene_opcion = True
                        break
                if not tiene_opcion:
                    return False
    return True

iteraciones = 0

inicio = time.time()

# Limpiar tablero con ac-3
preproceso_ac3(tablero)

solucionado = resolver_sudoku_16x16(tablero)
fin = time.time()

if solucionado:
    for f in tablero:
        print(" ".join(f))
    print(f"Iteraciones: {iteraciones}")
    print(f"Tiempo total: {fin - inicio:.6f}s")
else:
    print("No se encontro una solución para el tablero propuesto")