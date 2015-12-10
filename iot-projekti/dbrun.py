#
# This script is scheduled to run a database insert query, located
# in another .py file, every 10 seconds.
#
# Author: Juho Syrjanen - juhosyrjanen.com
#

#Importing Twisted pyhton libraries
from twisted.internet import task
from twisted.internet import reactor
import os

timeout = 10.0 #wait = 10 sec

#Work loop
def doWork():
    os.system("sudo python /home/pidb/projekti/iot-projekti/db.py")
    pass

l = task.LoopingCall(doWork)
l.start(timeout) #Call for def every 10 secs

#Run 
reactor.run()
