"""
Script Principal - Evaluación de Algoritmos de Ordenamiento
Autor: [Tu Nombre]
Fecha: Febrero 2026

Este script ejecuta el experimento completo de evaluación de rendimiento
de los algoritmos Bubble Sort y QuickSort.
"""

import json
import csv
from datetime import datetime
from performance_tester import ejecutar_pruebas_completas, generar_tabla_resultados


def guardar_resultados_json(resultados, ruta):
    """Guarda los resultados en formato JSON"""
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    print(f"✓ Resultados guardados en: {ruta}")


def guardar_resultados_csv(resultados, ruta):
    """Guarda los resultados en formato CSV"""
    if not resultados:
        return
    
    # Filtrar resultados sin errores
    resultados_validos = [r for r in resultados if 'error' not in r]
    
    if not resultados_validos:
        return
    
    # Escribir CSV
    with open(ruta, 'w', newline='', encoding='utf-8') as f:
        campos = ['algoritmo', 'escenario', 'tamano', 'repeticiones', 
                  'promedio_segundos', 'promedio_ms', 'desviacion_estandar']
        
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        
        for r in resultados_validos:
            fila = {campo: r[campo] for campo in campos}
            writer.writerow(fila)
    
    print(f"✓ Resultados guardados en: {ruta}")


def guardar_tabla_texto(resultados, ruta):
    """Guarda la tabla de resultados en formato texto"""
    tabla = generar_tabla_resultados(resultados)
    
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(tabla)
    
    print(f"✓ Tabla guardada en: {ruta}")


def generar_analisis_comparativo(resultados):
    """
    Genera un análisis comparativo de los resultados
    
    Args:
        resultados: Lista de resultados de las pruebas
    
    Returns:
        String con el análisis
    """
    analisis = "\n" + "=" * 80 + "\n"
    analisis += "ANÁLISIS COMPARATIVO DE RENDIMIENTO\n"
    analisis += "=" * 80 + "\n\n"
    
    # Agrupar por tamaño
    por_tamano = {}
    for r in resultados:
        if 'error' not in r:
            tamano = r['tamano']
            if tamano not in por_tamano:
                por_tamano[tamano] = []
            por_tamano[tamano].append(r)
    
    # Análisis por tamaño
    for tamano in sorted(por_tamano.keys()):
        analisis += f"\n--- Tamaño: {tamano:,} elementos ---\n\n"
        
        datos = por_tamano[tamano]
        
        # Agrupar por escenario
        por_escenario = {}
        for d in datos:
            esc = d['escenario']
            if esc not in por_escenario:
                por_escenario[esc] = {}
            por_escenario[esc][d['algoritmo']] = d['promedio_ms']
        
        # Comparar algoritmos en cada escenario
        for escenario, tiempos in por_escenario.items():
            analisis += f"Escenario: {escenario}\n"
            
            if 'Bubble Sort' in tiempos and 'QuickSort' in tiempos:
                bubble = tiempos['Bubble Sort']
                quick = tiempos['QuickSort']
                
                analisis += f"  • Bubble Sort: {bubble:.4f} ms\n"
                analisis += f"  • QuickSort: {quick:.4f} ms\n"
                
                if quick > 0:
                    factor = bubble / quick
                    analisis += f"  → QuickSort es {factor:.2f}x más rápido\n"
                    
                    if factor > 1:
                        ahorro_porcentaje = ((bubble - quick) / bubble) * 100
                        analisis += f"  → Ahorro de tiempo: {ahorro_porcentaje:.1f}%\n"
            
            analisis += "\n"
    
    # Observaciones generales
    analisis += "\n--- OBSERVACIONES CLAVE ---\n\n"
    
    analisis += "1. ESCALABILIDAD:\n"
    analisis += "   • Bubble Sort muestra crecimiento cuadrático O(n²)\n"
    analisis += "   • QuickSort muestra crecimiento logarítmico O(n log n)\n"
    analisis += "   • La diferencia se hace más notable con tamaños grandes\n\n"
    
    analisis += "2. ESCENARIOS:\n"
    analisis += "   • Lista invertida: peor caso para Bubble Sort\n"
    analisis += "   • Lista aleatoria: caso promedio para ambos\n"
    analisis += "   • QuickSort mantiene buen rendimiento en todos los casos\n\n"
    
    analisis += "3. APLICACIÓN EN ROBÓTICA:\n"
    analisis += "   • Procesamiento de datos de sensores: QuickSort preferible\n"
    analisis += "   • Tiempo real: QuickSort es crítico para respuesta rápida\n"
    analisis += "   • Grandes volúmenes: diferencia puede ser de segundos vs minutos\n"
    analisis += "   • Sistemas embebidos: considerar también uso de memoria\n\n"
    
    analisis += "=" * 80 + "\n"
    
    return analisis


def main():
    """Función principal que ejecuta todo el experimento"""
    
    print("\n" + "=" * 80)
    print("EVALUACIÓN DE MÉTODOS DE ORDENAMIENTO")
    print("Bubble Sort vs QuickSort")
    print("=" * 80 + "\n")
    
    # Configuración del experimento
    print("CONFIGURACIÓN DEL EXPERIMENTO:")
    print("-" * 40)
    
    TAMANOS = [100, 1000, 5000, 10000]
    ESCENARIOS = ['aleatoria', 'invertida']
    REPETICIONES = 5
    
    print(f"Tamaños a probar: {TAMANOS}")
    print(f"Escenarios: {ESCENARIOS}")
    print(f"Repeticiones por prueba: {REPETICIONES}")
    print(f"Total de pruebas: {len(TAMANOS) * len(ESCENARIOS) * 2}")
    print()
    
    # Ejecutar pruebas
    resultados = ejecutar_pruebas_completas(TAMANOS, ESCENARIOS, REPETICIONES)
    
    # Mostrar tabla de resultados
    print(generar_tabla_resultados(resultados))
    
    # Generar análisis
    analisis = generar_analisis_comparativo(resultados)
    print(analisis)
    
    # Guardar resultados
    print("\nGuardando resultados...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    guardar_resultados_json(
        resultados, 
        f"../results/resultados_{timestamp}.json"
    )
    
    guardar_resultados_csv(
        resultados,
        f"../results/resultados_{timestamp}.csv"
    )
    
    guardar_tabla_texto(
        resultados,
        f"../results/tabla_resultados_{timestamp}.txt"
    )
    
    # Guardar análisis
    with open(f"../results/analisis_{timestamp}.txt", 'w', encoding='utf-8') as f:
        f.write(analisis)
    print(f"✓ Análisis guardado en: ../results/analisis_{timestamp}.txt")
    
    print("\n" + "=" * 80)
    print("EXPERIMENTO COMPLETADO EXITOSAMENTE")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()