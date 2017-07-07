from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Meet_band')
def meet_band():
    return render_template('meet_the_band.html')

@app.route('/shows')
def shows():
    return render_template('gigs.html')
