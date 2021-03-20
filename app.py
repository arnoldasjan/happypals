from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '{"starting point":58}'


@app.route('/get/traverse')
def traverse_data():
    return '''
    {
        "video_start": 58,
        "highest_point": 2.56
    }
    '''


if __name__ == '__main__':
    app.run()
