
const int ledAzul = D0; // D0
const int ledRojo = D1;    // D1 
const int ledVerde = D2; // D2

void setup() {
pinMode(ledRojo,OUTPUT);
pinMode(ledVerde,OUTPUT);
pinMode(ledAzul,OUTPUT);

}
 
void loop() {
//Hacer color rojo
analogWrite(ledRojo, 250);
analogWrite(ledVerde,255);
analogWrite(ledAzul,255);
}
