
# Z-Lang🧃 – The Gen-Z Dictionary

I'm **Aryan Doifode** from Mumbai and a CS50 student. Z-Lang is my final project for CS50x — a fun, modern web app that helps people discover and understand Gen Z slang.

## 🧠 What It Does

Z-Lang is like your go-to Gen Z dictionary. You can:

* 🔍 Look up trending slang and see what it actually means
* 🌟 Discover a new **Word of the Day** every day
* ✏️ Submit your own slang suggestions(for review)
* ✅ Admins can review and approve slang into the public dictionary

## 🔧 Tech Stack

* **Flask** – for the backend logic and routing
* **SQLite** – to store all the slangs and submissions
* **HTML/CSS** – for a simple but responsive frontend
* **Python** – for loading csv data into database and etc

## 💡 Why I Built This

I’ve always loved language, memes, and making tools that feel alive also I developed a new interest SQL due to the course. This project gave me the chance to combine it all.

## ✨ Reflection

CS50x as a course has helped me make all my web projects more dynamic and interactive — until now, I only built static websites with no backend. Malan sir has taught the concepts so well that every lecture has left a lasting impression on my brain 😄. This course also sparked a new interest in SQL for me, and I’m definitely looking forward to diving deeper into it!

### 🗃️ Database Schema

Z-Lang uses SQLite database names slanglinker.db with two tables:

```sql
-- Table for approved slang
CREATE TABLE slang (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phrase TEXT NOT NULL,
    meaning TEXT NOT NULL,
    example TEXT,
    context TEXT
);

-- Table for submitted slang waiting for review
CREATE TABLE submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phrase TEXT NOT NULL,
    meaning TEXT NOT NULL,
    example TEXT,
    context TEXT
);
```
    
## 🚀 How to Clone & Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/aryan123pro/z-lang.git
   cd z-lang/slanglinker
   ```

2. **(Optional) Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**  
   ```bash
   flask run
   ```

5. Open your browser and visit:  
   [http://localhost:5000](http://localhost:5000)

---

## 🌍 Deployed Version

Live at: **[https://z-lang.onrender.com](https://z-lang.onrender.com)**

