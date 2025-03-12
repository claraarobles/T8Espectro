# Resumen del Proyecto

Este proyecto tiene como objetivo obtener, analizar y comparar señales espectrales provenientes del sistema T8. A partir de la forma de onda capturada, se calcula su espectro y se compara con el espectro obtenido directamente del T8, verificando la similitud de los resultados. A continuación se detallan los componentes clave del proyecto:

## Objetivos
- Analizar datos espectrales provenientes de diversas fuentes.
- Visualizar los resultados del análisis mediante gráficos y otras herramientas visuales.
- Desarrollar herramientas para la manipulación y transformación de espectros.
- Implementar algoritmos de procesamiento de señales para mejorar la calidad de los datos espectrales.
- Crear una interfaz de usuario intuitiva para facilitar la interacción con las herramientas desarrolladas.

## Organización
1. **Obtención de Datos (onda_generada.py y espectro.py)**
    - Se conecta con el servidor T8 para obtener la señal de la máquina específica.
    - Se decodifican los datos de acuerdo con el formato (zint, zlib o b64).
    - Se grafican la forma de onda y el espectro de la señal.

2. **Cálculo del Espectro (espectro_calculado.py)**
    - Se aplica la Transformada Rápida de Fourier (FFT) para obtener el espectro de la señal capturada.
    - Se implementa zero-padding para mejorar la resolución en frecuencia.

3. **Comparación de Resultados (graficar_espectro.py)**
    - Se superponen los espectros calculado y obtenido desde el T8 en una misma gráfica.
    - Se evalúa la similitud entre ambas representaciones.

4. **Pruebas y Validación (test_espectro_calculado.py)**
    - Se incluyen pruebas unitarias para verificar que la FFT detecta correctamente las frecuencias de prueba.
    - Se asegura la precisión del espectro obtenido.

## Componentes del Proyecto
- **Adquisición de Datos**: Módulo encargado de la recopilación de datos espectrales.
- **Procesamiento de Datos**: Algoritmos y técnicas para limpiar y preparar los datos para el análisis.
- **Análisis Espectral**: Métodos para interpretar y extraer información relevante de los datos espectrales.
- **Visualización**: Herramientas para representar gráficamente los resultados del análisis.
- **Interfaz de Usuario**: Desarrollo de una aplicación que permita a los usuarios interactuar con el sistema de manera eficiente.



