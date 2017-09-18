from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('base.html')

@app.route('/band')
def band():
    return render_template('band.html')

@app.route('/contact')
def about():
    return render_template('about.html')


@app.route('/tour')
def shows():
    return render_template('gigs.html')
