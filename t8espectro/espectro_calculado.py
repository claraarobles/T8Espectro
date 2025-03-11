import numpy as np
from matplotlib import pylab

def calcular_fft(wave, srate):
    # Calcular la Transformada Rápida de Fourier (FFT) de la señal
    spectrum = np.fft.fft(wave)
    
    # Calcular las frecuencias correspondientes a los componentes de la FFT
    freqs = np.fft.fftfreq(len(wave), 1/srate)
    
    # Tomar solo la mitad del espectro (parte positiva)
    half_spectrum = spectrum[:len(wave)//2]
    half_freqs = freqs[:len(wave)//2]
    
    return half_freqs, half_spectrum


