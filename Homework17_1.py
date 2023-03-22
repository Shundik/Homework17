from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registration.db'
app.config['SQLALCHEMY_TRACK_MADIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tel = db.Column(db.String(100), nullable=False)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def hello_world():
    return render_template('about.html')


@app.route('/registration')
def registration():
    return render_template('registration.html')


@app.route('/snowboarding', methods=['POST', 'GET'])
def snowboarding():
    if request.method == "POST":
        tel = request.form['tel']
        name = request.form['name']
        article = Article(name=name, tel=tel)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/registration')
        except:
            return 'Ошибка'
    else:
        return render_template('snowboarding.html')


@app.route('/index', methods=['POST', 'GET'])
def about():
    if request.method == "POST":
        tel = request.form['tel']
        name = request.form['name']
        article = Article(name=name, tel=tel)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/registration')
        except:
            return 'Ошибка'
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
