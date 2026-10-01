#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import json
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "app.db"
FRONTEND = BASE_DIR / "index.html"


def initialize_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS counter "
            "(id INTEGER PRIMARY KEY, visits INTEGER NOT NULL)"
        )
        connection.execute(
            "INSERT OR IGNORE INTO counter (id, visits) VALUES (1, 0)"
        )


def record_visit():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute(
            "UPDATE counter SET visits = visits + 1 WHERE id = 1"
        )
        return connection.execute(
            "SELECT visits FROM counter WHERE id = 1"
        ).fetchone()[0]


class ApplicationHandler(BaseHTTPRequestHandler):
    def send_content(self, status, content_type, body):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_content(
                200,
                "text/html; charset=utf-8",
                FRONTEND.read_bytes(),
            )
        elif self.path == "/api/visits":
            body = json.dumps({"visits": record_visit()}).encode()
            self.send_content(200, "application/json", body)
        else:
            self.send_content(404, "text/plain", b"Not found\n")


initialize_database()
print("Application running at http://127.0.0.1:8004")
HTTPServer(("127.0.0.1", 8004), ApplicationHandler).serve_forever()
