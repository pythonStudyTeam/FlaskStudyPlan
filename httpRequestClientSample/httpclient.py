'''
Created on 2020/08/31

@author: orimako1013
'''

# ↓Rakuten Rapid APIとかいう楽天が提供してるAPIプラットフォームから、今の為替を取得するAPIを叩く
# https://api.rakuten.net/fyhao/api/currency-exchange/endpoints

# HTTPリクエストは標準ライブラリであるurllibを使ってみた。単純なやつならこれで十分かも。
# ↓参考としての公式ドキュメントとQiita記事。Pythonは公式ドキュメントが丁寧だなぁ。
# https://docs.python.org/ja/3/howto/urllib2.html
# https://qiita.com/hoto17296/items/8fcf55cc6cd823a18217
import urllib.request

# URL
url = "https://currency-exchange.p.rapidapi.com/exchange"

# ヘッダ。APIキーについては多分人によって違うのでそれを入れないとうまくいかない。
# 試してみる場合はRakuten Rapid APIに会員登録(無料なはず)
# 自分でGoogle Apps Scriptとかでくそ簡単なwebアプリを作ってもよかったけど面倒だったし、ヘッダ読み取れなさそうだったし…
headers = {"x-rapidapi-host" : "currency-exchange.p.rapidapi.com",
          "x-rapidapi-key": "xxxxxxxxxxxxx"}

# APIに渡すデータ本文。GETで送るのでこれをクエリにして送る
params = {"q": "1.0",
          "from": "USD",
          "to": "JPY"}

# データを基にクエリ文字列を作成する。
query = urllib.parse.urlencode(params)

# URLとヘッダを渡してリクエストオブジェクト作成
# byte型でdata引数を渡すとPOSTリクエストで送れる
req = urllib.request.Request(url=f"{url}?{query}", headers=headers)

# HTTPErrorとURLErrorが送出される可能性がある。
# また、リソースのクローズが必要なのでwithを使う
# urlopenでHTTPリクエストを送ってレスポンスを取得できる。
try:
    with urllib.request.urlopen(req) as res:
        # レスポンス本文を取得
        body = res.read()
except urllib.error.HTTPError as err:
    print("HTTPError!")
    print(err.code)
except urllib.error.URLError as err:
    print("URLError!")
    print(err.reason)

# レスポンスの本文はbyte型で返ってくるので、UTF-8ででコードする。
print(body.decode("utf-8"))


# Rakuten Rapid APIへの会員登録なんてしゃらくせえ！！という若人のための
# 阿部寛のHPを取得するコードだよ！！ HTMLの構造が単純なので楽しいですよ。
'''
url = "http://abehiroshi.la.coocan.jp/top.htm"
req = urllib.request.Request(url=url)
try:
    with urllib.request.urlopen(req) as res:
        body = res.read()
except urllib.error.HTTPError as err:
    print("HTTPError!")
    print(err.code)
except urllib.error.URLError as err:
    print("URLError!")
    print(err.reason)

print(body.decode("S-JIS"))
'''