from flask import *
import os

app = Flask(__name__)


@app.route('/')
def index():
    user = "Михаил"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route('/first_page')
def first():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                    <img src = {url_for('static', filename='img/picture.jpg')} width = 100% />
                  </body>
                </html>"""


@app.route('/greeting/<username>')
def greeting(username):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>'''


@app.route('/get_number/<int:number>')
def get_number(number):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Запрошено число {number}!</h1>
                  </body>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''
        <!DOCTYPE html>
            <html lang="en">
            <head>
              <meta charset="UTF-8">
              <title>Login</title>
            </head>
            <body>
            <form action="" method="post">
                <p>
	              <label for="username">Username</label>
	              <input type="text" name="username">
	            </p>
	            <p>
	              <label for="password">Password</label>
	              <input type="password" name="password">
	            </p>
	            <p>
	              <input type="submit">
	            </p>
          </form>
        </body>
        </html>'''
    elif request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        print(username, password)
        return "Форма отправлена"


@app.route('/second/')
def second():
    numbers = [str(i) for i in range(10)]
    return "<BR>".join(numbers)


import json


@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list)


if __name__ == '__main__':
    # app.run(port=8080, host='127.0.0.1')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
