import numpy as np
import matplotlib.pyplot as pylab
from t8espectro.onda_generada import wave, srate  # Onda generada y tasa de muestreo
from t8espectro.espectro_calculado import calcular_fft  # FFT calculada
from t8espectro.espectro_generado import freq, sp  # Espectro del T8

# Obtener el espectro calculado usando la FFT
freqs, spectrum = calcular_fft(wave, srate, n_fft=None)

# Convertir las frecuencias y el espectro a arrays de numpy y tomar el valor absoluto del espectro
freqs = np.array(freqs)
spectrum = np.abs(np.array(spectrum)) 

# Filtrar los datos para que coincidan con el rango de `freq` del espectro T8
mask = (freqs >= freq.min()) & (freqs <= freq.max())
freqs_filtered = freqs[mask]
spectrum_filtered = spectrum[mask]

# Escalar el espectro calculado para que coincida con la amplitud del espectro T8
scaling_factor = np.max(sp) / np.max(spectrum_filtered)
spectrum_scaled = spectrum_filtered * scaling_factor

# Graficar ambos espectros para comparar
pylab.figure(figsize=(10, 6))
pylab.plot(freqs_filtered, spectrum_scaled, label="Espectro Calculado")
pylab.plot(freq, sp, label="Espectro T8", linestyle="--", alpha=0.6)

# Añadir título y etiquetas al gráfico
pylab.title("Comparación de Espectros")
pylab.xlabel("Frecuencia (Hz)")
pylab.ylabel("Amplitud")
pylab.legend()
pylab.grid(True)
pylab.show()
