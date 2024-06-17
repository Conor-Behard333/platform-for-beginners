from http.server import BaseHTTPRequestHandler, HTTPServer

class CustomHandler(BaseHTTPRequestHandler):

    # When a get request is sent to http://localhost:8080 this function runs
    def do_GET(self):
        html_content = ""
        # Open the index.html file, read it and store its contents in the variable "html_content"
        with open('index.html', 'rb') as file:
            html_content = file.read()
        
        # Tells the client what type of content it is about to receive
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send a 200 response to the client (200 means everything worked)
        self.send_response(200)
        
        self.wfile.write(html_content)

def run(port=8080):
    # Create the server class
    server_class=HTTPServer

    # Create the custom handler_class (a handler is a block of code that gets triggered when a certain event or request happens)
    handler_class=CustomHandler

    # set the server address with the port number
    server_address = ('', port)

    # Create the http process
    httpd = server_class(server_address, handler_class)

    # Tell the user which port the server is running on
    print(f'Server running on port {port}. Go to http://localhost:{port}')

    # Run the server until manually stopped
    httpd.serve_forever()

if __name__ == "__main__":
    run()


