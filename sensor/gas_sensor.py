# -*- coding: utf-8 -*-

import RPi.GPIO as g  # RPi.GPIO 라이브러리를 g로 불러옴
import time  # time 라이브러리를 불러옴
import math

# SPI 핀 번호 설정
spi_cs = 13  # Chip Select 핀
spi_mosi = 19  # Master Out Slave In 핀
spi_miso = 16  # Master In Slave Out 핀
spi_sck = 26  # Serial Clock 핀

LED = [4,17,18]
SENSOR = 9

RED = [1,0,0]
GREEN = [0,1,0]

def analog_read(ch):
    arr = []  # 읽어온 데이터를 저장할 리스트
    # SPI 명령어 설정 (읽을 채널 번호 포함)
    buffer = [(1<<2)|(1<<1)|(ch&4)>>2, (ch&3)<<6, 0]
    
    # Chip Select 신호 하강 구현 (데이터 전송 시작)
    g.output(spi_cs, 1)
    time.sleep(0.00001)
    g.output(spi_cs, 0)
    time.sleep(0.00002)
    
    # 데이터 쓰기/읽기
    for i in range(3):  # 3바이트 데이터 전송
        data = 0  # 받은 데이터를 저장할 변수
        for b in range(7, -1, -1):  # 8비트 데이터 전송
            g.output(spi_sck, 0)  # 클럭 신호 낮춤
            g.output(spi_mosi, (buffer[i] >> b) & 1)  # MOSI에 비트 설정
            time.sleep(0.00001)
            g.output(spi_sck, 1)  # 클럭 신호 높임
            val = g.input(spi_miso)  # MISO에서 비트 읽음
            data += val << b  # 읽은 비트를 데이터에 저장
            time.sleep(0.00001)
        arr.append(data)  # 읽은 데이터 리스트에 추가
        
    g.output(spi_cs, 1)  # Chip Select 신호 상승 (데이터 전송 종료)
    return arr  # 읽어온 데이터 반환

if __name__ == "__main__":
    
    # GPIO 설정
    g.setwarnings(False)  # 경고 메시지 비활성화
    g.setmode(g.BCM)  # GPIO 핀 번호 모드 설정 (BCM 모드)

    # SPI 핀 설정
    g.setup(spi_cs, g.OUT, initial=g.LOW)  # Chip Select 핀 출력 모드 설정 (초기값 LOW)
    g.setup(spi_mosi, g.OUT, initial=g.LOW)  # MOSI 핀 출력 모드 설정 (초기값 LOW)
    g.setup(spi_miso, g.IN)  # MISO 핀 입력 모드 설정
    g.setup(spi_sck, g.OUT, initial=g.LOW)  # 클럭 핀 출력 모드 설정 (초기값 LOW)
    
    g.setup(SENSOR, g.IN)
    
    for i in range(3):
        g.setup(LED[i], g.OUT, initial=g.LOW)
        
    while True:
        adc_data = analog_read(0)  # 채널 0에서 ADC 데이터 읽기
        # 읽어온 데이터에서 유효한 12비트 데이터 추출
        gas_adc = ((adc_data[1] & 0xf) << 8 | adc_data[2])
        
        print('gas_adc: %d' % (gas_adc))
        
        gas_bit = g.input(SENSOR)
        
        if gas_bit == True:
            for i in range(3):
                g.output(LED[i], RED[i])
        else:
            for i in range(3):
                g.output(LED[i], GREEN[i])
        
        time.sleep(1)  # 1초 대기
