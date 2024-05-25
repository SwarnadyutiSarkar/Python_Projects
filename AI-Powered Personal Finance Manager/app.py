# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/finance_db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    new_expense = Expense(
        user_id=data['user_id'],
        amount=data['amount'],
        category=data['category'],
        date=datetime.strptime(data['date'], '%Y-%m-%d')
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense added successfully'})

@app.route('/predict_expenses', methods=['GET'])
def predict_expenses():
    user_id = request.args.get('user_id')
    expenses = Expense.query.filter_by(user_id=user_id).all()
    data = [(e.amount, e.date) for e in expenses]
    df = pd.DataFrame(data, columns=['amount', 'date'])
    df['date'] = pd.to_datetime(df['date'])
    df['date_ordinal'] = df['date'].map(datetime.toordinal)

    model = LinearRegression()
    model.fit(df[['date_ordinal']], df['amount'])

    future_dates = pd.date_range(start=df['date'].max(), periods=30)
    future_dates_ordinal = future_dates.map(datetime.toordinal).values.reshape(-1, 1)
    predictions = model.predict(future_dates_ordinal)

    result = {'predictions': {str(date): pred for date, pred in zip(future_dates, predictions)}}
    return jsonify(result)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
