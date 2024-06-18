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
    
    # RS485 설정
    g.output(SEL_A, 1)
    g.output(SEL_B, 0)
    
    # 시리얼 포트 설정
    serial_port = serial.Serial('/dev/ttyTHS1', 9600, timeout=1)  # timeout을 1로 설정
    
    try:
        while True:
            serial_port.reset_input_buffer()  # flushInput() 대신 사용
            txdata = input("input : ")
            serial_port.write(txdata.encode())  # 이미 문자열이므로 괄호 삭제
            time.sleep(0.01)
            while serial_port.in_waiting > 0:  # inWating() -> in_waiting
                rxdata = serial_port.readline()
                print("output : ", rxdata.decode('utf-8').strip())  # 디코딩 및 줄바꿈 제거
    
    except KeyboardInterrupt:
        print("Exiting Program")
        
    except Exception as exception_error:
        print("Error occurred. Exiting Program")
        print("Error : ", str(exception_error))            
    finally:
        serial_port.close()
