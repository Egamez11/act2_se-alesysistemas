# Actividad Formativa 2: Simulación y Análisis de Señales con la Transformada de Fourier

Este repositorio contiene la resolución práctica para la asignatura de **Señales y Sistemas**. El objetivo del proyecto es modelar señales elementales en el dominio del tiempo, calcular su comportamiento espectral en el dominio de la frecuencia mediante la Transformada Rápida de Fourier (FFT) y analizar visualmente sus propiedades utilizando Python.

---

## 🚀 Contenido del Proyecto

El script principal genera, procesa y grafica tres tipos de señales fundamentales:
1. **Señal Senoidal:** Una señal periódica pura de $50\text{ Hz}$.
2. **Pulso Rectangular:** Una señal aperiódica con transiciones abruptas (activa entre los $0.3$ y $0.7$ segundos).
3. **Función Escalón Unitario:** Una señal de conmutación (activa a partir de los $0.2$ segundos).

Para cada señal se calcula e interpreta:
* Representación temporal discreta.
* Espectro de **Magnitud** (un solo lado corregido).
* Espectro de **Fase** en radianes.

---

## 🛠️ Requisitos e Instalación

Este proyecto está desarrollado en **Python 3** utilizando un entorno virtual. Para poder ejecutar el código, asegúrate de tener instaladas las siguientes librerías de cómputo científico:

pip install numpy matplotlib scipy

git clone [https://github.com/Egamez11/act2_se-alesistemas.git](https://github.com/Egamez11/act2_se-alesistemas.git)
cd act2_se-alesistemas

python act2.py
