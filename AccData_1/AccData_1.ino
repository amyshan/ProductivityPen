/*
  Demonstration code for the Parallax MMA7455 3-axis accelerometer, #28526
  
  Optional: Before use run the MMA7455_CalibrateOffset sketch to obtain the
  offset values. The offsets are subtracted from those received from the
  accelerometer, so that the return values are as close to X=0, Y=0, X=63
  as possible, when the device is stationary. 0 means 0g; 63 means 1g.
  
  ------------

  This sketch REQUIRES the use of a third-party library, MMA_7455. 
  It is available for download from the following source.

  https://code.google.com/p/mma-7455-arduino-library/downloads/detail?name=MMA_7455_UNO.zip

  Once downloaded, unzip the files and place them into your Arduino 'libraries' folder. 
  This folder is located within your Arduino sketch directory; on Windows this is usually 
  My Documents\Arduino. If there is no 'libraries' folder within the sketch 
  directory you must create one.

  For your convenience, the MMA_7455 library is also included in the download with this 
  demonstration sketch. Prior to use you MUST move the 'MMA_7455' library folder into 
  your Arduino sketch 'libraries' folder.

  Important! After moving the MMA_7455 library to the 'libraries' folder
  you MUST restart the Arduino IDE.
  
  This example code is for the Arduino Uno and direct compatible boards. 
  It has not been tested, nor designed for, other Arduino boards, including
  the Arduino Due.
  
  ------------

  Connections:
  MMA7455      Arduino
  GND          GND
  VDD          5V
  DATA*        Analog pin A4 (I2C SDA)
  CLK*         Analog pin A5 (I2C CLK)
  
  * Also add 1 each 4.7K resistor between the DATA and CLK pins and
  5V, as noted in the 28526-MMA7455-3-Axis-Accelerometer documentation.
  (Your accelerometer may work without these resistors, but for 
  consistent results they should be included.)
  
  Note: Refer to the 28526-MMA7455-3-Axis-Accelerometer documentation 
  for the pin locations. The pins are not definitively marked on the 
  device itself.
  
  Be VERY careful to not reverse the GND and VDD connections!  
  
  ------------
   
  To run this demo sketch, upload it to your Arduino, and display the
  Serial Monitor window. Be sure communications speed is set to 9600 baud.
  
  Return values for each of the X, Y, and Z axes are from -127 to 127,
  where (at 2g sensitivity mode) 0 = 0g, 63 = 1g, and -63 = -1g.
  
*/

#include <Wire.h>               //Include the Wire library
#include <MMA_7455.h>           //Include the MMA_7455 library

MMA_7455 accel = MMA_7455();    // Make MMA7455 object

char xVal, yVal, zVal;          // Return value variables
char xinit, yinit, zinit;
int button = 2; //Push button on data pin 2
int buzzer = 3; //Buzzer for nulltime
char nulltime;

void setup() {
  Serial.begin(9600);           // Use the Serial Monitor window at 9600 baud
  pinMode(button, INPUT);  //Initialize push-button
  // Set the g force sensitivity: 2=2g, 4=4g, 8-8g
  accel.initSensitivity(2);
  
 // Find initial x,y,z values, and calibrate accelerometer 
  xVal = accel.readAxis('x');
  yVal = accel.readAxis('y');
  zVal = accel.readAxis('z');
  
  //make sure the signs are right
  if (xVal > 0) {
    xinit = -xVal;}
    else {
      xinit = -xVal;
    }
  if (yVal > 0) {
    yinit = -yVal;}
    else {
      yinit = -yVal;
    }
  if (zVal > 63) {
    zinit = -zVal+63;}
    else {
      zinit = 63-zVal;
    }
    
  //Calibrate accel
  accel.calibrateOffset(xinit, yinit, zinit);

  //Complete loop number 1 in the setup
  xVal = accel.readAxis('x');
  yVal = accel.readAxis('y');
  zVal = accel.readAxis('z');
  Serial.print(xVal, DEC);
  Serial.print(" ");
  Serial.print(yVal, DEC);
  Serial.print(" ");
  Serial.println(zVal, DEC);
  delay(100);
}

void loop() {
  if digitalRead
  while (digitalRead(button) == HIGH) {
 
  //Begin the continuous data loop again
  xVal = accel.readAxis('x');   // Read X Axis
  yVal = accel.readAxis('y');   // Read Y Axis
  zVal = accel.readAxis('z');   // Read Z Axis

  if(Serial.available()){ // only send data back if data has been sent
    nulltime = Serial.read(); // read the incoming data
    if (nulltime == 'B') {
      digitalWrite(13, HIGH); //turn on LED
      Serial.println("You've been idle for too long!"); // acknowledge data reception
    }
  }

  nulltime = 'N';
  
  Serial.print(xVal, DEC);
  Serial.print(" ");
  
  Serial.print(yVal, DEC);
  Serial.print(" ");
  
  Serial.println(zVal, DEC);
  //Serial.print(" ");
  delay(100);
  
  }
}
