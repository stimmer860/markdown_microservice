import zmq
import markdown
import json

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Reply socket
    socket.bind("tcp://127.0.0.1:5555")  # Adjust port as needed

    print("Running Markdown-to-HTML Conversion")
    while True:
        try:
            request = socket.recv_string()
            data = json.loads(request)

            # Check for markdown content in the request
            if "markdown" in data:
                md_content = data["markdown"]
                converted_html = markdown.markdown(md_content)

                response = {
                    "success": True,
                    "html": converted_html,
                }
            # Error handling when no markdown content detected
            else:
                response = {
                    "success": False,
                    "error": "Missing 'markdown' field in the request."
                }

        # Deal with exceptions
        except Exception as e:
            response = {
                "success": False,
                "error": str(e)
            }

        print(response)

        # Send the response back as a JSON string
        socket.send_string(json.dumps(response))

if __name__ == "__main__":
    main()