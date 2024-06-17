# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time

FND = [4,17,18,27]


if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)

        
    for i in range(4):
        g.setup(FND[i], g.OUT, initial=g.LOW)
    
    while True:
        for buff in range(10):
            for i in range(4):
                g.output(FND[i], buff>>i & 0x01)
        
            time.sleep(1)
        