import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de los parámetros de muestreo
Fs = 1000          # Frecuencia de muestreo (Hz)
T = 1 / Fs         # Periodo de muestreo
L = 1000           # Longitud de la señal (Número de muestras)
t = np.arange(0, L) * T  # Vector de tiempo

# 2. Creación de señales elementales
# a) Función senoidal (ej. 50 Hz)
f0 = 50
senal_senoidal = np.sin(2 * np.pi * f0 * t)

# b) Pulso rectangular
senal_pulso = np.zeros(L)
senal_pulso[(t >= 0.3) & (t <= 0.7)] = 1.0  # Activo entre 0.3 y 0.7 segundos

# c) Función escalón unitario
senal_escalon = np.zeros(L)
senal_escalon[t >= 0.2] = 1.0  # Activo a partir de 0.2 segundos


# 3. Función para calcular y graficar la FFT (Magnitud y Fase)
def analizar_frecuencia(senal, nombre_senal):
    # Calcular la FFT usando numpy
    Y = np.fft.fft(senal)
    
    # Calcular el espectro de dos lados y luego obtener el de un solo lado
    P2 = np.abs(Y / L)
    P1 = P2[0:int(L/2)+1]
    P1[1:-1] = 2 * P1[1:-1] # Magnitud corregida
    
    # Calcular la fase
    fase2 = np.angle(Y)
    fase1 = fase2[0:int(L/2)+1]
    
    # Vector de frecuencias
    f = Fs * np.arange(0, (L/2)+1) / L

    # Graficación
    plt.figure(figsize=(12, 6))

    # Dominio del tiempo
    plt.subplot(3, 1, 1)
    plt.plot(t, senal, color='blue')
    plt.title(f'Señal en el Dominio del Tiempo - {nombre_senal}')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Amplitud')
    plt.grid(True)

    # Dominio de la frecuencia (Magnitud)
    plt.subplot(3, 1, 2)
    plt.stem(f, P1, linefmt='orange', markerfmt='or', basefmt=' ')
    plt.title('Espectro de Magnitud (Un solo lado)')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('|X(f)|')
    plt.grid(True)

    # Dominio de la frecuencia (Fase)
    plt.subplot(3, 1, 3)
    plt.plot(f, fase1, color='green')
    plt.title('Espectro de Fase')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Fase (radianes)')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# 4. Ejecutar el análisis para cada señal
analizar_frecuencia(senal_senoidal, "Función Senoidal (50 Hz)")
analizar_frecuencia(senal_pulso, "Pulso Rectangular")
analizar_frecuencia(senal_escalon, "Función Escalón")