# -*- coding: utf-8 -*-

import smbus2

class I2CComm(object):
    I2C_BUS_NUM = 1
    
    def __init__(self):
        self.master = smbus2.SMBus(self.I2C_BUS_NUM)
        self.slave_addr = 5
        
    def run(self):
        me = self.master
        rxByte = me.read_i2c_block_data(self.slave_addr, 0x01, 3)
        print("rx data : ", rxByte)

def main():
    i2c = I2CComm()
    i2c.run()

if __name__ == "__main__":
    main()
