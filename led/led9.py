# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time
from collections import deque

LED = [4,17,18]
data = deque([1,0,0])

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)
    
    # 핀 설정 : GPIO.setup(핀번호, 입/출력 설정, 초기값)
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
    
    for i in range(3):
        for j in range(3):
            g.output(LED[j], data[j])
        data.rotate(1)
        time.sleep(1)
        
    # 전체 소등
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
        