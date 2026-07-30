from flask import Flask, request, render_template, redirect, url_for, session
import statistics

app = Flask(__name__)
app.secret_key = "randomsecretkey123456"

user_stats = {}


@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/game", methods=["POST"])
def game():
    alarm_react_secs = request.form.get("time-to-finish", 0)
    selected_sound = request.form.get("alarm-sound", "")

    user_stats["alarm_react"] = int(alarm_react_secs)
    user_stats["sound_file"] = selected_sound

    return redirect(url_for("fivetests"))


@app.route("/fivetests")
def fivetests():
    sound = user_stats.get("sound_file", "")
    return render_template("fivetests.html", audio_filename=sound)


@app.route("/submit_timings", methods=["POST"])
def submit_game_times():
    user_stats["g1"] = int(request.form.get("g1", 0))
    user_stats["g2"] = int(request.form.get("g2", 0))
    user_stats["g3"] = int(request.form.get("g3", 0))
    user_stats["g4"] = int(request.form.get("g4", 0))
    user_stats["g5"] = int(request.form.get("g5", 0))

    return redirect(url_for("stats"))


@app.route("/stats")
def stats():
    return render_template("stats.html")

if __name__ == "__main__":
    app.run(debug=True)