from flask import Flask, render_template, request
app = Flask(__name__)

results_title = ["戦いに破れ机の上で爆睡", "逃げてPythonかたかた。", "お布団に包まれ...。", "踊り狂ってふらっふらふら　フラミンゴ", "逆立ちっ！できないっ！", "ぬこぬこぬこぬこ"]
results_sentence = ["あーるんは無理して戦ったので机の上で爆睡しました。３時間後に目が覚めて絶望してそのまま寝ました。",
                    "楽しかったので眠気には負けず、PythonかたかたしてたらこのWebアプリが完成しました。宿題は終わっていません。",
                    "大人しくそのまま寝たあーるんは、心地の良い夢の世界へ旅立ちました。ついでに朝まで目覚めることはありませんでした。ちゃんちゃん。",
                    "バレエのくるくる回るのがしたくてやってみましたが、目が回りました。ついでに捻挫もしました。あーるんに運動をさせてはいけません。",
                    "昔どっかの本で逆立ちしたら落ち着くって聞いたので逆立ちしました。できませんでした。頭に血が回ってふらっふらふら　フラミンゴ",
                    "にゃーにゃにゃにゃ、にゃーにゃーふにゃにゃ。にゃーごにゃ、にゃにゃにゃーーーーーにゃ。にゃっにゃ。"]
key_list = ["fight", "escape", "sleep", "dance", "handstand", "cat"]

@app.route("/")
def index():
    title = None
    sentence = None

    key = request.args.get("action_key","")
    if key in key_list:
        title = results_title[key_list.index(key)]
        sentence = results_sentence[key_list.index(key)]

    return render_template("index.html", methods=['POST','GET'], title=title, sentence=sentence)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')