import time
import sys
from networktables import NetworkTables

#Init of pyNetworkTables server
#IP of copressor(10.xx.yy.11)
ip = '10.31.160.144'
NetworkTables.initialize(server=ip)

led = NetworkTables.getTable("LED Ring Light")
LEDState = led.getAutoUpdateValue("LED-State", False)

switchx2 = True
while True:
        #NetworkTables based switch so programming doesn't lynch me
        if LEDState.value == True:
            print("Light is on")
        elif LEDState.value == False:
            print("Light is off")
            switchx2 = False
        time.sleep(.125)