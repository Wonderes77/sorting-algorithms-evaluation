"""
Módulo de Algoritmos de Ordenamiento
Autor: Esmeralda Gómez
Fecha: Febrero 2026
Descripción: Implementación de Bubble Sort y QuickSort para análisis comparativo
"""

def bubble_sort(lista):
    """
    Implementación del algoritmo Bubble Sort (Ordenamiento por Burbuja)
    
    Complejidad temporal: O(n²) en el peor caso
    Complejidad espacial: O(1) - ordenamiento in-place
    
    Args:
        lista: Lista de elementos a ordenar
    
    Returns:
        Lista ordenada en orden ascendente
    """
    # Crear una copia para no modificar la lista original
    arr = lista.copy()
    n = len(arr)
    
    # Recorrer todos los elementos
    for i in range(n):
        # Flag para optimización: detectar si hubo intercambios
        intercambio = False
        
        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            # Comparar elementos adyacentes
            if arr[j] > arr[j + 1]:
                # Intercambiar si están en el orden incorrecto
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambio = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not intercambio:
            break
    
    return arr


def quicksort(lista):
    """
    Implementación del algoritmo QuickSort (Recursivo)
    
    Justificación de elección recursiva:
    - Más intuitiva y legible
    - Representa fielmente el paradigma "divide y conquista"
    - Apropiada para fines educativos y análisis de complejidad
    
    Complejidad temporal: 
    - Mejor caso: O(n log n)
    - Caso promedio: O(n log n)
    - Peor caso: O(n²) cuando el pivote es siempre el menor/mayor elemento
    
    Complejidad espacial: O(log n) debido a la recursión
    
    Args:
        lista: Lista de elementos a ordenar
    
    Returns:
        Lista ordenada en orden ascendente
    """
    # Caso base: listas de 0 o 1 elemento ya están ordenadas
    if len(lista) <= 1:
        return lista.copy()
    
    # Seleccionar pivote (elemento del medio para mejor balance)
    pivote = lista[len(lista) // 2]
    
    # Particionar en tres sublistas
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    # Recursivamente ordenar y combinar
    return quicksort(menores) + iguales + quicksort(mayores)


# Función de prueba rápida
if __name__ == "__main__":
    # Datos de prueba
    test_data = [64, 34, 25, 12, 22, 11, 90]
    
    print("Lista original:", test_data)
    print("Bubble Sort:", bubble_sort(test_data))
    print("QuickSort:", quicksort(test_data))

