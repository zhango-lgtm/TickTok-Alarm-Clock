# ⏰ TickTok Alarm Clock

A retro-inspired web alarm clock that refuses to let you go back to sleep. Instead of simply dismissing the alarm, users must complete **five consecutive mini-games** before the alarm can be fully stopped. Performance is tracked, ranked, and compared against other users through a leaderboard and percentile-based statistics page.

Built with **Flask**, **SQLite**, **Pandas**, and **NES.css** for a fun pixel-art style.

---

## Features

* Custom alarm scheduling
* Multiple selectable alarm sounds
* Alarm persistence using session storage
* Optional custom username for leaderboard entries
* Five sequential mini-games
* Percentile-based performance statistics
* Global leaderboard stored in SQLite
* Correct / incorrect sound effects
* Retro UI powered by **NES.css**

---

## Mini-Games

### 1. Moving Target Challenge

Click a moving button **10 times** while avoiding fake penalty buttons.

### 2. Math Sprint

Solve **10 random math problems** within **45 seconds**.

### 3. Reverse Typing

Type a sentence **backwards** exactly as shown.

### 4. Number Guessing

Guess a random number from **1–20** within **5 attempts**.

### 5. Rapid Click Challenge

Click a target bar **100 times in 30 seconds**.

If a game is failed, it automatically restarts until completed.

---

## Screenshots

### Homepage

Add a screenshot here

### Mini-Games

Add a screenshot here

### Results & Leaderboard

Add a screenshot here

---

## How It Works

1. Open the homepage.
2. Enter a leaderboard name (or stay anonymous).
3. Set an alarm time and choose a sound.
4. When the alarm triggers, a looping alert sound begins.
5. Complete all five mini-games in order.
6. Submit your results. The alarm stops and your statistics are saved.
7. View your **percentile rankings**, **best game**, and **leaderboard position** on the results page.

---

## Tech Stack

| Technology                  | Purpose                                |
| --------------------------- | -------------------------------------- |
| **Flask**                   | Backend web framework                  |
| **SQLite**                  | Persistent leaderboard storage         |
| **Pandas**                  | Statistics and percentile calculations |
| **HTML / CSS / JavaScript** | Frontend and game logic                |
| **NES.css**                 | Retro pixel-art styling                |
| **Railway**                 | Deployment platform                    |

---

## Project Structure

```
TickTok-Alarm-Clock/
├── main.py
├── requirements.txt
├── ticktok.db
├── static/
│   └── styles.css
└── templates/
    ├── homepage.html
    ├── fivetests.html
    └── stats.html
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/TickTok-Alarm-Clock.git
cd TickTok-Alarm-Clock
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

Open **http://127.0.0.1:3000** in your browser.

---

## Statistics System

After each run, TickTok calculates:

* Alarm reaction percentile
* Percentile for each mini-game
* Total completion time
* Overall leaderboard rank
* Best-performing game

All runs are stored in **SQLite**, allowing the leaderboard to persist across sessions.

---

## Deployment

Try TickTok here:

**[https://your-app-name.up.railway.app](https://alert-cooperation-production.up.railway.app/)**

