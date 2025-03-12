
import numpy as np
from matplotlib import pylab
from t8espectro.onda_generada import wave, srate  # Importa los datos de la onda generada  # noqa: E501
from t8espectro.espectro_calculado import calcular_fft


freqs, spectrum = calcular_fft(wave, srate, n_fft=None)


freqs = np.array(freqs)
spectrum = np.array(spectrum)


# Verifica las dimensiones de freqs y spectrum
print(f"freqs shape: {freqs.shape}")
print(f"spectrum shape: {spectrum.shape}")




'''
#pylab.figure(figsize=(8, 4))
pylab.figure()
pylab.plot(freqs, np.abs(spectrum))
pylab.title("Espectro de la señal")
pylab.xlabel("Frecuencia (Hz)")
pylab.ylabel("Amplitud")
pylab.grid(True)
pylab.show()
'''

'''
import numpy as np
import matplotlib.pyplot as pylab
from t8espectro.onda_generada import wave, srate  # Onda generada y tasa de muestreo
from t8espectro.espectro_calculado import calcular_fft  # FFT calculada
from t8espectro.espectro_generado import freq, sp  # Espectro del T8

# Obtener el espectro calculado
freqs_calc, spectrum_calc = calcular_fft(wave, srate, n_fft=None)

# Graficar ambos espectros
pylab.figure(figsize=(10, 6))
pylab.plot(freqs_calc, (spectrum_calc), label="Espectro Calculado", linestyle="--")
pylab.plot(freq, sp, label="Espectro T8", alpha=0.7)

pylab.title("Comparación de Espectros")
pylab.xlabel("Frecuencia (Hz)")
pylab.ylabel("Amplitud")
pylab.legend()
pylab.grid(True)
pylab.show()
'''