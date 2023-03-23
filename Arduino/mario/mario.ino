
void setup() {
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    int shooting = Serial.parseInt();
    if(shooting == 1) {
      digitalWrite(8, HIGH);
    } else if(shooting == 0){
      digitalWrite(8, LOW);
    }
  } 
}
