from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/news")
def news():
    return "欢迎来到百度新闻首页"

print("在app_demo01文件中")
print(__name__)

if __name__ == "__main__":
    print(__name__)
    app.run(debug=True, host="0.0.0.0")
