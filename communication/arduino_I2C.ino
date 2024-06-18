#include <Wire.h>

const int my_I2C_addr = 5;
char mode = 0;

void setup() {
  Serial.begin(9600);
  Wire.begin(my_I2C_addr);
  Wire.onReceive(recvData);
  Wire.onRequest(sendData);
}

void loop() {
  delay(100);
}

void recvData(int byte_count){
  while(Wire.available()){
    int on_off = Wire.read();
    if (on_off == 1){
      mode = 1;
      Serial.println("mode A");
    }else{
      mode = 0;
      Serial.println("mode B");
    }
  }
}

void sendData(){
  Serial.println("Send chk");
  if (mode == 1){
    char arry[3] = {0x01, 0x02, 0x03};
    Wire.write(arry, 3);
  }else{
    char arry[3] = {0x04, 0x05, 0x06};
    Wire.write(arry, 3);
  }
}