from app import app
from flask import render_template


@app.route('/')
@app.route('/index', strict_slashes=False)
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

@app.errorhandler(404)
def not_found(error):
    "Not found page"
    return render_template(
        '404.html',
        title="404, Ooops!",
        description="Page does not exists"
    )
