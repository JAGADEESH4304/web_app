from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "admin")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")

# Function to test DB connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        return str(e)

@app.route("/")
def home():
    return jsonify({"message": "Backend API is running!"})

@app.route("/dbtest")
def db_test():
    conn = get_db_connection()
    if isinstance(conn, str):  # If it's an error message
        return jsonify({"error": conn}), 500
    conn.close()
    return jsonify({"message": "Connected to the database successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
