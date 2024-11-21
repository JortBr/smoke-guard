#include <Arduino.h>
int buttonPin = 8;
int counter = 0;
int daily_limit = 0;
int cigarettes_taken = 0;
bool limit_reached = false;
bool buttonPressed = false;

void setup() {
    Serial.begin(9600);
    pinMode(buttonPin, INPUT_PULLUP);
    pinMode(13, OUTPUT);
}

void loop() {
    if (Serial.available()) {
        String data = Serial.readStringUntil('\n'); // Ontvang data
        int separatorIndex = data.indexOf(','); // Zoek naar de komma
        if (separatorIndex != -1) {
            int cigarettesTaken = data.substring(0, separatorIndex).toInt(); // Verkrijg sigaretten die zijn genomen
            int dailyLimit = data.substring(separatorIndex + 1).toInt(); // Verkrijg dagelijks limiet

            // Alleen het bericht sturen zonder extra tekst
            if (cigarettesTaken >= dailyLimit) {
                Serial.println("status:limit_reached");
            } else {
                Serial.println("status:ok");
            }
            // Verstuur alleen de data in het juiste formaat:
            Serial.print(cigarettesTaken);
            Serial.print(",");
            Serial.println(dailyLimit);
        }
    }
    
    if (digitalRead(buttonPin) == LOW && !buttonPressed) {
        buttonPressed = true;  // Zorg ervoor dat de knop niet meerdere keren triggert

        if (!limit_reached) { // Alleen verhogen als de limiet niet bereikt is
            counter++;
            cigarettes_taken++;
            Serial.println(counter);  // Stuur de `counter` naar de seriële poort
        } else {
            Serial.println("Limiet bereikt! Geen sigaretten meer toegestaan.");
        }
        delay(500); // Vertraging om meerdere reads te voorkomen
    }

    // Reset knopstatus als de knop wordt losgelaten
    if (digitalRead(buttonPin) == HIGH) {
        buttonPressed = false;
    }
}
