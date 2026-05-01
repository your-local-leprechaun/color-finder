import os
from datetime import date

import db
from flask import Flask, render_template
from routes.auth import auth_bp, oauth

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-change-me")

oauth.init_app(app)
app.register_blueprint(auth_bp)

model = db.get_model()


@app.route("/")
def index():
    today = date.today().isoformat()
    return render_template("index.html", today=today)


@app.route("/health")
def health():
    try:
        model.db.collection("challenges").limit(1).get()
        db_status = "ok"
    except Exception as e:
        db_status = str(e)
    return {"status": "ok", "db": db_status}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host="0.0.0.0", port=port)
