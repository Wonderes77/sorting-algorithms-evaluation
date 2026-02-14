"""
Módulo de Generación de Datos de Prueba
Descripción: Genera diferentes tipos de conjuntos de datos para evaluar algoritmos
"""

import random


def generar_lista_aleatoria(tamano):
    """
    Genera una lista con números aleatorios
    
    Args:
        tamano: Cantidad de elementos en la lista
    
    Returns:
        Lista con números aleatorios entre 0 y tamano*10
    """
    return [random.randint(0, tamano * 10) for _ in range(tamano)]


def generar_lista_invertida(tamano):
    """
    Genera una lista ordenada en orden descendente (peor caso para Bubble Sort)
    
    Args:
        tamano: Cantidad de elementos en la lista
    
    Returns:
        Lista ordenada de mayor a menor
    """
    return list(range(tamano, 0, -1))


def generar_lista_casi_ordenada(tamano, porcentaje_desordenado=10):
    """
    Genera una lista casi ordenada con algunos elementos fuera de lugar
    
    Args:
        tamano: Cantidad de elementos en la lista
        porcentaje_desordenado: Porcentaje de elementos a desordenar
    
    Returns:
        Lista casi ordenada
    """
    lista = list(range(tamano))
    
    # Calcular cuántos elementos desordenar
    num_intercambios = int(tamano * porcentaje_desordenado / 100)
    
    # Realizar intercambios aleatorios
    for _ in range(num_intercambios):
        i = random.randint(0, tamano - 1)
        j = random.randint(0, tamano - 1)
        lista[i], lista[j] = lista[j], lista[i]
    
    return lista


def obtener_conjuntos_prueba(tamanos, escenarios):
    """
    Genera todos los conjuntos de prueba para los experimentos
    
    Args:
        tamanos: Lista con los tamaños a probar (ej: [100, 1000, 5000])
        escenarios: Lista con los tipos de escenarios (ej: ['aleatoria', 'invertida'])
    
    Returns:
        Diccionario con todos los conjuntos de datos generados
    """
    generadores = {
        'aleatoria': generar_lista_aleatoria,
        'invertida': generar_lista_invertida,
        'casi_ordenada': generar_lista_casi_ordenada,
    }
    
    conjuntos = {}
    
    for tamano in tamanos:
        for escenario in escenarios:
            if escenario in generadores:
                clave = f"{escenario}_{tamano}"
                conjuntos[clave] = generadores[escenario](tamano)
    
    return conjuntos


# Prueba del módulo
if __name__ == "__main__":
    print("Generando datos de prueba...")
    
    # Generar muestras pequeñas para verificación
    print("\nLista aleatoria (10 elementos):", generar_lista_aleatoria(10))
    print("Lista invertida (10 elementos):", generar_lista_invertida(10))
    print("Lista casi ordenada (10 elementos):", generar_lista_casi_ordenada(10))