import sqlite3
from typing import Optional, List

class Database:
    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                date_created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                click_count INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        self.conn.commit()

    def create_shortened_url(self, original_url: str, short_code: str) -> None:
        self.cursor.execute(
            "INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
            (original_url, short_code),
        )
        self.conn.commit()

    def get_original_url(self, short_code: str) -> Optional[str]:
        self.cursor.execute(
            "SELECT original_url FROM urls WHERE short_code = ?", (short_code,)
        )
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def get_all_shortened_urls(self) -> List[dict]:
        self.cursor.execute("SELECT * FROM urls")
        results = self.cursor.fetchall()
        return [
            {
                "id": result[0],
                "original_url": result[1],
                "short_code": result[2],
                "date_created": result[3],
                "click_count": result[4],
            }
            for result in results
        ]

db = Database("snaplink.db")