from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://blog.db'  # сюда можно добавлять другие базы данных

db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Article %r' % self.id  # когда мы вибраем какой либо объект из значений выше выдается сам объект и id


@app.route('/robots.txt')
def robots():
    return ('User-Agent: *')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/support')
def support():
    return render_template('support.html')



@app.route('/sign up')
def sign_up():
    return render_template('sign_up')


@app.route('/access')
def access():
    return render_template('access.html')


if __name__ == "__main__":
    app.run(debug=True)



