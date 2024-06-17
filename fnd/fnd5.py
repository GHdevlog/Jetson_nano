# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

COM = [4,17,18,27]
STR = 22
DATA = 23
CLK = 24

HEX_DATA = [
    0x3F,  # 0b00111111, '0'
    0x06,  # 0b00000110, '1'
    0x5B,  # 0b01011011, '2'
    0x4F,  # 0b01001111, '3'
    0x66,  # 0b01100110, '4'
    0x6D,  # 0b01101101, '5'
    0x7D,  # 0b01111101, '6'
    0x07,  # 0b00000111, '7'
    0x7F,  # 0b01111111, '8'
    0x6F,  # 0b01101111, '9'
    0x77,  # 0b01110111, 'A'
    0x7C,  # 0b01111100, 'B'
    0x39,  # 0b00111001, 'C'
    0x5E,  # 0b01011110, 'D'
    0x79,  # 0b01111001, 'E'
    0x71   # 0b01110001, 'F'
]

data = 5678

# 하나의 세그먼트 메소드에 대한 출력에 대한 함수
def fnd_data(buff):
    g.output(STR, 1)
    time.sleep(0.00001)
    
    for i in range(8):
        g.output(CLK, 0)
        g.output(DATA, (buff>>i)&0x01)
        time.sleep(0.00001)
        g.output(CLK,1)
        time.sleep(0.00001)
    
    g.output(STR, 0)

# COM 번호(세그먼트)를 지정하는 함수
def com_data(buff):
    for i in range(4):
        g.output(COM[i], (~buff>>i)&0x01)

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)
        
    for i in range(4):
        g.setup(COM[i], g.OUT, initial=g.LOW)
    
    g.setup(STR, g.OUT, initial=g.LOW)
    g.setup(DATA, g.OUT, initial=g.LOW)
    g.setup(CLK, g.OUT, initial=g.LOW)
    
    while True:
        for i in range(4):
            com_data(0)
            fnd_data(HEX_DATA[int(str(data)[i])])
            com_data(2**i)
            time.sleep(0.001)
        