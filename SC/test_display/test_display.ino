int a = 2; //a of 7-segment attach to digital pin 2
int b = 3; //b of 7-segment attach to digital pin 3
int c = 4; //c of 7-segment attach to digital pin 4
int d = 5; //d of 7-segment attach to digital pin 5
int e = 6; //e of 7-segment attach to digital pin 6
int f = 7; //f of 7-segment attach to digital pin 7
int g = 8; //g of 7-segment attach to digital pin 8
int d1 = 9; //1st digit attach to digital pin 9
int d2 = 10;

void setup() {
  pinMode(d1,OUTPUT)
  pinMode(d2,OUTPUT)
}

void loop() {
  digitalWrite(d1, HIGH);
  digitalWrite(d2, HIGH);
  digitalWrite(g,LOW);
  
}
