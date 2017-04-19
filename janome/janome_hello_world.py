from janome.tokenizer import Tokenizer

t = Tokenizer()
tokens = t.tokenize('pythonの本を読んだ')

for token in tokens:
    print(token)

# python	名詞,固有名詞,組織,*,*,*,*,*,*
# の	助詞,連体化,*,*,*,*,の,ノ,ノ
# 本	名詞,一般,*,*,*,*,本,ホン,ホン
# を	助詞,格助詞,一般,*,*,*,を,ヲ,ヲ
# 読ん	動詞,自立,*,*,五段・マ行,連用タ接続,読む,ヨン,ヨン
# だ	助動詞,*,*,*,特殊・タ,基本形,だ,ダ,ダ