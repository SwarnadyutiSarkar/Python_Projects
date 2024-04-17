from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snippet.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Snippet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('snippets', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    snippets = Snippet.query.all()
    return render_template('index.html', snippets=snippets)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))

        flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']

        snippet = Snippet(title=title, content=content, category=category, user=current_user)
        db.session.add(snippet)
        db.session.commit()

        flash('Snippet added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:snippet_id>', methods=['GET', 'POST'])
@login_required
def edit(snippet_id):
    snippet = Snippet.query.get_or_404(snippet_id)

    if snippet.user != current_user:
        return redirect(url_for('index'))

    if request.method == 'POST':
        snippet.title = request.form['title']
        snippet.content = request.form['content']
        snippet.category = request.form['category']

        db.session.commit()

        flash('Snippet updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit.html', snippet=snippet)

@app.route('/delete/<int:snippet_id>', methods=['POST'])
@login_required
def delete(snippet_id):
    snippet = Snippet.query.get_or_404(snippet_id)

    if snippet.user != current_user:
        return redirect(url_for('index'))

    db.session.delete(snippet)
    db.session.commit()

    flash('Snippet deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
