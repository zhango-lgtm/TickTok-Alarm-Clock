# ⏰ TickTok Alarm Clock

A retro-inspired web alarm clock that refuses to let you go back to sleep. Instead of simply dismissing the alarm, users must complete **five consecutive mini-games** before the alarm can be fully stopped. Performance is tracked, ranked, and compared against other users through a leaderboard and percentile-based statistics page.

Built with **Flask**, **SQLite**, **Pandas**, and **NES.css** for a fun pixel-art style.

---

## Features

- Create and manage custom alarms
- Session-based alarm storage so alarms persist while navigating between pages
- Choose from multiple custom alarm sounds
- Optional custom alarm labels
- Optional leaderboard username (or remain anonymous)
- Five wake-up mini-games:
  1. Chase a moving target while avoiding fake buttons
  2. Solve 10 random arithmetic questions against the clock
  3. Type a randomly selected sentence backwards
  4. Guess a random number within five attempts
  5. Click a target 100 times before time expires
- Automatic retry for failed challenge games
- Tracks alarm reaction time and each game's completion time
- Personal statistics page showing percentiles and best-performing game
- Persistent Top 10 leaderboard ranked by total completion time
- Retro NES.css-inspired interface

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

1. Enter an optional leaderboard name (or leave it blank to appear as **Anonymous**).
2. Create an alarm by choosing:
   - a time,
   - an optional label,
   - and a custom alarm sound.
3. Your scheduled alarms are saved in session storage and remain available while navigating the site.
4. When the alarm triggers:
   - the selected audio begins looping,
   - your alarm reaction time starts being recorded,
   - and you're prompted to dismiss the alarm.
5. Dismissing the alarm launches five wake-up mini-games.
6. Complete every challenge in order. If you fail a timed challenge, it automatically restarts.
7. After finishing all five games:
   - the alarm sound stops,
   - your reaction time and game times are submitted,
   - your leaderboard ranking is updated,
   - and a statistics page displays your performance compared with other users.
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

