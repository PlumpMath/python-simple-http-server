#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import argparse
import re

class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print self.headers.getheader('user-agent')
        print self.path
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(self.headers.getheader('user-agent'))
        return

    def do_POST(self):
        print self.headers.getheader('user-agent')
        print self.path
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(self.headers.getheader('user-agent'))
        return
 
 
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Simple HTTP Server')
    parser.add_argument('port', type=int, help='hosting port')
    args = parser.parse_args()
    httpd = HTTPServer(('127.0.0.1', args.port), HTTPRequestHandler)
    sa = httpd.socket.getsockname()
    print "Serving HTTP on", sa[0], "port", sa[1], "..."
    httpd.serve_forever()
