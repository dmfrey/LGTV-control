#!/usr/bin/env python
import ConfigParser, os
import SocketServer
import SimpleHTTPServer

from libLGTV_serial import LGTV

config = ConfigParser.ConfigParser()
config.read(['/etc/lg/lgrc.conf', os.path.expanduser('~/.lgrc')])

# Configure Serial Port
serial_port = config.get('SERIAL_CONFIG','serial_dev')

# Configure TV 
tv_model = config.get('TV_CONFIG', 'tv_model')
tv_inputs = config.get('TV_CONFIG', 'tv_inputs')

tv = LGTV(tv_model, serial_port)

PORT = 6080

def power():
    """ toggles power on and off """
    tv.debounce('togglepower')
    tv.send("togglepower")

    return 'power toggle complete!'

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/power':
            #This URL will trigger power to toggle on and off
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(power()) #call sample function here
            return
        else:
            # add other endpoints, such as inputs, here
            return

# Configure the http server
httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),CustomHandler)

#Start the http server
print "serving at port", PORT
httpd.serve_forever()
