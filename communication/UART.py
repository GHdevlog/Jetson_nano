# -*- coding: utf-8 -*-

import RPi.GPIO as g
import time
import serial

SEL_A = 20
SEL_B = 21

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)
    g.setmode(g.BCM)

    g.setup(SEL_A, g.OUT, initial=g.LOW)
    g.setup(SEL_B, g.OUT, initial=g.LOW)
    
    g.output(SEL_A, 0)
    g.output(SEL_B, 0)
    
    serial_port = serial.Serial('/dev/ttyTHS1', 9600, timeout=0)
    
    try:
        while True:
            serial_port.flushInput()
            txdata = input("input : ")
            serial_port.write((txdata).encode())
            time.sleep(0.01)
            while serial.inWating()>0:
                rxdata = serial_port.readline()
                print("output : ", rxdata)
    
    except KeyboardInterrupt:
        print("Exiting Program")
        
    except Exception as exception_error:
        print("Error occurred. Exiting Program")
        print("Error : ", str(exception_error))            
    finally:
        serial_port.close()