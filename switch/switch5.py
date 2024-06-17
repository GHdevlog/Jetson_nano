# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time
from collections import deque

LED = [4,17,18]
SWITCH = [7,5]
data = deque([1,0,0])

cnt0, cnt1 = 1, 1
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
        val = g.input(SWITCH[0])
        if val: 
            cnt0 = 1
        else:
            if (cnt0):
                cnt0 += 1
            if (cnt0>key_delay):
                cnt0 = 0
                data.rotate()
                for i in range(3):
                    g.output(LED[i], data[i])
        
        val = g.input(SWITCH[1])
        if val: 
            cnt1 = 1
        else:
            if (cnt1):
                cnt1 += 1
            if (cnt1>key_delay):
                cnt1 = 0
                data.rotate(-1)
                for i in range(3):
                    g.output(LED[i], data[i])
        
        # print(cnt0, cnt1)
        time.sleep(0.01)