
const int ledAzul = 10; // D0
const int ledRojo = 9;    // D1 
const int ledVerde = 11; // D2

void setup() {
pinMode(ledRojo,OUTPUT);
pinMode(ledVerde,OUTPUT);
pinMode(ledAzul,OUTPUT);

}
 
void loop() {
//Hacer color rojo
digitalWrite(ledRojo, 255);
analogWrite(ledVerde,0);
digitalWrite(ledAzul,255);
}
