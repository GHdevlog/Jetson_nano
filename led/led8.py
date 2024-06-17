# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time
import random

LED = [4,17,18]


if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)
    g.setup(LED, g.OUT, initial=g.LOW)
    
    # 핀 설정 : GPIO.setup(핀번호, 입/출력 설정, 초기값)
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
    
    for i in range(5):
        data = [random.randint(0,1) for _ in range(3)]
        for j in range(3):
            g.output(LED[j], data[j])
        time.sleep(1)
        
    # 전체 소등
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
        