from flask import Flask, jsonify, request
application = Flask(__name__)
from PIL import Image
import base64
import datetime
import os

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

all_words = A + B + C + D + E + F + G + H + I + J + K + L + M + N + O + P + Q + R + S + T + U + V + W + X + Y + Z

def findWords(board, trie):
    output, row_len, col_len = set(), len(board), len(board[0])
    directions = ((-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1))

    def backtrack(r, c, parent):
        letter = board[r][c]
        node = parent[letter]
        if '#' in node:
            output.add(node['#'])
        board[r][c] = '*'
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= row_len or nc < 0 or nc >= col_len or \
                    board[nr][nc] not in node:
                continue
            backtrack(nr, nc, node)
        board[r][c] = letter

    for i in range(row_len):
        for j in range(col_len):
            if board[i][j] in trie:
                backtrack(i, j, trie)
    return output

@application.route('/test', methods=['POST'])
def test():
    input_json = request.get_json(force=True)['file']
    input_json += "=" * ((4 - len(input_json) % 4) % 4)
    im_name = f'{datetime.datetime.now()}.jpeg'
    decoded_image = open(im_name, 'wb')
    decoded_image.write(base64.b64decode((input_json)))
    decoded_image.close()

    # im = Image.open(im_name)

    # width, height = im.size
    # w, h = width, height

    # im01 = im.crop((0, 0, w * .25, h * .25))
    # im02 = im.crop((w * .25, 0, w * .5, h * .25))
    # im03 = im.crop((w * .5, 0, w * .75, h * .25))
    # im04 = im.crop((w * .75, 0, w, h * .25))

    # im05 = im.crop((0, h * .25, w * .25, h * .5))
    # im06 = im.crop((w * .25, h * .25, w * .5, h * .5))
    # im07 = im.crop((w * .5, h * .25, w * .75, h * .5))
    # im08 = im.crop((w * .75, h * .25, w, h * .5))

    # im09 = im.crop((0, h * .5, w * .25, h * .75))
    # im10 = im.crop((w * .25, h * .5, w * .5, h * .75))
    # im11 = im.crop((w * .5, h * .5, w * .75, h * .75))
    # im12 = im.crop((w * .75, h * .5, w, h * .75))

    # im13 = im.crop((0, h * .75, w * .25, h))
    # im14 = im.crop((w * .25, h * .75, w * .5, h))
    # im15 = im.crop((w * .5, h * .75, w * .75, h))
    # im16 = im.crop((w * .75, h * .75, w, h))

    os.remove(decoded_image.name)

    board = [
        ["a", "n", "t", "h"],
        ["o", "p", "o", "r"],
        ["p", "a", "t", "h"],
        ["u", "m", "s", "i"],
    ]

    trie = {}
    for word in all_words:
        cur = trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['#'] = word

    found_words = findWords(board, trie)

    words_by_length = {}

    for word in found_words:
        if len(word) not in words_by_length:
            words_by_length[len(word)] = []
        words_by_length[len(word)].append(word)

    for word_length in words_by_length:
        words_by_length[word_length].sort()

    data = {"board": board, "words": words_by_length, "count": len(found_words)}

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