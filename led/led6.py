# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

LED = [4,17,18]


if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)
    g.setup(LED, g.OUT, initial=g.LOW)
    
    # 핀 설정 : GPIO.setup(핀번호, 입/출력 설정, 초기값)
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
    
    for i in range(3):
        g.output(LED[i], True)
        time.sleep(1)
        
    for i in range(2,-1,-1):
        g.output(LED[i], False)
        time.sleep(1)
        
    # 전체 소등
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
        