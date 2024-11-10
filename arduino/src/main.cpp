#include <Arduino.h>

int buttonPin = 8;  // Pin waarop de knop is aangesloten
int counter = 0;    // Startteller

void setup() {
    Serial.begin(9600);      // Start de seriële communicatie
    pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
    if (digitalRead(buttonPin) == LOW) {
        counter++;
        Serial.println(counter); // Stuur de `counter` naar de seriële poort
        delay(1000); // Vertraging om multiple reads te voorkomen
    }
}