#define BUTTONADD_PIN 4
#define BUTTONSUB_PIN 2
float potReading = 0;
float updatedPotReading = 0;
float threshold = 1.5;


void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(BUTTONADD_PIN, INPUT_PULLUP);
  pinMode(BUTTONSUB_PIN, INPUT_PULLUP);
}

// the loop routine runs over and over again forever:
void loop() {
  updatedPotReading = analogRead(A0);
  if(abs(updatedPotReading - potReading) > threshold){
    potReading = updatedPotReading;
    }
  
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  int buttonaddValue = 0;
  int buttonsubValue = 0;

  byte buttonAddState = digitalRead(BUTTONADD_PIN);
  byte buttonSubState = digitalRead(BUTTONSUB_PIN);

  if (buttonSubState == LOW) {
    buttonsubValue = 1;
    Serial.print(buttonsubValue);
  }
  else {
    buttonsubValue = 0;
    Serial.print(buttonsubValue);
  }

    Serial.print(" ");
  
  if (buttonAddState == LOW) {
    buttonaddValue = 1;
    Serial.print(buttonaddValue);
  }
  else {
    buttonaddValue = 0;
    Serial.print(buttonaddValue);
  }



  // print out the value you read:
  Serial.print(" ");
  Serial.println(potReading);
  delay(1);  // delay in between reads for stability
}
