# dummy app.py

from flask import Flask, jsonify, redirect, render_template, request

from modules.weather import get_weather

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", weather=get_weather())
    # return render_template(
    #   "index.html",
    #   weather=get_weather(),
    #   oldie=get_oldie_status(),
    #   space=get_space_card(),
    #   shopping=get_items(),
    #   timers=get_active_timers()
    # )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5020, debug=True)
