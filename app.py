from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '{"starting point":58}'


if __name__ == '__main__':
    app.run()
