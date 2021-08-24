from flask import Flask
from flask import request
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)


@app.route('/db')
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

# @app.route("/flask/v1/status")
# def ownCall():
#      return {
#         "username": "masum",
#         "theme": "user.theme",
#         "image": "url_for(user_image, filename=user.image)",
#     }

@app.route("/flask/v1/status", methods=['GET', 'POST'])
def routeTwo():
    r = request.get(
    'https://www.google.com',
    )
    return r
