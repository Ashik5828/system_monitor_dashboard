from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "system_monitor.db")

def get_stats(limit=20):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, cpu_usage, memory_usage, disk_usage FROM system_stats ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route("/")
def index():
    rows = get_stats(20)
    return render_template("index.html", rows=rows)
if __name__ == "__main__":
    app.run(debug=True)
