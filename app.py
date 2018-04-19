import os
from flask import Flask

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

x = os.environ['APP_SETTINGS']

@app.route('/')
def hello():
    # return "Hello World!"
    return str(os.environ['APP_SETTINGS'])

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    print(os.environ['APP_SETTINGS'])
    app.run()

