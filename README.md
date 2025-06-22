Here’s a clean, humanized, and not-too-technical `README.md` for your **Z-Lang** project:

---

# Z-Lang🧃 – The Gen Z Dictionary

I'm **Aryan Doifode** from Mumbai and a CS50 student. Z-Lang is my final project — a fun, modern web app that helps people discover and understand Gen Z slang.

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
* **Python** – for all the brains behind the scenes

## 💡 Why I Built This

I’ve always loved language, memes, and making tools that feel alive. This project gave me the chance to combine it all — and CS50 gave me the confidence to ship it

Feel free to explore it, use it, or even submit some new slang of your own. Thanks for stopping by! 🚀

### 🗃️ Database Schema

Z-Lang uses SQLite with two tables:

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

---
