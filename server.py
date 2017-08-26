import http
import os
import sys

def run():

    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    protocol = 'HTTP/1.0'
    server_address = ('', port) # What is 'bind' for

    http.server.SimpleHTTPRequestHandler.protocol_version = protocol
    
    with http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler) as httpd:
        sa = httpd.socket.getsockname()
        serve_message = 'Serving HTTP on {host} port {port} (http://{host}:{port}/) ...'
        print(serve_message.format(host=sa[0], port=sa[1]))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nKeyboard interrupt received, exiting.')
            sys.exit(0)