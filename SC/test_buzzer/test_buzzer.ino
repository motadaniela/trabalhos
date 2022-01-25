int buzzer = 11;

void setup() {
  pinMode(buzzer, OUTPUT);
}

void loop() {
  unsigned char i;
  for (int i=0;i<=100;i++){
    analogWrite(buzzer, i);
    delay(10);
    for (int i=100;i>=0;i--){
      analogWrite(buzzer, i);
      delay(5);
    }
  }

}
