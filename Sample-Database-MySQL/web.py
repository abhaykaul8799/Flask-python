from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = '8799'
app.config["MYSQL_HOST"] = 'localhost'
app.config["MYSQL_DB"] = 'main'
app.config["MYSQL_CURSORCLASS"] = 'DictCursor' 

mysql = MySQL(app)

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    # cur.execute("INSERT INTO example VALUES (3,'Abhi')")
    # cur.execute("INSERT INTO example VALUES (4,'Luminous')")
    # mysql.connection.commit()

    cur.execute("SELECT * from example")
    results = cur.fetchall()
    print(results)

    return results[0]['Name']

if __name__ == "__main__":
    app.run(debug=True)