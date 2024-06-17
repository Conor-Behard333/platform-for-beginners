from http.server import SimpleHTTPRequestHandler, HTTPServer

def run():
    port = 8080

    # Define server address and use the port variable as the port number 
    server_address = ('', port)  

    # Create a HTTP server
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

    # Tell the user which port the server is running on
    print(f'Server running on port {port}. Go to http://localhost:{port}')

    # Start the server and run until manually stopped 
    httpd.serve_forever()

if __name__ == "__main__":
    run()
