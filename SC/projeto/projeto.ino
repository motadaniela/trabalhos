//      A
//     ---
//  F |   | B
//    | G |
//     ---
//  E |   | C
//    |   |
//     ---
//      D

int a = 2; //a of 7-segment attach to digital pin 2
int b = 3; //b of 7-segment attach to digital pin 3
int c = 4; //c of 7-segment attach to digital pin 4
int d = 5; //d of 7-segment attach to digital pin 5
int e = 6; //e of 7-segment attach to digital pin 6
int f = 7; //f of 7-segment attach to digital pin 7
int g = 8; //g of 7-segment attach to digital pin 8
int d1 = 9; //1st digit attach to digital pin 9
int d2 = 10; //2nd digit attach to digital pin 10
#define led1 A3
#define led2 A4
#define led3 A5
#define buzzer 11
const int button = 1;
#define trigPin 12
#define echoPin 13
int sound = 10;


void setup()
{
  pinMode(d1,OUTPUT);
  pinMode(d2,OUTPUT);
  pinMode(a,OUTPUT);
  pinMode(b,OUTPUT);
  pinMode(c,OUTPUT);
  pinMode(d,OUTPUT);
  pinMode(e,OUTPUT);
  pinMode(f,OUTPUT);
  pinMode(g,OUTPUT);
  pinMode(button, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzer, OUTPUT);
}

void loop()
{
  if(digitalRead(button)== LOW){
  //number15
    unsigned char o,x;
    analogWrite(led1, 255); //turns on first led
    digit1(); //for the first digit
    display1(); //displays the number 1
    delay(10);
    digit2(); //for the second digit
    display5(); //display the number 5
    delay(1000); //wait a second
  //number14  
    digit1();
    display1();
    delay(8);
    digit2();
    display4();
    delay(1000);
  //number13 
    digit1();
    display1();
    digit2();
    display3();
    delay(1000);
  //number12
    digit1();
    display1();
    digit2();
    display2();
    delay(1000);
  //number11
    digitalWrite(d1, LOW);
    digitalWrite(d2, LOW);
    display1(); //both digits display the same number
    delay(1000);
  //number10
    analogWrite(led2, 255); //turns on second led
    digit1();
    display1();
    digit2();
    display0();
    delay(1000);
  //number09
    digit1();
    display0();
    digit2();
    display9();
    delay(1000);
  //number08
    digit1();
    display0();
    digit2();
    display8();
    delay(1000);
  //number07
    digit1();
    display0();
    digit2();
    display7();
    delay(1000);
  //number06
    digit1();
    display0();
    digit2();
    display6();
    delay(1000);
  //number05
    analogWrite(led3,255); //turns on third led
    digit1();
    display0();
    digit2();
    display5();
    delay(1000);
  //number04
    digit1();
    display0();
    digit2();
    display4();
    delay(1000);
  //number03
    digit1();
    display0();
    digit2();
    display3();
    delay(1000);
  //number02
    digit1();
    display0();
    digit2();
    display2();
    delay(1000);
  //number01
    digit1();
    display0();
    digit2();
    display1();
    delay(1000);
  //number00
    digitalWrite(d1, LOW);
    digitalWrite(d2, LOW);
    display0();
    delay(1000);
  //turns leds and display off
    digitalWrite(led1,LOW);
    digitalWrite(led2,LOW);
    digitalWrite(led3,LOW);
    digitalWrite(d1, HIGH);
    digitalWrite(d2, HIGH);
          
  //buzzer turns on for 2 seconds
    //analogWrite(buzzer, 100);
    //delay(2000);
    //analogWrite(buzzer, 0);
        
  //sensor
    long duration, distance;
    delay(500);
    digitalWrite(trigPin, LOW);
    //duration = pulseIn(echoPin, HIGH);
    //distance = (duration/2) / 29.1;
 
    if (distance <= 200) {
      analogWrite(buzzer, 50);
      delay(500);
}
    if (distance < 150) {
      analogWrite(buzzer, 75);
      delay(500);
}
    if (distance < 125) {
      analogWrite(buzzer, 100);
      delay(500);
}
    if (distance < 100) {
      analogWrite(buzzer, 125);
      delay(500);
}
    if (distance < 75) {
      analogWrite(buzzer, 150);
      delay(500);
}
    if (distance < 50) {
      analogWrite(buzzer, 200);
      delay(500);
}
    if (distance > 200 || distance <= 0){
      Serial.println("Out of range");
      noTone(buzzer);
}
    else {
      analogWrite(buzzer,100);
      Serial.print(distance);
      Serial.println(" cm");
      tone(buzzer, sound);
}
    delay(1000);
  }
}

//each digit
void digit1(){
  digitalWrite(d1, LOW);
  digitalWrite(d2, HIGH);
}
void digit2(){
  digitalWrite(d2, LOW);
  digitalWrite(d1, HIGH);
}

//each "displayX()" corresponds to each number(from 0-9), to be displayed
void display0()
{
  unsigned char k;
  for(k=2; k<=7; k++)
  {
    digitalWrite(k,HIGH); //turns from a to f on
    digitalWrite(g,LOW); //turns g off
  }
}
void display1()
{
   digitalWrite(b,HIGH); //turns b on
   digitalWrite(c,HIGH); //turns c on
   digitalWrite(a,LOW); //turns all from d to g off
   digitalWrite(d,LOW);
   digitalWrite(e,LOW);
   digitalWrite(f,LOW);
   digitalWrite(g,LOW);
}
void display2()
{
  unsigned char k;
  for(k=2; k<=3; k++)
  {
    digitalWrite(k,HIGH);
    digitalWrite(c,LOW);
    digitalWrite(d,HIGH);
    digitalWrite(e,HIGH);
    digitalWrite(f,LOW);
    digitalWrite(g,HIGH);
  }
}
void display3()
{
  unsigned char k;
  for(k=2; k<=5; k++)
  {
    digitalWrite(k,HIGH);
    digitalWrite(g,HIGH);
    digitalWrite(f,LOW);
    digitalWrite(e,LOW);
  }
}
void display4()
{
  digitalWrite(a,LOW);
  digitalWrite(b,HIGH);
  digitalWrite(c,HIGH);
  digitalWrite(d,LOW);
  digitalWrite(e,LOW);
  digitalWrite(f,HIGH);
  digitalWrite(g,HIGH);
  }
void display5()
{
  digitalWrite(a,HIGH);
  digitalWrite(b,LOW);
  digitalWrite(c,HIGH);
  digitalWrite(d,HIGH);
  digitalWrite(e,LOW);
  digitalWrite(f,HIGH);
  digitalWrite(g,HIGH);
}
void display6()
{
  unsigned char k;
  for(k=4; k<=8; k++)
  {
    digitalWrite(k,HIGH);
    digitalWrite(b,LOW);
    digitalWrite(a,HIGH);
  }
}
void display7()
{
  unsigned char k;
  for(k=5; k<=8; k++)
  {
    digitalWrite(a,HIGH);
    digitalWrite(b,HIGH);
    digitalWrite(c,HIGH);
    digitalWrite(k,LOW);
  }
}
void display8()
{
  unsigned char k;
  for(k=5; k<=8; k++)
  {
    digitalWrite(k,HIGH);
  }
}
void display9()
{
  unsigned char k;
  for(k=2; k<=4; k++)
  {
    digitalWrite(k,HIGH);
    digitalWrite(f,HIGH);
    digitalWrite(g,HIGH);
    digitalWrite(d,LOW);
    digitalWrite(e,LOW);
  }
}
