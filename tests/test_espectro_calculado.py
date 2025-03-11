from t8espectro.espectro_calculado import calcular_fft  # Importa la función desde tu código
import numpy as np

def test_fft_output():
    # Datos de prueba: señal senoidal simple
    srate = 1000  # Frecuencia de muestreo en Hz
    t = np.linspace(0, 1, srate, endpoint=False)  # 1 segundo de duración, vector de tiempo
    freq_real = 50  # Frecuencia de la señal en Hz
    wave = np.sin(2 * np.pi * freq_real * t)  # Genera una onda senoidal con la frecuencia especificada

    # Calcula la FFT
    freqs, spectrum = calcular_fft(wave, srate)  # Llama a la función para calcular la FFT de la señal

    # Encuentra el pico más alto del espectro
    peak_freq = freqs[np.argmax(np.abs(spectrum))]  # Encuentra la frecuencia con el mayor valor en el espectro

    # Verifica que la frecuencia detectada sea la esperada (50 Hz)
    assert np.isclose(peak_freq, freq_real, atol=1), f"Se detectó {peak_freq} Hz en lugar de {freq_real} Hz"  # Comprueba que la frecuencia detectada esté cerca de 50 Hz

    
    
