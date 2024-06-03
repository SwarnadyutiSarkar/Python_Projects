from app import db

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    device_type = db.Column(db.String(50), nullable=False)

class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'), nullable=False)
    action = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    device = db.relationship('Device', backref=db.backref('schedules', lazy=True))
