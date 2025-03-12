from t8espectro.espectro_calculado import calcular_fft  # Importa la función desde tu código
import numpy as np

def test_fft_output():
    
    '''
    Prueba la función de Transformada Rápida de Fourier (FFT).
    Genera una señal senoidal de 50 Hz y calcula su FFT para verificar que 
    la frecuencia detectada coincida con la frecuencia real.
    Pasos:
    1. Genera una señal senoidal de 50 Hz con una frecuencia de muestreo de 1000 Hz.
    2. Calcula la FFT de la señal.
    3. Encuentra la frecuencia con el valor más alto en el espectro.
    4. Verifica que la frecuencia detectada esté cerca de 50 Hz.
    '''

    # Datos de prueba: señal senoidal simple
    srate = 1000  # Frecuencia de muestreo en Hz
    t = np.linspace(0, 1, srate, endpoint=False)  # 1 segundo de duración, vector de tiempo
    freq_real = 50  # Frecuencia de la señal en Hz
    wave = np.sin(2 * np.pi * freq_real * t)  # Genera una onda senoidal con la frecuencia especificada

    # Llama a la función para calcular la FFT de la señal
    freqs, spectrum = calcular_fft(wave, srate)  

    # Encuentra la frecuencia con el mayor valor en el espectro
    peak_freq = freqs[np.argmax(np.abs(spectrum))] 

    # Verifica que la frecuencia detectada sea la esperada (50 Hz)
    assert np.isclose(peak_freq, freq_real, atol=1), f"Se detectó {peak_freq} Hz en lugar de {freq_real} Hz"  

