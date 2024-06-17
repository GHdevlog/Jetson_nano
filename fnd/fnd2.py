# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

FND = [4,17,18,27]
SWITCH = [7,5]

data = 0
cnt0, cnt1 = 1, 1
key_delay = 10

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)

    for i in range(2):
        g.setup(SWITCH[i],g.IN)
        
    for i in range(4):
        g.setup(FND[i], g.OUT, initial=g.LOW)
    
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
                data += 1
                if data>9: data=0
        
        val = g.input(SWITCH[1])
        if val: 
            cnt1 = 1
        else:
            if (cnt1):
                cnt1 += 1
            if (cnt1>key_delay):
                cnt1 = 0
                data -= 1
                if data<0: data=9
                
        for i in range(4):
            g.output(FND[i], data>>i & 0x01)
        
        # print(cnt0, cnt1)
        time.sleep(0.01)