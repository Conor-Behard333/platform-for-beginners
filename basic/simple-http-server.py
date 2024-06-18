import http.server
import socketserver

def run():
    # Define the handler to use for incoming requests
    handler = http.server.SimpleHTTPRequestHandler

    # Set the port number for the server
    port = 8080

    # Create the server and bind it to the specified port
    httpd = socketserver.TCPServer(("", port), handler)

    print(f'Server running on port {port}. Go to http://localhost:{port}')

    # Run the server indefinitely
    httpd.serve_forever()

if __name__ == "__main__":
    run()
