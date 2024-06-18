import http.server
import socketserver

class CustomHandler(http.server.BaseHTTPRequestHandler):

    # When a get request is sent to http://localhost:8080 this function runs
    def do_GET(self):
        html_content = ""
        return_code = 200
        try:
            # Open the index.html file, read it and store its contents in the variable "html_content"
            with open('index.html', 'rb') as file:
                html_content = file.read()
        except:
            # If the code within the try block throws an error then run this block of code
            print("something went wrong")
            # 500 means an internal server error occurred
            return_code = 500 

        # Send a code response to the client (200 means everything worked)
        self.send_response(return_code)
        # Tells the client what type of content it is about to receive
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(html_content)

def run():
    port = 8080

    # Create the custom handler_class (a handler is a block of code that gets triggered when a certain event or request happens)
    handler=CustomHandler

    # set the server address with the port number
    server_address = ('', port)

    # Create the http process
    httpd = socketserver.TCPServer(("", port), handler)

    # Tell the user which port the server is running on
    print(f'Server running on port {port}. Go to http://localhost:{port}')

    # Run the server until manually stopped
    httpd.serve_forever()

if __name__ == "__main__":
    run()


