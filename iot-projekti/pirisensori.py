 
#!/usr/bin/python +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# pirisensori.py
# Detect movement using a PIR module
#
# Author : Matt Hawkins // Juho Syrjanen
# Date   : 21/01/2013 // 12.10.2015
 
# Import required Python libraries
# Addtionally imported SQL libraries
import RPi.GPIO as GPIO
import time
import datetime

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PIR = 7
 
print " -- MOTION DETECTOR --"
print " - CoAP input script - "
 
# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

#Create variables to record current ja previous state 
Current_State  = 0
Previous_State = 0
#Create Movement + set to 0 by default
Movement  = 0
#Set datetime to default CoAP friendly format
Timenow = time.strftime("%Y-%m-%d %H:%M:%S") 
 
try:
 
  print "Waiting for PIR to settle ..."
 
  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0
 
  print " - Ready -  "
 
  # Loop until users quits with CTRL-C
  while True :
 
    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)
 
    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print " -- Motion detected -- "
      # Record previous state
      Previous_State=1
      Movement = 1
      

      #Printing variables and writing a new line to the CoAP input file

      print "Movement: %d " % Movement 
      print ("Time: " + time.strftime("%Y-%m-%d %H:%M:%S"))
      #save the sensor data into the CoAP -directory
      #Open the file in write mode
      file = open("/home/pi/CoAPthon/lukema.txt","w",0)
      #Write current time and movement
      file.write(time.strftime("%Y-%m-%d %H:%M:%S "))
      file.write("%d"%Movement)
      print "Writing file..."
      #Wait for 2 seconds
      time.sleep(2)
      print "Done!"
      print "Sending the log to NSA.."
      #Close the file
      file.close()

    elif Current_State==0 and Previous_State==1:

      # PIR has returned to ready state

      print " - Ready - "
      #Set previous state and movement back to 0
      Previous_State=0
      Movement = 0
 
    # Wait for 10 milliseconds
    time.sleep(0.01)

except KeyboardInterrupt:
    print "Quit"
    # Reset GPIO settings
    GPIO.cleanup()     
    
        # PIR has returned to ready state
    
    print " - Ready - "
    Previous_State=0
    Movement = 0
