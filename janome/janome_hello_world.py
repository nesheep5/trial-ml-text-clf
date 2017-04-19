from janome.tokenizer import Tokenizer

t = Tokenizer()
tokens = t.tokenize('pythonの本を読んだ')

for token in tokens:
    print(token)