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
