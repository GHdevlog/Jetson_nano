# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time
from collections import deque

LED = [4,17,18]
SWITCH = 7
data = deque([0,0,1])

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)

    g.setup(SWITCH, g.IN)
        
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
    
    
    while True:
        # 스위치 누름 인식 과정
        val = g.input(SWITCH)
        while val:
            val = g.input(SWITCH)
            
        for i in range(3):
            g.output(LED[i], data[i])
        
        data.rotate()
        
        # 스위치 떼기 인식 과정
        val = g.input(SWITCH)
        while not val:
            val = g.input(SWITCH)
        