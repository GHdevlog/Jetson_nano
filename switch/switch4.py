# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time
from collections import deque

LED = [4,17,18]
SWITCH = 7
data = deque([1,0,0])

cnt = 1
key_delay = 10

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
        if val: 
            cnt = 1
        else:
            if (cnt):
                cnt += 1
            if (cnt>key_delay):
                cnt = 0
                for i in range(3):
                    g.output(LED[i], data[i])
                data.rotate()
        
        print(cnt)
        time.sleep(0.1)