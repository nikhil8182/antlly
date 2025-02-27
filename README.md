# Antlly.ai

Antlly.ai is a website for an AI pet companion service, developed under the umbrella of Onwords. This repository contains the code for the Antlly.ai website.

## Overview

Antlly.ai provides an AI pet companion designed to bring joy, warmth, and emotional connection into users' lives. The website serves as a landing page to introduce potential users to the concept and benefits of the AI companion.

## Features

- Responsive design for mobile, tablet, and desktop
- Modern UI with a clean, vibrant color palette
- Optimized for performance and accessibility
- SEO-friendly with meta tags and structured data
- PWA capabilities with service worker for offline access

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Deployment**: Ready for Render deployment

## Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```
   python app.py
   ```
5. Visit `http://127.0.0.1:5001` in your browser

## Deployment on Render

This application is configured for deployment on Render.

### Setup Instructions

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Use the following settings:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn wsgi:app`
   - **Plan**: Free or Standard

## Project Structure

- `/app.py` - Main Flask application
- `/wsgi.py` - WSGI entry point for production
- `/requirements.txt` - Python dependencies
- `/Procfile` - Render deployment configuration
- `/templates/` - HTML templates
- `/static/` - Static assets (CSS, JS, images)

## About Onwords

Founded in 2020, Onwords specializes in smart home automation, gate automation, touch control switches, and more - all designed to enhance convenience and security in daily life. Learn more at [onwords.in](https://onwords.in).

## License

Copyright © 2025 Onwords. All rights reserved.