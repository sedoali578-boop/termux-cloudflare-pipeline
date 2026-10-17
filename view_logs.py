import sqlite3, os

db_path = os.path.expanduser("~/payload_audit.db")
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, timestamp, source_ip, user_agent, payload_data FROM payloads ORDER BY id DESC LIMIT 5;")
    rows = cursor.fetchall()
    print(f"\n📊 --- Latest {len(rows)} Logged Payloads --- \n")
    for row in rows:
        print(f"🆔 ID: {row[0]} | ⏰ Time: {row[1]} | 🌐 IP: {row[2]}")
        print(f"💻 Agent: {row[3]}")
        print(f"📦 Data: {row[4]}")
        print("=" * 60)
    conn.close()
else:
    print("[!] Audit database is empty or not created yet.")
