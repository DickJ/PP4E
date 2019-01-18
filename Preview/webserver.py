import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '/Users/rich/Google Drive/Code/Python/PP4E/Preview/'
port = 8888

os.chdir(webdir)
srvraddr = ("", port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
