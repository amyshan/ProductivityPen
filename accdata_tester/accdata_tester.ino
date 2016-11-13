
#include <Wire.h>               //Include the Wire library
#include <MMA_7455.h>  

MMA_7455 accel = MMA_7455();    // Make MMA7455 object

char xVal, yVal, zVal;          // Return value variables
char xinit, yinit, zinit;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  accel.initSensitivity(2);  
  xVal = accel.readAxis('x');
  yVal = accel.readAxis('y');
  zVal = accel.readAxis('z');

  if (xVal > 0) {
    xinit = -xVal;
  }
  else {
    xinit = -xVal;
  }
  if (yVal > 0) {
    yinit = -yVal;
  }
  else {
    yinit = -yVal;
  }
  if (zVal > 63) {
    zinit = -zVal + 63;
  }
  else {
    zinit = 63 - zVal;
  }

  accel.calibrateOffset(xinit, yinit, zinit);

  xVal = accel.readAxis('x');
  yVal = accel.readAxis('y');
  zVal = accel.readAxis('z');
  Serial.print(xVal, DEC);
  Serial.print(" ");
  Serial.print(yVal, DEC);
  Serial.print(" ");
  Serial.print(zVal, DEC);
  delay(100);

  

}

void loop() {
  // put your main code here, to run repeatedly:
  xVal = accel.readAxis('x');   // Read X Axis
  yVal = accel.readAxis('y');   // Read Y Axis
  zVal = accel.readAxis('z');   // Read Z Axis

  Serial.print(xVal, DEC);
  Serial.print(" ");

  Serial.print(yVal, DEC);
  Serial.print(" ");

  Serial.println(zVal, DEC);
  //Serial.print(" ");
  delay(100);
}
