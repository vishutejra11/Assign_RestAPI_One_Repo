from bank_api import db

class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    branches = db.relationship('Branch', backref='bank', lazy=True)

class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    branch = db.Column(db.String(100), nullable=False)
    ifsc = db.Column(db.String(11), nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id'), nullable=False)
