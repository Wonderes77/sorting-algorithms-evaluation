# 📊 Evaluación de Métodos de Ordenamiento

## 📝 Descripción y Objetivo

Este proyecto implementa y evalúa comparativamente dos algoritmos de ordenamiento clásicos (**Bubble Sort** y **QuickSort**) en Python, analizando su rendimiento mediante pruebas controladas.

### Objetivo Principal

Implementar y evaluar en Python dos métodos de ordenamiento (Bubble Sort y QuickSort) usando Visual Studio Code como entorno de desarrollo, comparando su rendimiento con pruebas controladas. La actividad refuerza el pensamiento algorítmico y el análisis de eficiencia, útiles para optimizar software en aplicaciones de robótica.

### Algoritmos Implementados

- **Bubble Sort (Ordenamiento de Burbuja)**: 
  - Algoritmo simple con complejidad temporal O(n²)
  - Incluye optimización de detección temprana
  - Ordenamiento in-place con complejidad espacial O(1)

- **QuickSort (Ordenamiento Rápido)**: 
  - Algoritmo eficiente con complejidad temporal O(n log n) en promedio
  - Implementación recursiva usando paradigma "divide y conquista"
  - Selección de pivote en el centro para mejor balance

---

## 🔧 Requisitos

### Software Necesario

- **Python**: Versión 3.8 o superior
- **Visual Studio Code**: Editor de código (recomendado)
- **Git**: Para control de versiones

### Librerías de Python

Las siguientes librerías son necesarias para ejecutar el proyecto completo:

```bash
matplotlib==3.7.0    # Para visualización de datos
pandas==2.0.0        # Para análisis de datos
reportlab==4.0.0     # Para generación de reportes PDF (opcional)
```

### Instalación de Dependencias

Instala todas las dependencias con:

```bash
pip install matplotlib pandas reportlab
```

O instálalas individualmente:

```bash
pip install matplotlib
pip install pandas
pip install reportlab
```

---

## 🚀 Cómo Ejecutar el Programa

### Opción 1: Ejecutar el experimento completo

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Wonderes77/sorting-algorithms-evaluation.git
   cd sorting-algorithms-evaluation
   ```

2. Navega a la carpeta `src`:
   ```bash
   cd src
   ```

3. Ejecuta el script principal:
   ```bash
   python main.py
   ```

   Este comando:
   - Genera conjuntos de datos de prueba
   - Ejecuta 16 pruebas de rendimiento (2 algoritmos × 4 tamaños × 2 escenarios)
   - Calcula estadísticas (promedio y desviación estándar)
   - Guarda resultados en `results/` en formatos JSON, CSV y TXT

### Opción 2: Generar visualizaciones

Después de ejecutar las pruebas, genera las gráficas:

```bash
python visualizacion.py
```

Esto creará gráficas comparativas en `results/grafica_comparativa.png`

### Opción 3: Probar algoritmos individualmente

Para verificar que los algoritmos funcionan correctamente:

```bash
python sorting_algorithms.py
```

---

## 📁 Estructura del Repositorio

```
sorting-algorithms-evaluation/
│
├── src/                                    # Código fuente
│   ├── sorting_algorithms.py              # Implementación de Bubble Sort y QuickSort
│   ├── data_generator.py                  # Generación de conjuntos de datos de prueba
│   ├── performance_tester.py              # Sistema de medición de rendimiento
│   ├── visualizacion.py                   # Generación de gráficas comparativas
│   ├── main.py                            # Script principal de ejecución
│   └── generar_reporte_sin_portada.py     # Generador del reporte PDF
│
├── results/                                # Resultados experimentales
│   ├── resultados_[timestamp].json        # Datos completos en formato JSON
│   ├── resultados_[timestamp].csv         # Tabla de resultados en CSV
│   ├── tabla_resultados_[timestamp].txt   # Tabla formateada en texto plano
│   ├── analisis_[timestamp].txt           # Análisis comparativo textual
│   └── grafica_comparativa.png            # Gráficas de visualización
│
├── docs/                                   # Documentación
│   └── Reporte_Evaluacion_Algoritmos.pdf  # Reporte final del proyecto
│
├── README.md                               # Este archivo - Documentación del proyecto
└── .gitignore                              # Archivos ignorados por Git

```

---

## 📊 Resumen de Resultados

### Configuración Experimental

- **Tamaños probados**: 100, 1,000, 5,000 y 10,000 elementos
- **Escenarios**: Listas aleatorias y listas invertidas (peor caso)
- **Repeticiones**: 5 ejecuciones por cada combinación
- **Herramienta de medición**: `timeit` (biblioteca estándar de Python)
- **Total de pruebas**: 16 pruebas independientes

### Hallazgos Principales

| Tamaño | Escenario | Bubble Sort (ms) | QuickSort (ms) | Factor de Mejora |
|--------|-----------|------------------|----------------|------------------|
| 100 | Aleatoria | 0.22 | 0.06 | **3.6x más rápido** |
| 100 | Invertida | 0.26 | 0.04 | **6.3x más rápido** |
| 1,000 | Aleatoria | 26.73 | 0.81 | **32.9x más rápido** |
| 1,000 | Invertida | 33.87 | 0.47 | **71.4x más rápido** |
| 5,000 | Aleatoria | 780.57 | 5.59 | **139.5x más rápido** |
| 5,000 | Invertida | 981.79 | 2.94 | **333.8x más rápido** |
| 10,000 | Aleatoria | 3,156.15 | 11.35 | **278.0x más rápido** |
| 10,000 | Invertida | 3,890.93 | 6.83 | **569.5x más rápido** ⚡ |

### Conclusiones Clave

✅ **Escalabilidad**: QuickSort demuestra escalabilidad superior, manteniendo eficiencia incluso con 10,000 elementos

✅ **Validación teórica**: Los resultados experimentales coinciden con la complejidad esperada:
   - Bubble Sort: O(n²) - crecimiento cuadrático confirmado
   - QuickSort: O(n log n) - crecimiento logarítmico confirmado

✅ **Impacto práctico**: La diferencia se acentúa dramáticamente con datasets grandes:
   - En 10,000 elementos: QuickSort ahorra **99.8% del tiempo**
   - Diferencia entre respuesta instantánea (11ms) vs perceptible (3.9s)

✅ **Aplicación en robótica**: Para procesamiento de datos de sensores en tiempo real, QuickSort es **crítico** y permite respuestas en milisegundos vs segundos

### Visualización de Resultados

Las gráficas generadas incluyen:
- Comparación de tiempos por escenario (barras)
- Análisis de escalabilidad (líneas logarítmicas)
- Factores de mejora de QuickSort sobre Bubble Sort
- Curvas de complejidad teórica vs real

---

## 🤖 Aplicación en Robótica

Este análisis es especialmente relevante para sistemas robóticos donde:

- **Procesamiento de nubes de puntos**: LiDAR genera miles de puntos que requieren ordenamiento
- **Planificación de trayectorias**: Algoritmos como A* necesitan mantener nodos ordenados
- **Fusión de sensores**: Combinar datos temporales requiere ordenamiento eficiente
- **Tiempo real**: La diferencia entre 11ms y 3,900ms determina si el sistema es funcional

**Ejemplo práctico**: Un robot autónomo procesando 10,000 lecturas:
- Con Bubble Sort: 3.9 segundos ❌ (inaceptable en tiempo real)
- Con QuickSort: 11 milisegundos ✅ (perfectamente viable)

---

## 👨‍💻 Autor

**ESMERALDA GÓMEZ HUERTA**

- Proyecto: Evaluación de Algoritmos de Ordenamiento
- Programa: Ingeniería en Robótica
- Fecha: Febrero 2026
- Repositorio: https://github.com/Wonderes77/sorting-algorithms-evaluation

---

## 📄 Documentación Adicional

Para más detalles sobre la metodología, resultados completos y análisis exhaustivo, consulta el **reporte en PDF**:

📑 **[U1PA4_REP-PROGRAMA_Gómez_Esmeralda.pdf](docs/U1PA4_REP-PROGRAMA_Gómez_Esmeralda.pdf)**

El reporte incluye:
- Metodología detallada del experimento
- Tablas completas de resultados
- Gráficas y visualizaciones
- Análisis estadístico
- Aplicaciones en robótica
- Conclusiones y referencias bibliográficas

---

## 📝 Licencia

Este proyecto es de código abierto y está disponible para fines educativos.

---

## 🙏 Referencias

- Cormen, T. H., et al. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
- Python Software Foundation. (2024). *Python timeit Documentation*.
- Knuth, D. E. (1998). *The Art of Computer Programming, Vol. 3: Sorting and Searching*.

---

**⭐ Si este proyecto te fue útil, no olvides darle una estrella en GitHub!**