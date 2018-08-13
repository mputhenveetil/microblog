from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Manoj2'}
    return render_template('index.html', title='Home2', user=user)
