#define led1 1
#define led2 2
#define led3 3

void setup ()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}
 
void loop()
{
  unsigned char x,y,z;
//-----------------------------alternative way
  for (int x=0; x<=85;x++){
    analogWrite(led1, x);
    delay(1000);
  for (int y=85;y<=170;y++){
    analogWrite(led1, y);
    analogWrite(led2, x);
    delay(1000);
  for (int z=170;z<=255;z++){
    analogWrite(led1,z);
    analogWrite(led2,y);
    analogWrite(led3,x);
    delay(1000);
    analogWrite(led2,z);
    analogWrite(led3,y);
    delay(1000);
    analogWrite(led3,z);
    delay(1000);
    }
    }
    }
  for (int z=255;z>=0;z--){
  analogWrite(led1,z);
  analogWrite(led2,z);
  analogWrite(led3,z);
  delay(8);
  }
}
