import sqlite3

conn = sqlite3.connect(
    "database/scribexa.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS lectures(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    transcript TEXT,
    notes TEXT,
    flashcards TEXT,
    mcqs TEXT
)
""")

conn.commit()

# Save Function
def save_lecture(
    filename,
    transcript,
    notes,
    flashcards,
    mcqs
):

    cursor.execute("""
    INSERT INTO lectures
    (
        filename,
        transcript,
        notes,
        flashcards,
        mcqs
    )
    VALUES(?,?,?,?,?)
    """,
    (
        filename,
        transcript,
        notes,
        flashcards,
        mcqs
    ))

    conn.commit()