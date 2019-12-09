#Code made by Colin Gideon, FRC 3223, Robotics of Central Kitsap
#Copyright 2019, protected under GNU General Public Licence
import RPi.GPIO as GPIO
import time
flashes = 4
flash_duration = .375
try:
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(18,GPIO.OUT)
    
    flashed = 0
    while flashes > flashed:
        GPIO.output(18,True)
        time.sleep(flash_duration)
        GPIO.output(18,False)
        flashed = flashed+1
    
    #Keeps pin on until program is interupted by Y is entered.
    GPIO.output(18,True)

    #Sketchy AF Ring Light switch
    switchx2 = False
    while True: 
        if switchx2 == True:
            switch2 = raw_input("Would you like to turn the Ring Light On? (Yes/No) ")
            switch = "No"
        else:
            switch = raw_input("Would you like to turn the Ring Light Off? (Yes/No) ")
            switch2 = "No"
    
        while str(switch) == "Yes":
            GPIO.output(18,False)
            switchx2 = True
            break
        while str(switch2) == "Yes":
            GPIO.output(18,True)
            switchx2 = False
            break

except KeyboardInterrupt:
    print("""
    
    Turning off Ring Light""")
    GPIO.output(18,False)
    exit()
