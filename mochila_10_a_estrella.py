import pandas
import re
import heapq

# Obtener el peso maximo del txt
with open("capacidades_mochila.txt" , "r" , encoding="utf-8") as archivo:
    contenido = archivo.read()
    resultado = re.search(r"capacidad=(\d+)", contenido)
    peso_maximo = int(resultado.group(1))

# Datos de los objetos
datos_objetos = pandas.read_csv("mochila_10.csv")
pesos = datos_objetos['peso'].to_list()
valores = datos_objetos['valor'].to_list()

# Heuristica Relajación Lineal 
def heuristica_mochila(indice_actual,capacidad_restante,pesos,valores):
    estimacion = 0
    objetos_restantes = []
    for i in range(indice_actual, len(pesos)):
        objetos_restantes.append((valores[i]/pesos[i],pesos[i],valores[i]))
    
    objetos_restantes.sort(reverse=True)

    for ratio , peso , valor in objetos_restantes:
        if capacidad_restante >= peso:
            capacidad_restante = capacidad_restante - peso
            estimacion = estimacion + valor
        else:
            estimacion = estimacion + (ratio * capacidad_restante)
            break

    return estimacion

def mochila_10_a_estrella(pesos,valores,capacidad_maxima):
   #estado_k = (indice_objeto, peso_acumulado, valor acumulado, objetos_seleccionados) 
    estado_0 = (0,0,0, ())
    f_inicial = heuristica_mochila(0,capacidad_maxima,pesos,valores)
    
    abrir = [(-f_inicial, estado_0)]

    while abrir:
        prioridad, estado_k = heapq.heappop(abrir)
        indice, p_acumulado, v_acumulado, seleccionados = estado_k

        # Decidimos para todos los objetos, encontramos una solucion        
        if(indice == len(pesos)):
            return v_acumulado, list(seleccionados), p_acumulado
    
        # Incluir el objeto si cabe
        if p_acumulado + pesos[indice] <= capacidad_maxima:
            p_nuevo = p_acumulado + pesos[indice]
            v_nuevo = v_acumulado + valores[indice]
            s_nuevo = seleccionados + (1,)

            #Volver a calcular h(n)
            h_v = heuristica_mochila(indice + 1, capacidad_maxima - p_nuevo, pesos, valores)
            #Volver a calcular f(n)
            f_v = v_nuevo + h_v

            heapq.heappush(abrir, (-f_v, (indice + 1, p_nuevo, v_nuevo, s_nuevo)))

        # No incluir el objeto
        s_nuevo = seleccionados + (0,)
        h_no = heuristica_mochila(indice + 1, capacidad_maxima - p_nuevo, pesos, valores)
        f_no = v_acumulado + h_no
        heapq.heappush(abrir, (-f_no, (indice + 1, p_acumulado, v_acumulado, s_nuevo)))
        

    return 0,[],0

valor_final, estado_final, peso_final = mochila_10_a_estrella(pesos,valores,peso_maximo)

print(valor_final)
print(estado_final)
print(peso_final)
