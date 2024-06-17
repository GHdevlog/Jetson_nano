# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

a = 7 # 모터 정회전
b = 5 # 모터 역회전


SWITCH = [22,23,24]
cnt0,cnt1,cnt2 = 0,0,0
key_delay = 50


if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)
    
    for i in range(3):
        g.setup(SWITCH[i], g.IN)

    g.setup(a, g.OUT, initial=g.LOW)
    g.setup(b, g.OUT, initial=g.LOW)
    
    try:
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
                    g.output(a, True)
                    g.output(b, False)
                    
            # 스위치 누름 인식 과정
            val = g.input(SWITCH[1])
            if val: 
                cnt1 = 1
            else:
                if (cnt1):
                    cnt1 += 1
                if (cnt1>key_delay):
                    cnt1 = 0
                    g.output(a, False)
                    g.output(b, True)
                    
            # 스위치 누름 인식 과정
            val = g.input(SWITCH[2])
            if val: 
                cnt2 = 1
            else:
                if (cnt2):
                    cnt2 += 1
                if (cnt2>key_delay):
                    cnt2 = 0
                    g.output(a, False)
                    g.output(b, False)
            
    finally:
        g.output(a, False)
        g.output(b, False)
        g.cleanup()