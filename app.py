from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sitemap.xml')
def sitemap():
    return app.send_static_file('sitemap.xml')


@app.route('/robots.txt')
def robots():
    return app.send_static_file('robots.txt')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html'), 404


if __name__ == '__main__':
    # Development
    app.run(debug=True, port=5001)
else:
    # Production
    app.config['DEBUG'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
