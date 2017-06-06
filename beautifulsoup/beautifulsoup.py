from bs4 import BeautifulSoup
import requests

url = "http://qiita.com/"
res = requests.get(url)
if not res.status_code == requests.codes.ok:
    print("Error")
    exit(1)

# HTML情報を取得
soup = BeautifulSoup(res.text, "lxml")
print(soup.h1.text)