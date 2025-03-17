
import numpy as np


def calcular_fft(wave, srate, n_fft=None):
    '''
    Calcula la Transformada Rápida de Fourier (FFT) de una señal de entrada.
    Parámetros:
    wave (array-like): La señal de entrada en el dominio del tiempo.
    srate (float): La tasa de muestreo de la señal.
    n_fft (int, opcional): El número de puntos para calcular la FFT. Si no se especifica
    se usa el tamaño de la señal.
    Retorna:
        - half_freqs (array-like): Las frecuencias correspondientes a los componentes de
        la FFT.
        - half_spectrum (array-like): La mitad positiva del espectro de la FFT.
    '''

    if n_fft is None:
        n_fft = len(wave)  # Por defecto, FFT del mismo tamaño de la señal

    # Calcular la Transformada Rápida de Fourier (FFT) de la señal
    spectrum = np.fft.fft(wave, n=n_fft)

    # Calcular las frecuencias correspondientes a los componentes de la FFT
    freqs = np.fft.fftfreq(n_fft, 1/srate)

    # Tomar solo la mitad del espectro (parte positiva)
    half_spectrum = np.asarray(spectrum[:n_fft//2])
    half_freqs = np.asarray(freqs[:n_fft//2])

    return half_freqs, (half_spectrum)
