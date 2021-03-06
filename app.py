from flask import Flask
import json
import data_manipulation

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is a homepage for Healthy Pals REST API'


@app.route('/get/traverse')
def traverse_data():
    x = {
        "video_start": data_manipulation.traverse_timestamp,
        "highest_point": data_manipulation.traverse_height_value,
        "start_time": data_manipulation.traverse_data['data']['start_time'],
        "end_time": data_manipulation.traverse_data['data']['end_time'],
        "summary": data_manipulation.traverse_data['data']['summary_stats']
    }
    return json.dumps(x)


@app.route('/get/vertical')
def vertical_data():
    x = {
        "video_start": data_manipulation.vertical_timestamp,
        "highest_point": data_manipulation.vertical_highest_value,
        "start_time": data_manipulation.vertical_data['data']['start_time'],
        "end_time": data_manipulation.vertical_data['data']['end_time'],
        "summary": data_manipulation.vertical_data['data']['summary_stats']
    }
    return json.dumps(x)


@app.route('/get/overhang')
def overhang_data():
    x = {
        "video_start": data_manipulation.overhang_timestamp,
        "highest_point": data_manipulation.overhang_height_value,
        "start_time": data_manipulation.overhang_data['data']['start_time'],
        "end_time": data_manipulation.overhang_data['data']['end_time'],
        "summary": data_manipulation.overhang_data['data']['summary_stats']
    }
    return json.dumps(x)


if __name__ == '__main__':
    app.run()
