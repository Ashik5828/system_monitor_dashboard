import psutil
import sqlite3
import datetime
import os

# Database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "system_monitor.db")

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        cpu_usage REAL,
        memory_usage REAL,
        disk_usage REAL,
        net_sent INTEGER,
        net_recv INTEGER
    )
    """)
    conn.commit()
    conn.close()

# Collect stats
def collect_stats():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    net_io = psutil.net_io_counters()
    net_sent = net_io.bytes_sent
    net_recv = net_io.bytes_recv
    return (timestamp, cpu, memory, disk, net_sent, net_recv)

# Save stats into DB
def save_stats(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO system_stats (timestamp, cpu_usage, memory_usage, disk_usage, net_sent, net_recv) VALUES (?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    stats = collect_stats()
    save_stats(stats)
    print(f"Saved: {stats}")
