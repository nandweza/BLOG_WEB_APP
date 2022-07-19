from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from flask import request
from werkzeug.urls import url_parse


#Home section
@app.route('/')
@app.route('/index', strict_slashes=False)
@login_required
def home():
    """Home page"""
    nav = [
        {'name': 'Home', 'url': '/'},
        {'name': 'About', 'url': '/about'},
        {'name': 'contact', 'url': '/contact'}
    ]
    return render_template(
        'index.html',
        nav=nav,
        title="Home",
        description="blog web app built with flask."
    )

@app.route('/about')
def about():
    "about page"
    nav = [
        {'name': 'Home', 'url': '/'},
        {'name': 'About', 'url': '/about'},
        {'name': 'contact', 'url': '/contact'}
    ]
    return render_template(
        'about.html',
        nav=nav,
        title="About us...",
        description="We are software Engineers from alx Africa.."
    )

@app.route('/contact')
def contact():
    "contact page"
    nav = [
        {'name': 'Home', 'url': '/'},
        {'name': 'About', 'url': '/about'},
        {'name': 'contact', 'url': '/contact'}
    ]
    return render_template(
        'contact.html',
        nav=nav,
        title="Contact",
        description="Leave me a message, lets get in touch.."
    )

#Error Handler
@app.errorhandler(404)
def not_found(error):
    "Not found page"
    return render_template(
        '404.html',
        title="404, Ooops!",
        description="Page does not exists"
    )

#login section
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)

@app.route("/logout")
def logout():
    """logout user"""
    logout_user()
    return redirect(url_for('index'))