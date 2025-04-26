#include <Servo.h>

#include <SoftwareSerial.h>
#include <DHT.h>

#define DHTPIN 4     // Digital pin connected to DHT11 sensor
#define RXPIN 3     // RX pin of the Bluetooth module
#define TXPIN 2     // TX pin of the Bluetooth module

#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);
SoftwareSerial bluetooth(RXPIN, TXPIN);

void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);
  dht.begin();
}

void loop() {
  // Read temperature and humidity from DHT11
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Send data to Bluetooth module
  bluetooth.print("T:");
  bluetooth.print(t);
  bluetooth.print("H:");
  bluetooth.println(h);

  delay(2000);
}