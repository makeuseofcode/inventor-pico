
#Control buzzer with a potentiometer.

import machine
import math
import time

buzzer = machine.PWM(machine.Pin(15)) #Assign the buzzer to pin 15
pot = machine.ADC(26) # Potentiometer ADC converter

prevFrequency = 0
buzzer.duty_u16(32767) # 1/2 of 65535

# Convert a value proportionally from one range to another
def scale(value, fromMin, fromMax, toMin, toMax):
    return toMin + ((value - fromMin) * ((toMax - toMin) / (fromMax - fromMin)))

# help control the tone while moving the pot
while True:
    potValue = pot.read_u16() 
    # convert analog input to frequency between 120Hz and 5kHz
    frequency = scale(potValue, 0, 65535, 120, 5000)
    #constant tone when you're moving the pot
    if ((frequency < (prevFrequency - 50)) or (frequency > (prevFrequency + 50))):
        prevFrequency = frequency
        buzzer.freq(math.trunc(frequency)) #change frequency 
    time.sleep_ms(25)
    
