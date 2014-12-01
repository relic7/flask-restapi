from sqlalchemy import Column, Integer, String
from restapi.database Base

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __init__(self, nickname=None, email=None):
        self.nickname = nickname
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class LookletShotList(Base):
    __tablename__ = 'looklet_shot_list'
    id = db.Column(db.Integer, primary_key = True)
    colorstyle = db.Column(db.String(9))
    photodate = db.Column(db.String(10))
    reshoot = db.Column(db.String(1))
    notes = db.Column(db.text)
    timestamp = db.Column(db.String(15))
    username = db.Column(db.String(30))

    def __init__(self, colorstyle=None, photodate=None, reshoot=None, notes=None, timestamp=None, username=None):
        self.colorstyle = colorstyle
        self.photodate  = photodate
        self.reshoot   = reshoot
        self.notes     = notes
        self.timestamp = timestamp
        self.username  = username

    def __repr__(self):
        return '<Colorstyle %r><PhotoDate %r>' % (self.colorstyle, self.photodate)
