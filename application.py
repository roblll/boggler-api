from flask import Flask, jsonify
application = Flask(__name__)

from words.A import A
from words.B import B
from words.C import C
from words.D import D
from words.E import E
from words.F import F
from words.G import G
from words.H import H
from words.I import I
from words.J import J
from words.K import K
from words.L import L
from words.M import M
from words.N import N
from words.O import O
from words.P import P
from words.Q import Q
from words.R import R
from words.S import S
from words.T import T
from words.U import U
from words.V import V
from words.W import W
from words.X import X
from words.Y import Y
from words.Z import Z

@application.route('/test')
def test():
    return 'test'

@application.route('/api', methods=['POST'])
def hello():
    
    words_found = {"words": ["apple", "ball", "cat", "dog"]}
    
    return jsonify(words_found)