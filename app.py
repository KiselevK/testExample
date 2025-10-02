from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello from Azure with Python! V1</h1>"

if __name__ == '__main__':
    app.run()
