from ipaddress import ip_address
from flask import jsonify, request, redirect, url_for, render_template, flash, session, request
from flask_kanji import app
from flask_kanji.models.sakanahen import Sakanahen
from flask_kanji.models.tori import Tori
from flask_kanji.models.kemono import Kemono
from flask_kanji.models.kusa import Kusa
from flask_kanji.models.ki import Ki
from flask_kanji.models.ipaddress import Ipaddress
from sqlalchemy.sql.expression import func
from flask_kanji import db


@app.route('/')
def top():
    # ipaddr = Ipaddress(request.remote_addr)
    # db.session.add(ipaddr)
    # db.session.commit()
    return render_template('index.html')
   
@app.route('/selection/<string:type>')
def select_mode(type):
    return render_template('mode_selection.html', type=type)
        
@app.route('/quiz/<string:type>/<string:level>')
def quiz(type, level):
    if type == 'tori':
        quiz_data = get_random_10_rows(Tori, level)
    if type == 'sakana':
        quiz_data = get_random_10_rows(Sakanahen, level)
    if type == 'kemono':
        quiz_data = get_random_10_rows(Kemono, level)
    if type == 'kusa':
        quiz_data = get_random_10_rows(Kusa, level)
    if type == 'ki':
        quiz_data = get_random_10_rows(Ki, level)
    return render_template('quiz.html', data=quiz_data, level=level, type=type)


'''指定されたレベルの漢字と読みを10個ランダムで取得する関数'''
def get_random_10_rows(Kanji_class, level):
    return Kanji_class.query.filter(Kanji_class.level==level).order_by(func.random()).limit(10)