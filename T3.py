import network
import urequests
import machine
import utime

# Configuración WiFi
SSID = "Casa Mendoza"
PASSWORD = "9818211992"

# Configuración de ThingSpeak
THINGSPEAK_API_KEY = "2R7WW3XCBDEG304Q"
THINGSPEAK_URL = "https://api.thingspeak.com/update?api_key=" + THINGSPEAK_API_KEY

# Configurar ADC
adc = machine.ADC(26)

# Función para conectar a WiFi
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    print("Conectando a WiFi...")
    tiempo_inicio = utime.time()
    
    while not wlan.isconnected():
        if utime.time() - tiempo_inicio > 10:  # Máximo 10 segundos de espera
            print("Error: No se pudo conectar a WiFi")
            return False
        utime.sleep(1)
    
    print("Conectado a WiFi:", wlan.ifconfig())
    return True

# Función para leer temperatura del sensor LM35
def leer_temperatura():
    valor_adc = adc.read_u16()
    voltaje = (valor_adc / 65535) * 3.3
    temperatura_celsius = voltaje * 100
    return temperatura_celsius

# Función para enviar datos a ThingSpeak
def enviar_a_thingspeak(valor):
    url = THINGSPEAK_URL + "&field1=" + str(valor)
    try:
        respuesta = urequests.get(url)
        print("Enviado a ThingSpeak:", respuesta.text)
        respuesta.close()
    except Exception as e:
        print("Error al enviar datos:", e)

# Conectar a WiFi antes de comenzar
if conectar_wifi():
    while True:
        temperatura = leer_temperatura()
        print("Temperatura LM35:", temperatura, "°C")
        enviar_a_thingspeak(temperatura)
        utime.sleep(180)  # Espera de 3 minutos
