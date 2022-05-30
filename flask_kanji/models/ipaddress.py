from flask_kanji import db


class Ipaddress(db.Model):
    __tablename__ = 'ipaddress'
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(64), nullable=False)

    def __init__(self, ip):
        self.ip = ip
