void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(115200);
}

float getTemperature() {
    float temp = -999;
    if (Serial.available() > 0) {
        temp = Serial.parseFloat();
    }
    return temp;
}


void loop() {
    float temp = getTemperature();
    
    if (temp != -999)
        Serial.println(temp);

    digitalWrite(13, !digitalRead(13)); // toggle led
    delay(1000);
}

