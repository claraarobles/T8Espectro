
import os
import sys
from base64 import b64decode
from datetime import UTC, datetime
from struct import unpack
from zlib import decompress

import numpy as np
import requests
from matplotlib import pylab

# Definir el formato de la codificación de datos
FORMAT = 'zint' # zint | zlib | b64
# Definir la dirección IP del dispositivo
DEVICE_IP = 'lzfs45.mirror.twave.io/lzfs45'
# Obtener las credenciales del usuario desde las variables de entorno
USER = os.getenv('T8_USER')
PASS = os.getenv('T8_PASSWORD')

# Definir máquina, punto, modo y fecha para la solicitud de datos
MACHINE = 'LP_Turbine'
POINT = 'MAD31CY005'
PMODE = 'AM1'
DATE = '11-04-2019 18:25:54'

# Convertir la fecha de captura al formato correcto (timestamp)
DATE = datetime.strptime(DATE, '%d-%m-%Y %H:%M:%S').replace(tzinfo=UTC)
DATE = str(int(DATE.timestamp()))

# Función para decodificar el formato 'zint' a float
def zint_to_float(raw_):
    """
    Decodes a 'zint' encoded string to a float numpy array.

    Parameters:
    raw_ (str): The encoded string.

    Returns:
    numpy.ndarray: The decoded float array.
    """
    d = decompress(b64decode(raw_.encode()))
    return np.array([unpack('h', d[i*2:(i+1)*2])[0] for i in range(int(len(d)/2))],
                 dtype='f')

# Diccionario para mapear el formato a la función de decodificación correspondiente
decode_format = {
    'zint': zint_to_float,
}

# Verificar si las credenciales del usuario están definidas
if not USER or not PASS:
    print("Error: Las variables de entorno T8_USER y T8_PASSWORD deben estar definidas")
    exit(1)

# Construir la URL para la solicitud de datos
URL = f"http://{DEVICE_IP}/rest/spectra/{MACHINE}/{POINT}/{PMODE}/{DATE}/?array_fmt={FORMAT}"

# Realizar la solicitud al servidor
r = requests.get(URL, auth=(USER, PASS), timeout=10)

# Verificar si la solicitud fue exitosa
if r.status_code != 200:
    print("Error obteniendo datos. Código de estado: ", r.status_code)
    sys.exit(1)

# Analizar la respuesta JSON
ret = r.json()

# Extraer campos relevantes de la respuesta JSON
fmin = ret.get('min_freq', 0)
fmax = ret['max_freq']
factor = ret['factor']
raw = ret['data']

# Decodificar los datos en bruto usando el formato especificado
sp = decode_format[FORMAT](raw)

# Aplicar el factor numérico a los datos
sp *= factor

# Generar el eje de frecuencia
freq = pylab.linspace(fmin, fmax, len(sp))

# Graficar el espectro
pylab.title("Espectro T8")
pylab.xlabel("Frecuencia (Hz)")
pylab.ylabel("Amplitud")
pylab.plot(freq, sp)
pylab.grid(True)
pylab.show()
