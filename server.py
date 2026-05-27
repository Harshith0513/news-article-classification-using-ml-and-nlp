from flask import Flask, request, render_template
from classifier import predict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index2.html")


@app.route("/classify", methods=["POST"])
def classify():
    news_text = request.form.get("news_article", "")

    category = str(predict(news_text))

    print("category found")
    print("category:", category)

    return category


if __name__ == "__main__":
    app.run()