int LDRenviroment = A0;
int LDRstlight = A1;// select the input pin for LDR
int LDRStreetlight=A1;
int LEDPin=11;
int sensorValue1 = 0; // variable to store the value coming from the sensor
int sensorValue2 = 0;
void setup() {
Serial.begin(9600); //sets serial port for communication
pinMode(LEDPin,OUTPUT);
}

void loop() {
  sensorValue1 = analogRead(LDRenviroment);
  sensorValue2 = analogRead(LDRstlight);
  
  Serial.print(sensorValue1);
  Serial.print(", ");
  Serial.println(sensorValue2);
if(sensorValue1<=600)
{
  digitalWrite(LEDPin,HIGH);
}
else
  {
  digitalWrite(LEDPin,LOW);
  }
delay(100);

}
