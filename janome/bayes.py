import math, sys
from janome.tokenizer import Tokenizer

class BaysianFilter:
    """ベイジアンフィルタ"""
    def __init__(self):
        self words = set() # 出現した単語を全て記録
        self.word_dict = {} # カテゴリごとの単語出現回数を記録
        self.category_dict = {} # カテゴリの出現回数を記録

    # 形態素解析を行う
    def split(self, text):
        result= []
        t = Tokenizer()
        malist = t.tokenize(text)
        for w in malist:
            sf = w.surface
            bf = w.base_form
            if bf =='' or bf =="*": bf = sf
            result.append(bf)

    # 単語とカテゴリを数える処理
    def inc_word(self, word,category):
        # 単語をカテゴリに追加
        if not category in self.word_dict:
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1
        self.words.add(word)

    def inc_category(self, category):
        # カテゴリを加算する
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    # テキストを学習する
    def fit(fit, text, category):
        """テキストの学習"""
        word_list = self.split(text)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(caategory)

        
