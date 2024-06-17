# -*- coding: utf-8 -*-

import RPi.GPIO as g  # RPi.GPIO 라이브러리를 g로 불러옴
import time  # time 라이브러리를 불러옴

MOTOR = [7,5]
SWITCH = 22
SENSOR = 11

key_delay = 10
cnt_run = False
cnt = 0

def myinterrupt(channel):
    global globalCounter
    global cnt_run
    global start
    
    if cnt_run == False:
        cnt_run = True
        globalCounter = 0
        start = time.time()
    globalCounter += 1

def ctimer():
    global sound_error
    if cnt_run == False:
        sound_error = False

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)  # 경고 메시지 비활성화
    g.setmode(g.BCM)  # GPIO 핀 번호 모드 설정 (BCM 모드)
        
    g.setup(SWITCH, g.IN)
    g.setup(SENSOR, g.IN)
    
    g.setup(MOTOR[0], g.OUT, initial=g.LOW)
    g.setup(MOTOR[1], g.OUT, initial=g.LOW)
    
    g.add_event_detect(SENSOR, g.RISING, callback=myinterrupt, bouncetime=100)
    
    while True:
        val = g.input(SWITCH)
        # 스위치 누름 인식 과정
        if val: 
            cnt = 1
        else:
            if (cnt):
                cnt += 1
            if (cnt>key_delay):
                cnt = 0
                g.output(MOTOR[0], True)
                g.output(MOTOR[1], False)
                
        if cnt_run == True:
            if (time.time() - start) > 1:
                if globalCounter < 5:
                    cnt_run = False
                    
            if globalCounter >= 5:
                cnt_run = False
                g.output(MOTOR[0], False)
                g.output(MOTOR[1], False)
