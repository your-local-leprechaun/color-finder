import os
from datetime import date

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    today = date.today().isoformat()
    return render_template("index.html", today=today)


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
