import numpy as np
from matplotlib import pylab

def calcular_fft(wave, srate, n_fft=None):
    
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





