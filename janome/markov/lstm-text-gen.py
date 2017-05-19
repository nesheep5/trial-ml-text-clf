from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM
from keras.optimazers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random, sys

# 元となるテキストを読み込む
path = "./text/夏目漱石/吾輩は猫である.txt"
bindata = open(path, "rb").read()
text = bindata.decode("shift_jis")
print('コーパスの長さ：', len(text))

# 一文字ずつバラバラにして文字にIDを振る
chars = sorted(list(set(text)))
print('使われている文字の数:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars)) #文字→ID
indices_char = dict((i, c) for i, c,in enumerate(chars)) #ID→文字

# テキストをmaxlen文字で区切って、その文の次にくる文字を記録する
maxlen = 20
step = 3
sentences = []
next_chars = []
for i in range(0, len(text)) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print("学習する文の数:", len(sentences))

print("テキストをIDベクトルにします...")
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in  enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

# モデルを構築する(LSTM)
