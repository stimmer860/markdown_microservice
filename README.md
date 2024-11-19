# Markdown Microservice
Takes a JSON string with Markdown and converts it to HTML. The program returns a JSON string with the HTML.

# Dependencies
pyzmq: Handles communication between the client and the server using ZeroMQ.

Markdown: Converts Markdown content to HTML in the server.

# Guide
Get the code: ```https://github.com/stimmer860/MarkdownMicroservice.git```

Install the required dependencies
```pip install pyzmq```
```pip install markdown```

Requesting Data

To request data, you will need to send a JSON string over ZeroMQ. The microservice expects the request to contain Markdown content in the following JSON format:
```
{
    "markdown": "Your Markdown content here"
}
```
Step 1) Set up a ZeroMQ Request socket (```zmq.REQ```) and connect it to the microservice address.

Step 2) Format your request as a Python dictionary containing the markdown key.

Step 3) Convert the dictionary to a JSON string using ```json.dumps()```.

Step 4) Use the ```socket.send_string()``` method to send the request to the microservice.

Example Call
```
import zmq
import json

# Step 1: Connect to the microservice
context = zmq.Context()
socket = context.socket(zmq.REQ)  # Request socket
socket.connect("tcp://127.0.0.1:5555")  # Connect to the microservice

# Step 2: Prepare the request payload
markdown_content = "Some **bold** and _italic_ text."
request = {"markdown": markdown_content}

# Step 3/4: Send the request
socket.send_string(json.dumps(request_payload))  # Convert to JSON string and send
```

Receiving Data

Once the microservice processes your request, it will respond with a JSON string.
```
{
    "success": true,
    "html": "<p>Some <strong>bold</strong> and <em>italic</em> text.</p>",
}
```
After sending the request, wait for the server to reply using ```socket.recv_string().```

Example Call
```
response = socket.recv_string()  # Receive the JSON string from the server
```

