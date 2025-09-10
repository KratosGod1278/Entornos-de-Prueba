from flask import Flask, render_template
import pyodbc

app = Flask(__name__, static_folder=".", static_url_path="")

# Conexión a SQL Server
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=GameHubDB;"
    "Trusted_Connection=yes;"
)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/games")
def games():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 10 Nombre, Genero FROM Juegos")
    rows = cursor.fetchall()
    conn.close()
    return {"games": [{"nombre": r[0], "genero": r[1]} for r in rows]}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
