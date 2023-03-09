from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost' # replace with your MySQL database host
app.config['MYSQL_USER'] = 'root' # replace with your MySQL database user
app.config['MYSQL_PASSWORD'] = 'manasvikalyan' # replace with your MySQL database password
app.config['MYSQL_DB'] = '`bennett_university1`' # replace with your MySQL database name

mysql = MySQL(app)

@app.route('/registerUser', methods=['POST'])
def register_user():
    # get request data
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']

    # create cursor
    cur = mysql.connection.cursor()

    # check if username already exists
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return jsonify({'message': 'Username already exists'}), 400

    # insert user into database
    cur.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
    mysql.connection.commit()

    # close cursor
    cur.close()

    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/loginUser', methods=['POST'])
def login_user():
    # get request data
    username = request.json['username']
    password = request.json['password']

    # create cursor
    cur = mysql.connection.cursor()

    # check if username and password match
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cur.fetchone()
    if not result:
        return jsonify({'message': 'Invalid username or password'}), 401

    # close cursor
    cur.close()

    return jsonify({'message': 'User logged in successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
