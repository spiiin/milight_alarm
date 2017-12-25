import milight
import time

HOST_ADDR = "192.168.0.104"
LIGHT_GROUP = 2

controller = milight.MiLight({'host': HOST_ADDR, 'port': 8899}, wait_duration=0)
light = milight.LightBulb(['rgbw']) #Lamp type


controller.send(light.brightness(0, LIGHT_GROUP))
time.sleep(3)
controller.send(light.white(LIGHT_GROUP))
time.sleep(3)
for x in xrange(0,100,10):
    controller.send(light.brightness(x, LIGHT_GROUP))
    time.sleep(0.5)