import sys
import re
import time
from collections import Counter

print(sys.path)

text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte es 3'
result = re.findall('[0-9]+', text)
print(result)

timestamp = time.time()
print(timestamp)  # Tiempo en formato UNIX

hora_local = time.localtime()
print(time.asctime(hora_local))  # Formato legible

numeros = [1, 2, 3, 1, 2, 1, 5, 4, 3, 1, 21]
frecuencia = Counter(numeros)
print(frecuencia)