# Tarea 2 IA: Selección de algoritmos y resolución de problemas

Este repositorio contiene la implementación de diversos algoritmos clásicos de Inteligencia Artificial para resolver los problemas específicos planteados en la Tarea 2 de la asignatura. El objetivo principal es aplicar técnicas como búsqueda informada, búsqueda local y problemas de satisfacción de restricciones (CSP) para encontrar soluciones eficientes a problemas de diversa escala.

## Contenido del Repositorio

El proyecto se organiza en archivos independientes para cada problema. Se han seleccionado los algoritmos basándose en la complejidad y naturaleza de cada reto:

* **Mochila 0/1 (10 y 100 objetos):** Resolución mediante el algoritmo A* para la instancia de 10 objetos y Algoritmos Genéticos para la instancia de 100 objetos.
* **N-Reinas (8 y 100):** Implementación utilizando Búsqueda Tabú para encontrar configuraciones con cero conflictos en tableros de ambos tamaños.
* **Sudoku 9x9:** Algoritmo de Backtracking (CSP) con selección de celdas vacías.
* **Sudoku 16x16 (Hexadoku):** Resolución mediante Backtracking incorporando pre-procesamiento AC-3 y la heurística MRV (Variable más restringida) para manejar el aumento en la complejidad.
* **Coloreo de Mapas (5 y 100 países):** Utilización de Recocido Simulado (Simulated Annealing) para encontrar el número mínimo de colores bajo restricciones de adyacencia.
* **Cuadro Mágico (10x10):** Implementación de Hill Climbing con Reinicios Aleatorios para abordar la complejidad de sumar la constante mágica 505 en todas las direcciones.

## Requisitos y Archivos de Datos

Cada script de Python requiere la presencia de archivos de datos específicos en el mismo directorio para funcionar correctamente. Asegúrese de contar con los siguientes archivos según el problema a ejecutar:

1.  **Problema 1 (Mochila):** `mochila_10.csv`, `mochila_100.csv` y `capacidades_mochila.txt`.
2.  **Problema 3 (Sudoku 9x9):** `sudoku_9x9_es.txt`.
3.  **Problema 4 (Sudoku 16x16):** `sudoku_16x16_es.txt`.
4.  **Problema 5 (Coloreo de Mapas):** `mapa_5_paises_adyacencias.txt` y `mapa_100_paises_adyacencias.txt`.
5.  **Problema 6 (Cuadro Mágico):** `cuadro_magico_10_especificacion.txt`.

## Instrucciones de Uso

Cada problema está contenido en su propio archivo de Python y puede ser ejecutado de manera independiente. Para resolver un problema específico, ejecute el script correspondiente desde la terminal:

```bash
python nombre_del_archivo.py
