from http.server import SimpleHTTPRequestHandler, HTTPServer

def run():
    port = 8080
    
    # Create the server class
    server_class=HTTPServer

    # Create the simple http request handler class (a handler is a block of code that gets triggered when a certain event or request happens)
    handler_class=SimpleHTTPRequestHandler

    # Define server address and use the port variable as the port number 
    server_address = ('', port)  

    # Create a HTTP server
    httpd = server_class(server_address, handler_class)

    # Tell the user which port the server is running on
    print(f'Server running on port {port}. Go to http://localhost:{port}')

    # Start the server and run until manually stopped 
    httpd.serve_forever()

if __name__ == "__main__":
    run()
