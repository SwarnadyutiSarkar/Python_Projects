from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        crypto_id = request.form.get('crypto_id')
        return redirect(url_for('crypto', crypto_id=crypto_id))
    return render_template('index.html')

@app.route('/crypto/<crypto_id>')
def crypto(crypto_id):
    response = requests.get(API_URL.format(crypto_id))
    data = response.json()
    if crypto_id in data:
        price = data[crypto_id]['usd']
    else:
        price = 'Invalid cryptocurrency ID'
    return render_template('crypto.html', crypto_id=crypto_id, price=price)

if __name__ == '__main__':
    app.run(debug=True)
