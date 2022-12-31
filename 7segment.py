#Control each part of a 7 segment display. 
#Count 0 to 9 and then 9 to 0.

import machine
import time

# define segments to GP12 to GP18
segA = machine.Pin(18, machine.Pin.OUT)
segB = machine.Pin(17, machine.Pin.OUT)
segC = machine.Pin(16, machine.Pin.OUT)
segD = machine.Pin(15, machine.Pin.OUT)
segE = machine.Pin(14, machine.Pin.OUT)
segF = machine.Pin(13, machine.Pin.OUT)
segG = machine.Pin(12, machine.Pin.OUT)

#pin list of light segments 
pins = [segA, segB, segC, segD, segE, segF, segG]
 

# numbers = [zero, one, two, three, four, five, six, seven, eight, nine, clear display]
numbers = [[1,1,1,1,1,1,0], 
          [0,1,1,0,0,0,0], 
          [1,1,0,1,1,0,1], 
          [1,1,1,1,0,0,1], 
          [0,1,1,0,0,1,1], 
          [1,0,1,1,0,1,1], 
          [1,0,1,1,1,1,1], 
          [1,1,1,0,0,0,0], 
          [1,1,1,1,1,1,1], 
          [1,1,1,0,0,1,1], 
          [0,0,0,0,0,0,0]]

clearDisplay = 10 # Clear display

# This function picks the right segment number from the pins list
def displayNumber(numberToDisplay):
    pin = 0
    for segment in range (7):
        pins[pin].value(numbers[numberToDisplay][segment])
        pin += 1
    
    return numberToDisplay

# Loop count displaying 0 - 9 - 0, clear, and repeat
while True: 
    for i in range(10):
        displayNumber(i)
        time.sleep_ms(600)
    
    for i in range (9, -1, -1):
        displayNumber(i)
        time.sleep_ms(600)
        
    displayNumber(clearDisplay)
    
    #could do time.sleep(1) as well
    time.sleep_ms(1000)
