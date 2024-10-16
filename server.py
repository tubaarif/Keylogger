from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        log_data = request.form.get('log')
        if log_data:
            with open('received_logs.txt', 'a') as f:
                f.write(log_data)  # Write received log data to a file
        return 'Log received', 200
    else:
        try:
            with open('received_logs.txt', 'r') as f:
                log_data = f.read()
            return log_data, 200
        except FileNotFoundError:
            return 'No logs available', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=<port number>)