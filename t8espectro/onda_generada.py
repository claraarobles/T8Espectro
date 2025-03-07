import json
import os
import sys
from base64 import b64decode
from datetime import UTC, datetime
from struct import unpack
from zlib import decompress

import numpy as np
import requests
from matplotlib import pylab

FORMAT = 'zint' # zint | zlib | b64
DEVICE_IP = 'lzfs45.mirror.twave.io/lzfs45'
USER = os.getenv('T8_USER')
PASS = os.getenv('T8_PASSWORD')

MACHINE = 'LP_Turbine'
POINT = 'MAD31CY005'
PMODE = 'AM1'
DATE = '11-04-2019 18:25:54'

# Conversión de la fecha de captura al formato correcto (timestamp)

DATE = datetime.strptime(DATE, '%d-%m-%Y %H:%M:%S').replace(tzinfo=UTC)
DATE = int(DATE.timestamp())
print(DATE)



def zint_to_float(raw):
	d = decompress(b64decode(raw.encode()))
	return np.array([unpack('h', d[i*2:(i+1)*2])[0] for i in range(int(len(d)/2))], dtype='f')

def zlib_to_float(raw):
	d = decompress(b64decode(raw.encode()))
	return np.array([unpack('f', d[i*4:(i+1)*4])[0] for i in range(int(len(d)/4))], dtype='f')

def b64_to_float(raw):
	return np.fromstring(b64decode(raw.encode()), dtype='f')

decode_format = {
	'zint': zint_to_float,
	'zlib': zlib_to_float,
	'b64': b64_to_float
}




'''
print(f"Usuario: {USER}")
print(f"contraseña: {PASS}")
'''
if not USER or not PASS:
    print("Error: Las variables de entorno T8_USER y T8_PASSWORD deben estar definidas.")
    exit(1)
    
    
    
url = 'http://%s/rest/waves/%s/%s/%s/%s/0?array_fmt=%s' % (DEVICE_IP, MACHINE, POINT, PMODE, DATE, FORMAT)

r = requests.get(url, auth=(USER, PASS))
if r.status_code != 200:
    print("Error getting data. Status code: ", r.status_code)
    sys.exit(1)

ret = r.json()

# extract json fields
srate = float(ret['sample_rate'])
factor = float(ret.get('factor', 1))
raw = ret['data']

wave = decode_format[FORMAT](raw)

# apply numeric factor
wave *= factor

# get time axis
t = pylab.linspace(0, len(wave)/srate, len(wave))

pylab.plot(t, wave)
pylab.grid(True)
pylab.show()