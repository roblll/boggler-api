from flask import Flask, jsonify, request
application = Flask(__name__)
from PIL import Image
import base64
import datetime
import os

@application.route('/test', methods=['POST'])
def test():
    input_json = request.get_json(force=True)['file']
    input_json += "=" * ((4 - len(input_json) % 4) % 4)
    im_name = f'{datetime.datetime.now()}.jpeg'
    decoded_image = open(im_name, 'wb')
    decoded_image.write(base64.b64decode((input_json)))
    decoded_image.close()

    os.remove(decoded_image.name)

    board = [
        ["l", "p", "t", "c"],
        ["j", "v", "e", "e"],
        ["w", "r", "u", "f"],
        ["q", "o", "r", "g"],
    ]

    data = {"board": board}

    return jsonify(data)

@application.route('/api', methods=['POST'])
def hello():
    
    words_found = {"words": ["apple", "ball", "cat", "dog"]}
    
    return jsonify(words_found)

@application.route('/hi')
def hi():
    
    words_found = {"words": ["apple", "ball", "cat", "dog"]}
    
    return jsonify(words_found)

@application.errorhandler(404)
def handle_404(e):
    return 'Not Found'