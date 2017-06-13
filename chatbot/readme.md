# チャットボットプログラム
Pythonの簡易Webサーバーを利用し、Webブラウザ上で実行できるチャットボットアプリを作成する。  
返答はマルコフ連鎖を使用して作文する。

## 実行方法
### サーバ起動
```
# 実行権限の付与
chmod +x cgi-bin/chatbot.py

# サーバ起動
python -m http.server --cgi 8080
```

## ブラウザ表示
```
http://localhost:8080/cgi-bin/chatbot.py
```

## 参考書籍
- http://amzn.to/2sncF6P
