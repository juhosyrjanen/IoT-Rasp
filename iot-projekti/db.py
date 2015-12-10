#!/bin/python
#
# This Python script connects to the local database, runs .sh script that 
# runs a CoAP get. Modifies the file fetched by the .sh script and inserts
# it to the database
#
# Author: Juho Syrjanen - juhosyrjanen.com

#import libraris
import MySQLdb
import os

#Runs .sh script that fetches the needed data
print "Connecting to CoAP-server"
os.system("sudo bash /home/pidb/projekti/iot-projekti/get.sh")
print "Data fetched"

#Login to the local MySQL-server
print "Connecting to the DB.."
db = MySQLdb.connect("localhost", "*nameofdb*", "*nameoftable*", "*passwd*" )
print "Connected."

cursor = db.cursor()

#Reads the file fetched by the .sh script
print "Reading PIR-sensor data.."
file = open("/home/pidb/projekti/iot-projekti/get.txt", "r")
file_content = file.read()
file.close()

#Modifies the file to fit into the db insert
Datetime = file_content[:-3] 
Movement = file_content[20:-1]

#printing variables
print "Printing variables to be inserted into DB"
print Datetime
print Movement
quote = "'"

#Run query with variables from CoAP
query = "INSERT IGNORE INTO RAW_DATA (Datetime, Movement) VALUES ("+quote+Datetime+quote+","+Movement+")"
print query

cursor.execute(query)
#Commit the query
print "Running query.."
db.commit()

print "Query ran. Closing connection.."
db.close()
#closing connection
