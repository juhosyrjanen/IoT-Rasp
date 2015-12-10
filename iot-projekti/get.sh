#/bin/bash
#
# Simple bash script that orders CoAP to fetch data from the PIR-sensor
# and prints it into a file

sudo coap get coap://172.28.170.197/Pir > /home/pidb/projekti/iot-projekti/get.txt
