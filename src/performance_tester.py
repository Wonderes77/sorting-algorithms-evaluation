"""
Módulo de Pruebas de Rendimiento
Descripción: Ejecuta y mide el rendimiento de los algoritmos de ordenamiento
"""

import timeit
import statistics
from sorting_algorithms import bubble_sort, quicksort


def medir_tiempo_algoritmo(algoritmo, datos, repeticiones=5):
    """
    Mide el tiempo de ejecución de un algoritmo de ordenamiento
    
    Args:
        algoritmo: Función del algoritmo a evaluar
        datos: Lista de datos a ordenar
        repeticiones: Número de veces que se ejecuta el algoritmo
    
    Returns:
        Tupla (promedio, desviacion_estandar, tiempos_individuales)
    """
    tiempos = []
    
    for _ in range(repeticiones):
        # Crear una copia de los datos para cada repetición
        datos_copia = datos.copy()
        
        # Medir tiempo de ejecución usando timeit
        tiempo = timeit.timeit(
            lambda: algoritmo(datos_copia),
            number=1
        )
        tiempos.append(tiempo)
    
    # Calcular estadísticas
    promedio = statistics.mean(tiempos)
    desviacion = statistics.stdev(tiempos) if len(tiempos) > 1 else 0
    
    return promedio, desviacion, tiempos


def ejecutar_pruebas_completas(tamanos, escenarios, repeticiones=5):
    """
    Ejecuta todas las pruebas de rendimiento para diferentes tamaños y escenarios
    
    Args:
        tamanos: Lista de tamaños a probar
        escenarios: Lista de escenarios a probar
        repeticiones: Número de repeticiones por prueba
    
    Returns:
        Lista de diccionarios con los resultados
    """
    from data_generator import obtener_conjuntos_prueba
    
    # Generar todos los conjuntos de datos
    print("Generando conjuntos de datos de prueba...")
    conjuntos = obtener_conjuntos_prueba(tamanos, escenarios)
    
    # Algoritmos a probar
    algoritmos = {
        'Bubble Sort': bubble_sort,
        'QuickSort': quicksort
    }
    
    resultados = []
    total_pruebas = len(conjuntos) * len(algoritmos)
    prueba_actual = 0
    
    print(f"\nIniciando {total_pruebas} pruebas de rendimiento...")
    print("=" * 70)
    
    # Ejecutar pruebas para cada combinación
    for nombre_conjunto, datos in conjuntos.items():
        # Extraer información del nombre del conjunto
        partes = nombre_conjunto.split('_')
        escenario = '_'.join(partes[:-1])
        tamano = int(partes[-1])
        
        for nombre_algo, funcion_algo in algoritmos.items():
            prueba_actual += 1
            print(f"\nPrueba {prueba_actual}/{total_pruebas}")
            print(f"Algoritmo: {nombre_algo}")
            print(f"Escenario: {escenario}")
            print(f"Tamaño: {tamano:,} elementos")
            print(f"Repeticiones: {repeticiones}")
            
            try:
                # Medir tiempo
                promedio, desviacion, tiempos = medir_tiempo_algoritmo(
                    funcion_algo, 
                    datos, 
                    repeticiones
                )
                
                # Guardar resultados
                resultado = {
                    'algoritmo': nombre_algo,
                    'escenario': escenario,
                    'tamano': tamano,
                    'repeticiones': repeticiones,
                    'promedio_segundos': promedio,
                    'desviacion_estandar': desviacion,
                    'tiempos_individuales': tiempos,
                    'promedio_ms': promedio * 1000  # Convertir a milisegundos
                }
                
                resultados.append(resultado)
                
                print(f"✓ Tiempo promedio: {promedio*1000:.4f} ms")
                print(f"  Desviación estándar: {desviacion*1000:.4f} ms")
                
            except Exception as e:
                print(f"✗ Error en la prueba: {str(e)}")
                resultado = {
                    'algoritmo': nombre_algo,
                    'escenario': escenario,
                    'tamano': tamano,
                    'repeticiones': repeticiones,
                    'error': str(e)
                }
                resultados.append(resultado)
    
    print("\n" + "=" * 70)
    print("Pruebas completadas!")
    
    return resultados


def generar_tabla_resultados(resultados):
    """
    Genera una tabla formateada con los resultados
    
    Args:
        resultados: Lista de diccionarios con resultados
    
    Returns:
        String con la tabla formateada
    """
    # Encabezado
    tabla = "\n" + "=" * 100 + "\n"
    tabla += "RESULTADOS DE PRUEBAS DE RENDIMIENTO\n"
    tabla += "=" * 100 + "\n\n"
    
    # Formato de columnas
    formato = "{:<15} {:<20} {:<12} {:<12} {:<15} {:<15}\n"
    
    tabla += formato.format(
        "Algoritmo",
        "Escenario",
        "Tamaño",
        "Repeticiones",
        "Promedio (ms)",
        "Desv. Est. (ms)"
    )
    tabla += "-" * 100 + "\n"
    
    # Datos
    for r in resultados:
        if 'error' not in r:
            tabla += formato.format(
                r['algoritmo'],
                r['escenario'],
                f"{r['tamano']:,}",
                r['repeticiones'],
                f"{r['promedio_ms']:.4f}",
                f"{r['desviacion_estandar']*1000:.4f}"
            )
    
    tabla += "=" * 100 + "\n"
    
    return tabla


# Función principal
if __name__ == "__main__":
    # Configuración de pruebas
    TAMANOS = [100, 1000, 5000, 10000]
    ESCENARIOS = ['aleatoria', 'invertida']
    REPETICIONES = 5
    
    # Ejecutar pruebas
    resultados = ejecutar_pruebas_completas(TAMANOS, ESCENARIOS, REPETICIONES)
    
    # Mostrar resultados
    print(generar_tabla_resultados(resultados))