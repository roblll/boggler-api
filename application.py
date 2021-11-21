from flask import Flask, jsonify
application = Flask(__name__)

@application.route('/test')
def test():
    return 'test'

@application.route('/api', methods=['POST'])
def hello():
    
    words_found = {"words": ["apple", "ball", "cat", "dog"]}
    
    return jsonify(words_found)