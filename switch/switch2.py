# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

LED = [4,17]
SWITCH = [7,5]


if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)

    for i in range(2):
        g.setup(SWITCH[i],g.IN)
        
    for i in range(2):
        g.setup(LED[i], g.OUT, initial=g.LOW)
    
    while True:
        for i in range(2):
            val = g.input(SWITCH[i])
            g.output(LED[i], not val)
        
        time.sleep(0.01)
        