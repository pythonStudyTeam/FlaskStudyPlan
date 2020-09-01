'''
Created on 2020/08/29

@author: orimako1013
'''

"""
    eclipseなら「ウィンドウ」→「設定」→「PyDev」→「インタープリター」→「Pythonインタープリター」
    に行き、右真ん中よりちょい下あたりの「Manage with pip」(もしかしたら「Install/Uninstall with pip」かも)から、
    「command to execute」に「install flask」と打つと自動でインストールしてくれる。
    あるいは、コマンドラインに単に「pip install flask」と打つだけでもインストールできる。(pipコマンドが見つからない場合は環境変数を設定する必要がある)

    インストールしたらこの.pyファイルは実行できる。実行するとサーバが起動した状態になるので、
    お好きなブラウザでhttp://localhost:5000/(URLパターン)と打ってリクエストすれば任意の関数が起動するはず。
    localhostじゃなくて127.0.0.1でもいける。ポート番号の5000は一番下の方で適当に指定してるだけなので変えられる。
    ブログ記事とか見てると8888とかがいいのかもしれないけど、Jupyter labのポート番号と被ってたので変えちゃいました。。。

    ここの内容自体はサーバが起動したままでも書き換えられるからサクサク変えて実験できて便利。
    インタープリタ使うぐらいだし、リクエストごとに読み取ってるのかしら。便利だけど実務だと更新はどういう手順で行うんだろう。

    eclipse + PyDevの環境だとエラーが出るけどコマンドラインで実行すればちゃんと実行できる。
    この環境だとなんでエラーが出ちゃうのかはよくわかんないけど。。。ecpliseでpython書くのはあんまり向いてない説はあるのかも？
"""

from flask import *

# eclipse + PyDevだとこの辺で何故かエラーが出る。。。
# コマンドラインでこの.pyを実行すればちゃんと実行できて、サーバが立ち上がる
app = Flask(__name__)

# ここでURLパターンを指定できる
@app.route("/")
def main():
    # 文字列をreturnするとこの文字列を表示するだけの単純なレスポンスが返る
    return "route page"

@app.route("/hello")
def hello():
    return "hello, world"

# <>で囲んで、同名の変数を引数として渡すと、異なるURLパターンでもリクエストを受け取れる。
# 例えば、http://localhost:5000/hiorikasaでnameにorikasaが格納されて、
# 「hi, orikasa」と表示される。
@app.route("/hi<name>")
def hi(name):
    return f"hi, {name}"

# メソッドを指定できる。デフォルトはGETのみ
@app.route("/test", methods=["GET", "POST"])
def exp():
    # eclipseだとなんかエラーになるけどこれもコマンドラインならいける。
    # request.formでフォームのデータも受け取れるっぽい。
    mtd = request.method
    return f"method: {mtd}"

@app.route("/form")
def form():
    return """
    整数を入力してね
    <form action="/req" method="POST">
    <input name="num" />
    </form>"""

@app.route("/req", methods=["POST"])
def showInt():
    # フォームの入力値はrequest.formで取得できる。辞書の形になっているので、
    # name属性をキーとすれば、valueを取得できる。これでデータも受け取れるぜ！
    num = request.form["num"]
    return f"入力したのは{num}です"

@app.route("/staticpage")
def staticPage():
    # ルートディレクトリ配下にtemplatesフォルダを用意し、その中にhtmlを作って
    # render_templateで指定して返却すれば、htmlを返せる
    return render_template("staticpage.html")

@app.route("/dynamicpage/<humanname>")
def dynamicPage(humanname):
    # html内に{{変数名}}で指定した変数名をキーにして値を渡せば、
    # 動的なページを作ることができる。
    return render_template("dynamicpage.html", name=humanname)


# メイン関数が実行されたら、デバッグモードで、0.0.0.0をホストにし、5000をポート番号として、
# スレッド処理でwebアプリケーションを実行し始める、という意味かな多分。この記述は多分必ず必要。
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000", threaded=True)