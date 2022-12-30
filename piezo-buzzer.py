
#Control buzzer with a potentiometer.

import machine
import math
import time

buzzer = machine.PWM(machine.Pin(15)) #GP15 assigned to buzzer
pot = machine.ADC(26) # Analog to Digital converter is on pin 26

prevFrequency = 0
buzzer.duty_u16(32767) # 65535 in half (50%) is 32767

# range value
def scale(value, fromMin, fromMax, toMin, toMax):
    return toMin + ((value - fromMin) * ((toMax - toMin) / (fromMax - fromMin)))
    
while True:
    potValue = pot.read_u16() 
    frequency = scale(potValue, 0, 65535, 120, 5000)
    if ((frequency < (prevFrequency - 50)) or (frequency > (prevFrequency + 50))):
        prevFrequency = frequency
        buzzer.freq(math.trunc(frequency)) 
    time.sleep_ms(25)
    