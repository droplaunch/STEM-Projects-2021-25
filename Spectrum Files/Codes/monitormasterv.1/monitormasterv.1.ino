x#define PIR_PIN 8 // Pin connected to PIR sensor's output
#define BUZZER_PIN 9 // Pin connected to buzzer

void setup() {
  pinMode(PIR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {
  if (digitalRead(PIR_PIN) == HIGH) {
    // PIR sensor detects motion
    tone(BUZZER_PIN, 1000); // Play a 1000Hz tone
    delay(1000);
    noTone(BUZZER_PIN); // Stop the tone
    delay(1000); // Wait for 1 second
  }
}