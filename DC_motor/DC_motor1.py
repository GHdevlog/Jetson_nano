# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

a = 7 # 모터 정회전
b = 5 # 모터 역회전


if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)

    g.setup(a, g.OUT, initial=g.LOW)
    g.setup(b, g.OUT, initial=g.LOW)
    
    try:
        while True:
            g.output(a, True)
            g.output(b, False)
            time.sleep(5)
            
            g.output(a, False)
            g.output(b, True)
            time.sleep(5)
            
    finally:
        g.output(a, False)
        g.output(b, False)
        g.cleanup()