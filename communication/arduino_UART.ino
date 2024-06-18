void setup() {
  // 기본 시리얼 포트 설정 (9600 baud rate)
  Serial.begin(9600);
}

void loop() {
  // 시리얼 포트에서 데이터가 있을 때 처리
  while (Serial.available() > 0) {
    // 시리얼 포트에서 데이터 읽기
    char data = Serial.read();
    
    // 읽은 데이터를 다시 시리얼 포트로 전송
    Serial.write(data);
  }
}
