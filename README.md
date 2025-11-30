# TCP-Client-Server

A basic TCP Client and Server implementation in Python.

## Key Features & Benefits

*   **Simple TCP Communication:** Establishes a fundamental client-server connection for data exchange.
*   **Easy to Understand:**  Clear and concise code, ideal for beginners learning network programming.
*   **Customizable Port:** Allows users to configure the port for communication.

## Prerequisites & Dependencies

*   **Python 3.x:**  Ensure Python 3 or a later version is installed on your system.
*   **No external libraries required:** This project only uses the built-in `socket` module.

## Installation & Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Paddywelch117/TCP-Client-Server.git
    cd TCP-Client-Server
    ```

2.  **No installation needed:** The project consists of Python scripts that can be run directly.

## Usage Examples

1.  **Run the server:**

    ```bash
    python TCP\ Server.py
    ```

2.  **Run the client:**

    ```bash
    python TCP\ Client.Py
    ```

    **Note:** Ensure the server is running before starting the client. The client will attempt to connect to the server at the specified host and port.
## Code Snippets

**TCP Server.py:**

```python
import socket


#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

serversocket.bind((host, port))

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection
    clientsocket,address = serversocket.accept()

    print("received connection from: %s " % str(address))

    #Message sent to client after successful connection
    message = 'hello! Thank you for connecting to the server' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
```

**TCP Client.py:**

```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

s.connect((host, port))

tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))

```

## Configuration Options

*   **Port:**  The default port is `4444`. You can modify the `port` variable in both `TCP Server.py` and `TCP Client.Py` to use a different port.  Ensure that both the client and server use the same port.

    ```python
    # Example: Changing the port to 12345
    port = 12345
    ```

*   **Host:**  The server uses `socket.gethostname()` to determine the host.  This is typically your local machine's hostname. You can change this to a specific IP address if needed, but ensure the client can reach that address.

## Contributing Guidelines

Contributions are welcome!  If you'd like to contribute to this project, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive messages.
4.  Submit a pull request to the main branch.

## License Information

This project has no specified license. All rights are reserved by the owner.

## Acknowledgments

N/A
