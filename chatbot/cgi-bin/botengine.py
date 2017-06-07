from janome.tokenizer import Tokenizer
import os, re, json, random

dict_file = "chatbot-data.json"
dic = {}
tokenizer = Tolenizer() # janome

# 辞書に単語を記録する
def register_dic(words):
    global dic
    if len(words) == 0: return
    tmp = ["@"]
    for i in words:
        word = i.surface
        if word in ["", "\r\n", "\n"]: continue
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word in ["。", "？"]:
            tmp = ["@"]
            continue

    # 辞書を更新する毎にファイルへ保存
    json.dump(dic, open(dict_file, "w", encoding="utf-8"))  