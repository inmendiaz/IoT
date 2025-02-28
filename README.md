# IoT
Repositorio para subir los recursos que se usaron para configurar la Raspberry Pico W

# Monitoreo de Temperatura IoT con Raspberry Pi Pico W y ThingSpeak

#Descripción
Este proyecto consiste en la creación de un sistema IoT para medir la temperatura mediante un sensor LM35 y una Raspberry Pi Pico W. Los datos se envían a ThingSpeak para su almacenamiento y visualización en tiempo real, además de ser analizados con MathWorks para generar alertas y calcular promedios.

# Instrucciones para realizar el proyecto

# 1. Materiales Necesarios
Raspberry Pi Pico W
Sensor de temperatura LM35
Cables de conexión (jumper cables)
Fuente de alimentación USB para la Raspberry Pi Pico W
Acceso a una red Wi-Fi

# 2. Configuración del Hardware
Conecta el sensor LM35 a la Raspberry Pi Pico W de la siguiente manera:

Pin del LM35	     Conexión en Raspberry Pi Pico W
VCC (pin 1)	       3.3V (pin 36 en la Pico W)
VOUT (pin 2)	     GP26 (ADC0) (pin 31 en la Pico W)
GND (pin 3)	       GND (pin 38 en la Pico W)

# 3. Configuración de ThingSpeak
Crea una cuenta en ThingSpeak.
Crea un canal nuevo y anota el Write API Key.
Configura un campo (field1) para almacenar los valores de temperatura.
Opcional: Configura gráficos para visualizar los datos y usa MathWorks para el análisis.

# 4. Instalación del Entorno de Desarrollo
Descarga e instala Thonny (IDE recomendado para MicroPython).
Puedes descargarlo desde thonny.org.
Instala MicroPython en la Raspberry Pi Pico W:
Conéctala por USB, enciéndela en modo BOOTSEL y arrastra el firmware de MicroPython.
Conéctate a la Raspberry Pi Pico W desde Thonny.

# 5. Código en MicroPython
Crea un archivo en Thonny llamado main.py y copia el siguiente código:
Usa el que se encuentra en el repositorio llamado T3.py

Modifica las siguientes líneas con tu información:

"TU_SSID" → Nombre de tu red Wi-Fi.
"TU_CONTRASEÑA" → Contraseña de tu Wi-Fi.
"TU_API_KEY" → API Key de tu canal en ThingSpeak.

# 6. Cargar y Ejecutar el Código
Guarda el archivo main.py en la Raspberry Pi Pico W.
Ejecuta el código desde Thonny.
Observa en la consola la conexión a Wi-Fi y la lectura de temperatura.
Revisa los datos en ThingSpeak en tiempo real.

# 7. Visualización y Análisis en ThingSpeak
En la pestaña “Private View”, agrega un gráfico (Chart) para visualizar los datos.
Usa MathWorks en la pestaña "Apps" para:

Calcular el promedio de temperatura de los últimos 10 datos.
Generar una alerta si la temperatura supera los 35°C.

Y listo ya podrás realizar el proyecto de medir temperaturas y hacer un análisis con el promedio de las temperaturas tomadas en ThingSpeak.

