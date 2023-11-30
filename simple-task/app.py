from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.rpute('/about')
def about():
    return 'Sistem ini merupakan percobaan untuk Simple Task'

if __name__ == '__main__':
    custom_port = 5000
    app.run(debug=True,host='0.0.0.0', port=custom_port)

