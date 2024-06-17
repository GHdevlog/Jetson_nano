# -*- coding: utf-8 -*-

import threading
import RPi.GPIO as g  # RPi.GPIO 라이브러리를 g로 불러옴
import time  # time 라이브러리를 불러옴

# SPI 핀 번호 설정
spi_cs = 13  # Chip Select 핀
spi_mosi = 19  # Master Out Slave In 핀
spi_miso = 16  # Master In Slave Out 핀
spi_sck = 26  # Serial Clock 핀

LED = [4,17,18]
SENSOR = 25
cnt_run = False
sound_error = False

RED = [1,0,0]
GREEN = [0,1,0]

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
    
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
        
    g.setup(SENSOR, g.IN)
    
    g.add_event_detect(SENSOR, g.RISING, callback=myinterrupt, bouncetime=100)
        
    while True:
        if cnt_run == True:
            if (time.time() - start) > 1:
                if globalCounter < 5:
                    cnt_run = False
                    sound_error = False
            if globalCounter >= 5:
                cnt_run = False
                sound_error = True
                timer = threading.Timer(1, ctimer)
                timer.start()
        
        if sound_error == True:
            for i in range(3):
                g.output(LED[i], RED[i])
        else:
            for i in range(3):
                g.output(LED[i], GREEN[i])
