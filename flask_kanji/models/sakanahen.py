from flask_kanji import db

class Sakanahen(db.Model):
    __tablename__ = 'sakanahen3'
    kanji = db.Column(db.String(4), primary_key=True)
    yomi = db.Column(db.String(32))
    level = db.Column(db.Integer)
    
    def __init__(self, kanji=None, yomi=None, level=None):
        self.kanji = kanji
        self.yomi = yomi
        self.level = level