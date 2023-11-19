from flask import render_template

from watchlist import app, db
from watchlist.models import User, Movie

@app.errorhandler(400)
def bad_request(e):
    return render_template('error/400.html'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/500.html'), 500