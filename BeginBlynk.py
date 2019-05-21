import BlynkLib
import network
import time
time.sleep(5)
WIFI_SSID = "INEX01_2.4GHz"
WIFI_PASS = "123456789-0"
wifi = network.WLAN(network.STA_IF)
wifi.active(True)  
wifi.connect(WIFI_SSID,WIFI_PASS)
while not wifi.isconnected() :
  pass
print(wifi.ifconfig())
BLYNK_AUTH = '533c052f5f614bbdb683178a1afb2a71'
blynk = BlynkLib.Blynk(BLYNK_AUTH)
def on_connect():
  print("connected")
blynk.on_connect(on_connect)
blynk.run()

