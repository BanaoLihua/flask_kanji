from flask import jsonify, request, redirect, url_for, render_template, flash, session
from flask_kanji import app
from flask_kanji.models.sakanahen import Sakanahen
from sqlalchemy.sql.expression import func


@app.route('/')
def top():
    return render_template('index.html')


@app.route('/sakanahen')
def sakanahen_top():
    return render_template('sakanahen_top.html')


@app.route('/sakanahen_quiz/<string:level>')
def sakanahen_quiz(level):
    sakanahen_easy = Sakanahen.query.filter(Sakanahen.level == 1).order_by(func.random()).limit(10)
    sakanahen_normal = Sakanahen.query.filter(Sakanahen.level == 2).order_by(func.random()).limit(10)
    sakanahen_hard = Sakanahen.query.filter(Sakanahen.level == 3).order_by(func.random()).limit(10)
    
    if level == 'easy':
       return render_template('sakanahen_quiz.html', data=sakanahen_easy, level=level)
    elif level == 'normal':
       return render_template('sakanahen_quiz.html', data=sakanahen_normal, level=level)
    elif level == 'hard':
       return render_template('sakanahen_quiz.html', data=sakanahen_hard, level=level)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        if request.form.get('username') != app.config['USER_ID']:
            print('ユーザ名が異なります')
        elif request.form.get('password') != app.config['PASSWORD']:
            print('パスワードが異なります')
        else:
            session['logged_in'] = True
            return redirect(url_for('sakanahen_top'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    print("hi")
    return redirect(url_for('sakanahen_top'))

@app.route('/mypage')
def mypage():
    if session['logged_in']:
        return render_template('mypage.html')
    else:
        return redirect(url_for('top'))