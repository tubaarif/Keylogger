In the server.py file, you can change the port number to your desired value. For example:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)

and In the main.py file, update the URL in the requests.post call to match the server's IP address and port number. For example:
**try:
    requests.post('http://<host_ip>:<port_number>/log', data={'log': log_data})**
Replace <host_ip> with the server's IP address and <port_number> with the port number specified in your server.py (e.g., 4444).
