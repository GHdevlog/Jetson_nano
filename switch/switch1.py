# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

LED = [4,17]
SWITCH = [9,25]


if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)

    for i in range(2):
        g.setup(SWITCH[i],g.IN)
        
    for i in range(2):
        g.setup(LED[i], g.OUT, initial=g.LOW)
    
    while True:
        val = g.input(SWITCH[0])
        g.output(LED[0], not val)
        
        val = g.input(SWITCH[1])
        g.output(LED[1], not val)
        
        time.sleep(0.01)
        