#define led1 1
#define led2 2
#define led3 3

void setup ()
{
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

x>y>z

 
void loop()
{
  unsigned char ,x,y,z;
  for (int x=0; x<=85;x++){
    for (int y=85;y<=170;y++){
      for (int z=170;z<=255;z++){
        analogWrite(led1, x);
        delay(1000);
        analogWrite(led1, y);
        for (int x=0; x<=85;x++){
        analogWrite(led2, x);
        delay(1000);
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
  }
  for (int a=255;a>=0;a--){
  analogWrite(led1,a);
  analogWrite(led2,a);
  analogWrite(led3,a);
  }
}
