
import matplotlib.pyplot as pylab
import numpy as np

from t8espectro.espectro_calculado import calcular_fft  # FFT calculada
from t8espectro.espectro_generado import freq, sp  # Espectro del T8
from t8espectro.onda_generada import srate, wave  # Onda generada y tasa de muestreo

# Obtener el espectro calculado usando la FFT
freq_fft, spectrum_fft = calcular_fft(wave, srate, n_fft=None)

# Convertir las frecuencias y el espectro a arrays de numpy y tomar el valor absoluto
# del espectro
freq_fft = np.array(freq_fft)
spectrum_fft = np.abs(np.array(spectrum_fft))

# Filtrar los datos para que coincidan con el rango de `freq` del espectro T8
mask = (freq_fft >= freq.min()) & (freq_fft <= freq.max())
freqs_filtered = freq_fft[mask]
spectrum_filtered = spectrum_fft[mask]

# Escalar el espectro calculado para que coincida con la amplitud del espectro T8
scaling_factor = np.max(sp) / np.max(spectrum_filtered)
spectrum_scaled = spectrum_filtered * scaling_factor

# Graficar ambos espectros para comparar
pylab.figure(figsize=(10, 6))
pylab.plot(freqs_filtered, spectrum_scaled, label="Espectro Calculado")
pylab.plot(freq, sp, label="Espectro T8", linestyle="--", alpha=0.6)

# Añadir título y etiquetas al gráfico
pylab.figure()
pylab.title("Comparación de Espectros")
pylab.xlabel("Frecuencia (Hz)")
pylab.ylabel("Amplitud")
pylab.legend()
pylab.grid(True)
pylab.show()
