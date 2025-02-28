from flask import Flask, render_template, request, redirect, send_from_directory, make_response
import os
from datetime import datetime, timedelta
from flask_compress import Compress

app = Flask(__name__)
# Enable compression
compress = Compress(app)

# Cache configuration for production
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 31536000  # 1 year in seconds


@app.route('/')
def home():
    response = make_response(render_template('index.html'))
    # Set cache headers for the home page
    response.headers['Cache-Control'] = 'public, max-age=3600'  # Cache for 1 hour
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


@app.route('/sitemap.xml')
def sitemap():
    response = app.send_static_file('sitemap.xml')
    # Allow caching for 24 hours
    response.headers['Cache-Control'] = 'public, max-age=86400'
    return response


@app.route('/robots.txt')
def robots():
    response = app.send_static_file('robots.txt')
    # Allow caching for 24 hours
    response.headers['Cache-Control'] = 'public, max-age=86400'
    return response


@app.route('/service-worker.js')
def service_worker():
    response = app.send_static_file('service-worker.js')
    # No caching for service worker
    response.headers['Cache-Control'] = 'no-cache'
    return response


@app.errorhandler(404)
def page_not_found(e):
    response = make_response(render_template('index.html'))
    response.status_code = 404
    # Don't cache error pages
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


if __name__ == '__main__':
    # Development
    app.run(debug=True, port=5001)
else:
    # Production settings
    app.config['DEBUG'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    
    # Security settings
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
