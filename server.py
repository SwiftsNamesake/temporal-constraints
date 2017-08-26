from http import server
import os
import sys

def run():

    host = '0.0.0.0'
    port = int(os.environ.get('PORT', 5000))
    protocol = 'HTTP/1.0'
    server_address = ('', port) # What is 'bind' for

    server.SimpleHTTPRequestHandler.protocol_version = protocol
    
    with server.HTTPServer(server_address, server.SimpleHTTPRequestHandler) as httpd:
        sa = httpd.socket.getsockname()
        serve_message = 'Serving HTTP on {host} port {port} (http://{host}:{port}/) ...'
        print(serve_message.format(host=sa[0], port=sa[1]))
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nKeyboard interrupt received, exiting.')
            sys.exit(0)


if __name__ == '__main__':
    print('Running server.py')
    run()