void setup()
{
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
}

void loop()
{
  if(Serial.available()){
    char sign = Serial.read();
    Serial.println(sign);
    switch(sign){
      case '1':{
        digitalWrite(2,1);
        break;
      }
      case '2':{
        digitalWrite(3,1);
        break;
      }
      case '3':{
        digitalWrite(4,1);
        break;
      }
      case '4':{
        digitalWrite(5,1);
        break;
      }
      case '5':{
        digitalWrite(6,1);
        break;
      }
      case '6':{
        digitalWrite(7,1);
        break;
      }
      case '0':{
        delay(1000);
        digitalWrite(6,0);
        digitalWrite(3,0);
        digitalWrite(4,0);
        digitalWrite(5,0);
        digitalWrite(2,0);
        digitalWrite(7,0);
        delay(1000);
        break;
      }
    }
  }
}
