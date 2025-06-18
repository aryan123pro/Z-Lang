import sqlite3
import csv

# Connect to SQLite DB
conn = sqlite3.connect('../slanglinker.db')
cur = conn.cursor()

# Drop old slang table
cur.execute('DROP TABLE IF EXISTS slang')

# Create new slang table with 'context'
cur.execute('''
    CREATE TABLE slang (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phrase TEXT NOT NULL,
        meaning TEXT NOT NULL,
        example TEXT,
        context TEXT
    )
''')

# Create submissions table (with context too)
cur.execute('''
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phrase TEXT NOT NULL,
        meaning TEXT NOT NULL,
        example TEXT,
        context TEXT
    )
''')

# Load slang.csv
with open('all_slangs.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        phrase = row.get('Slang', '').strip()
        meaning = row.get('Description', '').strip()
        example = row.get('Example', '').strip()
        context = row.get('Context', '').strip()

        if phrase and meaning:
            cur.execute(
                'INSERT INTO slang (phrase, meaning, example, context) VALUES (?, ?, ?, ?)',
                (phrase, meaning, example, context)
            )

# Save and close
conn.commit()
conn.close()
