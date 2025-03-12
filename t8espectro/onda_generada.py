import os
import sys
from base64 import b64decode
from datetime import UTC, datetime
from struct import unpack
from zlib import decompress

import numpy as np
import requests
from matplotlib import pylab

# Formato de decodificación de los datos
FORMAT = 'zint' # zint | zlib | b64
# Dirección IP del dispositivo
DEVICE_IP = 'lzfs45.mirror.twave.io/lzfs45'
# Usuario y contraseña obtenidos de las variables de entorno
USER = os.getenv('T8_USER')
PASS = os.getenv('T8_PASSWORD')

# Información de la máquina y punto de medición
MACHINE = 'LP_Turbine'
POINT = 'MAD31CY005'
PMODE = 'AM1'
# Fecha de captura de los datos
DATE = '11-04-2019 18:25:54'

# Convertir la fecha de captura al formato correcto (timestamp)
DATE = datetime.strptime(DATE, '%d-%m-%Y %H:%M:%S').replace(tzinfo=UTC)
DATE = str(int(DATE.timestamp()))

# Función para decodificar datos comprimidos en formato zint
def zint_to_float(raw):
    d = decompress(b64decode(raw.encode()))
    return np.array([unpack('h', d[i*2:(i+1)*2])[0] for i in range(int(len(d)/2))], 
                    dtype='f')  

# Función para decodificar datos comprimidos en formato zlib
def zlib_to_float(raw):
    d = decompress(b64decode(raw.encode()))
    return np.array([unpack('f', d[i*4:(i+1)*4])[0] for i in range(int(len(d)/4))], 
                    dtype='f')

# Función para decodificar datos en formato base64
def b64_to_float(raw):
    return np.fromstring(b64decode(raw.encode()), dtype='f')

# Diccionario para seleccionar la función de decodificación adecuada
decode_format = {
    'zint': zint_to_float,
    'zlib': zlib_to_float,
    'b64': b64_to_float
}

# Verificar que las variables de entorno estén definidas
if not USER or not PASS:
    print("Error: Las variables de entorno T8_USER y T8_PASSWORD deben estar definidas")
    exit(1)

# Construir la URL para la solicitud de datos
url = "http://{}/rest/waves/{}/{}/{}/{}/?array_fmt={}".format(DEVICE_IP, MACHINE, POINT, PMODE, DATE, FORMAT)

# Realizar la solicitud HTTP para obtener los datos
r = requests.get(url, auth=(USER, PASS), timeout=10)

# Verificar que la solicitud fue exitosa
if r.status_code != 200:
    print("Error getting data. Status code: ", r.status_code)
    sys.exit(1)

# Parsear la respuesta JSON
ret = r.json()

# Extraer campos del JSON
srate = float(ret['sample_rate'])
factor = float(ret.get('factor', 1))
raw = ret['data']

print("sample rate: ", srate)
print("raw: ", raw)

# Decodificar los datos crudos usando el formato especificado
wave = decode_format[FORMAT](raw)

# Aplicar el factor numérico a los datos
wave *= factor

# Obtener el eje de tiempo
t = pylab.linspace(0, (len(wave)/srate)*1000, len(wave))

# Graficar la onda
pylab.title("Onda T8")
pylab.xlabel("Tiempo (ms)")
pylab.ylabel("Amplitud")
pylab.plot(t, wave)
pylab.grid(True)
pylab.show()