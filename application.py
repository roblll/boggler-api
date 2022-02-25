from flask import Flask, jsonify, request
application = Flask(__name__)
from PIL import Image
import base64
import os
import random
import tensorflow as tf
import numpy as np
from tensorflow import keras

img_height = 180
img_width = 180
class_names = ['A_D', 'A_L', 'A_R', 'A_U', 'B_D', 'B_L', 'B_R', 'B_U', 'C_D', 'C_L', 'C_R', 'C_U', 'D_D', 'D_L', 'D_R', 'D_U', 'E_D', 'E_L', 'E_R', 'E_U', 'F_D', 'F_L', 'F_R', 'F_U', 'G_D', 'G_L', 'G_R', 'G_U', 'H_H', 'H_V', 'I_H', 'I_V', 'J_D', 'J_L', 'J_R', 'J_U', 'K_D', 'K_L', 'K_R', 'K_U', 'L_D', 'L_L', 'L_R', 'L_U', 'M_D', 'M_L',
               'M_R', 'M_U', 'N_D', 'N_L', 'N_R', 'N_U', 'O_H', 'O_V', 'P_D', 'P_L', 'P_R', 'P_U', 'Q_D', 'Q_L', 'Q_R', 'Q_U', 'R_D', 'R_L', 'R_R', 'R_U', 'S_H', 'S_V', 'T_D', 'T_L', 'T_R', 'T_U', 'U_D', 'U_L', 'U_R', 'U_U', 'V_D', 'V_L', 'V_R', 'V_U', 'W_D', 'W_L', 'W_R', 'W_U', 'X_H', 'X_V', 'Y_D', 'Y_L', 'Y_R', 'Y_U', 'Z_D', 'Z_L', 'Z_R', 'Z_U']
model = tf.keras.models.load_model('model_03')

@application.route('/api', methods=['POST'])
def api():
    input_json = request.get_json(force=True)['file']
    input_json += "=" * ((4 - len(input_json) % 4) % 4)
    random_hash = "%032x" % random.getrandbits(128)
    im_name = f'{random_hash}.jpeg'
    decoded_image = open(im_name, 'wb')
    decoded_image.write(base64.b64decode((input_json)))
    decoded_image.close()

    im = Image.open(im_name)

    width, height = im.size
    w, h = width, height

    os.remove(decoded_image.name)

    im01 = im.crop((0, 0, w * .25, h * .25))
    im02 = im.crop((w * .25, 0, w * .5, h * .25))
    im03 = im.crop((w * .5, 0, w * .75, h * .25))
    im04 = im.crop((w * .75, 0, w, h * .25))

    im05 = im.crop((0, h * .25, w * .25, h * .5))
    im06 = im.crop((w * .25, h * .25, w * .5, h * .5))
    im07 = im.crop((w * .5, h * .25, w * .75, h * .5))
    im08 = im.crop((w * .75, h * .25, w, h * .5))

    im09 = im.crop((0, h * .5, w * .25, h * .75))
    im10 = im.crop((w * .25, h * .5, w * .5, h * .75))
    im11 = im.crop((w * .5, h * .5, w * .75, h * .75))
    im12 = im.crop((w * .75, h * .5, w, h * .75))

    im13 = im.crop((0, h * .75, w * .25, h))
    im14 = im.crop((w * .25, h * .75, w * .5, h))
    im15 = im.crop((w * .5, h * .75, w * .75, h))
    im16 = im.crop((w * .75, h * .75, w, h))

    im01.save(f'./{random_hash}-01.jpg')
    im01 = keras.preprocessing.image.load_img(
        f'./{random_hash}-01.jpg', target_size=(img_height, img_width))
    im01 = keras.preprocessing.image.img_to_array(im01)
    im01 = tf.expand_dims(im01, 0)
    p01 = model.predict(im01)
    s01 = tf.nn.softmax(p01[0])
    r01 = f'{class_names[np.argmax(s01)][0]}'.lower()
    os.remove(f'./{random_hash}-01.jpg')

    im02.save(f'./{random_hash}-02.jpg')
    im02 = keras.preprocessing.image.load_img(
        f'./{random_hash}-02.jpg', target_size=(img_height, img_width))
    im02 = keras.preprocessing.image.img_to_array(im02)
    im02 = tf.expand_dims(im02, 0)
    p02 = model.predict(im02)
    s02 = tf.nn.softmax(p02[0])
    r02 = f'{class_names[np.argmax(s02)][0]}'.lower()
    os.remove(f'./{random_hash}-02.jpg')

    im03.save(f'./{random_hash}-03.jpg')
    im03 = keras.preprocessing.image.load_img(
        f'./{random_hash}-03.jpg', target_size=(img_height, img_width))
    im03 = keras.preprocessing.image.img_to_array(im03)
    im03 = tf.expand_dims(im03, 0)
    p03 = model.predict(im03)
    s03 = tf.nn.softmax(p03[0])
    r03 = f'{class_names[np.argmax(s03)][0]}'.lower()
    os.remove(f'./{random_hash}-03.jpg')

    im04.save(f'./{random_hash}-04.jpg')
    im04 = keras.preprocessing.image.load_img(
        f'./{random_hash}-04.jpg', target_size=(img_height, img_width))
    im04 = keras.preprocessing.image.img_to_array(im04)
    im04 = tf.expand_dims(im04, 0)
    p04 = model.predict(im04)
    s04 = tf.nn.softmax(p04[0])
    r04 = f'{class_names[np.argmax(s04)][0]}'.lower()
    os.remove(f'./{random_hash}-04.jpg')

    im05.save(f'./{random_hash}-05.jpg')
    im05 = keras.preprocessing.image.load_img(
        f'./{random_hash}-05.jpg', target_size=(img_height, img_width))
    im05 = keras.preprocessing.image.img_to_array(im05)
    im05 = tf.expand_dims(im05, 0)
    p05 = model.predict(im05)
    s05 = tf.nn.softmax(p05[0])
    r05 = f'{class_names[np.argmax(s05)][0]}'.lower()
    os.remove(f'./{random_hash}-05.jpg')

    im06.save(f'./{random_hash}-06.jpg')
    im06 = keras.preprocessing.image.load_img(
        f'./{random_hash}-06.jpg', target_size=(img_height, img_width))
    im06 = keras.preprocessing.image.img_to_array(im06)
    im06 = tf.expand_dims(im06, 0)
    p06 = model.predict(im06)
    s06 = tf.nn.softmax(p06[0])
    r06 = f'{class_names[np.argmax(s06)][0]}'.lower()
    os.remove(f'./{random_hash}-06.jpg')

    im07.save(f'./{random_hash}-07.jpg')
    im07 = keras.preprocessing.image.load_img(
        f'./{random_hash}-07.jpg', target_size=(img_height, img_width))
    im07 = keras.preprocessing.image.img_to_array(im07)
    im07 = tf.expand_dims(im07, 0)
    p07 = model.predict(im07)
    s07 = tf.nn.softmax(p07[0])
    r07 = f'{class_names[np.argmax(s07)][0]}'.lower()
    os.remove(f'./{random_hash}-07.jpg')

    im08.save(f'./{random_hash}-08.jpg')
    im08 = keras.preprocessing.image.load_img(
        f'./{random_hash}-08.jpg', target_size=(img_height, img_width))
    im08 = keras.preprocessing.image.img_to_array(im08)
    im08 = tf.expand_dims(im08, 0)
    p08 = model.predict(im08)
    s08 = tf.nn.softmax(p08[0])
    r08 = f'{class_names[np.argmax(s08)][0]}'.lower()
    os.remove(f'./{random_hash}-08.jpg')

    im09.save(f'./{random_hash}-09.jpg')
    im09 = keras.preprocessing.image.load_img(
        f'./{random_hash}-09.jpg', target_size=(img_height, img_width))
    im09 = keras.preprocessing.image.img_to_array(im09)
    im09 = tf.expand_dims(im09, 0)
    p09 = model.predict(im09)
    s09 = tf.nn.softmax(p09[0])
    r09 = f'{class_names[np.argmax(s09)][0]}'.lower()
    os.remove(f'./{random_hash}-09.jpg')

    im10.save(f'./{random_hash}-10.jpg')
    im10 = keras.preprocessing.image.load_img(
        f'./{random_hash}-10.jpg', target_size=(img_height, img_width))
    im10 = keras.preprocessing.image.img_to_array(im10)
    im10 = tf.expand_dims(im10, 0)
    p10 = model.predict(im10)
    s10 = tf.nn.softmax(p10[0])
    r10 = f'{class_names[np.argmax(s10)][0]}'.lower()
    os.remove(f'./{random_hash}-10.jpg')

    im11.save(f'./{random_hash}-11.jpg')
    im11 = keras.preprocessing.image.load_img(
        f'./{random_hash}-11.jpg', target_size=(img_height, img_width))
    im11 = keras.preprocessing.image.img_to_array(im11)
    im11 = tf.expand_dims(im11, 0)
    p11 = model.predict(im11)
    s11 = tf.nn.softmax(p11[0])
    r11 = f'{class_names[np.argmax(s11)][0]}'.lower()
    os.remove(f'./{random_hash}-11.jpg')

    im12.save(f'./{random_hash}-12.jpg')
    im12 = keras.preprocessing.image.load_img(
        f'./{random_hash}-12.jpg', target_size=(img_height, img_width))
    im12 = keras.preprocessing.image.img_to_array(im12)
    im12 = tf.expand_dims(im12, 0)
    p12 = model.predict(im12)
    s12 = tf.nn.softmax(p12[0])
    r12 = f'{class_names[np.argmax(s12)][0]}'.lower()
    os.remove(f'./{random_hash}-12.jpg')

    im13.save(f'./{random_hash}-13.jpg')
    im13 = keras.preprocessing.image.load_img(
        f'./{random_hash}-13.jpg', target_size=(img_height, img_width))
    im13 = keras.preprocessing.image.img_to_array(im13)
    im13 = tf.expand_dims(im13, 0)
    p13 = model.predict(im13)
    s13 = tf.nn.softmax(p13[0])
    r13 = f'{class_names[np.argmax(s13)][0]}'.lower()
    os.remove(f'./{random_hash}-13.jpg')

    im14.save(f'./{random_hash}-14.jpg')
    im14 = keras.preprocessing.image.load_img(
        f'./{random_hash}-14.jpg', target_size=(img_height, img_width))
    im14 = keras.preprocessing.image.img_to_array(im14)
    im14 = tf.expand_dims(im14, 0)
    p14 = model.predict(im14)
    s14 = tf.nn.softmax(p14[0])
    r14 = f'{class_names[np.argmax(s14)][0]}'.lower()
    os.remove(f'./{random_hash}-14.jpg')

    im15.save(f'./{random_hash}-15.jpg')
    im15 = keras.preprocessing.image.load_img(
        f'./{random_hash}-15.jpg', target_size=(img_height, img_width))
    im15 = keras.preprocessing.image.img_to_array(im15)
    im15 = tf.expand_dims(im15, 0)
    p15 = model.predict(im15)
    s15 = tf.nn.softmax(p15[0])
    r15 = f'{class_names[np.argmax(s15)][0]}'.lower()
    os.remove(f'./{random_hash}-15.jpg')

    im16.save(f'./{random_hash}-16.jpg')
    im16 = keras.preprocessing.image.load_img(
        f'./{random_hash}-16.jpg', target_size=(img_height, img_width))
    im16 = keras.preprocessing.image.img_to_array(im16)
    im16 = tf.expand_dims(im16, 0)
    p16 = model.predict(im16)
    s16 = tf.nn.softmax(p16[0])
    r16 = f'{class_names[np.argmax(s16)][0]}'.lower()
    os.remove(f'./{random_hash}-16.jpg')

    data = {
        "board": [
            [r01, r02, r03, r04],
            [r05, r06, r07, r08],
            [r09, r10, r11, r12],
            [r13, r14, r15, r16],
        ]
    }
    return jsonify(data)

@application.route('/test')
def test():
    print("TEST TEST TEST TEST TEST TEST TEST TEST TEST ")
    
    data = {
        "board": [
            ["a", "b", "c", "d"],
            ["e", "f", "g", "h"],
            ["i", "j", "k", "l"],
            ["m", "n", "o", "p"],
        ]
    }
    return jsonify(data)

@application.errorhandler(404)
def handle_404(e):
    return 'Not Found'