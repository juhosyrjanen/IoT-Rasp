import getopt
import logging
import sys
from coapthon.server.coap import CoAP
from Pir import Pir

__author__ = 'giacomo'


class CoAPServer(CoAP):
    def __init__(self, host, port, multicast=False):
        CoAP.__init__(self, (host, port), multicast)
        self.add_resource('Pir/', Pir())
        print "CoAP Server start on " + host + ":" + str(port)
        print self.root.dump()


def usage():
    print "coapserver.py -i <ip address> -p <port>"


def main(argv):
    ip = "172.28.170.197"
    port = 5683
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ["ip=", "port="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip = arg
        elif opt in ("-p", "--port"):
            port = int(arg)

    server = CoAPServer(ip, port)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."


if __name__ == "__main__":
    main(sys.argv[1:])
