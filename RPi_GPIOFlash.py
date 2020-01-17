#Code made by Colin Gideon, FRC 3223, Robotics of Central Kitsap
#Copyright 2019, protected under GNU General Public Licence
import RPi.GPIO as GPIO
import time
import sys
from networktables import NetworkTables

flashes = 4
flash_duration = .125
try:
    #Init of pyNetworkTables server
    #IP of copressor(10.xx.yy.11)
    ip = '10.xx.yy.zz'
    NetworkTables.initialize(server=ip)

    led = NetworkTables.getTable("LED Ring Light")
    LEDState = led.getAutoUpdateValue("LED-State", False)
       
    #Start of control program
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(18,GPIO.OUT)
    
    flashed = 0
    while flashes > flashed:
        GPIO.output(18,True)
        time.sleep(flash_duration)
        GPIO.output(18,False)
        time.sleep(flash_duration)
        flashed = flashed+1
    
    #Keeps pin on until program is interupted by Y is entered.

    #Sketchy AF Ring Light switch
    switchx2 = False
    while True:  
        if switchx2 == True:
            switch2 = raw_input("Would you like to lock out the Ring Light & turn it off? (Y/N) ")
            switch = "N"
        else:
            switch = raw_input("Would you like to unlock the Ring Light & turn it on? (Y/N) ")
            switch2 = "N"
    
        while str(switch) == "Y":
           LEDState.value = False
            GPIO.output(18,False)
            switchx2 = True
            break
        while str(switch2) == "Y":
            LEDState.value = True
            #NetworkTables based switch so programming doesn't lynch me
            if LEDState.value == True:
                GPIO.output(18,True)
            elif LEDState.value == False:
                GPIO.output(18,False)
                switchx2 = False
            break
        

except KeyboardInterrupt:
    print("""
    
    Turning off Ring Light""")
    GPIO.output(18,False)
    GPIO.cleanup(18)
    exit()
