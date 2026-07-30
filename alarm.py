from flask import Flask, request, render_template, redirect, url_for, session
import statistics
import pandas as pd

app = Flask(__name__)
app.secret_key = "randomsecretkey123456"
DATABASE = "sqlite:///ticktok.db"

user_stats = {}


@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/fivetests", methods=["GET","POST"])
def fivetests():
    input_username = request.form.get("user_name", "")
    selected_sound = request.form.get("alarm-sound", "")
    alarm_react_secs = request.form.get("time-to-finish", 0)
    return render_template("fivetests.html", audio_filename=selected_sound, alarm_react_secs=alarm_react_secs, input_username=input_username)


@app.route("/submit_timings", methods=["POST"])
def submit_game_times():
    alarm_react = int(request.form.get("alarm_react", 0))
    g1 = int(request.form.get("g1", 0))
    g2 = int(request.form.get("g2", 0))
    g3 = int(request.form.get("g3", 0))
    g4 = int(request.form.get("g4", 0))
    g5 = int(request.form.get("g5", 0))
    user_name = request.form.get("user_name", "Anonymous")

    total_time = g1 + g2 + g3 + g4 + g5

    df = pd.read_sql("SELECT MAX(run_id) as max_id FROM runs", con=DATABASE)
    new_run_id = 1 if df["max_id"][0] is None else int(df["max_id"][0]) + 1
    
    new_row = pd.DataFrame([{
        "run_id": new_run_id,
        "user_name": user_name,
        "alarm_react": alarm_react,
        "g1": g1,
        "g2": g2,
        "g3": g3,
        "g4": g4,
        "g5": g5,
        "total_time": total_time
    }])
    new_row.to_sql("runs", con=DATABASE, if_exists="append", index=False)

    return redirect(
        url_for("stats",
        alarm_react=alarm_react,
        user_name=user_name,
        g1=g1, g2=g2, g3=g3, g4=g4, g5=g5,
        total_time=total_time
    ))


@app.route("/stats")
def stats():
    alarm_react = int(request.args.get("alarm_react", 0))
    g1 = int(request.args.get("g1", 0))
    g2 = int(request.args.get("g2", 0))
    g3 = int(request.args.get("g3", 0))
    g4 = int(request.args.get("g4", 0))
    g5 = int(request.args.get("g5", 0))
    user_name = request.args.get("user_name", "Anonymous")
    total_time = int(request.args.get("total_time", 0))

    all_records = pd.read_sql("SELECT * FROM runs", con = DATABASE)

    def get_better_percent(user_time, column):
        total_num = all_records.shape[0]
        if total_num < 2:
            return 100
        count_worser_time = all_records[all_records[column] > user_time].shape[0]
        return round((count_worser_time / (total_num-1)) * 100)

    pAlarm = get_better_percent(alarm_react, "alarm_react")
    pG1 = get_better_percent(g1, "g1")
    pG2 = get_better_percent(g2, "g2")
    pG3 = get_better_percent(g3, "g3")
    pG4 = get_better_percent(g4, "g4")
    pG5 = get_better_percent(g5, "g5")

    leaderboard_dt = pd.read_sql("SELECT user_name, total_time FROM runs ORDER BY total_time ASC", con=DATABASE)
    leaderboard = leaderboard_dt.to_dict("records")
    rank_list = []
    for data in leaderboard:
        single = data["total_time"]
        rank_list.append(single)
    user_rank = rank_list.index(total_time) + 1

    user_game_data = [
        ("Game 1", g1, pG1),
        ("Game 2", g2, pG2),
        ("Game 3", g3, pG3),
        ("Game 4", g4, pG4),
        ("Game 5", g5, pG5)
    ]

    user_best_game = ""
    user_best_p = -10000

    for game, time, percent in user_game_data:
        if percent > user_best_p:
            user_best_p = percent
            user_best_game = game
        
    return render_template(
        "stats.html",
        alarm_react=alarm_react,
        user_name=user_name,
        g1=g1,
        g2=g2,
        g3=g3,
        g4=g4,
        g5=g5,
        total_time=total_time,
        alarm_percentile=pAlarm,
        g1_percentile=pG1,
        g2_percentile=pG2,
        g3_percentile=pG3,
        g4_percentile=pG4,
        g5_percentile=pG5,
        rank=user_rank,
        best_game=user_best_game,
        best_percentile=user_best_p,
        leaderboard=leaderboard
    )
        



if __name__ == "__main__":
    app.run(debug=True)





