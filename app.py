from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'exampleuser',
    'password': os.environ.get("DB_PASS"),
    'database': 'exampledb'
}

@app.route('/')
def home():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    timestamp = result[0]

    # Render template and inject timestamp
    return render_template('index.html', db_time=timestamp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
