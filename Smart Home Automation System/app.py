from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from devices import devices_list

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smarthome.db'
db = SQLAlchemy(app)

from models import Device, Schedule

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    devices = Device.query.all()
    return render_template('index.html', devices=devices)

@app.route('/devices')
def devices():
    return render_template('devices.html', devices=devices_list)

@app.route('/add_device', methods=['POST'])
def add_device():
    name = request.form.get('name')
    device_type = request.form.get('device_type')
    new_device = Device(name=name, device_type=device_type)
    db.session.add(new_device)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/schedule')
def schedule():
    schedules = Schedule.query.all()
    return render_template('schedule.html', schedules=schedules)

@app.route('/add_schedule', methods=['POST'])
def add_schedule():
    device_id = request.form.get('device_id')
    action = request.form.get('action')
    time = request.form.get('time')
    new_schedule = Schedule(device_id=device_id, action=action, time=time)
    db.session.add(new_schedule)
    db.session.commit()
    return redirect(url_for('schedule'))

if __name__ == '__main__':
    app.run(debug=True)
