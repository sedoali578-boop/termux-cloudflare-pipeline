import os
import sqlite3
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
DB_PATH = os.path.expanduser("~/payload_audit.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payloads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_ip TEXT,
            user_agent TEXT,
            payload_data TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/", methods=["POST", "GET"])
def handle_payload():
    init_db()
    if request.method == "POST":
        data = request.json or request.form.to_dict() or request.data.decode("utf-8")
        client_ip = request.headers.get("CF-Connecting-IP", request.remote_addr)
        ua = request.headers.get("User-Agent", "Unknown")
        now = str(datetime.datetime.now())

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO payloads (timestamp, source_ip, user_agent, payload_data) VALUES (?, ?, ?, ?)",
            (now, client_ip, ua, str(data))
        )
        conn.commit()
        conn.close()

        print(f"[+] Secure Payload Logged Successfully at {now} from IP: {client_ip}")
        return jsonify({
            "status": "success",
            "audit": "logged_in_termux_engine",
            "client_ip": client_ip,
            "timestamp": now
        }), 200
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM payloads;")
    count = cursor.fetchone()[0]
    conn.close()

    return f"🚀 Ultimate Termux-Cloudflare Engine is Online! Total Logged Payloads: {count}", 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7771)
