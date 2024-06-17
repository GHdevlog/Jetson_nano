# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time
import threading

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

data = 0
buff = 0
cnt = 0
running = True

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

# 별도의 타이머를 이용한 정확한 시간측정
def ctimer():
    global data
    data += 1
    if (data > 9999): data = 0
    timer = threading.Timer(1, ctimer)
    timer.start()

# 타이머 스레드 함수
def timer_thread():
    global data
    next_call = time.perf_counter()
    while running:
        data += 1
        if data > 9999:
            data = 0
        next_call += 1
        sleep_time = next_call - time.perf_counter()
        if sleep_time > 0:
            time.sleep(sleep_time)

buff_nums = [0,0,0,0]

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)
        
    for i in range(4):
        g.setup(COM[i], g.OUT, initial=g.LOW)
    
    g.setup(STR, g.OUT, initial=g.LOW)
    g.setup(DATA, g.OUT, initial=g.LOW)
    g.setup(CLK, g.OUT, initial=g.LOW)
    
    # ctimer()
    
    # 타이머 스레드 시작
    timer = threading.Thread(target=timer_thread)
    timer.start()
    
    while True:
        
        buff = data
        for i in range(4):
            buff_nums[-1-i] = buff%10
            buff //= 10
        
        for i in range(4):
            com_data(0)
            fnd_data(HEX_DATA[buff_nums[i]])
            com_data(2**i)
            time.sleep(0.001)
        
        