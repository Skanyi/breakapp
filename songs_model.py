from flask_sqlalchemy import SQLAlchemy
from breakapp import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Hearty160@localhost/Music'
app.secret_key = 'some secret key'
db = SQLAlchemy(app)

class Playlist(db.Model):
    __tablename__ = 'Playlist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    title= db.Column(db.String(50))


    def __init__(self, name, title):
        self.name = name
        self.title = title

    # Check on what this does
    def __repr__(self):
        return '<Playlist %r>' % self.name

class Playlist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(20))


    def __init__(self, artist):
        self.artist = artist

    # Check on what this does
    def __repr__(self):
        return '<Playlist %r>' % self.artist
