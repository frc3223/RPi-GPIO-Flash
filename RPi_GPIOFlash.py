#Code made by Colin Gideon, FRC 3223, Robotics of Central Kitsap
#Copyright 2019, protected under GNU General Public Licence
import RPi.GPIO as GPIO
import time
import sys
import time
from networktables import NetworkTables

flashes = 4
flash_duration = .125
try:
    #Init of pyNetworkTables server
    #IP of copressor(10.xx.yy.11)
    ip = '10.xx.yy.zz'
    NetworkTables.initialize(server=ip)

    led = NetworkTables.getTable("LED Ring Light")
    auto_value = led.getAutoUpdateValue("LED-State", True)
       
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
    GPIO.output(18,True)

    #Sketchy AF Ring Light switch
    switchx2 = False
    while True: 
        #NetworkTables based switch so programming doesn't lynch me
        if auto_value.value == True:
            switchx2 = False
            GPIO.output(18,True)
            
        elif auto_value.value == False:
            switchx2 = True
            GPIO.output(18,False)
        
        time.sleep(.25)

except KeyboardInterrupt:
    print("""
    
    Turning off Ring Light""")
    GPIO.output(18,False)
    GPIO.cleanup(18)
    exit()
