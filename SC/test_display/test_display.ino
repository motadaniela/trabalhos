int a = 2; //a of 7-segment attach to digital pin 2
int b = 3; //b of 7-segment attach to digital pin 3
int c = 4; //c of 7-segment attach to digital pin 4
int d = 5; //d of 7-segment attach to digital pin 5
int e = 6; //e of 7-segment attach to digital pin 6
int f = 7; //f of 7-segment attach to digital pin 7
int g = 8; //g of 7-segment attach to digital pin 8
int d1 = 9; //1st digit attach to digital pin 9
int d2 = 10;
const int button = 1;
int bttn_state = 0;

void setup() {
  pinMode(button, INPUT);
  pinMode(d1,OUTPUT);
  pinMode(d2,OUTPUT);
  pinMode(a,OUTPUT);
  pinMode(b,OUTPUT);
  pinMode(c,OUTPUT);
  pinMode(d,OUTPUT);
  pinMode(e,OUTPUT);
  pinMode(f,OUTPUT);
  pinMode(g,OUTPUT);
}

void loop() {
  //if(digitalRead(button)==HIGH)
  //{
   //while (true){
    digitalWrite(d1, HIGH);
    digitalWrite(d2, LOW);
    digitalWrite(a,HIGH);
    digitalWrite(b,HIGH);
    digitalWrite(c,HIGH);
    digitalWrite(d,HIGH);
    digitalWrite(e,HIGH);
    digitalWrite(f,HIGH);
    digitalWrite(g,LOW);
    delay(100);
    //if(digitalRead(button)==HIGH){
      //break;
      //}
    digitalWrite(d2, HIGH);
    digitalWrite(d1, LOW);
    digitalWrite(a,HIGH);
    digitalWrite(b,HIGH);
    digitalWrite(c,HIGH);
    digitalWrite(d,HIGH);
    digitalWrite(e,HIGH);
    
    digitalWrite(f,HIGH);
    digitalWrite(g,HIGH);
    delay(100);
    //if(digitalRead(button)==HIGH){
      //break;
      //}
   //}
  //}
   //digitalWrite(d1,HIGH);
   //digitalWrite(d2,HIGH);
   //delay(500);
}
