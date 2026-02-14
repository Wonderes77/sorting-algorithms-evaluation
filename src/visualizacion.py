"""
Módulo de Visualización de Resultados
Genera gráficas comparativas del rendimiento de los algoritmos
"""

import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import glob


def cargar_resultados(ruta_json):
    """Carga los resultados desde un archivo JSON"""
    with open(ruta_json, 'r', encoding='utf-8') as f:
        return json.load(f)


def crear_grafica_comparativa(resultados, ruta_salida):
    """Crea una gráfica comparativa de los tiempos de ejecución"""
    # Filtrar resultados válidos
    resultados_validos = [r for r in resultados if 'error' not in r]
    
    # Convertir a DataFrame
    df = pd.DataFrame(resultados_validos)
    
    # Crear figura con subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Evaluación de Rendimiento: Bubble Sort vs QuickSort', 
                 fontsize=16, fontweight='bold')
    
    # Gráfica 1: Barras - Escenario Aleatorio
    ax1 = axes[0, 0]
    datos_aleatorio = df[df['escenario'] == 'aleatoria']
    
    tamanos = sorted(datos_aleatorio['tamano'].unique())
    bubble_times = [datos_aleatorio[(datos_aleatorio['tamano'] == t) & 
                                     (datos_aleatorio['algoritmo'] == 'Bubble Sort')]['promedio_ms'].values[0] 
                    for t in tamanos]
    quick_times = [datos_aleatorio[(datos_aleatorio['tamano'] == t) & 
                                    (datos_aleatorio['algoritmo'] == 'QuickSort')]['promedio_ms'].values[0] 
                   for t in tamanos]
    
    x = np.arange(len(tamanos))
    width = 0.35
    
    ax1.bar(x - width/2, bubble_times, width, label='Bubble Sort', color='#FF6B6B')
    ax1.bar(x + width/2, quick_times, width, label='QuickSort', color='#4ECDC4')
    
    ax1.set_xlabel('Tamaño de la lista', fontweight='bold')
    ax1.set_ylabel('Tiempo (ms)', fontweight='bold')
    ax1.set_title('Escenario: Lista Aleatoria')
    ax1.set_xticks(x)
    ax1.set_xticklabels([f'{t:,}' for t in tamanos])
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfica 2: Barras - Escenario Invertido
    ax2 = axes[0, 1]
    datos_invertido = df[df['escenario'] == 'invertida']
    
    bubble_times_inv = [datos_invertido[(datos_invertido['tamano'] == t) & 
                                         (datos_invertido['algoritmo'] == 'Bubble Sort')]['promedio_ms'].values[0] 
                        for t in tamanos]
    quick_times_inv = [datos_invertido[(datos_invertido['tamano'] == t) & 
                                        (datos_invertido['algoritmo'] == 'QuickSort')]['promedio_ms'].values[0] 
                       for t in tamanos]
    
    ax2.bar(x - width/2, bubble_times_inv, width, label='Bubble Sort', color='#FF6B6B')
    ax2.bar(x + width/2, quick_times_inv, width, label='QuickSort', color='#4ECDC4')
    
    ax2.set_xlabel('Tamaño de la lista', fontweight='bold')
    ax2.set_ylabel('Tiempo (ms)', fontweight='bold')
    ax2.set_title('Escenario: Lista Invertida')
    ax2.set_xticks(x)
    ax2.set_xticklabels([f'{t:,}' for t in tamanos])
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Gráfica 3: Líneas - Escalabilidad
    ax3 = axes[1, 0]
    
    ax3.plot(tamanos, bubble_times, marker='o', linewidth=2, 
             markersize=8, label='Bubble Sort (Aleatoria)', color='#FF6B6B')
    ax3.plot(tamanos, bubble_times_inv, marker='s', linewidth=2, 
             markersize=8, label='Bubble Sort (Invertida)', color='#FF8E8E', linestyle='--')
    ax3.plot(tamanos, quick_times, marker='o', linewidth=2, 
             markersize=8, label='QuickSort (Aleatoria)', color='#4ECDC4')
    ax3.plot(tamanos, quick_times_inv, marker='s', linewidth=2, 
             markersize=8, label='QuickSort (Invertida)', color='#6FD9D0', linestyle='--')
    
    ax3.set_xlabel('Tamaño de la lista', fontweight='bold')
    ax3.set_ylabel('Tiempo (ms)', fontweight='bold')
    ax3.set_title('Escalabilidad de los Algoritmos')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    ax3.legend()
    ax3.grid(True, which="both", alpha=0.3)
    
    # Gráfica 4: Factor de mejora
    ax4 = axes[1, 1]
    
    factores_aleatorio = [b/q for b, q in zip(bubble_times, quick_times)]
    factores_invertido = [b/q for b, q in zip(bubble_times_inv, quick_times_inv)]
    
    ax4.bar(x - width/2, factores_aleatorio, width, label='Lista Aleatoria', color='#95E1D3')
    ax4.bar(x + width/2, factores_invertido, width, label='Lista Invertida', color='#F38181')
    
    ax4.set_xlabel('Tamaño de la lista', fontweight='bold')
    ax4.set_ylabel('Factor de mejora (veces más rápido)', fontweight='bold')
    ax4.set_title('QuickSort vs Bubble Sort: Factor de Mejora')
    ax4.set_xticks(x)
    ax4.set_xticklabels([f'{t:,}' for t in tamanos])
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # Añadir valores sobre las barras
    for i, (v1, v2) in enumerate(zip(factores_aleatorio, factores_invertido)):
        ax4.text(i - width/2, v1, f'{v1:.1f}x', ha='center', va='bottom', fontsize=9)
        ax4.text(i + width/2, v2, f'{v2:.1f}x', ha='center', va='bottom', fontsize=9)
    
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=300, bbox_inches='tight')
    print(f"✓ Gráfica guardada en: {ruta_salida}")


if __name__ == "__main__":
    # Buscar el archivo JSON más reciente
    archivos = glob.glob("../results/resultados_*.json")
    if archivos:
        archivo_reciente = max(archivos)
        print(f"Cargando resultados de: {archivo_reciente}")
        
        resultados = cargar_resultados(archivo_reciente)
        
        # Crear gráfica
        crear_grafica_comparativa(resultados, "../results/grafica_comparativa.png")
        
        print("\n✓ Gráfica generada exitosamente")
    else:
        print("No se encontraron archivos de resultados")