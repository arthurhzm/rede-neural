from config.db import get_connection
from dotenv import load_dotenv
import os
import requests

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
    newdata = fetch_data()
    insert_data(newdata)
    

if __name__ == "__main__":
    main()
