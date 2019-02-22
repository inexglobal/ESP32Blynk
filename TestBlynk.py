
import BlynkLib
import network
import time
import machine
import dht
d = dht.DHT22(machine.Pin(18))

WIFI_SSID = "INEXWIFI"
WIFI_PASS = "123456789-0"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
#wifi.scan()       
wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())

BLYNK_AUTH = 'b0b68a5aeeb040c7850dd80bd555e44a'
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
# Start Blynk (this call should never return)

def v3_write_handler(value):
  print(value)
 # register the virtual pin
blynk.add_virtual_pin(3, write=v3_write_handler)


# Register virtual pin handler
def my_user_task():
  # Read DHT22
  d.measure() 
  t=d.temperature() # eg. 23.6 (°C) 
  h=d.humidity() # eg. 41.3 (% RH)
  print('Temp={}'.format(t))
  print('Humi={}'.format(h))
  
  blynk.virtual_write(1, t)
  blynk.virtual_write(2, h)

# Register task handler
blynk.set_user_task(my_user_task, 2000)

blynk.run()




























