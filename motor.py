

#Control motor using a transistor that will spin up a fan automatically.

#Although all pins have the PWM functionality, we're using GP15 in this experiment. 

import machine
import time

motorControlPin = machine.PWM(machine.Pin(15)) # Setup GP15 as the pin controlling the transistor with a PWM output

while True: 
    # Speed up the motor which drives the fan (100%)
    for outputValue in range(0, 65536, 100):
        motorControlPin.duty_u16(outputValue)
        time.sleep_ms(5)
        
    # Pause to visually demonstrate what the code is doing
    time.sleep(1)
    # Slow down the motor which drives the fan)
    for outputValue in range(65536, 0, -100):
        motorControlPin.duty_u16(outputValue)
        time.sleep_ms(5)
    
    # Pause at stop for 1 second to visually demostrate what the code is doing
    time.sleep(1)
