from config.db import get_connection
from dotenv import load_dotenv
import os
import requests
import time
from datetime import datetime

def fetch_data():
    response = requests.get(os.getenv("BLAZE_DOUBLE_URL"))
    return response.json()
    
def insert_row(cursor, row):
    cursor.execute(
        """INSERT INTO 
            blaze_double_data 
                (
                    id, 
                    color, 
                    roll,
                    server_seed,
                    created_at
                ) 
            VALUES 
                (
                    %s, 
                    %s, 
                    %s,
                    %s,
                    %s
                )
            ON CONFLICT (id) DO NOTHING
        """, 
        (
            row["id"], 
            row["color"], 
            row["roll"],
            row["server_seed"],
            row["created_at"]
        )
    ) 
    
def insert_data(data):
    conn = get_connection()
    cursor = conn.cursor()
    for row in data:
        insert_row(cursor, row)
    conn.commit()

def main():
    load_dotenv()
    while True:
        now = datetime.now()
        if now.second == 50:
            newdata = fetch_data()
            insert_data(newdata)
            time.sleep(60)  # Evita que rode várias vezes no segundo 50
        else:
            time.sleep(1)  # Espera 1 segundo antes de verificar de novo

if __name__ == "__main__":
    main()
