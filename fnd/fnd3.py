# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

COM = [4,17,18,27]
STR = 22
DATA = 23
CLK = 24

digit_map = {
    '0': 0x3F,  # 0b00111111
    '1': 0x06,  # 0b00000110
    '2': 0x5B,  # 0b01011011
    '3': 0x4F,  # 0b01001111
    '4': 0x66,  # 0b01100110
    '5': 0x6D,  # 0b01101101
    '6': 0x7D,  # 0b01111101
    '7': 0x07,  # 0b00000111
    '8': 0x7F,  # 0b01111111
    '9': 0x6F,  # 0b01101111
    'A': 0x77,  # 0b01110111
    'B': 0x7C,  # 0b01111100
    'C': 0x39,  # 0b00111001
    'D': 0x5E,  # 0b01011110
    'E': 0x79,  # 0b01111001
    'F': 0x71   # 0b01110001
}

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

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)
        
    for i in range(4):
        g.setup(COM[i], g.OUT, initial=g.LOW)
    
    g.setup(STR, g.OUT, initial=g.LOW)
    g.setup(DATA, g.OUT, initial=g.LOW)
    g.setup(CLK, g.OUT, initial=g.LOW)
    
    g.output(COM[0], 1)
    g.output(COM[1], 1)
    g.output(COM[2], 1)
    g.output(COM[3], 0)
    
    while True:
        for buff in range(10):
            fnd_data(digit_map[str(buff)])
            time.sleep(1)
        